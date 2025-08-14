import whisper

def warm_up_model(model_name):
    # Load the model once and return it
    model = whisper.load_model(model_name)
    return model

def convert(model, file):
    # Use the already-loaded model
    result = model.transcribe(f"videos/{file}.mp3")
    print(result["text"])
    return(result)

if __name__ == "__main__":
    model = warm_up_model("turbo")  # Load once
    convert(model)    # Reuse the loaded model