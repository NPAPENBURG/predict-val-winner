from bs4 import BeautifulSoup
import requests
import psycopg2
from queries import insert_players, search_players

# Variables to connect to postgresql
DBNAME = 'tjxowylx'
USER = 'tjxowylx'
PASSWORD = 'TDkJKWZgU_nRKiCj84cyMNYueF0pYlKg'
HOST = 'castor.db.elephantsql.com'

# Connecting to PostgresSQL
PG_CONN = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
PG_CURS = PG_CONN.cursor()

# URL FOR THE MATCHES
url = 'https://www.vlr.gg/69877/cloud9-vs-100-thieves-champions-tour-north-america-stage-1-challengers-w1/?game=70808&tab=overview'

# USING REQUESTS TO PULL THE URL
result = requests.get(url)
# CREATING THE URL INTO A HTML USING BEAUTIFULSOUP
doc = BeautifulSoup(result.text, "html.parser")

# GETTING BOTH TEAMS
teams = doc.findAll(class_='wf-title-med')
# CLEANING TO GET FIRST TEAM NAME
team1 = teams[0].string.strip()
# CLEANING TO GET SECOND TEAM NAME
team2 = teams[1].string.strip()

# Getting the scores of the Best of 3.  EXAMPLE 2-0 // 2-1
winning_team = doc.findAll(class_='match-header-vs-score-winner')
winning_score = int(winning_team[0].text.strip())

losing_team = doc.findAll(class_='match-header-vs-score-loser')
losing_score = int(losing_team[0].text.strip())
print()

# VARIABLES USED TO HOLD DATA
players_stats = []
game_scores = []
maps = []


def agentpool(string):
    '''this function is used to get a player's agent for that match'''
    agentlist = ['sova', 'jett', 'astra', 'viper', 'chamber', 'kayo', 'skye', 'raze', 'sage', 'cypher', 'reyna',
                 'breach', 'killjoy']
    for agent in agentlist:
        if agent in string:
            return agent


# if losing score is 0 that means only 2 games were played
# so we only need information for those 2 games
if losing_score == 0:
    # grabbing score information from the html using beautiful soup
    scores = doc.findAll(class_='vm-stats-game-header')
    agents = doc.findAll(class_='stats-sq mod-agent small')
    date = doc.findAll(class_='moment-tz-convert')

    agent_count = 0

    # This for loop will grab score information and map names
    for num in range(2):
        # storing match score the information into a list of strings
        list = " ".join(scores[num].text.split()).split()
        # Grabbing team ones score and turning it into an int
        team1_score = int(list[0])
        # Grabbing team twos score and turning it into an int
        team2_score = int(list[-1])
        # Save the scores as a tuple into a list
        game_scores.append((team1_score, team2_score))

        # getting the maps played
        map = doc.findAll('span', attrs={'style': 'position: relative;'})
        # getting the map name
        map = str(map[num].text).replace("PICK", "").strip()
        # save the map to the maps list
        maps.append(map)

    ### BREAK THE BELOW DOWN
    # Team 1 Game 1
    player_stats = doc.findAll('tr')
    # This for loop will gather the first teams stats for each players
    for player in player_stats[1:6]:
        # Empty list to start players stats
        player_stats = []
        # For loop to get players stats and clean them
        for stat in player.text.split():
            # Saving players cleaned stats to players_stats
            player_stats.append(stat.replace('/', '').replace('%', '').replace('%', '').replace('+', ''))
        # Saving the players used agent to players_stats
        player_stats.append(agentpool(str(agents[agent_count])))
        agent_count += 1
        # Saving the map played to player_stats
        player_stats.append(maps[0])
        # Saving the opponent to player_stats
        player_stats.append(team2)

        # If team 1 score is higher than team 2 save win. Otherwise, Save Lose to player_stats
        if game_scores[0][0] > game_scores[0][1]:
            player_stats.append('Win')
        else:
            player_stats.append('Lose')
        # Saving the game date to player_stats
        player_stats.append(date[0].text.strip())
        # Save the player_stats to the players_stats list at the top of this script
        players_stats.append(player_stats)

    # Team 2 Game 1
    player_stats = doc.findAll('tr')
    # This for loop will gather the first teams stats for each player
    for player in player_stats[7:12]:
        # Empty list to start players stats
        player_stats = []
        # For loop to get players stats and clean them
        for stat in player.text.split():
            # Saving players cleaned stats to players_stats
            player_stats.append(stat.replace('/', '').replace('%', '').replace('%', '').replace('+', ''))
        # Saving the players used agent to players_stats
        player_stats.append(agentpool(str(agents[agent_count])))
        agent_count += 1
        # Saving the map played to player_stats
        player_stats.append(maps[0])
        # Saving the opponent to player_stats
        player_stats.append(team1)
        # If team 2 score is higher than team 1 save win. Otherwise, Save Lose to player_stats
        if game_scores[0][0] < game_scores[0][1]:
            player_stats.append('Win')
        else:
            player_stats.append('Lose')
        # Saving the game date to player_stats
        player_stats.append(date[0].text.strip())
        # Save the player_stats to the players_stats list at the top of this script
        players_stats.append(player_stats)

    # Team 1 Game 2
    player_stats = doc.findAll('tr')
    # This for loop will gather the first teams stats for each player
    for player in player_stats[25:30]:
        # Empty list to start players stats
        player_stats = []
        # For loop to get players stats and clean them
        for stat in player.text.split():
            # Saving players cleaned stats to players_stats
            player_stats.append(stat.replace('/', '').replace('%', '').replace('%', '').replace('+', ''))
        # Saving the players used agent to players_stats
        player_stats.append(agentpool(str(agents[agent_count])))
        agent_count += 1
        # Saving the map played to player_stats
        player_stats.append(maps[1])
        # Saving the opponent to player_stats
        player_stats.append(team2)
        # If team 1 score is higher than team 2 save win. Otherwise, Save Lose to player_stats
        if game_scores[0][0] > game_scores[0][1]:
            player_stats.append('Win')
        else:
            player_stats.append('Lose')
        # Saving the game date to player_stats
        player_stats.append(date[0].text.strip())
        # Save the player_stats to the players_stats list at the top of this script
        players_stats.append(player_stats)

    # Team 2 Game 2
    player_stats = doc.findAll('tr')
    # This for loop will gather the first teams stats for each player
    for player in player_stats[31:36]:
        # Empty list to start players stat
        player_stats = []
        # For loop to get players stats and clean them
        for stat in player.text.split():
            # Saving players cleaned stats to players_stats
            player_stats.append(stat.replace('/', '').replace('%', '').replace('%', '').replace('+', ''))
        # Saving the players used agent to players_stats
        player_stats.append(agentpool(str(agents[agent_count])))
        agent_count += 1
        # Saving the map played to player_stats
        player_stats.append(maps[1])
        # Saving the opponent to player_stats
        player_stats.append(team1)
        # If team 1 score is higher than team 2 save win. Otherwise, Save Lose to player_stats
        if game_scores[0][0] < game_scores[0][1]:
            player_stats.append('Win')
        else:
            player_stats.append('Lose')
        # Saving the game date to player_stats
        player_stats.append(date[0].text.strip())
        # Save the player_stats to the players_stats list at the top of this script
        players_stats.append(player_stats)

    # Searching the players_stats table to check on dubs
    PG_CURS.execute(search_players)
    # Saving the result of the search
    result = PG_CURS.fetchall()
    # creating a list of tuples
    player_searched = [i for i in result]
    # converting all values in each tuple into a str
    converted_player_searched = [tuple(str(x) for x in tup) for tup in player_searched]

    # For loop to get each player in players_stats
    for player in players_stats:
        # converting player into a tuple and checking if its in converted_player_searched
        if (tuple(player)) in converted_player_searched:
            # if tuple is in converted_player_searched let us know
            print('This players stats have already been added')
        else:
            # Otherwise, let's add it to the Database
            PG_CURS.execute(insert_players, player)

    PG_CONN.commit()






