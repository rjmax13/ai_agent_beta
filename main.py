import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompt import system_prompt
from call_function import available_functions
import json

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)



def main():
    # PARSER CONFIGURATION
    parser = argparse.ArgumentParser(description="AI Agent Beta")
    parser.add_argument(
        "user_prompt",
        type=str,
        help="User promt",
        
    )

    parser.add_argument(
        "--verbose", 
        action="store_true", 
        help="Enable verbose output"
    )
    args = parser.parse_args()

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ]



    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=available_functions
    )


    # print("Hello from ai-agent-beta!")

    if response.usage == None:
        raise RuntimeError("Response usage is None")
    if response.usage != None and args.verbose == True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
        # print(response.choices[0].message.content)
    if response.choices[0].message.tool_calls:
        for tool_call in response.choices[0].message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")
    else:
        print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
