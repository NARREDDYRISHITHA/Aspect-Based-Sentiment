from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from textblob import TextBlob
import os
import pandas as pd
from docx import Document

app = Flask(__name__)

# Set a folder for file uploads
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

translator = Translator()

def translate_to_english(text):
    translated = translator.translate(text, dest='en')
    return translated.text

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # Ranges from -1 (negative) to +1 (positive)
    if sentiment > 0:
        return "Positive", sentiment
    elif sentiment < 0:
        return "Negative", sentiment
    else:
        return "Neutral", sentiment

def interpret_sentiment(sentiment):
    if sentiment == "Positive":
        return "The feedback suggests that the product is good."
    elif sentiment == "Negative":
        return "The feedback suggests that the product may not be good."
    else:
        return "The feedback is neutral about the product."

def read_comments_from_file(file):
    comments = []
    if file.filename.endswith('.txt'):
        comments = file.read().decode('utf-8').splitlines()
    elif file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        comments = df.iloc[:, 0].tolist()  # Assuming comments are in the first column
    elif file.filename.endswith('.docx'):
        doc = Document(file)
        for para in doc.paragraphs:
            comments.append(para.text)
    return comments

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.form
    text = data.get("text")
    file = request.files.get("file")
    results = []

    if file:
        comments = read_comments_from_file(file)

        for comment in comments:
            translated_text = translate_to_english(comment.strip())
            sentiment, polarity_score = analyze_sentiment(translated_text)
            product_feedback = interpret_sentiment(sentiment)
            results.append({
                "comment": comment.strip(),
                "translated_text": translated_text,
                "sentiment": sentiment,
                "polarity_score": polarity_score,
                "product_feedback": product_feedback
            })

    if text:
        translated_text = translate_to_english(text)
        sentiment, polarity_score = analyze_sentiment(translated_text)
        product_feedback = interpret_sentiment(sentiment)
        results.append({
            "comment": text,
            "translated_text": translated_text,
            "sentiment": sentiment,
            "polarity_score": polarity_score,
            "product_feedback": product_feedback
        })

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
