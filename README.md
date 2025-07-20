
# 🌐🧠 Multilingual Sentiment Analysis Web App

This is a **Flask-based web application** that analyzes the sentiment of user-provided text in **any language**. It uses **Google Translate** to convert text into English and then uses **TextBlob** for sentiment analysis.

Ideal for analyzing customer feedback or product reviews in multiple languages!

---

## ✨ Features

- 🌍 **Multilingual Support** (auto-translates to English)
- 📈 **Sentiment Analysis** (Positive, Negative, Neutral)
- 📊 **Polarity & Subjectivity Scores**
- 🧠 **Interpretation of Product Feedback**
- 🕒 **Timestamped Results**
- 🧩 Easy-to-integrate **API**

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Sentiment Analysis**: [TextBlob](https://textblob.readthedocs.io/en/dev/)
- **Translation**: [Googletrans](https://py-googletrans.readthedocs.io/en/latest/)

---

## 🖥️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app
````

### 2. Install Dependencies

```bash
pip install flask textblob googletrans==4.0.0-rc1
python -m textblob.download_corpora
```

> ⚠️ Note: Make sure you use the correct version of `googletrans`:
>
> ```bash
> pip install googletrans==4.0.0-rc1
> ```

### 3. Run the Application

```bash
python app.py
```

The app will run at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📮 API Usage

### Endpoint

```
POST /analyze
```

### Request (JSON)

```json
{
  "text": "Me encanta este producto, es excelente."
}
```

### Response

```json
{
  "translated_text": "I love this product, it is excellent.",
  "sentiment": "Positive",
  "polarity_score": 0.625,
  "subjectivity": 0.6,
  "product_feedback": "This feedback is highly positive.",
  "timestamp": "2025-05-29 14:23:11"
}
```

---

## 📁 Project Structure

```
project/
├── app.py               # Flask app with translation + sentiment logic
├── templates/
│   └── index.html       # Frontend UI (can be added or customized)
├── static/              # Static files (optional)
├── requirements.txt     # Python dependencies (optional)
└── README.md            # Project documentation
```

---

## 🧪 Example Use Cases

* Customer feedback monitoring for e-commerce platforms
* Social media sentiment analysis
* Multilingual review summarization
* Internal employee feedback processing

---

## 📸 Screenshots


<img src="https://github.com/user-attachments/assets/0ffcc6c8-f9fb-42f9-988d-ff3e32b31808" alt="Output Image" width="600"/>


---

---

## 🙌 Acknowledgements

* [Flask](https://flask.palletsprojects.com/)
* [Googletrans](https://github.com/ssut/py-googletrans)
* [TextBlob](https://textblob.readthedocs.io/en/dev/)

```

