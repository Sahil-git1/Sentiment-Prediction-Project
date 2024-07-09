from transformers import pipeline

# Load pre-trained sentiment-analysis model
classifier = pipeline('sentiment-analysis')

def predict_text_sentiment(text):
    result = classifier(text)[0]
    sentiment = result['label']
    motivation = get_motivation_text(sentiment)
    return sentiment, motivation

def predict_image_sentiment(image):
    # Here, we should implement an image sentiment analysis
    # For the purpose of this example, we'll return a mock sentiment
    sentiment = "POSITIVE"  # Placeholder for actual image sentiment analysis
    motivation = get_motivation_text(sentiment)
    return sentiment, motivation

def get_motivation_text(sentiment):
    if sentiment == "Happy !!":
        return "Keep up the great work! The sky is not the limit!"
    elif sentiment == "Sad":
        return "Don't give up. Even stars need darkness to shine."
    else:
        return "Stay neutral and keep exploring the universe!"
