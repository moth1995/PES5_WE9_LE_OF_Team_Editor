import csv


def create_csv(filename):
    #creamos el csv
    try:
        with open(filename, 'w',newline='', encoding='utf-8') as f:
            csv_escribir = csv.writer(f)
            csv_escribir.writerow([
            
            # Player basic settings
            "ID","NAME","SHIRT_NAME", "CALLNAME ID", "NATIONALITY", "AGE", "STRONG FOOT", "INJURY TOLERANCE", 
            "DRIBBLE STYLE", "FREE KICK STYLE", "PK STYLE", "DROP KICK STYLE", "GOAL CELEBRATION 1", "GOAL CELEBRATION 2",
            #"GROWTH TYPE",
            
            # Player position settings
            "REGISTERED POSITION", "FAVOURED SIDE", "GK  0", "CWP  2", "CBT  3", "SB  4", "DMF  5", "WB  6", "CMF  7", "SMF  8", "AMF  9", "WF 10","SS  11","CF  12",
            
            # Player ability settings
            "ATTACK", "DEFENSE", "BALANCE", "STAMINA", "TOP SPEED", "ACCELERATION", "RESPONSE", "AGILITY", "DRIBBLE ACCURACY", "DRIBBLE SPEED", "SHORT PASS ACCURACY",
            "SHORT PASS SPEED", "LONG PASS ACCURACY", "LONG PASS SPEED", "SHOT ACCURACY", "SHOT POWER", "SHOT TECHNIQUE", "FREE KICK ACCURACY", "CURLING", "HEADING", "JUMP", "TECHNIQUE", 
            "AGGRESSION", "MENTALITY", "GOAL KEEPING", "TEAM WORK", "CONSISTENCY", "CONDITION / FITNESS", "WEAK FOOT ACCURACY", "WEAK FOOT FREQUENCY",
            
            # Player special abilities settings
            "DRIBBLING", "TACTICAL DRIBBLE", "POSITIONING", "REACTION", "PLAYMAKING", 
            "PASSING", "SCORING", "1-1 SCORING", "POST PLAYER",
            "LINES", "MIDDLE SHOOTING", "SIDE", "CENTRE", "PENALTIES", "1-TOUCH PASS", 
            "OUTSIDE", "MARKING", "SLIDING", "COVERING", "D-LINE CONTROL",
            "PENALTY STOPPER", "1-ON-1 STOPPER", "LONG THROW",
            
            # Player appearence settings
            # Head
            "FACE TYPE", "SKIN COLOUR", "HEAD HEIGHT", "HEAD WIDTH", "FACE ID", "HEAD OVERALL POSITION",
            "BROWS TYPE", "BROWS ANGLE", "BROWS HEIGHT", "BROWS SPACING",
            "EYE TYPE", "EYE COLOUR 1", "EYE COLOUR 2",
            "NOSE TYPE", "NOSE HEIGHT", "NOSE WIDTH",
            "CHEECKS TYPE", "CHEECKS SHAPE",
            "MOUTH TYPE", "MOUTH SIZE", "MOUTH POSITION",
            "JAW TYPE", "JAW CHIN", "JAW WIDTH",
            # Hair
            #"HAIR",
            "FACIAL HAIR TYPE", "FACIAL HAIR COLOUR", 
            "SUNGLASSES TYPE", "SUNGLASSES COLOUR",
            
            # Physical
            "HEIGHT", "WEIGHT",
            "NECK LENGTH", "NECK WIDTH", "SHOULDER WIDTH", "ARM CIRCUMFERENCE", "LEG CIRCUMFERENCE", "LEG LENGTH", 
            
            # Boots/Acc.
            "BOOT TYPE", "BOOT COLOUR",
            "NECK WARMER", "NECKLACE TYPE", "NECKLACE COLOUR", "WISTBAND", "WISTBAND COLOUR", "FRIENDSHIP BRACELET", "FRIENDSHIP BRACELET COLOUR", "GLOVES",
            "FINGER BAND", "SHIRT", "SLEEVES", "UNDER SHORT", "UNDER SHORT COLOUR", "SOCKS", "TAPE",
            
            # Rare stats found on PES Editor Source code
            "ASW ?", "STAT X", "B F FEINT", "GK KICK", "STAT EDITED",
            
            ])
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

