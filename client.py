import requests
import re
data = input("url for youtube video you want to turn into a recipe:")
url = "http://localhost:5000/to-recipe-chat"
data = {"text": data}

response = requests.post(url, json=data)
def capitalize_bolded_text(text):
    # Find all instances of **text** and replace with TEXT (uppercase)
    text = re.sub(r"\*\*(.*?)\*\*", lambda match: match.group(1).upper(), text)
    return (text)
result = response.json()
recipe_text = result["recipe"]
formatted_recipe = capitalize_bolded_text(recipe_text)

# Print the actual content returned by the server
print(formatted_recipe)  # This gives you the parsed JSON dictionary