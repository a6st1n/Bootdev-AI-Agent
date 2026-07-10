import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
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
            {"role" : "user",
             "content" : user_prompt}
        ]
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    

    response = client.chat.completions.create(

        model = "openrouter/free",
        messages = messages
        
    )
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}\n"
            f"Response tokens: {response.usage.completion_tokens}\n"
        )
    else:
            #check usage is not None
        if response.usage is not None:
            pass

            #prompt uses
            print(
                
                f"Prompt tokens: {response.usage.prompt_tokens}\n"
                f"Response tokens: {response.usage.completion_tokens}\n"
                
            )
        else:
            pass
            raise RuntimeError("response usage is None. please " \
            "check your API key and model name.")

    print(response.choices[0].message.content)
        
        
    




if __name__ == "__main__":
    main()
