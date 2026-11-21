
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("no api key is there")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-20b"
role="user"

prompt1="hii"
prompt2="explain time travel in detail"
prompt3="write an essay of 1000 words on machine learning"

prompts=[prompt1,prompt2,prompt3]

for prompt in prompts:
    message={
        "role":role,
        "content":prompt
    }
    messages=[message]

    response=client.chat.completions.create(model=model,messages=messages)

    usage=response.usage

    print("\n" + "="*60)
    print(f"PROMPT: {prompt}")
    print("="*60)

    print(response.choices[0].message.content)

    print("\nTOKEN USAGE")
    print(f"Prompt tokens: {usage.prompt_tokens}")
    print(f"Completion tokens: {usage.completion_tokens}")
    print(f"Total tokens: {usage.total_tokens}")
    print("="*60)
