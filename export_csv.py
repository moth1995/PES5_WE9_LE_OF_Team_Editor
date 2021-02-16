import csv


def create_csv(filename):
    #creamos el csv
    try:
        with open(filename, 'w',newline='', encoding='utf-8') as f:
            csv_escribir = csv.writer(f)
            csv_escribir.writerow(["ID","NAME","SHIRT_NAME", "ASW ?", "GK  0","CWP  2","CBT  3","SB  4","DMF  5","WB  6","CMF  7","SMF  8","AMF  9",
            "WF 10","SS  11","CF  12","REGISTERED POSITION","HEIGHT","STRONG FOOT","FAVOURED SIDE","WEAK FOOT ACCURACY","WEAK FOOT FREQUENCY",
            "ATTACK","DEFENSE","BALANCE","STAMINA","TOP SPEED","ACCELERATION","RESPONSE","AGILITY","DRIBBLE ACCURACY","DRIBBLE SPEED",
            "SHORT PASS ACCURACY","SHORT PASS SPEED","LONG PASS ACCURACY","LONG PASS SPEED","SHOT ACCURACY","SHOT POWER","SHOT TECHNIQUE",
            "FREE KICK ACCURACY","CURLING","HEADING","JUMP","TECHNIQUE","AGGRESSION","MENTALITY","CONSISTENCY","GOAL KEEPING","TEAM WORK",
            "CONDITION / FITNESS", "STAT X" ,"DRIBBLING","TACTICAL DRIBBLE","POST PLAYER","POSITIONING","REACTION","LINES","MIDDLE SHOOTING","SCORING",
            "PLAYMAKING","PASSING", "B F FEINT", "PENALTIES","1-1 SCORING","LONG THROW","1-TOUCH PASS","SIDE","CENTRE","OUTSIDE","MARKING","D-LINE CONTROL",
            "SLIDING","COVERING","GK KICK","PENALTY STOPPER","1-ON-1 STOPPER","INJURY TOLERANCE","DRIBBLE STYLE","FREE KICK STYLE","PK STYLE",
            "DROP KICK STYLE","AGE","WEIGHT","NATIONALITY","CALLNAME ID", "STAT EDITED", "GOAL CELEBRATION 1", "GOAL CELEBRATION 2", "SKIN COLOUR"])
        return filename
    except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
        return False

def write_csv(filename,players):
    file=create_csv(filename)
    if file:
        with open(file, 'a',newline='', encoding='utf-8') as f:
            csv_out=csv.writer(f)
            #csv_out.writerows(players)
            for player in players:
                #print(player)
                csv_out.writerow(player)
        return True
    return False

