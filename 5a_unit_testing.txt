from EmotionDetection import emotion_detector

def test_joy():
    result = emotion_detector("I am so happy I am doing this.")
    assert result["dominant_emotion"] == "joy"
    print('test_joy passed')

def test_anger():
    result = emotion_detector("I am really mad about this.")
    assert result["dominant_emotion"] == "anger"
    print('test_anger passed')

def test_fear():
    result = emotion_detector("I am so scared to do this.")
    assert result["dominant_emotion"] == "fear"
    print('test_fear passed')

def test_disgust():
    result = emotion_detector("I feel disgusted just hearing about this.")
    assert result["dominant_emotion"] == "disgust"
    print('test_disgust passed')

def test_sadness():
    result = emotion_detector("I am feeling very sad and down.")
    assert result["dominant_emotion"] == "sadness"
    print('test_sadness passed')

if __name__ == "__main__":
    test_joy()
    test_anger()
    test_fear()
    test_disgust()
    test_sadness()