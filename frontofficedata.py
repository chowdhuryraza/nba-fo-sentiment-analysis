import requests
from collections import defaultdict
from dotenv import load_dotenv
import os

load_dotenv()


nba_team_names = {"76ers", "Bucks", "Bulls", "Celtics", "Cavs", "Clippers", "Grizzlies", 
                  "Hawks", "Heat", "Hornets", "Jazz", "Kings", "Knicks", "Lakers", "Magic", 
                  "Mavericks", "Nets", "Nuggets", "Pacers", "Pelicans", "Pistons", "Raptors", 
                  "Rockets", "Spurs", "Suns", "Thunder", "Trail Blazers", "Timberwolves", 
                  "Warriors", "Wizards"}
nba_teams_personnel = defaultdict(list)
added_teams = set()

headers = {"accept": "application/json"}

try:
    url = f"https://api.sportradar.com/nba/trial/v8/en/league/teams.json?api_key={os.getenv('SPORTRADAR_API_KEY')}"

    response = requests.get(url, headers=headers)
except BaseException as e:
    print("Error: ", e)


for team in (response.json()["teams"]):
    if team["name"] in nba_team_names and team["name"] not in added_teams:
        added_teams.add(team["name"])

        try:
            team_info_url = f"https://api.sportradar.com/nba/trial/v8/en/teams/{team['id']}/profile.json?api_key={os.getenv('SPORTRADAR_API_KEY')}"
            team_info_response = requests.get(team_info_url, headers=headers).json()

            if "president" not in team_info_response: 
                nba_teams_personnel[team["name"]].append(None)
            else: 
                nba_teams_personnel[team["name"]].append(team_info_response["president"])
            if "general_manager" not in team_info_response: 
                nba_teams_personnel[team["name"]].append(None)
            else: 
                nba_teams_personnel[team["name"]].append(team_info_response["general_manager"])
        except BaseException as e:
            print("Error: ", e)


nba_personnel_data  = {'76ers': ['Daryl Morey', 'Elton Brand'], 
 'Bucks': ['Peter Feigin', 'Jon Horst'], 
 'Bulls': ['Arturas Karnisovas', 'Marc Eversley'],
 'Cavs': ['Koby Altman', None], 
 'Celtics': ['Rich Gotham', 'Brad Stevens'], 
 'Clippers': ['Lawrence Frank', 'Trent Redden'], 
 'Grizzlies': ['Jason Wexler', 'Zachary Kleiman'], 
 'Hawks': ['Steve Koonin', 'Landry Fields'], 
 'Heat': ['Pat Riley', 'Andy Elisburg'], 
 'Hornets': [None, 'Jeff Peterson'], 
 'Jazz': ['Jim Olson', 'Justin Zanik'], 
 'Kings': ['John Rinehart', 'Monte McNair'], 
 'Knicks': ['Leon Rose', None], 
 'Lakers': ['Jeanie Buss', 'Rob Pelinka'], 
 'Magic': ['Jeff Weltman', 'Anthony Parker'], 
 'Mavericks': ['Cynthia Marshall', 'Nico Harrison'], 
 'Nets': ['Sam Zussman', 'Sean Marks'], 
 'Nuggets': ['Josh Kroenke', 'Calvin Booth'], 
 'Pacers': ['Kevin Pritchard', 'Chad Buchanan'], 
 'Pelicans': ['Dennis Lauscha', 'Trajan Langdon'], 
 'Pistons': ['Trajan Langdon', None], 
 'Raptors': ['Masai Ujiri', 'Bobby Webster'], 
 'Rockets': ['Gretchen Sheirr', 'Rafael Stone'], 
 'Spurs': ['Gregg Popovich', 'Brian Wright'], 
 'Suns': ['James Jones', 'James Jones'], 
 'Thunder': [None, 'Sam Presti'], 
 'Timberwolves': ['Tim Connelly', 'Tim Connelly'], 
 'Trail Blazers': ['Dewayne Hankins', 'Joe Cronin'], 
 'Warriors': ['Brandon Schneider', 'Mike Dunleavy Jr.'], 
 'Wizards': ['Michael Winger', 'Will Dawkins']}