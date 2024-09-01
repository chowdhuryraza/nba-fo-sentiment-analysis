import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

nba_team_names = {"76ers", "Bucks", "Bulls", "Celtics", "Cavs", "Clippers", "Grizzlies", 
                  "Hawks", "Heat", "Hornets", "Jazz", "Kings", "Knicks", "Lakers", "Magic", 
                  "Mavericks", "Nets", "Nuggets", "Pacers", "Pelicans", "Pistons", "Raptors", 
                  "Rockets", "Spurs", "Suns", "Thunder", "Trail Blazers", "Timberwolves", 
                  "Warriors", "Wizards"}

team = input(f'''Team Names:\n{list(nba_team_names)}\n
Type in the team name to understand the sentiment around the front office of that team: ''')

df = pd.read_csv(f"Reddit Data/{team} FO Data.csv")
sia = SIA()

total_sentiment = {'Negative': 0,
                   'Neutral': 0,
                   'Positive': 0,
                   'Compound': 0}
total_rows = len(df)

def row_sentiment(row):
    row_score = {}
    if not pd.isnull(row['Title']):
        row_score = sia.polarity_scores(row["Title"])
    if not pd.isnull(row['Content']):
        row_score = sia.polarity_scores(row["Content"])
    if not pd.isnull(row['Title']) and not pd.isnull(row['Content']):
        row_score = sia.polarity_scores(row["Title"] + "\n" + row["Content"])

    total_sentiment['Negative'] += row_score['neg']
    total_sentiment['Neutral'] += row_score['neu']
    total_sentiment['Positive'] += row_score['pos']
    total_sentiment['Compound'] += row_score['compound']

df.apply(row_sentiment, axis=1)

print(f"Average Negative Sentiment: {total_sentiment['Negative']/total_rows}")
print(f"Average Neutral Sentiment: {total_sentiment['Neutral']/total_rows}")
print(f"Average Positive Sentiment: {total_sentiment['Positive']/total_rows}")
print(f"Average Compound Sentiment: {total_sentiment['Compound']/total_rows}")