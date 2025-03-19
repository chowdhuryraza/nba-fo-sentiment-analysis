# NBA Front Office Sentiment Analysis

This project analyzes the sentiment of NBA fans towards front office personnel by extracting data from Reddit and calculating sentiment scores using natural language processing (NLP) techniques.

## Features

- **Data Extraction**: Uses the SportsRadar API to gather NBA-related data and PRAW to scrape Reddit discussions regarding front office personnel, such as general managers, executives, and other decision-makers.
- **Sentiment Analysis**: 
  - VADER (Valence Aware Dictionary and sEntiment Reasoner) from NLTK is used for basic sentiment analysis.
  - A fine-tuned Roberta model is utilized for deeper contextual sentiment analysis.
- **Sentiment Aggregation**: The sentiment scores are averaged to provide an overall understanding of fan reactions towards trades, signings, or general sentiment about front office decisions.
  
## Use Cases

- **Trade & Signing Reactions**: Track how fans feel about specific trades or player signings made by front office personnel.
- **General Consensus**: Understand the overall fan sentiment regarding management, leadership, and decision-making.
- **Decision Feedback**: Gain insights into how NBA team management's decisions are perceived by the public.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/nba-front-office-sentiment-analysis.git
    cd nba-front-office-sentiment-analysis
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables for API keys:
    - SportsRadar API key
    - Reddit API credentials (Client ID, Secret, User Agent)
