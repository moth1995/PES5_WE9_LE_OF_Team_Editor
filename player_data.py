from COFPES_OF_Editor_5.editor.utils.common_functions import zero_fill_right_shift, to_int, to_byte


# This function is use to get option file data into integer and assign it to a variable

def get_value(of, player_id, offset, shift, mask, stat_name):
    i = start_address + 48 + player_id * 124 + offset
    if player_id > last_player_id:
        i = start_address_edited + (player_id - first_edited_id) * 124 + offset
    j = to_int(of.data[i]) << 8 | to_int(of.data[(i - 1)])
    #print(j)
    j = zero_fill_right_shift(j,shift)
    #print(j)
    j &= mask
    #print(stat_name)
    #print(j)
    return j

# This function is use to set/modify a value from any source to the option file into byte


def set_value(of, player_id, offset, shift, mask, new_value):
    i = start_address + 48 + (player_id * 124) + offset
    if (player_id >= last_player_id):
        i = start_address_edited + ((player_id - first_edited_id) * 124) + offset
    j = to_int(of.data[i]) << 8 | to_int(of.data[(i - 1)])
    k = 0xFFFF & (mask << shift ^ 0xFFFFFFFF)
    j &= k
    new_value &= mask
    new_value <<= shift
    new_value = j | new_value
    #print(type(of.data[(i - 1)]))
    of.data[(i - 1)] = to_byte(new_value & 0xFF)
    of.data[i] = to_byte(zero_fill_right_shift(new_value,8))

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

            name = f"{prefix} (ID: {player_id})"
        #get the shirt name
        shirt_name_address = player_offset + 32
        name_byte_array = of.data[
            shirt_name_address : shirt_name_address
            + name_bytes_length // 2
        ]
        shirt_name = name_byte_array.partition(b"\0")[0].decode()

    #print (name)
    #print (shirt_name)
    return name, shirt_name


def get_stats(player_id, of):
    #nota, para la altura hay que sumar 148, para la edad hay que sumarle 15
    player_name, player_shirt_name = get_names(player_id, of)
    player_cbwL = get_value(of, player_id, 11, 14, 1, "ASW")
    player_gk = get_value(of, player_id, 8, 6, 1, "GK")
    player_cbwS = get_value(of, player_id, 8, 7, 1, "CWP")
    player_cbt = get_value(of, player_id, 12, 4, 1, "CBT")
    player_sb = get_value(of, player_id, 12, 5, 1, "SB")
    player_dm = get_value(of, player_id, 12, 6, 1, "DM")
    player_wb = get_value(of, player_id, 12, 7, 1, "WB")
    player_cm = get_value(of, player_id, 16, 4, 1, "CM")
    player_sm = get_value(of, player_id, 16, 5, 1, "SM")
    player_om = get_value(of, player_id, 16, 6, 1, "AM")
    player_wg = get_value(of, player_id, 16, 7, 1, "WG")
    player_ss = get_value(of, player_id, 20, 4, 1, "SS")
    player_cf = get_value(of, player_id, 20, 5, 1, "CF")
    player_regPos = get_value(of, player_id, 6, 4, 15, "Registered position")
    player_height = get_value(of, player_id, 41, 0, 63, "Height") + 148
    player_foot = get_value(of, player_id, 5, 0, 1, "Foot")
    player_favSide = get_value(of, player_id, 20, 6, 3, "Fav side")
    player_wfa = get_value(of, player_id, 34, 5, 7, "W Foot Acc")
    player_wff = get_value(of, player_id, 35, 0, 7, "W Foot Freq")
    player_attack = get_value(of, player_id, 7, 0, 127, "Attack")
    player_defence = get_value(of, player_id, 7, 7, 127, "Defense")
    player_balance = get_value(of, player_id, 9, 0, 127, "Balance")
    player_stamina = get_value(of, player_id, 9, 7, 127, "Stamina")
    player_speed = get_value(of, player_id, 10, 6, 127, "Speed")
    player_accel = get_value(of, player_id, 11, 5, 127, "Accel")
    player_response = get_value(of, player_id, 13, 0, 127, "Response")
    player_agility = get_value(of, player_id, 13, 7, 127, "Agility")
    player_dribAcc = get_value(of, player_id, 14, 6, 127, "Drib Acc")
    player_dribSpe = get_value(of, player_id, 15, 5, 127, "Drib Spe")
    player_sPassAcc = get_value(of, player_id, 17, 0, 127, "S Pass Acc")
    player_sPassSpe = get_value(of, player_id, 17, 7, 127, "S Pass Spe")
    player_lPassAcc = get_value(of, player_id, 18, 6, 127, "L Pass Acc")
    player_lPassSpe = get_value(of, player_id, 19, 5, 127, "L Pass Spe")
    player_shotAcc = get_value(of, player_id, 21, 0, 127, "Shot Acc")
    player_shotPow = get_value(of, player_id, 21, 7, 127, "Shot Power")
    player_shotTec = get_value(of, player_id, 22, 6, 127, "Shot Tech")
    player_fk = get_value(of, player_id, 23, 5, 127, "FK Acc")
    player_curling = get_value(of, player_id, 25, 0, 127, "Curling")
    player_heading = get_value(of, player_id, 25, 7, 127, "Heading")
    player_jump = get_value(of, player_id, 26, 6, 127, "Jump")
    player_tech = get_value(of, player_id, 29, 0, 127, "Tech")
    player_aggress = get_value(of, player_id, 29, 7, 127, "Aggression")
    player_mental = get_value(of, player_id, 30, 6, 127, "Mentality")
    player_consistency = get_value(of, player_id, 33, 7, 7, "Consistency")
    player_gkAbil = get_value(of, player_id, 31, 5, 127, "GK")
    player_team = get_value(of, player_id, 33, 0, 127, "Team Work")
    player_condition = get_value(of, player_id, 34, 2, 7, "Condition")
    player_statX = get_value(of, player_id, 27, 5, 127, "StatX")
    player_drib = get_value(of, player_id, 24, 4, 1, "Dribbling")
    player_dribKeep = get_value(of, player_id, 24, 5, 1, "Anti-Dribble")
    player_post = get_value(of, player_id, 32, 4, 1, "Post")
    player_posit = get_value(of, player_id, 24, 6, 1, "Positioning")
    player_offside = get_value(of, player_id, 24, 7, 1, "Reaction")
    player_linePos = get_value(of, player_id, 32, 5, 1, "Line Position")
    player_midShot = get_value(of, player_id, 32, 6, 1, "Mid shooting")
    player_scorer = get_value(of, player_id, 28, 6, 1, "Scoring")
    player_play = get_value(of, player_id, 28, 4, 1, "Playmaking")
    player_pass = get_value(of, player_id, 28, 5, 1, "Passing")
    player_bff = get_value(of, player_id, 20, 6, 1, "B F Feint")
    player_pk = get_value(of, player_id, 35, 6, 1, "Penalties")
    player_k11 = get_value(of, player_id, 28, 7, 1, "1-1 Scoring")
    player_longThrow = get_value(of, player_id, 36, 7, 1, "Long Throw")
    player_direct = get_value(of, player_id, 35, 7, 1, "1-T Pass")
    player_side = get_value(of, player_id, 32, 7, 1, "Side")
    player_centre = get_value(of, player_id, 35, 5, 1, "Centre")
    player_outside = get_value(of, player_id, 36, 0, 1, "Outside")
    player_man = get_value(of, player_id, 36, 1, 1, "Marking")
    player_dLine = get_value(of, player_id, 36, 4, 1, "D-L Control")
    player_slide = get_value(of, player_id, 36, 2, 1, "Sliding")
    player_cover = get_value(of, player_id, 36, 3, 1, "Cover")
    player_gkKick = get_value(of, player_id, 20, 7, 1, "GK Kick")
    player_keeperPK = get_value(of, player_id, 36, 5, 1, "Penalty GK")
    player_keeper11 = get_value(of, player_id, 36, 6, 1, "1-on-1 GK")
    player_injury = get_value(of, player_id, 35, 3, 3, "Injury T")
    player_dribSty = get_value(of, player_id, 6, 0, 3, "Dribble Style")
    player_freekick = get_value(of, player_id, 5, 1, 15, "FK Style")
    player_pkStyle = get_value(of, player_id, 5, 5, 7, "PK Style")
    player_dkSty = get_value(of, player_id, 6, 2, 3, "DK Style")
    player_age = get_value(of, player_id, 62, 5, 31, "Age") +15
    player_weight = get_value(of, player_id, 41, 6, 127, "Weight")
    player_nation = get_value(of, player_id, 63, 2, 127, "Nationality")
    player_callName = get_value(of, player_id, 1, 0, 65535, "Callname ID")
    player_statEdited = get_value(of, player_id, 39, 7, 1, "Stat Edited")
    
    return ([player_id, player_name, player_shirt_name, player_cbwL,player_gk ,player_cbwS ,player_cbt ,player_sb ,player_dm ,player_wb ,player_cm ,player_sm ,player_om ,
        player_wg ,player_ss ,player_cf ,player_regPos ,player_height ,player_foot ,player_favSide ,player_wfa ,player_wff ,player_attack ,player_defence ,player_balance ,
        player_stamina ,player_speed ,player_accel ,player_response ,player_agility ,player_dribAcc ,player_dribSpe ,player_sPassAcc ,player_sPassSpe ,player_lPassAcc ,
        player_lPassSpe ,player_shotAcc ,player_shotPow ,player_shotTec ,player_fk ,player_curling ,player_heading ,player_jump ,player_tech ,player_aggress ,player_mental ,
        player_consistency ,player_gkAbil ,player_team ,player_condition ,player_statX ,player_drib ,player_dribKeep ,player_post ,player_posit ,player_offside ,player_linePos ,
        player_midShot ,player_scorer ,player_play ,player_pass ,player_bff ,player_pk ,player_k11 ,player_longThrow ,player_direct ,player_side ,player_centre ,player_outside ,
        player_man ,player_dLine ,player_slide ,player_cover ,player_gkKick ,player_keeperPK ,player_keeper11 ,player_injury ,player_dribSty ,player_freekick ,player_pkStyle ,
        player_dkSty ,player_age ,player_weight ,player_nation ,player_callName ,player_statEdited ])


start_address = 36872
start_address_edited = 14048
last_player_id = 4999
first_edited_id = 32768
total_edit = 184
first_unused = 4896