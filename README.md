This project is a Flask-based web application that transforms spoken content—such as cooking videos or food-related audio—into structured, AI-generated recipes using the power of Ollama's local language models.

🚀 Key Features
Audio Download & Transcription Automatically downloads audio from a given URL and converts it into text using a pre-warmed transcription model.

AI Recipe Generation Uses a large language model (e.g., deepseek-r1:14b) via Ollama to analyze the transcribed text and generate a detailed recipe.

Text Cleanup & Formatting Removes unnecessary tags and capitalizes bolded text for improved readability.

GPU Memory Management Efficiently clears GPU memory after model usage to optimize performance.

Web Interface A simple Flask server provides endpoints for:

Viewing the homepage (/)

Submitting transcribed text to generate a recipe (/to-recipe-chat)

🧩 Modules & Integrations
download_audio: Handles downloading audio from a URL.

convert_audio_to_text: Transcribes audio using a local model.

ollama_intergration: Interfaces with the Ollama server to generate recipes.

flask: Powers the web server and API endpoints.

re: Cleans and formats the generated text.

🛠️ Workflow Overview
User submits a URL or audio content.

Audio is downloaded and transcribed.

Transcribed text is sent to Ollama for recipe generation.

Generated recipe is cleaned, formatted, and returned to the use
