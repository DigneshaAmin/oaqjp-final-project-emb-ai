from EmotionDetection import emotion_detector

def test_joy():
    result = emotion_detector("I am so happy I am doing this.")
    assert result["dominant_emotion"] == "joy"

def test_anger():
    result = emotion_detector("I am really mad about this.")
    assert result["dominant_emotion"] == "anger"

def test_fear():
    result = emotion_detector("I am so scared to do this.")
    assert result["dominant_emotion"] == "fear"

def test_disgust():
    result = emotion_detector("I feel disgusted just hearing about this.")
    assert result["dominant_emotion"] == "disgust"

def test_sadness():
    result = emotion_detector("I am feeling very sad and down.")
    assert result["dominant_emotion"] == "sadness"
