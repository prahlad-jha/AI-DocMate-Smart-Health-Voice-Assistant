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
    # Ensure query is a string
    if not isinstance(query, str):
        query = str(query)
    
    client = Groq()
    
    # Use proper vision model format for Groq
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
    
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        # If vision format fails, try text-only format as fallback
        print(f"Vision API error: {e}. Trying text-only fallback...")
        messages_text_only = [
            {
                "role": "user",
                "content": query
            }
        ]
        chat_completion = client.chat.completions.create(
            messages=messages_text_only,
            model=model
        )
        return chat_completion.choices[0].message.content
