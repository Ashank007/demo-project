# AI-Powered Analysis Suite

This repository contains two AI-based applications: a Fake News Classifier and a Personality Tester. Both tools leverage machine learning models trained on curated datasets to provide intelligent insights, and are bundled with the required dependencies and serialized model files for deployment or further development.

## 📁 Project Structure

```
.
├── fake_news_classifer/
│   ├── main.py                 # Entry point for fake news detection
│   ├── news.pkl                # Trained ML model for classifying news
│   └── requirements.txt        # Dependencies for fake news classifier
└── personality_tester/
    ├── main.py                 # Entry point for personality testing
    ├── personality_test.pkl    # Trained ML model for personality analysis
    └── requirements.txt        # Dependencies for personality tester
```

## 🔍 1. Fake News Classifier

This module uses Natural Language Processing and machine learning techniques to classify news articles as real or fake. It is trained on a labeled dataset of news content and utilizes preprocessing, vectorization, and a classification model pipeline.

### Features:

- Classifies news text using a pre-trained model.

- Easily extendable with new datasets or model enhancements.

- Lightweight and ready for deployment.

### How to Run:

```
cd fake_news_classifer
pip install -r requirements.txt
streamlit run main.py
```

## 🧠 2. Personality Tester

This application uses user responses to a psychological questionnaire to predict personality traits based on established psychometric models.

### Features:

- Predicts personality profile from a set of inputs.

- Trained model embedded (personality_test.pkl) for offline usage.

- Clean and modular design for easy API or UI integration.

### How to Run:
```
cd personality_tester
pip install -r requirements.txt
streamlit main.py
```

## 📦 Requirements

Each module includes its own requirements.txt. You should install dependencies separately for each project folder, depending on which module you're using.

## 🛠️ Customization

Both modules are designed to be easily customizable:

- Replace or retrain the model .pkl files as needed.

- Integrate with web frameworks or APIs.

- Enhance with data visualizations or logging mechanisms.

## 📌 Notes

- This repository assumes basic familiarity with Python and machine learning concepts.

- For production deployment or integration, proper input validation and model versioning are recommended.