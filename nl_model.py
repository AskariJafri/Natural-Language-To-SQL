
from groq import Groq

messages =[]

def get_query(prompt):
    
    global messages
    
    client = Groq(api_key="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")
    if not messages:
      messages.append({
                "role":"system",
                "content" : get_system_message_from_txt()
            })
    
    messages.append( {
            "role":"user",
            "content":prompt
            })
    
    chat = client.chat.completions.create(
        messages=messages,
        model = "llama3-70b-8192"
    )
    messages.append({
                "role":"system",
                "content" : chat.choices[0].message.content  
            })

    return chat.choices[0].message.content

def get_system_message_from_txt():
    # Read the system message from the text file
    with open('data', mode='r') as file:
        system_message = file.read()
    return system_message

# print(get_query())