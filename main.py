import os
import json
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_functions import available_functions_to_use, call_functions
def main():

    # load enviroment variables from .env file
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    parser = argparse.ArgumentParser(description="Bootdev Chatbot")
    parser.add_argument("user_prompt", type=str,help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    user_prompt = args.user_prompt
    verbose = args.verbose
    

    if api_key == None:

        raise RuntimeError("no API key found. please set the OPENROUTER_API_KEY " \
        "environment variable in the .env file")
    

   
    
    messages = [

            {"role" : "system",
             "content" : system_prompt},
            {"role" : "user",
             "content" : user_prompt}
        ]
    client = OpenAI(

        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    

    response = client.chat.completions.create(

        model = "openrouter/free",
        messages = messages,
        tools = available_functions_to_use,
        
    )
    message = response.choices[0].message

   


    if response.usage is None:

        raise RuntimeError(
        "response usage is None. please check your API key and model name."
    )

    if verbose:

        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")


    
    

    if message.tool_calls:

        for tool_call in message.tool_calls:

            #result from call_functions
            result_message = call_functions(tool_call,verbose)

            if result_message["content"]== "":
                raise Exception(f"Exception raised because of {tool_call}") 
            
            if verbose:
                print(f"-> {result_message['content']}")


    else:
        print(message.content)

    
        
        
    




if __name__ == "__main__":
    main()
