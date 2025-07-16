import requests
import json
def callOLLAMA(user_message):
    url="http://localhost:11434/api/generate"
    payload={
        "model":"phi3",
        "prompt": user_message,
        "stream": False
    } 
    response= requests.post(
    url,
        headers={"content-type": "application/json"},
        data=json.dumps(payload),
        timeout=120
    )
    if response.status_code==200:
        result=response.json()
        bot_response=result.get("response","sorry, I am unable to help you")
        return bot_response.strip()
    
    