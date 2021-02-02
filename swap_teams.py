import os
from COFPES_OF_Editor_5.editor.option_file import OptionFile

def read_data(file_to_read,pos,grab):
    with open(file_to_read,'rb') as opened_file:
        opened_file.seek(pos,0)
        grabed_data=opened_file.read(grab)
    return grabed_data

def encrypt_and_save(temp_file,of):
    if temp_file=="":
        return False
    try:
        with open(temp_file, "r+b") as binary_file:    
            #antes de guardar el archivo
            #binary_file.seek(0,0)
            of.data = bytearray(binary_file.read())
            # Save/encrypt the option file
            #print("Saving option file...")
            of.save_option_file()
            #print("Option file saved.")
            #os.remove("temp.bin")
        return True
    except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
        return False


def swap_teams_data(temp_file,team_a_id,team_b_id):
    #print(type(team_a_id))
    #print(type(team_b_id))
    if team_a_id==team_b_id:
        return False
    team_a_players_relink = read_data(temp_file,clubs_players_relink_offset+(team_a_id*clubs_players_relink_size),clubs_players_relink_size)
    team_b_players_relink = read_data(temp_file,clubs_players_relink_offset+(team_b_id*clubs_players_relink_size),clubs_players_relink_size)

    team_a_jersey_number = read_data(temp_file,clubs_jersey_number_offset+(team_a_id*clubs_jersey_number_size),clubs_jersey_number_size)
    team_b_jersey_number = read_data(temp_file,clubs_jersey_number_offset+(team_b_id*clubs_jersey_number_size),clubs_jersey_number_size)

    team_a_name=read_data(temp_file,clubs_names_offset+(team_a_id*clubs_names_distance),clubs_names_size)
    team_b_name=read_data(temp_file,clubs_names_offset+(team_b_id*clubs_names_distance),clubs_names_size)

    #print(team_a_name.decode('utf8'))
    #print(team_b_name.decode('utf8'))

    team_a_three_letter_name=read_data(temp_file,three_letter_clubs_name_offset+(team_a_id*clubs_names_distance),three_letter_clubs_name_size)
    team_b_three_letter_name=read_data(temp_file,three_letter_clubs_name_offset+(team_b_id*clubs_names_distance),three_letter_clubs_name_size)

    #print(team_a_three_letter_name.decode('utf8'))
    #print(team_b_three_letter_name.decode('utf8'))

    team_a_formation_data = read_data(temp_file,club_formation_data_offset+(team_a_id*team_formation_data_size),team_formation_data_size)
    team_b_formation_data = read_data(temp_file,club_formation_data_offset+(team_b_id*team_formation_data_size),team_formation_data_size)

    #Now we write our data in the temporary file to later save it to the encrypted OF

    with open(temp_file, "r+b") as binary_file:
        #Here we swap players from team A to team B offsets location
        binary_file.seek(clubs_players_relink_offset+(team_b_id*clubs_players_relink_size),0)
        binary_file.write(team_a_players_relink)
        binary_file.seek(clubs_players_relink_offset+(team_a_id*clubs_players_relink_size),0)
        binary_file.write(team_b_players_relink)
        
        #Here we swap jersey number team A to team B offsets location
        binary_file.seek(clubs_jersey_number_offset+(team_b_id*clubs_jersey_number_size),0)
        binary_file.write(team_a_jersey_number)
        binary_file.seek(clubs_jersey_number_offset+(team_a_id*clubs_jersey_number_size),0)
        binary_file.write(team_b_jersey_number)
        
        #Here we swap team names team A to team B offsets location
        binary_file.seek(clubs_names_offset+(team_b_id*clubs_names_distance),0)
        binary_file.write(team_a_name)
        binary_file.seek(clubs_names_offset+(team_a_id*clubs_names_distance),0)
        binary_file.write(team_b_name)
        
        #Here we swap 3 letters name team A to team B offsets location
        binary_file.seek(three_letter_clubs_name_offset+(team_b_id*clubs_names_distance),0)
        binary_file.write(team_a_three_letter_name)
        binary_file.seek(three_letter_clubs_name_offset+(team_a_id*clubs_names_distance),0)
        binary_file.write(team_b_three_letter_name)

        #Here we swap formation data team A to team B offsets location
        binary_file.seek(club_formation_data_offset+(team_b_id*team_formation_data_size),0)
        binary_file.write(team_a_formation_data)
        binary_file.seek(club_formation_data_offset+(team_a_id*team_formation_data_size),0)
        binary_file.write(team_b_formation_data)

        #print("Temporary file changed")
    return True

#Offsets definition
nations_players_relink_offset = 0xA21F6
nations_players_relink_size = 0x2E
clubs_players_relink_offset = 0xA2F42
clubs_players_relink_size = 0x40
nation_jersey_number_offset = 0xA0930
nation_jersey_number_size = 0x17
clubs_jersey_number_offset = 0xA0FD6
clubs_jersey_number_size = 0x20
clubs_names_offset = 0xC4318
clubs_names_size = 0x30
three_letter_clubs_name_offset = 0XC4361
three_letter_clubs_name_size = 0x3
clubs_names_distance = 0x8C
#nations_kicker_captain_offset = 0xA53EE
#clubs_kicker_captain_offset = 0xAF0EE
#kicker_captain_size = 0x6
club_formation_data_offset = 0xAF084
team_formation_data_size = 0x274