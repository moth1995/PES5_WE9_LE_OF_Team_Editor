def get_players_nations(of, team_id):
    players=[]
    for i in range (0, 23):
        players.append(int.from_bytes(of.data[nations_players_relink_offset + (i * 2) + (team_id * nations_players_relink_size) : nations_players_relink_offset + (i * 2) + 2  + (team_id * nations_players_relink_size)], byteorder='little'))
    return players

def get_players_clubs(of, team_id):
    team_id-=64
    players=[]
    for i in range (0, 32):
        players.append(int.from_bytes(of.data[clubs_players_relink_offset + (i * 2) + (team_id * clubs_players_relink_size) : clubs_players_relink_offset + (i * 2) + 2 + (team_id * clubs_players_relink_size)], byteorder='little'))
    return players

nations_players_relink_offset = 664054
clubs_players_relink_offset = 667458
nations_players_relink_size = 46
clubs_players_relink_size = 64
