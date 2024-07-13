from transformers import pipeline, ViTFeatureExtractor, ViTForImageClassification
from PIL import Image
import torch
import requests

# Load pre-trained text sentiment analysis model
text_classifier = pipeline('sentiment-analysis')

# Load pre-trained image classification model
model_name = "google/vit-base-patch16-224"
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

# Define sentiment classes
id2label = {0: "NEGATIVE", 1: "NEUTRAL", 2: "POSITIVE"}
label2id = {v: k for k, v in id2label.items()}

# Fine-tune the model for sentiment analysis (this step is simplified for this example)
model.classifier = torch.nn.Linear(model.classifier.in_features, len(id2label))
model.config.id2label = id2label
model.config.label2id = label2id

def predict_text_sentiment(text):
    result = text_classifier(text)[0]
    sentiment = result['label']
    motivation = get_motivation_text(sentiment)
    return sentiment, motivation

def predict_image_sentiment(image_path):
    # Load and preprocess the image
    image = Image.open(image_path).convert('RGB')
    inputs = feature_extractor(images=image, return_tensors="pt")
    
    # Make prediction
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    
    # Get sentiment and motivation
    sentiment = id2label[predicted_class_idx]
    motivation = get_motivation_text(sentiment)
    
    return sentiment, motivation

def get_motivation_text(sentiment):
    if sentiment in ["LABEL_POSITIVE", "POSITIVE"]:
        return "Keep up the great work! The sky is not the limit!"
    elif sentiment in ["LABEL_NEGATIVE", "NEGATIVE"]:
        return "Don't give up. Even stars need darkness to shine."
    else:
        return "Stay neutral and keep exploring the universe!"

# Example usage
text = "I'm feeling really excited about this new project!"
text_sentiment, text_motivation = predict_text_sentiment(text)
print(f"Text: {text}")
print(f"Sentiment: {text_sentiment}")
print(f"Motivation: {text_motivation}")

# For image sentiment, you would typically use a local file path
# But for this example, let's download a sample image
image_url = "https://example.com/path/to/your/image.jpg"
image_path = "sample_image.jpg"
response = requests.get(image_url)
with open(image_path, "wb") as f:
    f.write(response.content)

image_sentiment, image_motivation = predict_image_sentiment(image_path)
print(f"\nImage Sentiment: {image_sentiment}")
print(f"Image Motivation: {image_motivation}")
