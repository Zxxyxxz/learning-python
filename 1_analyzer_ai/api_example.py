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
def send_to_cli(msg_to_cli):
    if api_key is None:
        print(f" please enter the api key")
    else:
        client = anthropic.Anthropic(api_key= os.getenv("ANTHROPIC_API_KEY"))
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4024,
            messages=[
                {
                "role":"user",
                "content":msg_to_cli
                
            }
                ]
            
        )
        return message.content[0].text
messages=[]
if __name__=="__main__":
    inn="0"
    i=0
    while inn!="q":
        if inn == '0':
            print(f"please enter whatever you want to ask to the chatbot adn you end the converstation by jsut pressing q and enter")
            
        inn = sys.stdin.readline().strip()
        print(inn)
        messages.append({"role":"user", "content":inn, "role":"assistant", "content":send_to_cli(inn)})
        messages.append({})
        print((messages[i].get[1]))
        i+=1
        
        
    # for i in msg.content[0].text:
    #     print(i)
    # try:
    #     print(f""" 1 learnign tool we will gain out of here is the inspectino tools of python 
    #           \n 1- dir(xxx) this shows us all the available methods and attribiutes that is available on a object
    #           \n kind of asking  what can i do with this object?
    #           \n 2- type(xxx) this is tells us what class or type an object is
    #           \n such as type(msg) => {type(msg)} will give us string if the antrhopic comm is not 
    #           ebtablished if so then antroppiuc type message should it be and type(int)  => {type(int)} will give us ttpye
    #           \n 2.1 > also lets try one interesting thing and see what is going to happen {type(type(int))}this interesting thig gives us this {type(type(int))} \n
    #           \n as of also to see something else because we just observeed teh same thing as single type of an int so lets try ewith the message
    #           \n 1 type -> {type(msg)} , then 2 type {type(type(msg))} maybe also 3 types {type(type(type(msg)))}
    #            \nlets print the msg -> {msg}
    #           \n then lets print the tpye of it {type(msg)}
    #           \n lets also see the type of its content {type(msg.content)} \n
    #           \n {{dir()}}, {dir()}
    #           \n now we will the  {{dir(msg)}}, {dir(msg)} \n 
    #           \nand then {{dir(msg.content)}} => {dir(msg.content)}\n
                         
              
              
    #           \n
               
    #           """)
        
    # except:
    #     print("it failed")
  