import anthropic
import sys
import os
# get the api key
msg="Not_set_yet"
api_key = os.getenv("ANTHROPIC_API_KEY")
if api_key is None:
    print("""your api key is not set please visit  https://console.anthropic.com and use this command to set your api key 
          export ANTHROPIC_API_KEY="what eveer key you have"
          enter this command in bash the command line prb in the working directory
          
          """)
else:

    # create the client
    client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[
            {
                    "role":"user",
                    "content":"Hello, Claude tel yoyo if you receive this message"
             }
        ]
        
        
    )
    msg=message.content
    
if __name__=="__main__":
    try:
        print(msg)
        print(sys.argv)
    except:
        print("it failed")
  