from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from textblob import TextBlob
import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'
translator = Translator()

# Helper Functions
def translate_text(text):
    try:
        translated = translator.translate(text, dest='en')  # Always translate to English
        return translated.text
    except Exception as e:
        return f"Translation error: {str(e)}"

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    if sentiment > 0:
        return "Positive", sentiment, subjectivity
    elif sentiment < 0:
        return "Negative", sentiment, subjectivity
    else:
        return "Neutral", sentiment, subjectivity

@app.route('/')
def index():
    return render_template('index.html')  # No language selection needed

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Translate Text to English
    translated_text = translate_text(text)
    if "Translation error" in translated_text:
        return jsonify({"error": translated_text}), 500

    # Analyze Sentiment
    sentiment, polarity_score, subjectivity = analyze_sentiment(translated_text)

    # Interpret Sentiment
    feedback_interpretation = (
        "This feedback is highly positive." if polarity_score > 0.5 else
        "The feedback is slightly positive." if 0 < polarity_score <= 0.5 else
        "This feedback is neutral." if polarity_score == 0 else
        "The feedback is slightly negative." if -0.5 <= polarity_score < 0 else
        "This feedback is highly negative."
    )

    response = {
        "translated_text": translated_text,
        "sentiment": sentiment,
        "polarity_score": polarity_score,
        "subjectivity": subjectivity,
        "product_feedback": feedback_interpretation,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
