from flask import Flask, request, jsonify, render_template
from server.src.model import predict_text_sentiment, predict_image_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_text', methods=['POST'])
def predict_text():
    data = request.get_json()
    text = data['text']
    sentiment, motivation = predict_text_sentiment(text)
    return jsonify({'sentiment': sentiment, 'motivation': motivation})

@app.route('/predict_image', methods=['POST'])
def predict_image():
    file = request.files['file']
    sentiment, motivation = predict_image_sentiment(file)
    return jsonify({'sentiment': sentiment, 'motivation': motivation})

if __name__ == '__main__':
    app.run(debug=True)
