from COFPES_OF_Editor_5.editor.utils.common_functions import zero_fill_right_shift, to_int, to_byte

# Thanks to evo-web's user mattmid for helping me with various player attributes!

# This function is use to get option file data into integer and assign it to a variable
from teams import get_players_nations, get_players_clubs, get_players_ml


def get_value(of, player_id, offset, shift, mask, stat_name):
    i = start_address + 48 + player_id * 124 + offset
    if player_id > last_player_id:
        #print((player_id - first_edited_id))
        i = start_address_edited + 48 + (player_id - first_edited_id) * 124 + offset
    #print(i)
    #print("{0:x}".player_hair_shapet(of.data[i]))
    #print(of.data[i])
    #print("left shift previous value by 8 bytes")
    #print("{0:b}".player_hair_shapet((to_int(of.data[i]) << 8)))
    #print("previous offset value in binary")
    #print("{0:b}".player_hair_shapet(to_int(of.data[(i-1)])))
    #j = to_int(of.data[i]) << 8 | to_int(of.data[(i - 1)])
    j = (of.data[i]) << 8 | (of.data[(i - 1)])
    #print("result of OR operation between two previous values")
    #print("{0:b}".player_hair_shapet(j))
    j = zero_fill_right_shift(j,shift)
    #print("previous value after apply zero fill right shift by " + str(shift))
    #print("{0:b}".player_hair_shapet(j))
    j &= mask
    #print(stat_name)
    #print("previous value after AND operation with " + str(mask))
    #print("{0:b}".player_hair_shapet(j))
    #print(j)
    return j


#Most of the code for the function below was taken from peterc10 file player.py thanks a lot pete!

def get_names(player_id, of):
    name = "???"
    name_bytes_length = 32
    player_offset = start_address + player_id * 124
    if player_id>last_player_id:
        player_offset = start_address_edited + ((player_id - first_edited_id) * 124)
    if (
        player_id > 0
        and (player_id <= last_player_id or player_id >= first_edited_id)
        and player_id < first_edited_id + total_edit
    ):
        all_name_bytes = of.data[
             player_offset : player_offset + name_bytes_length
        ]
        name_only_bytes = bytearray(name_bytes_length // 2)

        for i in range(0, name_bytes_length, 2):
            name_only_bytes[i // 2] = all_name_bytes[i]

        name = name_only_bytes.partition(b"\0")[0]
        name = "".join(map(chr, name))

        if not name:
            no_name_prefixes = {
                first_edited_id: "Edited",
                first_unused: "Unused",
                1: "Unknown",
            }

            for address, address_prefix in no_name_prefixes.items():
                if player_id >= address:
                    prefix = address_prefix
                    break

            name = f"{prefix} ({player_id})"
        #get the shirt name
        shirt_name_address = player_offset + 32
        name_byte_array = of.data[
            shirt_name_address : shirt_name_address
            + name_bytes_length // 2
        ]
        #print(player_id)
        shirt_name = name_byte_array.partition(b"\0")[0].decode()

    #print (name)
    #print (shirt_name)
    return name, shirt_name


# This function is use to set/modify a value from any source to the option file into byte

def set_value(of, player_id, offset, shift, mask, new_value):
    #print (start_address, player_id * 124, offset)
    i = start_address + 48 + (player_id * 124) + offset
    if (player_id > last_player_id):
        i = start_address_edited + 48 + ((player_id - first_edited_id) * 124) + offset
    #j = to_int(of.data[i]) << 8 | to_int(of.data[(i - 1)])
    #print(i)
    j = (of.data[i]) << 8 | (of.data[(i - 1)])
    k = 0xFFFF & (mask << shift ^ 0xFFFFFFFF)
    j &= k
    new_value &= mask
    new_value <<= shift
    new_value = j | new_value
    #print(type(of.data[(i - 1)]))
    #of.data[(i - 1)] = to_byte(new_value & 0xFF)
    of.data[(i - 1)] = (new_value & 0xFF)
    #of.data[i] = to_byte(zero_fill_right_shift(new_value,8))
    of.data[i] = (zero_fill_right_shift(new_value,8))



def set_name(of, player_id, new_name):
    name_bytes_length = 32
    max_name_size = 15
    new_name = new_name[: max_name_size]
    if (new_name == "Unknown (" + str(player_id) + ")" or new_name == "Edited (" + str(player_id) + ")" or new_name == "Unused (" + str(player_id) + ")" or new_name == ""):
        player_name_bytes=[0] * name_bytes_length
    else:
        player_name_bytes = [0] * name_bytes_length
        new_name_bytes = str.encode(new_name, "utf-16-le")
        player_name_bytes[: len(new_name_bytes)] = new_name_bytes
    player_offset = start_address + player_id * 124
    if player_id>last_player_id:
        player_offset = start_address_edited + ((player_id - first_edited_id) * 124)
    if (
        player_id > 0
        and (player_id <= last_player_id or player_id >= first_edited_id)
        and player_id < first_edited_id + total_edit
    ):
        for i, byte in enumerate(player_name_bytes):
            of.data[player_offset + i] = byte

def set_shirt_name(of, player_id, new_shirt_name):
    max_name_size = 15
    shirt_name_bytes_length = 16
    player_offset = start_address + player_id * 124
    if player_id>last_player_id:
        player_offset = start_address_edited + ((player_id - first_edited_id) * 124)
    if (
        player_id > 0
        and (player_id <= last_player_id or player_id >= first_edited_id)
        and player_id < first_edited_id + total_edit
    ):

        shirt_name_address = player_offset + 32
        new_name = new_shirt_name[: max_name_size].upper()

        player_shirt_name_bytes = [0] * shirt_name_bytes_length
        new_name_bytes = str.encode(new_name)
        player_shirt_name_bytes[: len(new_name_bytes)] = new_name_bytes

        for i, byte in enumerate(player_shirt_name_bytes):
            of.data[shirt_name_address + i] = byte


def get_stats(player_id, of, rare_stats_flag):
    # Basic seetings
    player_name, player_shirt_name = get_names(player_id, of)
    player_callName = get_value(of, player_id, 49-48, 0, 65535, "Callname ID")
    player_nation = nationalities[get_value(of, player_id, 111-48, 2, 127, "Nationality")]
    player_foot = get_value(of, player_id, 53-48, 0, 1, "Foot")
    if player_foot == 0:
        player_foot = "R"
    else:
        player_foot = "L"
    player_injury = get_value(of, player_id, 35, 3, 3, "Injury T")
    if player_injury == 2:
        player_injury = "A"
    elif player_injury == 1:
        player_injury = "B"
    else:
        player_injury = "C"
    player_dribSty = get_value(of, player_id, 54-48, 0, 3, "Dribble Style") + 1
    player_freekick = get_value(of, player_id, 53-48, 1, 15, "FK Style") + 1
    player_pkStyle = get_value(of, player_id, 53-48, 5, 7, "PK Style") + 1
    player_dkSty = get_value(of, player_id, 54-48, 2, 3, "DK Style") + 1
    player_age = get_value(of, player_id, 110-48, 5, 31, "Age") +15
    player_goal_c1 = get_value(of,player_id,85-48, 1, 127, "GOAL CELEBRATION 1")
    player_goal_c2 = get_value(of,player_id,86-48, 0, 127, "GOAL CELEBRATION 2")
    # Offset for growth type is rigth, but i cant get the proper value in any elif, also this value seems to be related to salary of player
    player_growth_type= get_value(of,player_id,87-48, 0, 0xff, "Growth type")
    
    # Position settings
    player_regPos = get_value(of, player_id, 54-48, 4, 15, "Registered position")
    player_gk = get_value(of, player_id, 56-48, 6, 1, "GK")
    player_cbwS = get_value(of, player_id, 56-48, 7, 1, "CWP")
    player_cbt = get_value(of, player_id, 60-48, 4, 1, "CBT")
    player_sb = get_value(of, player_id, 60-48, 5, 1, "SB")
    player_dm = get_value(of, player_id, 60-48, 6, 1, "DM")
    player_wb = get_value(of, player_id, 60-48, 7, 1, "WB")
    player_cm = get_value(of, player_id, 64-48, 4, 1, "CM")
    player_sm = get_value(of, player_id, 64-48, 5, 1, "SM")
    player_om = get_value(of, player_id, 64-48, 6, 1, "AM")
    player_wg = get_value(of, player_id, 64-48, 7, 1, "WG")
    player_ss = get_value(of, player_id, 68-48, 4, 1, "SS")
    player_cf = get_value(of, player_id, 68-48, 5, 1, "CF")
    player_favSide = get_value(of, player_id, 68-48, 6, 3, "Fav side")

    if player_foot == "R":
        if player_favSide == 0:
            player_favSide = "R"
        elif player_favSide == 1:
            player_favSide = "L"
        else:
            player_favSide = "B"
    elif player_foot == "L":
        if player_favSide == 0:
            player_favSide = "L"
        elif player_favSide == 1:
            player_favSide = "R"
        else:
            player_favSide = "B"

    # Abilities
    player_wfa = get_value(of, player_id, 82-48, 5, 7, "W Foot Acc") + 1
    player_wff = get_value(of, player_id, 83-48, 0, 7, "W Foot Freq") + 1
    player_attack = get_value(of, player_id, 55-48, 0, 127, "Attack")
    player_defence = get_value(of, player_id, 55-48, 7, 127, "Defense")
    player_balance = get_value(of, player_id, 57-48, 0, 127, "Balance")
    player_stamina = get_value(of, player_id, 57-48, 7, 127, "Stamina")
    player_speed = get_value(of, player_id, 58-48, 6, 127, "Speed")
    player_accel = get_value(of, player_id, 59-48, 5, 127, "Accel")
    player_response = get_value(of, player_id, 61-48, 0, 127, "Response")
    player_agility = get_value(of, player_id, 61-48, 7, 127, "Agility")
    player_dribAcc = get_value(of, player_id, 62-48, 6, 127, "Drib Acc")
    player_dribSpe = get_value(of, player_id, 63-48, 5, 127, "Drib Spe")
    player_sPassAcc = get_value(of, player_id, 65-48, 0, 127, "S Pass Acc")
    player_sPassSpe = get_value(of, player_id, 65-48, 7, 127, "S Pass Spe")
    player_lPassAcc = get_value(of, player_id, 66-48, 6, 127, "L Pass Acc")
    player_lPassSpe = get_value(of, player_id, 67-48, 5, 127, "L Pass Spe")
    player_shotAcc = get_value(of, player_id, 69-48, 0, 127, "Shot Acc")
    player_shotPow = get_value(of, player_id, 69-48, 7, 127, "Shot Power")
    player_shotTec = get_value(of, player_id, 70-48, 6, 127, "Shot Tech")
    player_fk = get_value(of, player_id, 71-48, 5, 127, "FK Acc")
    player_curling = get_value(of, player_id, 73-48, 0, 127, "Curling")
    player_heading = get_value(of, player_id, 73-48, 7, 127, "Heading")
    player_jump = get_value(of, player_id, 74-48, 6, 127, "Jump")
    player_tech = get_value(of, player_id, 77-48, 0, 127, "Tech")
    player_aggress = get_value(of, player_id, 77-48, 7, 127, "Aggression")
    player_mental = get_value(of, player_id, 78-48, 6, 127, "Mentality")
    player_consistency = get_value(of, player_id, 81-48, 7, 7, "Consistency") + 1
    player_gkAbil = get_value(of, player_id, 79-48, 5, 127, "GK")
    player_team = get_value(of, player_id, 81-48, 0, 127, "Team Work")
    player_condition = get_value(of, player_id, 82-48, 2, 7, "Condition") + 1
    
    # Special Abilities
    player_drib = get_value(of, player_id, 72-48, 4, 1, "Dribbling")
    player_dribKeep = get_value(of, player_id, 72-48, 5, 1, "Anti-Dribble")
    player_post = get_value(of, player_id, 80-48, 4, 1, "Post")
    player_posit = get_value(of, player_id, 72-48, 6, 1, "Positioning")
    player_offside = get_value(of, player_id, 72-48, 7, 1, "Reaction")
    player_linePos = get_value(of, player_id, 80-48, 5, 1, "Line Position")
    player_midShot = get_value(of, player_id, 80-48, 6, 1, "Mid shooting")
    player_scorer = get_value(of, player_id, 76-48, 6, 1, "Scoring")
    player_play = get_value(of, player_id, 76-48, 4, 1, "Playmaking")
    player_pass = get_value(of, player_id, 76-48, 5, 1, "Passing")
    player_pk = get_value(of, player_id, 83-48, 6, 1, "Penalties")
    player_k11 = get_value(of, player_id, 76-48, 7, 1, "1-1 Scoring")
    player_longThrow = get_value(of, player_id, 84-48, 7, 1, "Long Throw")
    player_direct = get_value(of, player_id, 83-48, 7, 1, "1-T Pass")
    player_side = get_value(of, player_id, 80-48, 7, 1, "Side")
    player_centre = get_value(of, player_id, 83-48, 5, 1, "Centre")
    player_outside = get_value(of, player_id, 84-48, 0, 1, "Outside")
    player_man = get_value(of, player_id, 84-48, 1, 1, "Marking")
    player_dLine = get_value(of, player_id, 84-48, 4, 1, "D-L Control")
    player_slide = get_value(of, player_id, 84-48, 2, 1, "Sliding")
    player_cover = get_value(of, player_id, 84-48, 3, 1, "Cover")
    player_keeperPK = get_value(of, player_id, 84-48, 5, 1, "Penalty GK")
    player_keeper11 = get_value(of, player_id, 84-48, 6, 1, "1-on-1 GK")
    
    # Player appearence settings
    # Head
    
    # Face menu
    player_face_type = get_value(of,player_id,108-48,2, 3, "face TYPE")
    if player_face_type == 0: 
        player_face_type = "BUILD"
    elif player_face_type == 1:
        player_face_type = "PRESET SPECIAL"
    elif player_face_type == 2:
        player_face_type = "PRESET NORMAL"
    else:
        player_face_type = "ERROR"
    player_skin_colour = get_value(of,player_id, 91-48,1, 3, "skin colour") + 1    
    player_head_height = get_value(of,player_id, 91-48, 3, 15, "head height") - 7
    player_head_width = get_value(of,player_id, 91-48, 7, 15, "head width") - 7
    player_face_id = get_value(of,player_id, 53,3, 0x1FF, "face id") + 1
    player_head_ov_pos = get_value(of,player_id, 124-48,5, 7, "Head overall position") - 3
    
    # Brows menu
    player_brows_type = get_value(of,player_id, 119-48, 5, 31, "Brows type") + 1
    player_brows_angle = (get_value(of,player_id, 119-48, 2, 7, "Brown angle") - 3)*-1
    player_brows_height = (get_value(of,player_id, 118-48, 4, 7, "Brown height") - 3)*-1
    player_brows_spacing = (get_value(of,player_id, 118-48, 7, 7, "Brown spacing") - 3)*-1
    
    # Eyes menu
    player_eyes_type = get_value(of,player_id, 116-48, 3, 31, "Eyes type") + 1
    player_eyes_position = (get_value(of,player_id, 117-48, 0, 7, "Eye Position")-3)*-1
    player_eyes_angle = (get_value(of,player_id, 117-48, 3, 7, "Eye Angle") -3)*-1
    player_eyes_lenght = (get_value(of,player_id, 117-48, 6, 7, "Eye Length") -3)*-1
    player_eyes_width = (get_value(of,player_id, 118-48, 1, 7, "Eye Width") -3)*-1
    player_eyes_c1 = get_value(of,player_id, 94-48, 9, 3, "Eyes colour 1") + 1
    player_eyes_c2 = get_value(of,player_id, 95-48, 3, 15, "Eyes colour 2")
    if player_eyes_c2 == 0:
        player_eyes_c2 = "BLACK 1"
    elif player_eyes_c2 == 1:
        player_eyes_c2 = "BLACK 2"
    elif player_eyes_c2 == 2:
        player_eyes_c2 = "DARK GREY 1"
    elif player_eyes_c2 == 3:
        player_eyes_c2 = "DARK GREY 2"
    elif player_eyes_c2 == 4:
        player_eyes_c2 = "BROWN 1"
    elif player_eyes_c2 == 5:
        player_eyes_c2 = "BROWN 2"
    elif player_eyes_c2 == 6:
        player_eyes_c2 = "LIGHT BLUE 1"
    elif player_eyes_c2 == 7:
        player_eyes_c2 = "LIGHT BLUE 2"
    elif player_eyes_c2 == 8:
        player_eyes_c2 = "BLUE 1"
    elif player_eyes_c2 == 9:
        player_eyes_c2 = "BLUE 2"
    elif player_eyes_c2 == 10:
        player_eyes_c2 = "GREEN 1"
    elif player_eyes_c2 == 11:
        player_eyes_c2 = "GREEN 2"
    else:
        player_eyes_c2 = "ERROR"
    
    # Nose menu
    player_nose_type = get_value(of,player_id,121-48, 0, 7, "Nose type") + 1
    player_nose_height = (get_value(of,player_id,121-48, 6, 7, "Nose height") - 3)*-1
    player_nose_width = (get_value(of,player_id,121-48, 3, 7, "Nose width") - 3)*-1
    
    # Cheeks menu
    player_cheecks_type = get_value(of,player_id,120-48, 2, 7, "cheeks type") + 1
    player_cheecks_shape = (get_value(of,player_id,120-48, 5, 7, "cheecks shape") - 3)*-1
    
    # Mouth menu
    player_mouth_type = get_value(of,player_id,122-48, 1, 31, "mouth type") + 1
    player_mouth_size = (get_value(of,player_id,123-48, 1, 7, "mouth type") - 3)*-1
    player_mouth_position = (get_value(of,player_id,122-48, 6, 7, "mouth position") - 3)*-1
    
    # Jaw menu
    player_jaw_type = get_value(of,player_id,123-48, 4, 7, "Jaw type") + 1
    player_jaw_chin = (get_value(of,player_id,123-48, 7, 7, "Jaw chin") - 3)*-1
    player_jaw_width = (get_value(of,player_id,124-48, 2, 7, "Jaw width") - 3)*-1

    # Hair menu
    # The variable below will get the Hairstyle id but we have to return many other variables such a hair type, shape, front, volume, darkness and bandana
    # Millions of thanks to Pato_lucas18 for this code who save me from doom
    player_hair =  get_value(of,player_id,93-48, 0, 2047, "Hair id")
    
    # Bald
    if 0 <= player_hair <= 3:
        player_hair_type = "BALD"
        player_hair_shape = player_hair + 1
        player_hair_front = 1
        player_hair_volume = 1
        player_hair_darkness = 1
        player_hair_bandana = 1
    # Buzz cut
    elif 4 <= player_hair <= 83:
        player_hair_type = "BUZZ CUT"
        player_hair_shape = 1
        player_hair_front = 1
        player_hair_volume = 1
        player_hair_darkness = 0
        player_hair_bandana = 1
        for c in range(4, player_hair + 1):
            player_hair_darkness += 1
            if player_hair_darkness == 5:
                player_hair_darkness = 1
                player_hair_front += 1
                if player_hair_front == 6:
                    player_hair_front = 1
                    player_hair_shape += 1
    # Very short 1
    elif 84 <= player_hair <= 107:
        player_hair_type = "VERY SHORT 1"
        player_hair_shape = 1
        player_hair_front = 0
        player_hair_volume = 1
        player_hair_darkness = 1
        player_hair_bandana = 1
        for c in range(84, player_hair +1 ):
            player_hair_front += 1
            if player_hair_front == 7:
                player_hair_front = 1
                player_hair_shape += 1
    # Very short 2
    elif 108 <= player_hair <= 152:
        player_hair_type = "VERY SHORT 2"
        player_hair_front = 0
        player_hair_volume = 1
        player_hair_darkness = 1
        player_hair_bandana = 1
        if player_hair >= 138:
            player_hair_shape = 4
            for c in range(138, player_hair + 1):
                player_hair_front += 1
                if player_hair_front == 6:
                    player_hair_front = 1
                    player_hair_shape += 1
        else:
            player_hair_shape = 1
            for c in range(108, player_hair + 1):
                player_hair_front += 1
                if player_hair_front == 11:
                    player_hair_front = 1
                    player_hair_shape += 1
    # Straight 1
    elif 153 <= player_hair <= 560:
        player_hair_type = "STRAIGHT 1"
        player_hair_shape = 1
        player_hair_front = 1
        player_hair_volume = 1
        player_hair_darkness = 1
        player_hair_bandana = 0
        for c in range(153, player_hair + 1):
            player_hair_bandana += 1
            if player_hair_bandana > 3 :
                player_hair_volume += 1
                player_hair_bandana = 1
                if player_hair_volume == 4 :
                    player_hair_front += 1
                    player_hair_volume = 1
                    if player_hair_front == 17 :
                        player_hair_shape += 1
                        player_hair_front = 1
                if player_hair_front >= 10:
                    player_hair_bandana = 4
    # Straight 2
    elif 561 <= player_hair <= 659:
        player_hair_type = "STRAIGHT 2"
        player_hair_shape = 1
        player_hair_front = 1
        player_hair_volume = 1
        player_hair_darkness = 1
        player_hair_bandana = 0
        for c in range(561, player_hair + 1):
            player_hair_bandana += 1
            if player_hair_bandana > 3:
                player_hair_volume += 1
                player_hair_bandana = 1
                if player_hair_volume == 4:
                    player_hair_front += 1
                    player_hair_volume = 1
                    if player_hair_front == 8:
                        player_hair_shape += 1
                        player_hair_front = 1
                if player_hair_front >= 3:
                    player_hair_bandana = 4
    # Curly 1
    elif 660 <= player_hair <= 863:
        player_hair_type = "CURLY 1"
        player_hair_shape = 1
        player_hair_front = 1
        player_hair_volume = 1
        player_hair_darkness = 1
        player_hair_bandana = 0
        for c in range(660, player_hair + 1):
            player_hair_bandana += 1
            if player_hair_bandana > 3 :
                player_hair_volume += 1
                player_hair_bandana = 1
                if player_hair_volume == 4 :
                    player_hair_front += 1
                    player_hair_volume = 1
                    if player_hair_front == 8 :
                        player_hair_shape += 1
                        player_hair_front = 1
                if player_hair_front >= 6:
                    player_hair_bandana = 4
    # Curly 2
    elif 864 <= player_hair <= 911:
        player_hair_type = "CURLY 2"
        player_hair_shape = 1
        player_hair_front = 1
        player_hair_volume = 0
        player_hair_darkness = 1
        player_hair_bandana = 1
        for c in range(864, player_hair + 1):
            player_hair_volume += 1
            if player_hair_volume == 3 :
                player_hair_front += 1
                player_hair_volume = 1
                if player_hair_front == 7 :
                    player_hair_shape += 1
                    player_hair_front = 1
    # Ponytail 1
    elif 912 <= player_hair <= 947:
        player_hair_type = "PONYTAIL 1"
        player_hair_shape = 1
        player_hair_front = 1
        player_hair_volume = 0
        player_hair_darkness = 1
        player_hair_bandana = 1
        for c in range(912, player_hair + 1):
            player_hair_volume += 1
            if player_hair_volume == 4 :
                player_hair_front += 1
                player_hair_volume = 1
                if player_hair_front == 5:
                    player_hair_shape += 1
                    player_hair_front = 1
    # Ponytail 2
    elif 948 <= player_hair <= 983:
        player_hair_type = "PONYTAIL 2"
        player_hair_shape = 1
        player_hair_front = 1
        player_hair_volume = 0
        player_hair_darkness = 1
        player_hair_bandana = 1
        for c in range(948, player_hair + 1):
            player_hair_volume += 1
            if player_hair_volume == 4 :
                player_hair_front += 1
                player_hair_volume = 1
                if player_hair_front == 5:
                    player_hair_shape += 1
                    player_hair_front = 1
    # Dreadlocks
    elif 984 <= player_hair <= 1007:
        player_hair_type = "DREADLOCKS"
        player_hair_shape = 1
        player_hair_front = 1
        player_hair_volume = 0
        player_hair_darkness = 1
        player_hair_bandana = 1
        for c in range(984, player_hair + 1):
            player_hair_volume += 1
            if player_hair_volume == 3 :
                player_hair_front += 1
                player_hair_volume = 1
                if player_hair_front == 5 :
                    player_hair_shape += 1
                    player_hair_front = 1
    # Pulled back
    elif 1008 <= player_hair <= 1025:
        player_hair_type = "PULLED BACK"
        player_hair_shape = 1
        player_hair_front = 0
        player_hair_volume = 1
        player_hair_darkness = 1
        player_hair_bandana = 1
        for c in range(1008, player_hair + 1):
            player_hair_front += 1
            if player_hair_front == 7:
                player_hair_shape += 1
                player_hair_front = 1
    # Special hair
    elif 1026 <= player_hair <= 2047:
        player_hair_type = "SPECIAL HAIRSTYLES"
        player_hair_shape = player_hair - 1025
        player_hair_front = 1
        player_hair_volume = 1
        player_hair_darkness = 1
        player_hair_bandana = 1        
    # Another case that should not happen... just to return a value :)
    else:
        player_hair_type = "OUT OF RANGE ERROR"
        player_hair_shape = player_hair
        player_hair_front = 1
        player_hair_volume = 1
        player_hair_darkness = 1
        player_hair_bandana = 1

    # Hair colour menu
    player_hair_colour_config = get_value(of, player_id, 94-48, 3, 63, "hair colour config") + 1
    player_hair_rgb_r = (get_value(of, player_id, 102-48, 5, 63, "hair colour rgb R") - 63)*-1
    player_hair_rgb_g = (get_value(of, player_id, 103-48, 3, 63, "hair colour rgb G") - 63)*-1
    player_hair_rgb_b = (get_value(of, player_id, 104-48, 1, 63, "hair colour rgb B") - 63)*-1
    # Hair bandana menu
    if player_hair_bandana==4:
        player_hair_bandana=1
    player_hair_bandana-=1
    player_hair_bandana_colour = get_value(of,player_id,109-48, 2, 7, "bandana colour") + 1
    # Cap menu
    player_cap = get_value(of, player_id, 98-48, 6, 1, "cap")
    player_cap_colour = get_value(of, player_id, 114-48, 3, 7, "cap colour") + 1
    # Facial hair menu
    player_facial_hair_type = get_value(of,player_id,95-48, 7, 127, "facial hair")
    player_facial_hair_colour = get_value(of,player_id,97-48, 0, 63, "facial hair colour") + 1
    # Sunglasses menu
    player_sunglasses = get_value(of,player_id,97-48, 6, 3, "Sun glasses type")
    player_sunglasses_colour = get_value(of,player_id,114-48, 0, 7, "Sun glasses colour") + 1
    
    # Physical settings
    player_height = get_value(of, player_id, 89-48, 0, 63, "Height") + 148
    player_weight = get_value(of, player_id, 89-48, 6, 127, "Weight")
    player_neck_length = get_value(of,player_id,105-48, 2, 15, "Neck Length") - 7
    player_neck_width = get_value(of,player_id,92-48, 3, 15, "Neck Width") - 7
    player_shoulder_height = get_value(of,player_id,109-48, 5, 15, "Shoulder Height") -7
    player_should_width = get_value(of,player_id,110-48, 1, 15, "Shoulder Width") - 7
    player_chest_measu = get_value(of,player_id,105-48, 6, 15, "Chest measurement") - 7
    player_waist_circu = get_value(of,player_id,106-48, 6, 15, "Waist Circ") -7
    player_arm_circu = get_value(of,player_id,106-48, 2, 15, "Arm Circumferemce") - 7
    player_leg_circu = get_value(of,player_id,107-48, 2, 15, "Leg Circumference") - 7
    player_calf_circu = get_value(of,player_id,107-48, 6, 15, "Calf Circ") - 7
    player_leg_length = get_value(of,player_id,108-48, 4, 15, "Leg Length") - 7
    body_parameters = [player_neck_length, player_neck_width, player_shoulder_height, player_should_width, player_chest_measu, player_waist_circu, player_arm_circu, 
    player_leg_circu, player_calf_circu, player_leg_length]
    player_body_type = body_types.index(body_parameters) + 1 if body_parameters in body_types else "Edited"

    # Boots/Accesories
    player_boot_type = get_value(of, player_id, 99-48, 9, 15, "boot type")
    player_boot_colour = get_value(of, player_id, 99-48, 13, 3, "boot COLOUR") + 1 
    player_neck_warm = get_value(of,player_id,98-48, 0, 1, "Neck Warmer")
    player_necklace_type = get_value(of,player_id,98-48, 1, 3, "Necklace type")
    player_necklace_colour = get_value(of,player_id,98-48, 3, 7, "Necklace colour") + 1
    player_wistband = get_value(of,player_id,98-48, 7, 3, "wistband")
    player_wistband_colour = get_value(of,player_id,99-48, 1, 7, "wistband colour") + 1
    player_friend_brace =  get_value(of,player_id,99-48, 4, 3, "friendship bracelate")
    player_friend_brace_colour =  get_value(of,player_id,99-48, 6, 7, "friendship bracelate colour") + 1
    player_gloves = get_value(of,player_id,104-48, 7, 1, "Gloves")
    player_finger_band = get_value(of,player_id,109-48, 0, 3, "Finger Band")
    player_shirt = get_value(of,player_id,92-48, 7, 1, "Shirt")
    player_sleeves =  get_value(of,player_id,96-48, 6, 3, "Sleeves")
    player_under_short =  get_value(of,player_id,100-48, 7, 1, "under short")
    player_under_short_colour =  get_value(of,player_id,101-48, 0, 7, "under short colour") + 1
    player_socks =  get_value(of,player_id,105-48, 0, 3, "Socks") + 1
    player_tape =  get_value(of,player_id,102-48, 4, 1, "Tape")

    # Rare stats
    player_cbwL = get_value(of, player_id, 59-48, 14, 1, "ASW")
    player_statX = get_value(of, player_id, 75-48, 5, 127, "StatX") + 1
    player_bff = get_value(of, player_id, 68-48, 6, 1, "B F Feint")
    player_gkKick = get_value(of, player_id, 68-48, 7, 1, "GK Kick")
    player_statEdited = get_value(of, player_id, 87-48, 7, 1, "Stat Edited")
    player_club = "Free Agent"
    for i in range(0,138):
        club_validation=get_players_clubs(of,i+64)
        #print(club_validation)
        if player_id in club_validation:
            player_club=of.clubs[i].name
            break
    ml_united_squad = get_players_ml(of)
    if player_id in ml_united_squad:
        player_club = "ML United"


    player_national_team = "Not Registered"
    for i in range(0,64):
        club_validation=get_players_nations(of,i)
        #print(club_validation)
        if player_id in club_validation:
            player_national_team=national_teams[i]
            break


    player_special_flag = ""
    if player_id in fake_players:
        player_special_flag = "Fake Player"
    elif player_id in elastico_players:
        player_special_flag = "Elastico Move"
    elif player_id in shop_players:
        player_special_flag = "Shop"
    elif player_id in ml_old:
        player_special_flag = "ML Old"
    elif player_id in ml_youth:
        player_special_flag = "ML Youth"
    list_csv=[
    
    # Here we return all the stats to make a beautiful csv file
    
    # Player basic settings
    player_id, player_name, player_shirt_name, player_callName, player_nation, player_age, player_foot, player_injury, 
    player_dribSty, player_freekick, player_pkStyle, player_dkSty, player_goal_c1, player_goal_c2,
    player_growth_type,
    
    # Player position settings
    player_regPos, player_favSide, player_gk, player_cbwS, player_cbt, player_sb, player_dm, player_wb, player_cm, player_sm, player_om, player_wg, player_ss, player_cf,
    
    # Player ability settings
    player_attack, player_defence, player_balance, player_stamina, player_speed, player_accel, player_response, player_agility, player_dribAcc, player_dribSpe, player_sPassAcc, 
    player_sPassSpe, player_lPassAcc, player_lPassSpe, player_shotAcc, player_shotPow, player_shotTec, player_fk, player_curling, player_heading, player_jump, player_tech, 
    player_aggress, player_mental, player_gkAbil, player_team, player_consistency, player_condition, player_wfa, player_wff,
    
    # Player special abilities settings
    player_drib, player_dribKeep, player_posit, player_offside, player_play, player_pass, player_scorer, player_k11, player_post, player_linePos, player_midShot, player_side, 
    player_centre, player_pk, player_direct, player_outside, player_man, player_slide, player_cover, player_dLine, player_keeperPK, player_keeper11, player_longThrow,
    
    # Player appearence settings
    # Head
    player_face_type, player_skin_colour, player_head_height, player_head_width, player_face_id, player_head_ov_pos,
    player_brows_type, player_brows_angle, player_brows_height, player_brows_spacing,
    player_eyes_type, player_eyes_position, player_eyes_angle, player_eyes_lenght, player_eyes_width, player_eyes_c1, player_eyes_c2,
    player_nose_type, player_nose_height, player_nose_width,
    player_cheecks_type, player_cheecks_shape,
    player_mouth_type, player_mouth_size, player_mouth_position,
    player_jaw_type, player_jaw_chin, player_jaw_width,
    
    # Hair
    #player_hair, 
    player_hair_type, player_hair_shape, player_hair_front, player_hair_volume, player_hair_darkness, 
    player_hair_colour_config, player_hair_rgb_r, player_hair_rgb_g, player_hair_rgb_b, 
    player_hair_bandana, player_hair_bandana_colour,
    player_cap, player_cap_colour,
    player_facial_hair_type, player_facial_hair_colour, 
    player_sunglasses, player_sunglasses_colour,
    
    # Physical
    player_height, player_weight, player_body_type,
    player_neck_length, player_neck_width, player_shoulder_height, player_should_width, player_chest_measu, player_waist_circu, player_arm_circu, player_leg_circu, player_calf_circu, player_leg_length,  
        
        
    # Boots/Acc.
    player_boot_type, player_boot_colour,
    player_neck_warm, player_necklace_type, player_necklace_colour, player_wistband, player_wistband_colour, player_friend_brace, player_friend_brace_colour, player_gloves,
    player_finger_band, player_shirt, player_sleeves, player_under_short, player_under_short_colour, player_socks, player_tape,
    
    # Player registration in club and national team
    player_national_team, player_club, player_special_flag,
    
    ]
    if rare_stats_flag:
         # Rare stats found on PES Editor Source code
        list_csv+= [player_cbwL, player_statX, player_bff, player_gkKick, player_statEdited]
    return list_csv


start_address = 36872
start_address_edited = 14044
last_player_id = 4999
first_edited_id = 32768
total_edit = 184
first_unused = 4896
#pes5 nationalities taken from pes5 editor source code
nationalities = ["Austria", "Belgium", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "England", "Finland", "France", "Germany", "Greece", 
"Hungary", "Ireland", "Italy", "Latvia", "Netherlands", "Northern Ireland", "Norway", "Poland", "Portugal", "Romania", "Russia", "Scotland", "Serbia and Montenegro", 
"Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "Wales", "Cameroon", "Cote d'Ivoire", "Morocco", "Nigeria", 
"Senegal", "South Africa", "Tunisia", "Costa Rica", "Mexico", "USA", "Argentina", "Brazil", "Chile", "Colombia", 
"Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela", "China", "Iran", "Japan", "Saudi Arabia", "South Korea", "Australia", "Albania", "Armenia", "Belarus", 
"Bosnia and Herzegovina", "Cyprus", "Georgia", "Estonia", "Faroe Islands", "Iceland", "Israel", "Lithuania", "Luxembourg", "Macedonia", "Moldova", "Algeria", 
"Angola", "Burkina Faso", "Cape Verde", "Congo", "DR Congo", "Egypt", "Equatorial Guinea", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Liberia", 
"Libya", "Mali", "Mauritius", "Mozambique", "Namibia", "Sierra Leone", "Togo", "Zambia", "Zimbabwe", "Canada", "Grenada", "Guadeloupe", "Guatemala", "Honduras", 
"Jamaica", "Martinique", "Netherlands Antilles", "Panama", "Trinidad and Tobago", "Bolivia", "Guyana", "Uzbekistan", "New Zealand", "Free Nationality" ]

national_teams=[
"Austria", "Belgium", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "England", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", 
"Netherlands", "Northern Ireland", "Norway", "Poland", "Portugal", "Romania", "Russia", "Scotland", "Serbia and Montenegro", "Slovakia", "Slovenia", "Spain", "Sweden", 
"Switzerland", "Turkey", "Ukraine", "Wales", "Cameroon", "Cote d'Ivoire", "Morocco", "Nigeria", "Senegal", "South Africa", "Tunisia", "Costa Rica", "Mexico", "USA", 
"Argentina", "Brazil", "Chile", "Colombia", "Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela", "China", "Iran", "Japan", "Saudi Arabia", "South Korea", "Australia",
"Classic Argentina", "Classic Brazil", "Classic England", "Classic France", "Classic Germany", "Classic Italy", "Classic Netherlands"
]

body_types = [
[-1, 0, -2, -2, -1, 0, -1, 1, 0, -2],
[-2, 0, 1, 1, 2, 0, 1, 1, 0, -1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0, 0, -1, -2, 2],
[2, 0, 1, 1, 1, 0, 0, 0, -2, 4],
[-3, 0, 3, 1, 0, 0, 2, 3, 2, -2],
[-1, 0, 0, 2, 0, 0, 0, 1, 0, 2],
[-2, 0, 2, 2, 2, 0, 2, 2, 0 ,2]
]




# Thanks a lot to Fabri55 from Evo-Web for the list of fake players

fake_players = [
 229, 77, 216, 103, 676, 722, 57, 350, 359, 
 366, 1274, 352, 1037, 361, 838, 769, 675, 
 213, 723, 358, 220, 211, 1239, 1287, 540, 
 217, 102, 218, 212, 1271, 219, 367, 964, 
 539, 74, 1225, 1228, 356, 460, 1273, 79, 
 949, 355, 101, 228, 214, 363, 536, 761, 
 72, 365, 351, 346, 210, 1229
 ]

# Information taken from  https://www.neoseeker.com/forums/25233/t548037-tricks-skills/21.htm and also testing in game

elastico_players = [
999, # Ronaldinho - Brazil - FC Barcelona
1000, # Ronaldo - Brazil - Real Madrid
631, # Zlatan Ibrahimovic - Sweden - Juventus
2531, # Naohiro Takahara - Not registered - Hamburg
446, # Cristiano Ronaldo - Portugal - Manchester United
1635, # Djibril Cisse - Not registered - Liverpool
628, # Christian Wilhelmsson - Sweden - Anderlecht
1712, # James Milner - Not registered - Newcastle
3249, # Mauro Rosales - Not registered - Ajax
1342, # Lidoanho (Rivelino) - Classic Brazil - None
 ]

shop_players = [*range(4558, 4686, 1)]
ml_youth = [*range(4686, 4886, 1)]
ml_old = [*range(4886, 4896, 1)]