import csv
from player_data import set_value, set_boot_type_colour, set_name, set_shirt_name

def load_csv(of, file):
    try:
        with open(file, 'r', encoding='utf-8') as csvf:
            # list to store the names of columns
            csv_reader = csv.reader(csvf, delimiter = ',')
            list_of_column_names = [] 
          
            # loop to iterate thorugh the rows of csv 
            for row in csv_reader: 
          
                # adding the first row 
                list_of_column_names = row
          
                # breaking the loop after the 
                # first iteration itself 
                break
            #print(list_of_column_names)
            if 'ID' in list_of_column_names:
                for row in csv_reader: 
                    player_id = int(row[list_of_column_names.index('ID')])

                    if 'NAME' in list_of_column_names:
                        csv_name=(row[list_of_column_names.index('NAME')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_name)
                        set_name(of, player_id, csv_name)
                        
                    if 'SHIRT_NAME' in list_of_column_names:
                        csv_shirt_name=(row[list_of_column_names.index('SHIRT_NAME')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_shirt_name)
                        set_shirt_name(of, player_id, csv_shirt_name)
                    
                    if 'ASW ?' in list_of_column_names:
                        csv_cbwL=int(row[list_of_column_names.index('ASW ?')])
                        # Here we limit the stat to already know konami range
                        if csv_cbwL<0:
                            csv_cbwL=0
                        elif csv_cbwL>1:
                            csv_cbwL=1
                        #print(player_id, csv_cbwL)
                        set_value(of, player_id, 11, 14, 1, csv_cbwL)
                    
                    if 'GK  0' in list_of_column_names:
                        csv_gk=int(row[list_of_column_names.index('GK  0')])
                        # Here we limit the stat to already know konami range
                        if csv_gk<0:
                            csv_gk=0
                        elif csv_gk>1:
                            csv_gk=1
                        #print(player_id, csv_gk)
                        set_value(of, player_id, 8, 6, 1, csv_gk)
                        
                    if 'CWP  2' in list_of_column_names:
                        csv_cbwS=int(row[list_of_column_names.index('CWP  2')])
                        # Here we limit the stat to already know konami range
                        if csv_cbwS<0:
                            csv_cbwS=0
                        elif csv_cbwS>1:
                            csv_cbwS=1
                        #print(player_id, csv_cbwS)
                        set_value(of, player_id, 8, 7, 1, csv_cbwS)
                    
                    if 'CBT  3' in list_of_column_names:
                        csv_cbt=int(row[list_of_column_names.index('CBT  3')])
                        # Here we limit the stat to already know konami range
                        if csv_cbt<0:
                            csv_cbt=0
                        elif csv_cbt>1:
                            csv_cbt=1
                        #print(player_id, csv_cbt)
                        set_value(of, player_id, 12, 4, 1, csv_cbt)
                        
                    if 'SB  4' in list_of_column_names:
                        csv_sb=int(row[list_of_column_names.index('SB  4')])
                        # Here we limit the stat to already know konami range
                        if csv_sb<0:
                            csv_sb=0
                        elif csv_sb>1:
                            csv_sb=1
                        #print(player_id, csv_sb)
                        set_value(of, player_id, 12, 5, 1, csv_sb)
                    
                    if 'DMF  5' in list_of_column_names:
                        csv_dm=int(row[list_of_column_names.index('DMF  5')])
                        # Here we limit the stat to already know konami range
                        if csv_dm<0:
                            csv_dm=0
                        elif csv_dm>1:
                            csv_dm=1
                        #print(player_id, csv_dm)
                        set_value(of, player_id, 12, 6, 1, csv_dm)
                        
                    if 'WB  6' in list_of_column_names:
                        csv_wb=int(row[list_of_column_names.index('WB  6')])
                        # Here we limit the stat to already know konami range
                        if csv_wb<0:
                            csv_wb=0
                        elif csv_wb>1:
                            csv_wb=1
                        #print(player_id, csv_wb)
                        set_value(of, player_id, 12, 7, 1, csv_wb)
                        
                    if 'CMF  7' in list_of_column_names:
                        csv_cm=int(row[list_of_column_names.index('CMF  7')])
                        # Here we limit the stat to already know konami range
                        if csv_cm<0:
                            csv_cm=0
                        elif csv_cm>1:
                            csv_cm=1
                        #print(player_id, csv_cm)
                        set_value(of, player_id, 16, 4, 1, csv_cm)
                        
                    if 'SMF  8' in list_of_column_names:
                        csv_sm=int(row[list_of_column_names.index('SMF  8')])
                        # Here we limit the stat to already know konami range
                        if csv_sm<0:
                            csv_sm=0
                        elif csv_sm>1:
                            csv_sm=1
                        #print(player_id, csv_sm)
                        set_value(of, player_id, 16, 5, 1, csv_sm)
                        
                    if 'AMF  9' in list_of_column_names:
                        csv_om=int(row[list_of_column_names.index('AMF  9')])
                        # Here we limit the stat to already know konami range
                        if csv_om<0:
                            csv_om=0
                        elif csv_om>1:
                            csv_om=1
                        #print(player_id, csv_om)
                        set_value(of, player_id, 16, 6, 1, csv_om)
                        
                    if 'WF 10' in list_of_column_names:
                        csv_wg=int(row[list_of_column_names.index('WF 10')])
                        # Here we limit the stat to already know konami range
                        if csv_wg<0:
                            csv_wg=0
                        elif csv_wg>1:
                            csv_wg=1
                        #print(player_id, csv_wg)
                        set_value(of, player_id, 16, 7, 1, csv_wg)
                        
                    if 'SS  11' in list_of_column_names:
                        csv_ss=int(row[list_of_column_names.index('SS  11')])
                        # Here we limit the stat to already know konami range
                        if csv_ss<0:
                            csv_ss=0
                        elif csv_ss>1:
                            csv_ss=1
                        #print(player_id, csv_ss)
                        set_value(of, player_id, 20, 4, 1, csv_ss)
                        
                    if 'CF  12' in list_of_column_names:
                        csv_cf=int(row[list_of_column_names.index('CF  12')])
                        # Here we limit the stat to already know konami range
                        if csv_cf<0:
                            csv_cf=0
                        elif csv_cf>1:
                            csv_cf=1
                        #print(player_id, csv_cf)
                        set_value(of, player_id, 20, 5, 1, csv_cf)
                        
                    if 'REGISTERED POSITION' in list_of_column_names:
                        csv_regPos=int(row[list_of_column_names.index('REGISTERED POSITION')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_regPos)
                        set_value(of, player_id, 6, 4, 15, csv_regPos)
                        
                        
                    if 'HEIGHT' in list_of_column_names:
                        csv_height=int(row[list_of_column_names.index('HEIGHT')])-148
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_height)
                        set_value(of, player_id, 41, 0, 63, csv_height)
                        
                    if 'STRONG FOOT' in list_of_column_names:
                        csv_foot=(row[list_of_column_names.index('STRONG FOOT')])
                        # Here we limit the stat to already know konami range
                        if csv_foot=="R":
                            csv_foot=0
                        else:
                            csv_foot=1
                        #print(player_id, csv_foot)
                        set_value(of, player_id, 5, 0, 1, csv_foot)
                        
                    if 'FAVOURED SIDE' in list_of_column_names:
                        csv_favSide=(row[list_of_column_names.index('FAVOURED SIDE')])
                        # Here we limit the stat to already know konami range
                        if csv_favSide=="R":
                            csv_favSide=0
                        elif csv_favSide=="L":
                            csv_favSide=1
                        else:
                            csv_favSide=2
                        #print(player_id, csv_favSide)
                        set_value(of, player_id, 20, 6, 3, csv_favSide)
                        
                    if 'WEAK FOOT ACCURACY' in list_of_column_names:
                        csv_wfa=int(row[list_of_column_names.index('WEAK FOOT ACCURACY')]) - 1
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_wfa)
                        set_value(of, player_id, 34, 5, 7, csv_wfa)
                        
                    if 'WEAK FOOT FREQUENCY' in list_of_column_names:
                        csv_wff=int(row[list_of_column_names.index('WEAK FOOT FREQUENCY')]) - 1
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_wff)
                        set_value(of, player_id, 35, 0, 7, csv_wff)
                        
                    if 'ATTACK' in list_of_column_names:
                        csv_attack=int(row[list_of_column_names.index('ATTACK')])
                        # Here we limit the stat to already know konami range
                        if csv_attack<=0:
                            csv_attack=1
                        elif csv_attack>99:
                            csv_attack=99
                        #print(player_id, csv_attack)
                        set_value(of, player_id, 7, 0, 127, csv_attack)
                        
                    if 'DEFENSE' in list_of_column_names:
                        csv_defence=int(row[list_of_column_names.index('DEFENSE')])
                        # Here we limit the stat to already know konami range
                        if csv_defence<=0:
                            csv_defence=1
                        elif csv_defence>99:
                            csv_defence=99
                        #print(player_id, csv_defence)
                        set_value(of, player_id, 7, 7, 127, csv_defence)
                        
                    if 'BALANCE' in list_of_column_names:
                        csv_balance=int(row[list_of_column_names.index('BALANCE')])
                        # Here we limit the stat to already know konami range
                        if csv_balance<=0:
                            csv_balance=1
                        elif csv_balance>99:
                            csv_balance=99
                        #print(player_id, csv_balance)
                        set_value(of, player_id, 9, 0, 127, csv_balance)
                        
                    if 'STAMINA' in list_of_column_names:
                        csv_stamina=int(row[list_of_column_names.index('STAMINA')])
                        # Here we limit the stat to already know konami range
                        if csv_stamina<=0:
                            csv_stamina=1
                        elif csv_stamina>99:
                            csv_stamina=99
                        #print(player_id, csv_stamina)
                        set_value(of, player_id, 9, 7, 127, csv_stamina)
                        
                    if 'TOP SPEED' in list_of_column_names:
                        csv_speed=int(row[list_of_column_names.index('TOP SPEED')])
                        # Here we limit the stat to already know konami range
                        if csv_speed<=0:
                            csv_speed=1
                        elif csv_speed>99:
                            csv_speed=99
                        #print(player_id, csv_speed)
                        set_value(of, player_id, 10, 6, 127, csv_speed)
                        
                    if 'ACCELERATION' in list_of_column_names:
                        csv_accel=int(row[list_of_column_names.index('ACCELERATION')])
                        # Here we limit the stat to already know konami range
                        if csv_accel<=0:
                            csv_accel=1
                        elif csv_accel>99:
                            csv_accel=99
                        #print(player_id, csv_accel)
                        set_value(of, player_id, 11, 5, 127, csv_accel)
                        
                    if 'RESPONSE' in list_of_column_names:
                        csv_response=int(row[list_of_column_names.index('RESPONSE')])
                        # Here we limit the stat to already know konami range
                        if csv_response<=0:
                            csv_response=1
                        elif csv_response>99:
                            csv_response=99
                        #print(player_id, csv_response)
                        set_value(of, player_id, 13, 0, 127, csv_response)
                        
                    if 'AGILITY' in list_of_column_names:
                        csv_agility=int(row[list_of_column_names.index('AGILITY')])
                        # Here we limit the stat to already know konami range
                        if csv_agility<=0:
                            csv_agility=1
                        elif csv_agility>99:
                            csv_agility=99
                        #print(player_id, csv_agility)
                        set_value(of, player_id, 13, 7, 127, csv_agility)
                        
                    if 'DRIBBLE ACCURACY' in list_of_column_names:
                        csv_dribAcc=int(row[list_of_column_names.index('DRIBBLE ACCURACY')])
                        # Here we limit the stat to already know konami range
                        if csv_dribAcc<=0:
                            csv_dribAcc=1
                        elif csv_dribAcc>99:
                            csv_dribAcc=99
                        #print(player_id, csv_dribAcc)
                        set_value(of, player_id, 14, 6, 127, csv_dribAcc)
                        
                    if 'DRIBBLE SPEED' in list_of_column_names:
                        csv_dribSpe=int(row[list_of_column_names.index('DRIBBLE SPEED')])
                        # Here we limit the stat to already know konami range
                        if csv_dribSpe<=0:
                            csv_dribSpe=1
                        elif csv_dribSpe>99:
                            csv_dribSpe=99
                        #print(player_id, csv_dribSpe)
                        set_value(of, player_id, 15, 5, 127, csv_dribSpe)
                        #hasta aca llegaste wacho
                        
                    if 'SHORT PASS ACCURACY' in list_of_column_names:
                        csv_sPassAcc=int(row[list_of_column_names.index('SHORT PASS ACCURACY')])
                        # Here we limit the stat to already know konami range
                        if csv_sPassAcc<=0:
                            csv_sPassAcc=1
                        elif csv_sPassAcc>99:
                            csv_sPassAcc=99
                        #print(player_id, csv_sPassAcc)
                        set_value(of, player_id, 17, 0, 127, csv_sPassAcc)
                        
                    if 'SHORT PASS SPEED' in list_of_column_names:
                        csv_sPassSpe=int(row[list_of_column_names.index('SHORT PASS SPEED')])
                        # Here we limit the stat to already know konami range
                        if csv_sPassSpe<=0:
                            csv_sPassSpe=1
                        elif csv_sPassSpe>99:
                            csv_sPassSpe=99
                        #print(player_id, csv_sPassSpe)
                        set_value(of, player_id, 17, 7, 127, csv_sPassSpe)
                        
                    if 'LONG PASS ACCURACY' in list_of_column_names:
                        csv_lPassAcc=int(row[list_of_column_names.index('LONG PASS ACCURACY')])
                        # Here we limit the stat to already know konami range
                        if csv_lPassAcc<=0:
                            csv_lPassAcc=1
                        elif csv_lPassAcc>99:
                            csv_lPassAcc=99
                        #print(player_id, csv_lPassAcc)
                        set_value(of, player_id, 18, 6, 127, csv_lPassAcc)
                        
                    if 'LONG PASS SPEED' in list_of_column_names:
                        csv_lPassSpe=int(row[list_of_column_names.index('LONG PASS SPEED')])
                        # Here we limit the stat to already know konami range
                        if csv_lPassSpe<=0:
                            csv_lPassSpe=1
                        elif csv_lPassSpe>99:
                            csv_lPassSpe=99
                        #print(player_id, csv_lPassSpe)
                        set_value(of, player_id, 19, 5, 127, csv_lPassSpe)
                        
                    if 'SHOT ACCURACY' in list_of_column_names:
                        csv_shotAcc=int(row[list_of_column_names.index('SHOT ACCURACY')])
                        # Here we limit the stat to already know konami range
                        if csv_shotAcc<=0:
                            csv_shotAcc=1
                        elif csv_shotAcc>99:
                            csv_shotAcc=99
                        #print(player_id, csv_shotAcc)
                        set_value(of, player_id, 21, 0, 127, csv_shotAcc)
                        
                    if 'SHOT POWER' in list_of_column_names:
                        csv_shotPow=int(row[list_of_column_names.index('SHOT POWER')])
                        # Here we limit the stat to already know konami range
                        if csv_shotPow<=0:
                            csv_shotPow=1
                        elif csv_shotPow>99:
                            csv_shotPow=99
                        #print(player_id, csv_shotPow)
                        set_value(of, player_id, 21, 7, 127, csv_shotPow)
                        
                    if 'SHOT TECHNIQUE' in list_of_column_names:
                        csv_shotTec=int(row[list_of_column_names.index('SHOT TECHNIQUE')])
                        # Here we limit the stat to already know konami range
                        if csv_shotTec<=0:
                            csv_shotTec=1
                        elif csv_shotTec>99:
                            csv_shotTec=99
                        #print(player_id, csv_shotTec)
                        set_value(of, player_id, 22, 6, 127, csv_shotTec)
                        
                    if 'FREE KICK ACCURACY' in list_of_column_names:
                        csv_fk=int(row[list_of_column_names.index('FREE KICK ACCURACY')])
                        # Here we limit the stat to already know konami range
                        if csv_fk<=0:
                            csv_fk=1
                        elif csv_fk>99:
                            csv_fk=99
                        #print(player_id, csv_fk)
                        set_value(of, player_id, 23, 5, 127, csv_fk)
                        
                    if 'CURLING' in list_of_column_names:
                        csv_curling=int(row[list_of_column_names.index('CURLING')])
                        # Here we limit the stat to already know konami range
                        if csv_curling<=0:
                            csv_curling=1
                        elif csv_curling>99:
                            csv_curling=99
                        #print(player_id, csv_curling)
                        set_value(of, player_id, 25, 0, 127, csv_curling)
                        
                    if 'HEADING' in list_of_column_names:
                        csv_heading=int(row[list_of_column_names.index('HEADING')])
                        # Here we limit the stat to already know konami range
                        if csv_heading<=0:
                            csv_heading=1
                        elif csv_heading>99:
                            csv_heading=99
                        #print(player_id, csv_heading)
                        set_value(of, player_id, 25, 7, 127, csv_heading)
                        
                    if 'JUMP' in list_of_column_names:
                        csv_jump=int(row[list_of_column_names.index('JUMP')])
                        # Here we limit the stat to already know konami range
                        if csv_jump<=0:
                            csv_jump=1
                        elif csv_jump>99:
                            csv_jump=99
                        #print(player_id, csv_jump)
                        set_value(of, player_id, 26, 6, 127, csv_jump)
                        
                    if 'TECHNIQUE' in list_of_column_names:
                        csv_tech=int(row[list_of_column_names.index('TECHNIQUE')])
                        # Here we limit the stat to already know konami range
                        if csv_tech<=0:
                            csv_tech=1
                        elif csv_tech>99:
                            csv_tech=99
                        #print(player_id, csv_tech)
                        set_value(of, player_id, 29, 0, 127, csv_tech)
                        
                    if 'AGGRESSION' in list_of_column_names:
                        csv_aggress=int(row[list_of_column_names.index('AGGRESSION')])
                        # Here we limit the stat to already know konami range
                        if csv_aggress<=0:
                            csv_aggress=1
                        elif csv_aggress>99:
                            csv_aggress=99
                        #print(player_id, csv_aggress)
                        set_value(of, player_id, 29, 7, 127, csv_aggress)
                        
                    if 'MENTALITY' in list_of_column_names:
                        csv_mental=int(row[list_of_column_names.index('MENTALITY')])
                        # Here we limit the stat to already know konami range
                        if csv_mental<=0:
                            csv_mental=1
                        elif csv_mental>99:
                            csv_mental=99
                        #print(player_id, csv_mental)
                        set_value(of, player_id, 30, 6, 127, csv_mental)
                        
                    if 'CONSISTENCY' in list_of_column_names:
                        csv_consistency=int(row[list_of_column_names.index('CONSISTENCY')]) - 1
                        # Here we limit the stat to already know konami range
                        if csv_consistency<0:
                            csv_consistency=0
                        elif csv_consistency>7:
                            csv_consistency=7
                        #print(player_id, csv_consistency)
                        set_value(of, player_id, 33, 7, 7, csv_consistency)
                        
                    if 'GOAL KEEPING' in list_of_column_names:
                        csv_gkAbil=int(row[list_of_column_names.index('GOAL KEEPING')])
                        # Here we limit the stat to already know konami range
                        if csv_gkAbil<=0:
                            csv_gkAbil=1
                        elif csv_gkAbil>99:
                            csv_gkAbil=99
                        #print(player_id, csv_gkAbil)
                        set_value(of, player_id, 31, 5, 127, csv_gkAbil)
                        
                    if 'TEAM WORK' in list_of_column_names:
                        csv_team=int(row[list_of_column_names.index('TEAM WORK')])
                        # Here we limit the stat to already know konami range
                        if csv_team<=0:
                            csv_team=1
                        elif csv_team>99:
                            csv_team=99
                        #print(player_id, csv_team)
                        set_value(of, player_id, 33, 0, 127, csv_team)
                        
                    if 'CONDITION / FITNESS' in list_of_column_names:
                        csv_condition=int(row[list_of_column_names.index('CONDITION / FITNESS')]) - 1
                        # Here we limit the stat to already know konami range
                        if csv_condition<0:
                            csv_condition=0
                        elif csv_condition>7:
                            csv_condition=7
                        #print(player_id, csv_condition)
                        set_value(of, player_id, 34, 2, 7, csv_condition)
                        
                    if 'STAT X' in list_of_column_names:
                        csv_statX=int(row[list_of_column_names.index('STAT X')]) - 1
                        # Here we limit the stat to already know konami range
                        if csv_statX<=0:
                            csv_statX=1
                        elif csv_statX>99:
                            csv_statX=99
                        #print(player_id, csv_statX)
                        set_value(of, player_id, 27, 5, 127, csv_statX)
                        
                    if 'DRIBBLING' in list_of_column_names:
                        csv_drib=int(row[list_of_column_names.index('DRIBBLING')])
                        # Here we limit the stat to already know konami range
                        if csv_drib<0:
                            csv_drib=0
                        elif csv_drib>1:
                            csv_drib=1
                        #print(player_id, csv_drib)
                        set_value(of, player_id, 24, 4, 1, csv_drib)
                        
                    if 'TACTICAL DRIBBLE' in list_of_column_names:
                        csv_dribKeep=int(row[list_of_column_names.index('TACTICAL DRIBBLE')])
                        # Here we limit the stat to already know konami range
                        if csv_dribKeep<0:
                            csv_dribKeep=0
                        elif csv_dribKeep>1:
                            csv_dribKeep=1
                        #print(player_id, csv_dribKeep)
                        set_value(of, player_id, 24, 5, 1, csv_dribKeep)
                        
                    if 'POST PLAYER' in list_of_column_names:
                        csv_post=int(row[list_of_column_names.index('POST PLAYER')])
                        # Here we limit the stat to already know konami range
                        if csv_post<0:
                            csv_post=0
                        elif csv_post>1:
                            csv_post=1
                        #print(player_id, csv_post)
                        set_value(of, player_id, 32, 4, 1, csv_post)
                        
                    if 'POSITIONING' in list_of_column_names:
                        csv_posit=int(row[list_of_column_names.index('POSITIONING')])
                        # Here we limit the stat to already know konami range
                        if csv_posit<0:
                            csv_posit=0
                        elif csv_posit>1:
                            csv_posit=1
                        #print(player_id, csv_posit)
                        set_value(of, player_id, 24, 6, 1, csv_posit)
                        
                    if 'REACTION' in list_of_column_names:
                        csv_offside=int(row[list_of_column_names.index('REACTION')])
                        # Here we limit the stat to already know konami range
                        if csv_offside<0:
                            csv_offside=0
                        elif csv_offside>1:
                            csv_offside=1
                        #print(player_id, csv_offside)
                        set_value(of, player_id, 24, 7, 1, csv_offside)
                        
                    if 'LINES' in list_of_column_names:
                        csv_linePos=int(row[list_of_column_names.index('LINES')])
                        # Here we limit the stat to already know konami range
                        if csv_linePos<0:
                            csv_linePos=0
                        elif csv_linePos>1:
                            csv_linePos=1
                        #print(player_id, csv_linePos)
                        set_value(of, player_id, 32, 5, 1, csv_linePos)
                        
                    if 'MIDDLE SHOOTING' in list_of_column_names:
                        csv_midShot=int(row[list_of_column_names.index('MIDDLE SHOOTING')])
                        # Here we limit the stat to already know konami range
                        if csv_midShot<0:
                            csv_midShot=0
                        elif csv_midShot>1:
                            csv_midShot=1
                        #print(player_id, csv_midShot)
                        set_value(of, player_id, 32, 6, 1, csv_midShot)
                        
                    if 'SCORING' in list_of_column_names:
                        csv_scorer=int(row[list_of_column_names.index('SCORING')])
                        # Here we limit the stat to already know konami range
                        if csv_scorer<0:
                            csv_scorer=0
                        elif csv_scorer>1:
                            csv_scorer=1
                        #print(player_id, csv_scorer)
                        set_value(of, player_id, 28, 6, 1, csv_scorer)
                        
                    if 'PLAYMAKING' in list_of_column_names:
                        csv_play=int(row[list_of_column_names.index('PLAYMAKING')])
                        # Here we limit the stat to already know konami range
                        if csv_play<0:
                            csv_play=0
                        elif csv_play>1:
                            csv_play=1
                        #print(player_id, csv_play)
                        set_value(of, player_id, 28, 4, 1, csv_play)
                        
                    if 'PASSING' in list_of_column_names:
                        csv_pass=int(row[list_of_column_names.index('PASSING')])
                        # Here we limit the stat to already know konami range
                        if csv_pass<0:
                            csv_pass=0
                        elif csv_pass>1:
                            csv_pass=1
                        #print(player_id, csv_pass)
                        set_value(of, player_id, 28, 5, 1, csv_pass)
                        
                    if 'B F FEINT' in list_of_column_names:
                        csv_bff=int(row[list_of_column_names.index('B F FEINT')])
                        # Here we limit the stat to already know konami range
                        if csv_bff<0:
                            csv_bff=0
                        elif csv_bff>1:
                            csv_bff=1
                        #print(player_id, csv_bff)
                        set_value(of, player_id, 20, 6, 1, csv_bff)
                        
                    if 'PENALTIES' in list_of_column_names:
                        csv_pk=int(row[list_of_column_names.index('PENALTIES')])
                        # Here we limit the stat to already know konami range
                        if csv_pk<0:
                            csv_pk=0
                        elif csv_pk>1:
                            csv_pk=1
                        #print(player_id, csv_pk)
                        set_value(of, player_id, 35, 6, 1, csv_pk)
                        
                    if '1-1 SCORING' in list_of_column_names:
                        csv_k11=int(row[list_of_column_names.index('1-1 SCORING')])
                        # Here we limit the stat to already know konami range
                        if csv_k11<0:
                            csv_k11=0
                        elif csv_k11>1:
                            csv_k11=1
                        #print(player_id, csv_k11)
                        set_value(of, player_id, 28, 7, 1, csv_k11)
                        
                    if 'LONG THROW' in list_of_column_names:
                        csv_longThrow=int(row[list_of_column_names.index('LONG THROW')])
                        # Here we limit the stat to already know konami range
                        if csv_longThrow<0:
                            csv_longThrow=0
                        elif csv_longThrow>1:
                            csv_longThrow=1
                        #print(player_id, csv_longThrow)
                        set_value(of, player_id, 36, 7, 1, csv_longThrow)
                        
                    if '1-TOUCH PASS' in list_of_column_names:
                        csv_direct=int(row[list_of_column_names.index('1-TOUCH PASS')])
                        # Here we limit the stat to already know konami range
                        if csv_direct<0:
                            csv_direct=0
                        elif csv_direct>1:
                            csv_direct=1
                        #print(player_id, csv_direct)
                        set_value(of, player_id, 35, 7, 1, csv_direct)
                        
                    if 'SIDE' in list_of_column_names:
                        csv_side=int(row[list_of_column_names.index('SIDE')])
                        # Here we limit the stat to already know konami range
                        if csv_side<0:
                            csv_side=0
                        elif csv_side>1:
                            csv_side=1
                        #print(player_id, csv_side)
                        set_value(of, player_id, 32, 7, 1, csv_side)
                        
                    if 'CENTRE' in list_of_column_names:
                        csv_centre=int(row[list_of_column_names.index('CENTRE')])
                        # Here we limit the stat to already know konami range
                        if csv_centre<0:
                            csv_centre=0
                        elif csv_centre>1:
                            csv_centre=1
                        #print(player_id, csv_centre)
                        set_value(of, player_id, 35, 5, 1, csv_centre)
                        
                    if 'OUTSIDE' in list_of_column_names:
                        csv_outside=int(row[list_of_column_names.index('OUTSIDE')])
                        # Here we limit the stat to already know konami range
                        if csv_outside<0:
                            csv_outside=0
                        elif csv_outside>1:
                            csv_outside=1
                        #print(player_id, csv_outside)
                        set_value(of, player_id, 36, 0, 1, csv_outside)
                        
                    if 'MARKING' in list_of_column_names:
                        csv_man=int(row[list_of_column_names.index('MARKING')])
                        # Here we limit the stat to already know konami range
                        if csv_man<0:
                            csv_man=0
                        elif csv_man>1:
                            csv_man=1
                        #print(player_id, csv_man)
                        set_value(of, player_id, 36, 1, 1, csv_man)
                        
                    if 'D-LINE CONTROL' in list_of_column_names:
                        csv_dLine=int(row[list_of_column_names.index('D-LINE CONTROL')])
                        # Here we limit the stat to already know konami range
                        if csv_dLine<0:
                            csv_dLine=0
                        elif csv_dLine>1:
                            csv_dLine=1
                        #print(player_id, csv_dLine)
                        set_value(of, player_id, 36, 4, 1, csv_dLine)
                        
                    if 'SLIDING' in list_of_column_names:
                        csv_slide=int(row[list_of_column_names.index('SLIDING')])
                        # Here we limit the stat to already know konami range
                        if csv_slide<0:
                            csv_slide=0
                        elif csv_slide>1:
                            csv_slide=1
                        #print(player_id, csv_slide)
                        set_value(of, player_id, 36, 2, 1, csv_slide)
                        
                    if 'COVERING' in list_of_column_names:
                        csv_cover=int(row[list_of_column_names.index('COVERING')])
                        # Here we limit the stat to already know konami range
                        if csv_cover<0:
                            csv_cover=0
                        elif csv_cover>1:
                            csv_cover=1
                        #print(player_id, csv_cover)
                        set_value(of, player_id, 36, 3, 1, csv_cover)
                        
                    if 'GK KICK' in list_of_column_names:
                        csv_gkKick=int(row[list_of_column_names.index('GK KICK')])
                        # Here we limit the stat to already know konami range
                        if csv_gkKick<0:
                            csv_gkKick=0
                        elif csv_gkKick>1:
                            csv_gkKick=1
                        #print(player_id, csv_gkKick)
                        set_value(of, player_id, 20, 7, 1, csv_gkKick)
                        
                    if 'PENALTY STOPPER' in list_of_column_names:
                        csv_keeperPK=int(row[list_of_column_names.index('PENALTY STOPPER')])
                        # Here we limit the stat to already know konami range
                        if csv_keeperPK<0:
                            csv_keeperPK=0
                        elif csv_keeperPK>1:
                            csv_keeperPK=1
                        #print(player_id, csv_keeperPK)
                        set_value(of, player_id, 36, 5, 1, csv_keeperPK)
                        
                    if '1-ON-1 STOPPER' in list_of_column_names:
                        csv_keeper11=int(row[list_of_column_names.index('1-ON-1 STOPPER')])
                        # Here we limit the stat to already know konami range
                        if csv_keeper11<0:
                            csv_keeper11=0
                        elif csv_keeper11>1:
                            csv_keeper11=1
                        #print(player_id, csv_keeper11)
                        set_value(of, player_id, 36, 6, 1, csv_keeper11)
                        
                    if 'INJURY TOLERANCE' in list_of_column_names:
                        csv_injury=(row[list_of_column_names.index('INJURY TOLERANCE')])
                        if csv_injury == "A":
                            csv_injury = 2
                        elif csv_injury == "B":
                            csv_injury = 1
                        else:
                            csv_injury = 0
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_injury)
                        set_value(of, player_id, 35, 3, 3, csv_injury)
                        
                    if 'DRIBBLE STYLE' in list_of_column_names:
                        csv_dribSty=int(row[list_of_column_names.index('DRIBBLE STYLE')]) - 1
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_dribSty)
                        set_value(of, player_id, 6, 0, 3, csv_dribSty)
                        
                    if 'FREE KICK STYLE' in list_of_column_names:
                        csv_freekick=int(row[list_of_column_names.index('FREE KICK STYLE')]) - 1
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_freekick)
                        set_value(of, player_id, 5, 1, 15, csv_freekick)
                        
                    if 'PK STYLE' in list_of_column_names:
                        csv_pkStyle=int(row[list_of_column_names.index('PK STYLE')]) - 1
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_pkStyle)
                        set_value(of, player_id, 5, 5, 7, csv_pkStyle)
                        
                    if 'DROP KICK STYLE' in list_of_column_names:
                        csv_dkSty=int(row[list_of_column_names.index('DROP KICK STYLE')]) - 1
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_dkSty)
                        set_value(of, player_id, 6, 2, 3, csv_dkSty)
                        
                    if 'AGE' in list_of_column_names:
                        csv_age=int(row[list_of_column_names.index('AGE')])-15
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_age)
                        set_value(of, player_id, 62, 5, 31, csv_age)
                        
                    if 'WEIGHT' in list_of_column_names:
                        csv_weight=int(row[list_of_column_names.index('WEIGHT')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_weight)
                        set_value(of, player_id, 41, 6, 127, csv_weight)
                        
                    if 'NATIONALITY' in list_of_column_names:
                        csv_nation=nationalities.index(row[list_of_column_names.index('NATIONALITY')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_nation)
                        set_value(of, player_id, 63, 2, 127, csv_nation)
                        
                    if 'CALLNAME ID' in list_of_column_names:
                        csv_callName=int(row[list_of_column_names.index('CALLNAME ID')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_callName)
                        set_value(of, player_id, 1, 0, 65535, csv_callName)
                        
                    if 'STAT EDITED' in list_of_column_names:
                        csv_statEdited=int(row[list_of_column_names.index('STAT EDITED')])
                        # Here we limit the stat to already know konami range
                        if csv_statEdited<0:
                            csv_statEdited=0
                        elif csv_statEdited>1:
                            csv_statEdited=1
                        #print(player_id, csv_statEdited)
                        set_value(of, player_id, 39, 7, 1, csv_statEdited)
                        
                    if (('BOOT TYPE' in list_of_column_names) and ('BOOT COLOUR' in list_of_column_names)):
                        csv_boot_type=int(row[list_of_column_names.index('BOOT TYPE')])
                        csv_boot_colour=int(row[list_of_column_names.index('BOOT COLOUR')])
                        #print(player_id, csv_boot_type, csv_boot_colour)
                        set_boot_type_colour(of, player_id, 51, csv_boot_type, csv_boot_colour)
                    # breaking the loop after the 
                    # first iteration itself 
                    #break
                return True
    except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
        #print ("something happened")
        return False

nationalities = ["Austria", "Belgium", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "England", "Finland", "France", "Germany", "Greece", 
"Hungary", "Ireland", "Italy", "Latvia", "Netherlands", "Northern Ireland", "Norway", "Poland", "Portugal", "Romania", "Russia", "Scotland", "Serbia and Montenegro", 
"Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "Wales", "Cameroon", "Cote d'Ivoire", "Morocco", "Nigeria", 
"Senegal", "South Africa", "Tunisia", "Costa Rica", "Mexico", "USA", "Argentina", "Brazil", "Chile", "Colombia", 
"Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela", "China", "Iran", "Japan", "Saudi Arabia", "South Korea", "Australia", "Albania", "Armenia", "Belarus", 
"Bosnia and Herzegovina", "Cyprus", "Georgia", "Estonia", "Faroe Islands", "Iceland", "Israel", "Lithuania", "Luxembourg", "Macedonia", "Moldova", "Algeria", 
"Angola", "Burkina Faso", "Cape Verde", "Congo", "DR Congo", "Egypt", "Equatorial Guinea", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Liberia", 
"Libya", "Mali", "Mauritius", "Mozambique", "Namibia", "Sierra Leone", "Togo", "Zambia", "Zimbabwe", "Canada", "Grenada", "Guadeloupe", "Guatemala", "Honduras", 
"Jamaica", "Martinique", "Netherlands Antilles", "Panama", "Trinidad and Tobago", "Bolivia", "Guyana", "Uzbekistan", "New Zealand", "Free Nationality" ]
