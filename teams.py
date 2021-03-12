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

def get_players_ml(of):
    players=[]
    for i in range (0, 32):
        players.append(int.from_bytes(of.data[ml_players_relink_offset + (i * 2) : ml_players_relink_offset + (i * 2) + 2], byteorder='little'))
    return players

def get_formation(of, team_id):
    if 0 <= team_id <= 63:
        formation_data = of.data[nations_formation_data_offset + (team_id * formation_data_size) : nations_formation_data_offset + formation_data_size + (team_id * formation_data_size) ]
    elif 64 <= team_id <= 201:
        formation_data = of.data[clubs_formation_data_offset + ((team_id - 64) * formation_data_size) : clubs_formation_data_offset + formation_data_size + ((team_id - 64) * formation_data_size) ]
    return formation_data

def get_formation_generic(of, team_id):
    if 0 <= team_id <= 63:
        formation_data = of.data[nations_formation_data_offset + (team_id * formation_data_size) + 3 : nations_formation_data_offset + formation_data_size + (team_id * formation_data_size) ]
    elif 64 <= team_id <= 201:
        formation_data = of.data[clubs_formation_data_offset + ((team_id - 64) * formation_data_size) + 3: clubs_formation_data_offset + formation_data_size + ((team_id - 64) * formation_data_size) ]
    return formation_data

def set_formation(of, team_id, formation_data):
    if 0 <= team_id <= 63:
        for i, byte in enumerate(formation_data):
            of.data[nations_formation_data_offset+(team_id*formation_data_size) + i] = byte
    elif 64 <= team_id <= 201:
        for i, byte in enumerate(formation_data):
            of.data[clubs_formation_data_offset+((team_id - 64)*formation_data_size) + i] = byte

def set_formation_generic(of, team_id, formation_data):
    if 0 <= team_id <= 63:
        for i, byte in enumerate(formation_data):
            of.data[nations_formation_data_offset + 3 + (team_id*formation_data_size) + i] = byte
    elif 64 <= team_id <= 201:
        for i, byte in enumerate(formation_data):
            of.data[clubs_formation_data_offset+ 3 + ((team_id - 64)*formation_data_size) + i] = byte


clubs_formation_data_offset = 716932
nations_formation_data_offset = 676740
formation_data_size = 628
nations_players_relink_offset = 664054
clubs_players_relink_offset = 667458
ml_players_relink_offset = 676290
nations_players_relink_size = 46
clubs_players_relink_size = 64
