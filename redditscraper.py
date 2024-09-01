import praw
import pandas as pd
from dotenv import load_dotenv
import os
from frontofficedata import nba_personnel_data

load_dotenv()

subreddit_names = {"76ers": "sixers", "Bucks": "MkeBucks", "Bulls": "chicagobulls", "Celtics": "bostonceltics", 
                   "Cavs": "clevelandcavs", "Clippers": "LAClippers", "Grizzlies": "memphisgrizzlies", 
                   "Hawks": "AtlantaHawks", "Heat": "heat", "Hornets": "CharlotteHornets", "Jazz": "UtahJazz", 
                   "Kings": "kings", "Knicks": "NYKnicks", "Lakers": "lakers", "Magic": "OrlandoMagic", 
                   "Mavericks": "Mavericks", "Nets": "GoNets", "Nuggets": "denvernuggets", "Pacers": "pacers", 
                   "Pelicans": "NOLAPelicans", "Pistons": "DetroitPistons", "Raptors": "torontoraptors", 
                   "Rockets": "rockets", "Spurs": "NBASpurs", "Suns": "suns", "Thunder": "Thunder", "Trail Blazers": "ripcity", 
                   "Timberwolves": "timberwolves", "Warriors": "warriors", "Wizards": "washingtonwizards"}


reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent="Front Office Data Scraper",
)

for team_name, team_subreddit in subreddit_names.items():
    subreddit_search = reddit.subreddit(team_subreddit)
    personnel_info = nba_personnel_data[team_name]
    reddit_data = []
    
    if personnel_info[0] is not None:
        president_search = subreddit_search.search(personnel_info[0], time_filter='year')
        for submission in president_search:
            submission_info = {}
            submission_info["Title"] = submission.title
            submission_info["Content"] = submission.selftext
            reddit_data.append(submission_info)

    if personnel_info[1] is not None:
        gm_search = subreddit_search.search(personnel_info[1], time_filter='year')
        for submission in gm_search:
            submission_info = {}
            submission_info["Title"] = submission.title
            submission_info["Content"] = submission.selftext
            reddit_data.append(submission_info)

    df = pd.DataFrame.from_dict(reddit_data)
    df.to_csv(f'Reddit Data/{team_name} FO Data.csv', encoding='utf-8')