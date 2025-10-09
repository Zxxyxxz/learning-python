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
    msg=message
    
if __name__=="__main__":
    try:
        print(f""" 1 learnign tool we will gain out of here is the inspectino tools of python 
              \n 1- dir(xxx) this shows us all the available methods and attribiutes that is available on a object
              \n kind of asking  what can i do with this object?
              \n 2- type(xxx) this is tells us what class or type an object is
              \n such as type(msg) => {type(msg)} will give us string if the antrhopic comm is not 
              ebtablished if so then antroppiuc type message should it be and type(int)  => {type(int)} will give us ttpye
               lets print the msg -> {msg}
              \n then lets print the tpye of it {type(msg)}
              \n lets also see the type of its content {type(msg.content)} \n
              \n {{dir()}}, {dir()}
              \n now we will the  {{dir(msg)}}, {dir(msg)} \n 
              \nand then {{dir(msg.content)}} => {dir(msg.content)}\n
                         
              
              
              \n
               
              """)
        
    except:
        print("it failed")
  