from bs4 import BeautifulSoup
import urllib, os, json, time, urllib.request, subprocess, datetime
from COFPES_OF_Editor_5.editor.utils.common_functions import resource_path
from player_data import set_value, set_name, set_shirt_name
import csv

def fetch_url(url, mode="PYTHON"):
    agent =  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
    if (mode == "PYTHON"):
        req = urllib.request.Request(url, data=None, headers={'User-Agent': agent})
        with urllib.request.urlopen(req) as f:
            data = f.read().decode('utf-8', 'ignore')
        return data
    else:
        out = subprocess.Popen([r"curl-7.74.0_2-win64-mingw\lastest\curl.exe" ,url, "-H 'Connection: keep-alive'", "-H 'Upgrade-Insecure-Requests: 1'", "-H '{}'".format(agent), "-H 'Sec-Fetch-Mode: navigate'", "-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'", "-H 'Sec-Fetch-Site: none'", "-H 'Accept-Encoding: gzip, deflate, br'", "-H 'Cookie: cookieconsent_dismissed=yes; defaultFormat=6;'", "--compressed"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout,stderr = out.communicate()
        return stdout

def find_nationality(dem):
    csv_file = csv.reader(open(resource_path('demonyms.csv'), "r", encoding='utf-8'), delimiter=",")
    for row in csv_file:
        if row[0] == dem:
             return (row[1])
    return "Free Nationality"


def find_positions(pos_list):
    for i in range(0,len(pos_list)):
        #print(pos_list[i].isascii())
        if not pos_list[i].isascii():
            #print(pos_list[i])
            reg_pos = pos_list[i].encode("ascii", "ignore").decode('utf-8')
        pos_list[i]=pos_list[i].encode("ascii", "ignore").decode('utf-8')
    return reg_pos, pos_list

def get_pos_reg(pos):
    return {
        'GK': 0,
        'CWP': 2,
        'CBT': 3,
        'SB': 4,
        'DMF': 5,
        'WB': 6,
        'CMF': 7,
        'SMF': 8,
        'AMF': 9,
        'WF': 10,
        'SS': 11,
        'CF': 12   
    }.get(pos, 0)    # si no encontramos la posicion devolvemos 0 que es GK


def get_pos(posicion,posiciones):
    equivalencias= {
        0: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7,
        9: 8,
        10: 9,
        11: 10,
        12: 11   
    }
    indice=equivalencias.get(posicion)
    posiciones[indice]=1
    return posiciones

def name_normalization(name):
    x=""
    x=name.split()
    if len(x)==1:
       name=x[0]
    else:
        primer_nombre = x[0]
        apellido = x[-1]
        name=primer_nombre[0] + ". " + apellido
        if len(name)>16:
            name=apellido
            if len(name)>16:
              name=apellido[:15]
    
    return name

def parse_psd_data(data, player_id, of):
    stats = ""
    soup = BeautifulSoup(data, "lxml")
    for br in soup.find_all("br"):
        br.replace_with("\n")
    try:
        tmp = soup.find(attrs={"id" : "info"})
        stats += tmp.getText()
        tmp = soup.find(attrs={"id" : "other_info"})
        stats += tmp.getText()
    except:
        pass
    player = (list(filter(None, stats.split('\n\n'))))
    for i in range(0,len(player)):
        if 'Long Pass Accuracy' in player[i]:
            player[i]=(player[i].split('\r')[0].replace(" "*28, "").replace("\n",""))
        elif 'Short Pass Speed' in player[i]:
            player[i]=(player[i].split('\r')[0].replace(" "*28, "").replace("\n",""))
        else:
            player[i]=(player[i].replace(" "*28, "").replace("\n","").split(u'\xa0')[0])

    #print(player)
    #print(repr(player))

    for i in range(0, len(player)):
        #print(player[i])
        if "Name" == player[i].split(':')[0].strip():
            player_name = name_normalization(player[i].split(':')[1].strip())
            set_name(of, player_id, player_name)

        if "Shirt Name" in player[i]:
            player_sh_name = player[i].split(':')[1].strip()
            set_shirt_name(of, player_id, player_sh_name)

        if "Positions" in player[i]:
            player_reg_pos, player_pos_list = find_positions(player[i].split(':')[1].strip().split(', '))

        if "Nationality" in player[i]:
            player_nationality = find_nationality(player[i].split(':')[1].strip())
            if (player_nationality) in nationalities:
                player_nationality = nationalities.index(player_nationality)
            else:
                player_nationality = nationalities.index("Free Nationality")
            #print(player_id, csv_nation)
            set_value(of, player_id, 63, 2, 127, player_nationality)

        if "Age" in player[i]:
            player_age = int(player[i].split(':')[1].strip()) - 15
            set_value(of, player_id, 62, 5, 31, player_age)

        if "Height" in player[i]:
            player_height = int(player[i].split(':')[1].strip()) - 148
            set_value(of, player_id, 41, 0, 63, player_height)

        if "Weight" in player[i]:
            player_weight = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 41, 6, 127, player_weight)

        if "Injury Tolerance" in player[i]:
            player_inj_tol = player[i].split(':')[1].strip()
            if player_inj_tol == "A":
                player_inj_tol = 2
            elif player_inj_tol == "B":
                player_inj_tol = 1
            else:
                player_inj_tol = 0
            # Here we limit the stat to already know konami range
            #print(player_id, csv_injury)
            set_value(of, player_id, 35, 3, 3, player_inj_tol)

        if "Foot" == player[i].split(':')[0].strip():
            player_foot = player[i].split(':')[1].strip()
            if player_foot=="R":
                player_foot=0
            else:
                player_foot=1
            #print(player_id, csv_foot)
            set_value(of, player_id, 5, 0, 1, player_foot)

        if "Side" == player[i].split(':')[0].strip():
            player_fav_side = player[i].split(':')[1].strip()
            if player_fav_side=="R":
                player_fav_side=0
            elif player_fav_side=="L":
                player_fav_side=1
            else:
                player_fav_side=2
            #print(player_id, csv_favSide)
            #print(player_fav_side)
            set_value(of, player_id, 20, 6, 3, player_fav_side)                   

        if "Attack" in player[i]:
            player_attack = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 7, 0, 127, player_attack)

        if "Defence" in player[i]:
            player_defense = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 7, 7, 127, player_defense)

        if "Balance" in player[i]:
            player_balance = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 9, 0, 127, player_balance)

        if "Stamina" in player[i]:
            player_stamina = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 9, 7, 127, player_stamina)

        if "Top Speed" in player[i]:
            player_top_speed = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 10, 6, 127, player_top_speed)

        if "Acceleration" in player[i]:
            player_accel = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 11, 5, 127, player_accel)

        if "Response" in player[i]:
            player_response = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 13, 0, 127, player_response)

        if "Agility" in player[i]:
            player_agility = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 13, 7, 127, player_agility)

        if "Dribble Accuracy" in player[i]:
            player_drib_accu = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 14, 6, 127, player_drib_accu)

        if "Dribble Speed" in player[i]:
            player_drib_speed = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 15, 5, 127, player_drib_speed)

        if "Short Pass Accuracy" in player[i]:
            player_sh_pass_acc = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 17, 0, 127, player_sh_pass_acc)

        if "Short Pass Speed" in player[i]:
            player_sh_pass_speed = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 17, 7, 127, player_sh_pass_speed)

        if "Long Pass Accuracy" in player[i]:
            player_long_pass_acc = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 18, 6, 127, player_long_pass_acc)

        if "Long Pass Speed" in player[i]:
            player_long_pass_speed = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 19, 5, 127, player_long_pass_speed)

        if "Shot Accuracy" in player[i]:
            player_shot_acc = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 21, 0, 127, player_shot_acc)

        if "Shot Power" in player[i]:
            player_shot_power = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 21, 7, 127, player_shot_power)

        if "Shot Technique" in player[i]:
            player_shot_tech = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 22, 6, 127, player_shot_tech)
            

        if "Free Kick Accuracy" in player[i]:
            player_fk_acc = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 23, 5, 127, player_fk_acc)

        if "Curling" in player[i]:
            player_curling = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 25, 0, 127, player_curling)

        if "Header" in player[i]:
            player_header = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 25, 7, 127, player_header)

        if "Jump" in player[i]:
            player_jump = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 26, 6, 127, player_jump)

        if "Technique" in player[i]:
            player_techn = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 29, 0, 127, player_techn)

        if "Aggression" in player[i]:
            player_aggre = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 29, 7, 127, player_aggre)

        if "Mentality" in player[i]:
            player_mentality = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 30, 6, 127, player_mentality)

        if "Keeper Skills" in player[i]:
            player_gk_skills = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 31, 5, 127, player_gk_skills)

        if "Teamwork" in player[i]:
            player_teamwork = int(player[i].split(':')[1].strip())
            set_value(of, player_id, 33, 0, 127, player_teamwork)

        if "Condition" in player[i] or "Fitness" in player[i]:
            player_condition = int(player[i].split(':')[1].strip()) - 1
            set_value(of, player_id, 34, 2, 7, player_condition)

        if "Consistency" in player[i]:
            player_consistency = int(player[i].split(':')[1].strip()) - 1
            set_value(of, player_id, 33, 7, 7, player_consistency)

        if "Weak Foot Accuracy" in player[i]:
            player_wf_acc = int(player[i].split(':')[1].strip()) - 1
            set_value(of, player_id, 34, 5, 7, player_wf_acc)

        if "Weak Foot Frequency" in player[i]:
            player_wf_fre = int(player[i].split(':')[1].strip()) - 1
            set_value(of, player_id, 35, 0, 7, player_wf_fre)

        if "Dribbling" in player[i]:
            player_dribbling = 1
            set_value(of, player_id, 24, 4, 1, player_dribbling)

        if "Tactical Dribble" in player[i]:
            player_tac_drib = 1
            set_value(of, player_id, 24, 5, 1, player_tac_drib)

        if "Positioning" in player[i]:
            player_positioning = 1
            set_value(of, player_id, 24, 6, 1, player_positioning)

        if "Playmaking" in player[i]:
            player_playmaking = 1
            set_value(of, player_id, 28, 4, 1, player_playmaking)

        if "Passing" in player[i]:
            player_pass = 1
            set_value(of, player_id, 28, 5, 1, player_pass)

        if "★ Scoring" == player[i]:
            player_scoring = 1
            #print(player_scoring)
            set_value(of, player_id, 28, 6, 1, player_scoring)

        if "Centre" in player[i]:
            player_centre = 1
            set_value(of, player_id, 35, 5, 1, player_centre)

        if "Outside" in player[i]:
            player_outside = 1
            set_value(of, player_id, 36, 0, 1, player_outside)

        if "Covering" in player[i]:
            player_covering = 1
            set_value(of, player_id, 36, 3, 1, player_covering)

        if "1-1 Scoring" in player[i]:
            player_11_sco = 1
            set_value(of, player_id, 28, 7, 1, player_11_sco)

        if " Side" in player[i]:
            player_side = 1
            set_value(of, player_id, 32, 7, 1, player_side)

        if "Penalties" in player[i]:
            player_penalties = 1
            set_value(of, player_id, 35, 6, 1, player_penalties)

        if "1-Touch Pass" in player[i]:
            player_1_touch = 1
            set_value(of, player_id, 35, 7, 1, player_1_touch)

        if "Lines" in player[i]:
            player_lines = 1
            set_value(of, player_id, 32, 5, 1, player_lines)

        if "Sliding" in player[i]:
            player_sliding = 1
            set_value(of, player_id, 36, 2, 1, player_sliding)

        if "Reaction" in player[i]:
            player_reaction = 1
            set_value(of, player_id, 24, 7, 1, player_reaction)

        if "Post Player" in player[i]:
            player_post_player = 1
            set_value(of, player_id, 32, 4, 1, player_post_player)

        if "Marking" in player[i]:
            player_making = 1
            set_value(of, player_id, 36, 1, 1, player_making)

        if "Penalty Stopper" in player[i]:
            player_pk_stop = 1
            set_value(of, player_id, 36, 5, 1, player_pk_stop)

        if "1-on-1 Stopper" in player[i]:
            player_11_stop = 1
            set_value(of, player_id, 36, 6, 1, player_11_stop)

        if "Long Throw" in player[i]:
            player_long_throw = 1
            set_value(of, player_id, 36, 7, 1, player_long_throw)

        if "D-Line Control" in player[i]:
            player_dline = 1
            set_value(of, player_id, 36, 4, 1, player_dline)

        if "Middle Shooting" in player[i]:
            player_mid_shoot = 1
            set_value(of, player_id, 32, 6, 1, player_mid_shoot)

        if "Dribble Style" in player[i]:
            player_drib_style = int(player[i].split(':')[1].strip()) - 1
            set_value(of, player_id, 6, 0, 3, player_drib_style)            

        if "Free Kick Style" in player[i]:
            player_fk_style = int(player[i].split(':')[1].strip()) - 1
            set_value(of, player_id, 5, 1, 15, player_fk_style)

        if "Penalty Kick Style" in player[i]:
            player_pk_style = int(player[i].split(':')[1].strip()) - 1
            set_value(of, player_id, 5, 5, 7, player_pk_style)

        if "Drop Kick Style" in player[i]:
            player_dk_style = int(player[i].split(':')[1].strip()) - 1
            set_value(of, player_id, 6, 2, 3, player_dk_style)
    csv_positions=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(player_pos_list)):
        csv_positions=get_pos(get_pos_reg(player_pos_list[i]),csv_positions)
    #print (csv_positions, get_pos_reg(player_reg_pos))
    set_value(of, player_id, 6, 4, 15, get_pos_reg(player_reg_pos))
    set_value(of, player_id, 8, 6, 1, csv_positions[0])
    set_value(of, player_id, 8, 7, 1, csv_positions[1])
    set_value(of, player_id, 12, 4, 1, csv_positions[2])
    set_value(of, player_id, 12, 5, 1, csv_positions[3])
    set_value(of, player_id, 12, 6, 1, csv_positions[4])
    set_value(of, player_id, 12, 7, 1, csv_positions[5])
    set_value(of, player_id, 16, 4, 1, csv_positions[6])
    set_value(of, player_id, 16, 5, 1, csv_positions[7])
    set_value(of, player_id, 16, 6, 1, csv_positions[8])
    set_value(of, player_id, 16, 7, 1, csv_positions[9])
    set_value(of, player_id, 20, 4, 1, csv_positions[10])
    set_value(of, player_id, 20, 5, 1, csv_positions[11])
    #return(player)



def import_stats_from_psd(of, player_id, url):
    #print(player_id, url)
    data = fetch_url(url, "PYTHON")
    #print(data)
    parse_psd_data(data, player_id, of)
    

def main():
    import_stats_from_psd(0, "https://pesstatsdatabase.com/PSD/Player_old2011.php?Id=25891")

if __name__ == "__main__":
    main()


nationalities = ["Austria", "Belgium", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "England", "Finland", "France", "Germany", "Greece", 
"Hungary", "Ireland", "Italy", "Latvia", "Netherlands", "Northern Ireland", "Norway", "Poland", "Portugal", "Romania", "Russia", "Scotland", "Serbia and Montenegro", 
"Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "Wales", "Cameroon", "Cote d'Ivoire", "Morocco", "Nigeria", 
"Senegal", "South Africa", "Tunisia", "Costa Rica", "Mexico", "USA", "Argentina", "Brazil", "Chile", "Colombia", 
"Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela", "China", "Iran", "Japan", "Saudi Arabia", "South Korea", "Australia", "Albania", "Armenia", "Belarus", 
"Bosnia and Herzegovina", "Cyprus", "Georgia", "Estonia", "Faroe Islands", "Iceland", "Israel", "Lithuania", "Luxembourg", "Macedonia", "Moldova", "Algeria", 
"Angola", "Burkina Faso", "Cape Verde", "Congo", "DR Congo", "Egypt", "Equatorial Guinea", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Liberia", 
"Libya", "Mali", "Mauritius", "Mozambique", "Namibia", "Sierra Leone", "Togo", "Zambia", "Zimbabwe", "Canada", "Grenada", "Guadeloupe", "Guatemala", "Honduras", 
"Jamaica", "Martinique", "Netherlands Antilles", "Panama", "Trinidad and Tobago", "Bolivia", "Guyana", "Uzbekistan", "New Zealand", "Free Nationality" ]
