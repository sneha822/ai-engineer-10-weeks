
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Windows terminals default to cp1252 and can't print some characters LLMs
# return (emoji, special spaces). Force UTF-8 output so printing never crashes.
sys.stdout.reconfigure(encoding="utf-8")

# Load .env from the same directory as this script
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("No API key found. Check your .env file.")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"

messages = [
    {
        "role": "user",
        "content": "Do you know Padho with Pratyush?"
    }
]

response = client.chat.completions.create(
    model=model,
    messages=messages
)

print(response.choices[0].message.content)
