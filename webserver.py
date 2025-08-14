import ollama
import os
import convert_audio_to_text
import download_audio
import time
import ollama_intergration
import flask
import json
import re
# Create a client instance pointing to the local Ollama server
client = ollama.Client(host='http://localhost:11434')

def capitalize_bolded_text(text):
    # Find all instances of **text** and replace with TEXT (uppercase)
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    text = re.sub(r"\*\*(.*?)\*\*", lambda match: match.group(1).upper(), text)
    return (text)


def check_if_videos_folder_exists():
    if not os.path.isdir("videos"):
        print("videos folder doesn't exist, creating it...")
        os.mkdir("videos")
def clean_gpu(model):
    del model  # Remove reference to the model
    import gc
    gc.collect()  # Run garbage collection

    import torch
    torch.cuda.empty_cache()  # Clear GPU memory if used
    return()


from flask import Flask, request, redirect, jsonify
import ollama
import flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return flask.render_template("home.html")

def main(url,model):
    print("welcome")
    
    client = ollama_intergration.check_connection()
    model = convert_audio_to_text.warm_up_model("turbo")
    title = download_audio.download(url)
    time.sleep(1)
    convered_text = convert_audio_to_text.convert(model, title)
    print(convered_text["text"])
    clean_gpu(model)
    time.sleep(5)
    recipe = ollama_intergration.genrate_recipe(client=client,model="deepseek-r1:14b",text=convered_text["text"])
    recipe = capitalize_bolded_text(recipe)
    print(recipe)
    clean_gpu('')
    return(recipe)


@app.route("/to-recipe-chat", methods=["POST"])
def receive_paragraph():
    data = request.get_json()
    print(data)
    paragraph = data.get("text")
    print(paragraph)
    model = "deepseek-r1:14b"
    print(f"using {model} for recipe generation")
    response = main(paragraph,model)
    print(response)
    return jsonify({"recipe": response})

if __name__ == "__main__":
    app.run(debug=True)