from transformers import pipeline

# Load pre-trained sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

while True:
    text = input("Enter a sentence (or type 'exit' to quit): ")
    if text.lower() == 'exit':
        break
    result = sentiment_analyzer(text)
    label = result[0]['label']
    score = result[0]['score']
    print(f"\nSentiment: {label} (confidence: {score:.2f})\n")
