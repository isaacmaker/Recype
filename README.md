# 🧠🎙️ AI-Powered Recipe Generator from Audio

This project is a **Flask-based web application** that transforms spoken content—such as cooking videos or food-related audio—into **structured, AI-generated recipes** using the power of **Ollama's local language models**.

---

## 🚀 Features

- **🎧 Audio Download & Transcription**  
  Automatically downloads audio from a given URL and converts it into text using a pre-warmed transcription model.

- **🧠 AI Recipe Generation**  
  Uses a large language model (e.g., `deepseek-r1:14b`) via Ollama to analyze the transcribed text and generate a detailed recipe.

- **🧹 Text Cleanup & Formatting**  
  Removes unnecessary tags and capitalizes bolded text for improved readability.

- **⚙️ GPU Memory Management**  
  Efficiently clears GPU memory after model usage to optimize performance.

- **🌐 Web Interface**  
  A simple Flask server provides endpoints for:
  - Viewing the homepage (`/`)
  - Submitting transcribed text to generate a recipe (`/to-recipe-chat`)

---

## 🧩 Modules & Integrations

- `download_audio`: Handles downloading audio from a URL.
- `convert_audio_to_text`: Transcribes audio using a local model.
- `ollama_intergration`: Interfaces with the Ollama server to generate recipes.
- `flask`: Powers the web server and API endpoints.
- `re`: Cleans and formats the generated text.
- `requests`: Enables client-side interaction with the Flask API.

---

## 🛠️ How It Works

1. **User submits a YouTube URL or audio content.**
2. **Audio is downloaded and transcribed.**
3. **Transcribed text is sent to Ollama for recipe generation.**
4. **Generated recipe is cleaned, formatted, and returned to the user.**

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/recipe-generator.git
   cd recipe-generator


# Install dependencies
pip install -r requirements.txt

# Make sure Ollama is running locally
ollama serve

# Run the Flask app
 webserver.py


## 🧠 Model Notes

- Transcription uses a lightweight `"turbo"` model  
- Recipe generation uses `"deepseek-r1:14b"` via Ollama  

---

## 🧼 GPU Cleanup

To prevent memory leaks and optimize performance, the app includes GPU memory cleanup after model usage using Python's `gc` and PyTorch's `cuda.empty_cache()`.

---

## 🧪 Example: Client-Side Script

Use this Python script to interact with the Flask API and print the formatted recipe:

```python
import requests
import re

# Prompt user for YouTube video URL
data = input("URL for YouTube video you want to turn into a recipe: ")

# Send request to Flask API
url = "http://localhost:5000/to-recipe-chat"
payload = {"text": data}
response = requests.post(url, json=payload)

# Format bolded text to uppercase
def capitalize_bolded_text(text):
    text = re.sub(r"\*\*(.*?)\*\*", lambda match: match.group(1).upper(), text)
    return text

# Parse and display the recipe
result = response.json()
recipe_text = result["recipe"]
formatted_recipe = capitalize_bolded_text(recipe_text)
print(formatted_recipe)
```

---

## 📄 License

MIT License. See `LICENSE` file for details.

---

## 🤝 Contributing Isaac Hunacek

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

Happy cooking with AI! 🍳
```
