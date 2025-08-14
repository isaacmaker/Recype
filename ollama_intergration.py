from ollama import Client
def check_connection():
    try:
        client = Client(host='http://localhost:11434')
        client.generate(model="llama3.2:latest",keep_alive=0,prompt="hello",system="testing")
        return(client)
    except:
        print("ollama connection was not successful")

def genrate_recipe(client,model, text):
    response = client.chat(model='deepseek-r1:14b', messages=[
        {'role': 'system', 'content': 'You are a helpful assistant that will make a recipe with exact amounts of each ingredient needed to cook this meal from the text provided by the user'},

        {'role': 'user', 'content': text}
        
        ])
    return(response.message.content)
    