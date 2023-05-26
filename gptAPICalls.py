import openai
import os

# Set up the OpenAI API client
openai.api_key = "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"

# Function to generate summary using ChatGPT API
def getOneLine(messages):
 
    
    response = openai.ChatCompletion.create( model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,

    )
    
    message = response.choices[0].message.content.strip()
    return message

# Generate and print the summary


# print(getOneLine([
#                 {"role": "system", "content": "You are an assistant crafting short outbound messages to be sent to potential customers."},
#                 {"role": "user", "content": "here is my prompt"},
#             ],))