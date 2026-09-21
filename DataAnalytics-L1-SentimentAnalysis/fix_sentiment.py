import json
with open('Sentiment_Analysis_Airline_Tweets.ipynb', 'r', encoding='utf-8') as f:
    d = f.read()
d = d.replace(
    "sns.barplot(x=order, y=class_counts.reindex(order).values, palette=colors)", 
    "sns.barplot(x=order, y=class_counts.reindex(order).values, hue=order, palette=colors, legend=False)"
)
with open('Sentiment_Analysis_Airline_Tweets.ipynb', 'w', encoding='utf-8') as f:
    f.write(d)
