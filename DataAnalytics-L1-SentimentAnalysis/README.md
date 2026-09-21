# DataAnalytics-L1-SentimentAnalysis

**Track:** Data Analytics
**Level:** Level 1 — Task 4
**Task:** Sentiment Analysis

## Objective

Build a machine learning model that classifies the sentiment of text data (positive,
negative, or neutral), providing insight into customer feedback.

## Tech Stack

Python, pandas, scikit-learn, NLTK, WordCloud, matplotlib/seaborn, Jupyter Notebook

## Dataset

`data/Tweets.csv` — the **Twitter US Airline Sentiment** dataset: 14,640 tweets directed at
major US airlines (scraped Feb 2015), each labelled `positive`, `negative`, or `neutral`.
Class distribution is imbalanced: 63% negative, 21% neutral, 16% positive.

## What's in this folder

```
DataAnalytics-L1-SentimentAnalysis/
├── README.md
├── requirements.txt
├── Sentiment_Analysis_Airline_Tweets.ipynb   # main notebook, pre-executed with all outputs
├── data/
│   └── Tweets.csv
└── screenshots/
    ├── 01_sentiment_distribution.png
    ├── 02_wordclouds_by_sentiment.png
    └── 03_confusion_matrices.png
```

## Feature checklist (all complete)

- [x] Load dataset and inspect class distribution (bar chart + percentages)
- [x] Text preprocessing pipeline: lowercase, URL/mention removal, punctuation removal,
      tokenisation, stopword removal, lemmatisation
- [x] Feature extraction: TF-IDF vectorisation (with markdown explaining its purpose)
- [x] Train/test split (80/20, stratified by sentiment)
- [x] Two classifiers trained: Multinomial Naive Bayes + Linear SVM
- [x] Evaluation: accuracy, precision, recall, F1-score, and confusion matrix for each model
- [x] Visualisation: sentiment distribution bar chart + a WordCloud per sentiment class
- [x] Error analysis: 5 misclassified examples with a discussion of likely causes
- [x] Conclusion: best-performing model + a real-world application

## Results

| Metric | Naive Bayes | Linear SVM |
|---|---|---|
| Accuracy | 0.740 | **0.775** |
| Precision (macro) | 0.765 | 0.727 |
| Recall (macro) | 0.562 | **0.693** |
| F1-score (macro) | 0.604 | **0.708** |

**Linear SVM was the better model overall.** Naive Bayes edges it out on macro precision, but
only by being conservative — it defaults to "negative" more often, missing far more true
neutral/positive tweets (recall of just 0.27 / 0.44 on those classes). SVM's higher recall and
F1 make it the more useful classifier in practice.

**Real-world application:** automatic triage of airline social-media mentions — routing
negative tweets to customer service quickly, tracking sentiment trends to catch emerging
service issues, and surfacing positive tweets as marketing/testimonial candidates. Known blind
spots (see the notebook's error analysis): sarcasm, mixed-sentiment tweets, and
numeric/rating-style feedback (e.g. "my rating: -9/10") that word-based features can't fully
capture.

## How to run

```bash
pip install -r requirements.txt
jupyter notebook
```
Then open `Sentiment_Analysis_Airline_Tweets.ipynb` and run all cells
(`Kernel → Restart & Run All`). The notebook downloads its own NLTK corpora
(stopwords, wordnet, punkt) on first run.

## Author

*(Add your full name here before pushing to GitHub / recording your demo video.)*
