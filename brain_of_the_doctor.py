#s-1 setup groq api key
import os
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
#s-2 convert image to required format
import base64

#image_path="acne.jpeg"
#imge_file=open(image_path,"rb")
#encoded_image=base64.b64encode(imge_file.read()).decode("utf-8")

def encode_image(image_path):
    imge_file=open(image_path,"rb")
    return base64.b64encode(imge_file.read()).decode("utf-8")
#s-3 set multimodel LLM
from groq import Groq
query="is there something wrong with my face?"
model="llama-3.2-90b-vision-preview"
def analyse_image_with_query(query, model, encoded_image):
    client = Groq()
    
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    
    return chat_completion.choices[0].message.content  # <-- Fixed indentation & return statement
