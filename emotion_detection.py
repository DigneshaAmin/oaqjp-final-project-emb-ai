import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the Emotion Detection API
    URL= 'https://sn-watson-emotion.labs.skills.network/emotion_detection'

    
    readtext = { "text": text_to_analyze }

    # Send POST request
    response = requests.post(URL, json=readtext)

    # Convert response to JSON
    results = json.loads(response.text)
    if "anger" not in results:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "error": results
        }   
    anger_score = results['anger']
    disgust_score = results['disgust']
    fear_score = results['fear']
    joy_score = results['joy']
    sadness_score = results['sadness']

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Add dominant emotion to result
    results['dominant_emotion'] = dominant_emotion

    return results
    
