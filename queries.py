create_ps_table = '''
        CREATE TABLE IF NOT EXISTS player_stats(
        name VARCHAR(50) NOT NULL,
        org VARCHAR(50) NOT NULL,
        acs INTEGER NOT NULL,
        kills INTEGER NOT NULL,
        deaths INTEGER NOT NULL,
        assist INTEGER NOT NULL,
        kd INTEGER NOT NULL,
        kast INTEGER NOT NULL,
        adr INTEGER NOT NULL,
        hs INTEGER NOT NULL,
        firstkill INTEGER NOT NULL,
        firstdeath INTEGER NOT NULL,
        fkfd INTEGER NOT NULL,
        agent VARCHAR(50) NOT NULL,
        map VARCHAR(50) NOT NULL,
        opponent VARCHAR(50) NOT NULL,
        outcome VARCHAR(50) NOT NULL,
        date VARCHAR(50) NOT NULL
        );
        '''

insert_players = """INSERT INTO player_stats (name, org, acs, kills, deaths, assist, kd, kast, adr, hs, firstkill, 
firstdeath, fkfd, agent, map, opponent, outcome, date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
%s) """


weather_create_table = '''
        CREATE TABLE IF NOT EXISTS weather(
        weather_desc VARCHAR(50) NOT NULL,
        temp INTEGER NOT NULL,
        feels_like INTEGER NOT NULL,
        humidity INT NOT NULL,
        date VARCHAR(50) NOT NULL
        );
        '''

weather_insert_query = """INSERT INTO weather (weather_desc, temp, feels_like, humidity, date) VALUES (%s,%s,%s,%s,%s)"""

search_players = """SELECT * FROM player_stats"""