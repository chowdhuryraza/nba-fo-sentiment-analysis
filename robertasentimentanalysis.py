from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch.nn.functional as F
import pandas as pd


MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

nba_team_names = {"76ers", "Bucks", "Bulls", "Celtics", "Cavs", "Clippers", "Grizzlies", 
                  "Hawks", "Heat", "Hornets", "Jazz", "Kings", "Knicks", "Lakers", "Magic", 
                  "Mavericks", "Nets", "Nuggets", "Pacers", "Pelicans", "Pistons", "Raptors", 
                  "Rockets", "Spurs", "Suns", "Thunder", "Trail Blazers", "Timberwolves", 
                  "Warriors", "Wizards"}

team = input(f'''Team Names:\n{list(nba_team_names)}\n
Type in the team name to understand the sentiment around the front office of that team: ''')

df = pd.read_csv(f"Reddit Data/{team} FO Data.csv")

total_sentiment = {'Negative': 0,
                   'Neutral': 0,
                   'Positive': 0,
                   'Compound': 0}

sentiment_analyzed_count = 0

def row_sentiment(row):
    global sentiment_analyzed_count
    row_negative = 0
    row_neutral = 0
    row_positive = 0

    if not pd.isnull(row['Title']):
        encoded_text = tokenizer(
            row["Title"],
            padding=True,
            return_tensors='pt',
            truncation=True,
            max_length=512
        )
        output = model(**encoded_text)
        sentiment_probs = F.softmax(output.logits, dim=1)
        row_negative = sentiment_probs[0][0].item()
        row_neutral = sentiment_probs[0][1].item()
        row_positive = sentiment_probs[0][2].item()

        sentiment_analyzed_count += 1
        
    if not pd.isnull(row['Content']):
        encoded_text = tokenizer(
            row["Title"],
            padding=True,
            return_tensors='pt',
            truncation=True,
            max_length=512
        )
        output = model(**encoded_text)
        sentiment_probs = F.softmax(output.logits, dim=1)
        row_negative += sentiment_probs[0][0].item()
        row_neutral += sentiment_probs[0][1].item()
        row_positive += sentiment_probs[0][2].item()
        
        sentiment_analyzed_count += 1

    total_sentiment['Negative'] += row_negative
    total_sentiment['Neutral'] += row_neutral
    total_sentiment['Positive'] += row_positive

df.apply(row_sentiment, axis=1)


print(f"Average Negative Sentiment: {total_sentiment['Negative']/sentiment_analyzed_count}")
print(f"Average Neutral Sentiment: {total_sentiment['Neutral']/sentiment_analyzed_count}")
print(f"Average Positive Sentiment: {total_sentiment['Positive']/sentiment_analyzed_count}")
