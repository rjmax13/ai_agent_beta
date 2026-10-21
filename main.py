import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# PARSER CONFIGURATION
parser = argparse.ArgumentParser(description="AI Agent Beta")
parser.add_argument(
    "user_prompt",
    type=str,
    help="User promt",
    
)
args = parser.parse_args()

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ],
)




def main():
    print("Hello from ai-agent-beta!")

    if response.usage == None:
        raise RuntimeError("Response usage is None")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")


    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
