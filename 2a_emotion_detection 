import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the Emotion Detection API
    URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    
    readtext = { "text": text_to_analyze }

    # Send POST request
    response = requests.post(url, json=reaadtext)

    # Convert response to JSON
    result = json.loads(response.text)

    return result
