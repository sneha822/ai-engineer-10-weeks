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
prompt="I love you baby"

message_system={
    "role":"system",
    "content":"you are my strict collegue"
}

message={
    "role":role,
    "content":prompt
}
messages=[message_system,message]

response=client.chat.completions.create(model=model,messages=messages, temperature=0)
print("##########################################################")
ans=response.choices[0].message.content
print(ans)