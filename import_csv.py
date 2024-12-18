import csv
from tkinter import messagebox
from player_data import set_value, set_name, set_shirt_name, get_value
#from psd import import_stats_from_psd
import traceback

def load_csv(of, file):
    try:
        with open(file, 'r', encoding='utf-8') as csvf:
            # list to store the names of columns
            csv_reader = csv.reader(csvf, delimiter = ',')
            list_of_column_names = []
            # csv_psd_link = ""
          
            # loop to iterate thorugh the rows of csv 
            for row in csv_reader: 
          
                # adding the first row 
                list_of_column_names = row
          
                # breaking the loop after the 
                # first iteration itself 
                break
            print(list_of_column_names)
            if 'ID' in list_of_column_names:
                for row in csv_reader: 
                    
                    player_id_str = (row[list_of_column_names.index('ID')])
                    print(player_id_str)
                    if player_id_str == "": continue
                    else: player_id = int(player_id_str)
                    
                    # Basic settings

                    if 'NAME' in list_of_column_names:
                        csv_name=(row[list_of_column_names.index('NAME')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_name)
                        if csv_name !="":
                            set_name(of, player_id, csv_name)
                        
                    if 'SHIRT_NAME' in list_of_column_names:
                        csv_shirt_name=(row[list_of_column_names.index('SHIRT_NAME')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_shirt_name)
                        if csv_shirt_name !="":
                            set_shirt_name(of, player_id, csv_shirt_name)

                    if 'CALLNAME ID' in list_of_column_names:
                        csv_callName=(row[list_of_column_names.index('CALLNAME ID')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_callName)
                        if csv_callName !="":
                            try:
                                set_value(of, player_id, 1, 0, 65535, int(csv_callName))
                            except (ValueError, TypeError):
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with callname, must be an integer not string\nError type: {e}")
                        
                    if 'NATIONALITY' in list_of_column_names:
                        csv_nation=row[list_of_column_names.index('NATIONALITY')]
                        if csv_nation !="":
                            if (csv_nation) in nationalities:
                                csv_nation = nationalities.index(csv_nation)
                            else:
                                csv_nation = nationalities.index("Free Nationality")
                            #print(player_id, csv_nation)
                            set_value(of, player_id, 63, 2, 127, csv_nation)
                        
                    if 'AGE' in list_of_column_names:
                        csv_age=(row[list_of_column_names.index('AGE')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_age)
                        if csv_age !="":
                            try:
                                set_value(of, player_id, 62, 5, 31, int(csv_age)-15)
                            except (ValueError, TypeError):
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with age, must be an integer not string\nError type: {e}")
                        
                    if 'STRONG FOOT' in list_of_column_names:
                        csv_foot=(row[list_of_column_names.index('STRONG FOOT')])
                        # Here we limit the stat to already know konami range
                        if csv_foot !="":
                            if csv_foot=="R":
                                csv_foot=0
                            else:
                                csv_foot=1
                            #print(player_id, csv_foot)
                            set_value(of, player_id, 5, 0, 1, csv_foot)

                    if 'INJURY TOLERANCE' in list_of_column_names:
                        csv_injury=(row[list_of_column_names.index('INJURY TOLERANCE')])
                        if csv_injury !="":
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
                        csv_dribSty=(row[list_of_column_names.index('DRIBBLE STYLE')])
                        if (csv_dribSty !=""):
                            # Here we limit the stat to already know konami range
                            #print(player_id, csv_dribSty)
                            try:
                                set_value(of, player_id, 6, 0, 3, int(csv_dribSty)-1)
                            except (ValueError, TypeError):
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with DRIBBLE STYLE, must be an integer not string\nError type: {e}")

                    if 'FREE KICK STYLE' in list_of_column_names:
                        csv_freekick=(row[list_of_column_names.index('FREE KICK STYLE')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_freekick)
                        if csv_freekick !="":
                            try:
                                set_value(of, player_id, 5, 1, 15, int(csv_freekick)-1)
                            except (ValueError, TypeError):
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with FREE KICK STYLE, must be an integer not string\nError type: {e}")
                        
                    if 'PK STYLE' in list_of_column_names:
                        csv_pkStyle=(row[list_of_column_names.index('PK STYLE')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_pkStyle)
                        if csv_pkStyle !="":
                            try:
                                set_value(of, player_id, 5, 5, 7, int(csv_pkStyle)-1)
                            except (ValueError, TypeError):
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with PK STYLE, must be an integer not string\nError type: {e}")
                        
                    if 'DROP KICK STYLE' in list_of_column_names:
                        csv_dkSty=(row[list_of_column_names.index('DROP KICK STYLE')])
                        if csv_dkSty !="":
                            # Here we limit the stat to already know konami range
                            #print(player_id, csv_dkSty)
                            try:
                                set_value(of, player_id, 6, 2, 3, int(csv_dkSty)-1)
                            except (ValueError, TypeError):
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with DROP KICK STYLE, must be an integer not string\nError type: {e}")

                    if 'GOAL CELEBRATION 1' in list_of_column_names:
                        csv_goal_c1=(row[list_of_column_names.index('GOAL CELEBRATION 1')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_goal_c1)
                        if csv_goal_c1 !="":
                            try:
                                set_value(of, player_id, 85-48, 1, 127, int(csv_goal_c1))
                            except (ValueError, TypeError):
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with GOAL CELEBRATION 1, must be an integer not string\nError type: {e}")

                    if 'GOAL CELEBRATION 2' in list_of_column_names:
                        csv_goal_c2=(row[list_of_column_names.index('GOAL CELEBRATION 2')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_goal_c2)
                        if csv_goal_c2 !="":
                            try:
                                set_value(of, player_id, 86-48, 0, 127, int(csv_goal_c2))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with GOAL CELEBRATION 2, must be an integer not string\nError type: {e}")

                        
                    if 'GROWTH TYPE' in list_of_column_names:
                        csv_growth_type=int(row[list_of_column_names.index('GROWTH TYPE')])
                        #Here we limit the stat to already know konami range
                        #print(player_id, csv_growth_type)
                        set_value(of, player_id, 87-48, 0, 0xff, csv_growth_type)

                    # Position settings


                    if 'REGISTERED POSITION' in list_of_column_names:
                        csv_regPos=(row[list_of_column_names.index('REGISTERED POSITION')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_regPos)
                        if csv_regPos!="":
                            try:
                                set_value(of, player_id, 6, 4, 15, int(csv_regPos))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with REGISTERED POSITION, must be an integer not string\nError type: {e}")

                    if 'FAVOURED SIDE' in list_of_column_names:
                        csv_favSide=(row[list_of_column_names.index('FAVOURED SIDE')])
                        # Here we limit the stat to already know konami range
                        if csv_favSide!="":
                            player_foot = get_value(of, player_id, 53-48, 0, 1, "Foot")
                            if player_foot: # L
                                if csv_favSide=="L":
                                    csv_favSide=0
                                elif csv_favSide=="R":
                                    csv_favSide=1
                                else:
                                    csv_favSide=2
                            else: # R
                                if csv_favSide=="R":
                                    csv_favSide=0
                                elif csv_favSide=="L":
                                    csv_favSide=1
                                else:
                                    csv_favSide=2
                            #print(player_id, csv_favSide)
                            set_value(of, player_id, 20, 6, 3, csv_favSide)                   

                    if 'GK  0' in list_of_column_names:
                        csv_gk=(row[list_of_column_names.index('GK  0')])
                        # Here we limit the stat to already know konami range
                        #if csv_gk<0:
                        #    csv_gk=0
                        #elif csv_gk>1:
                        #    csv_gk=1
                        #print(player_id, csv_gk)
                        if csv_gk!="":
                            try:
                                set_value(of, player_id, 8, 6, 1, int(csv_gk))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with GK  0, must be an integer not string\nError type: {e}")

                    if 'CWP  2' in list_of_column_names:
                        csv_cbwS=(row[list_of_column_names.index('CWP  2')])
                        # Here we limit the stat to already know konami range
                        #if csv_cbwS<0:
                        #    csv_cbwS=0
                        #elif csv_cbwS>1:
                        #    csv_cbwS=1
                        #print(player_id, csv_cbwS)
                        if csv_cbwS!="":
                            try:
                                set_value(of, player_id, 8, 7, 1, int(csv_cbwS))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with CWP  2, must be an integer not string\nError type: {e}")

                    if 'CBT  3' in list_of_column_names:
                        csv_cbt=(row[list_of_column_names.index('CBT  3')])
                        # Here we limit the stat to already know konami range
                        #if csv_cbt<0:
                        #    csv_cbt=0
                        #elif csv_cbt>1:
                        #    csv_cbt=1
                        #print(player_id, csv_cbt)
                        if csv_cbt!="":
                            try:
                                set_value(of, player_id, 12, 4, 1, int(csv_cbt))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with CBT  3, must be an integer not string\nError type: {e}")

                    if 'SB  4' in list_of_column_names:
                        csv_sb=int(row[list_of_column_names.index('SB  4')])
                        # Here we limit the stat to already know konami range
                        #if csv_sb<0:
                        #    csv_sb=0
                        #elif csv_sb>1:
                        #    csv_sb=1
                        #print(player_id, csv_sb)
                        if csv_sb!="":
                            try:
                                set_value(of, player_id, 12, 5, 1, int(csv_sb))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with SB  4, must be an integer not string\nError type: {e}")

                    if 'DMF  5' in list_of_column_names:
                        csv_dm=(row[list_of_column_names.index('DMF  5')])
                        # Here we limit the stat to already know konami range
                        if csv_dm!="":
                            try:
                                set_value(of, player_id, 12, 6, 1, int(csv_dm))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with DMF  5, must be an integer not string\nError type: {e}")

                    if 'WB  6' in list_of_column_names:
                        csv_wb=(row[list_of_column_names.index('WB  6')])
                        # Here we limit the stat to already know konami range
                        #if csv_wb<0:
                        #    csv_wb=0
                        #elif csv_wb>1:
                        #    csv_wb=1
                        #print(player_id, csv_wb)
                        if csv_wb!="":
                            try:
                                set_value(of, player_id, 12, 7, 1, int(csv_wb))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with WB  6, must be an integer not string\nError type: {e}")


                    if 'CMF  7' in list_of_column_names:
                        csv_cm=(row[list_of_column_names.index('CMF  7')])
                        # Here we limit the stat to already know konami range
                        #if csv_cm<0:
                        #    csv_cm=0
                        #elif csv_cm>1:
                        #    csv_cm=1
                        #print(player_id, csv_cm)
                        if csv_cm!="":
                            try:
                                set_value(of, player_id, 16, 4, 1, int(csv_cm))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with CMF  6, must be an integer not string\nError type: {e}")

                        
                    if 'SMF  8' in list_of_column_names:
                        csv_sm=(row[list_of_column_names.index('SMF  8')])
                        # Here we limit the stat to already know konami range
                        #if csv_sm<0:
                        #    csv_sm=0
                        #elif csv_sm>1:
                        #    csv_sm=1
                        #print(player_id, csv_sm)
                        if (csv_sm!=""):
                            try:
                                set_value(of, player_id, 16, 5, 1, int(csv_sm))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with SMF  8, must be an integer not string\nError type: {e}")

                        
                    if 'AMF  9' in list_of_column_names:
                        csv_om=(row[list_of_column_names.index('AMF  9')])
                        # Here we limit the stat to already know konami range
                        #if csv_om<0:
                        #    csv_om=0
                        #elif csv_om>1:
                        #    csv_om=1
                        #print(player_id, csv_om)
                        if csv_om!="":
                            try:
                                set_value(of, player_id, 16, 6, 1, int(csv_om))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with AMF  9, must be an integer not string\nError type: {e}")

                        
                    if 'WF 10' in list_of_column_names:
                        csv_wg=(row[list_of_column_names.index('WF 10')])
                        # Here we limit the stat to already know konami range
                        #if csv_wg<0:
                        #    csv_wg=0
                        #elif csv_wg>1:
                        #    csv_wg=1
                        #print(player_id, csv_wg)
                        if csv_wg !="":
                            try:
                                set_value(of, player_id, 16, 7, 1, int(csv_wg))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with WF  10, must be an integer not string\nError type: {e}")

                        
                    if 'SS  11' in list_of_column_names:
                        csv_ss=(row[list_of_column_names.index('SS  11')])
                        # Here we limit the stat to already know konami range
                        #if csv_ss<0:
                        #    csv_ss=0
                        #elif csv_ss>1:
                        #    csv_ss=1
                        #print(player_id, csv_ss)
                        if csv_ss !="":
                            try:
                                set_value(of, player_id, 20, 4, 1, int(csv_ss))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with SS  11, must be an integer not string\nError type: {e}")

                    if 'CF  12' in list_of_column_names:
                        csv_cf=(row[list_of_column_names.index('CF  12')])
                        # Here we limit the stat to already know konami range
                        #if csv_cf<0:
                        #    csv_cf=0
                        #elif csv_cf>1:
                        #    csv_cf=1
                        #print(player_id, csv_cf)
                        if csv_cf !="":
                            try:
                                set_value(of, player_id, 20, 5, 1, int(csv_cf))
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with CF  12, must be an integer not string\nError type: {e}")

                    # Player ability settings     
                        
                        
                    if 'WEAK FOOT ACCURACY' in list_of_column_names:
                        csv_wfa=(row[list_of_column_names.index('WEAK FOOT ACCURACY')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_wfa)
                        if csv_wfa!="":
                            try:
                                set_value(of, player_id, 34, 5, 7, int(csv_wfa)-1)
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with WEAK FOOT ACCURACY, must be an integer not string\nError type: {e}")

                    if 'WEAK FOOT FREQUENCY' in list_of_column_names:
                        csv_wff=(row[list_of_column_names.index('WEAK FOOT FREQUENCY')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_wff)
                        if (csv_wff!=""):
                            try:
                                set_value(of, player_id, 35, 0, 7, int(csv_wff)-1)
                            except (ValueError, TypeError) as e:
                                messagebox.showerror(f"ERROR", "error on player id {player_id} with WEAK FOOT FREQUENCY, must be an integer not string\nError type: {e}")
                        
                    if 'ATTACK' in list_of_column_names:
                        csv_attack=(row[list_of_column_names.index('ATTACK')])
                        if csv_attack == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_attack<=0:
                        #    csv_attack=1
                        #elif csv_attack>99:
                        #    csv_attack=99
                        #print(player_id, csv_attack)
                        set_value(of, player_id, 7, 0, 127, int(csv_attack))
                        
                    if 'DEFENSE' in list_of_column_names:
                        csv_defence=(row[list_of_column_names.index('DEFENSE')])
                        if csv_attack == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_defence<=0:
                        #    csv_defence=1
                        #elif csv_defence>99:
                        #    csv_defence=99
                        #print(player_id, csv_defence)
                        set_value(of, player_id, 7, 7, 127, int(csv_defence))
                        
                    if 'BALANCE' in list_of_column_names:
                        csv_balance=(row[list_of_column_names.index('BALANCE')])
                        if csv_balance == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_balance<=0:
                        #    csv_balance=1
                        #elif csv_balance>99:
                        #    csv_balance=99
                        #print(player_id, csv_balance)
                        set_value(of, player_id, 9, 0, 127, int(csv_balance))
                        
                    if 'STAMINA' in list_of_column_names:
                        csv_stamina=(row[list_of_column_names.index('STAMINA')])
                        if csv_stamina == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_stamina<=0:
                        #    csv_stamina=1
                        #elif csv_stamina>99:
                        #    csv_stamina=99
                        #print(player_id, csv_stamina)
                        set_value(of, player_id, 9, 7, 127, int(csv_stamina))
                        
                    if 'TOP SPEED' in list_of_column_names:
                        csv_speed=(row[list_of_column_names.index('TOP SPEED')])
                        if csv_speed == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_speed<=0:
                        #    csv_speed=1
                        #elif csv_speed>99:
                        #    csv_speed=99
                        #print(player_id, csv_speed)
                        set_value(of, player_id, 10, 6, 127, int(csv_speed))
                        
                    if 'ACCELERATION' in list_of_column_names:
                        csv_accel=(row[list_of_column_names.index('ACCELERATION')])
                        if csv_accel == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_accel<=0:
                        #    csv_accel=1
                        #elif csv_accel>99:
                        #    csv_accel=99
                        #print(player_id, csv_accel)
                        set_value(of, player_id, 11, 5, 127, int(csv_accel))
                        
                    if 'RESPONSE' in list_of_column_names:
                        csv_response=(row[list_of_column_names.index('RESPONSE')])
                        if csv_response == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_response<=0:
                        #    csv_response=1
                        #elif csv_response>99:
                        #    csv_response=99
                        #print(player_id, csv_response)
                        set_value(of, player_id, 13, 0, 127, int(csv_response))
                        
                    if 'AGILITY' in list_of_column_names:
                        csv_agility=(row[list_of_column_names.index('AGILITY')])
                        if csv_agility == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_agility<=0:
                        #    csv_agility=1
                        #elif csv_agility>99:
                        #    csv_agility=99
                        #print(player_id, csv_agility)
                        set_value(of, player_id, 13, 7, 127, int(csv_agility))
                        
                    if 'DRIBBLE ACCURACY' in list_of_column_names:
                        csv_dribAcc=(row[list_of_column_names.index('DRIBBLE ACCURACY')])
                        if csv_dribAcc == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_dribAcc<=0:
                        #    csv_dribAcc=1
                        #elif csv_dribAcc>99:
                        #    csv_dribAcc=99
                        #print(player_id, csv_dribAcc)
                        set_value(of, player_id, 14, 6, 127, int(csv_dribAcc))
                        
                    if 'DRIBBLE SPEED' in list_of_column_names:
                        csv_dribSpe=(row[list_of_column_names.index('DRIBBLE SPEED')])
                        if csv_dribSpe == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_dribSpe<=0:
                        #    csv_dribSpe=1
                        #elif csv_dribSpe>99:
                        #    csv_dribSpe=99
                        #print(player_id, csv_dribSpe)
                        set_value(of, player_id, 15, 5, 127, int(csv_dribSpe))
                        
                    if 'SHORT PASS ACCURACY' in list_of_column_names:
                        csv_sPassAcc=(row[list_of_column_names.index('SHORT PASS ACCURACY')])
                        if csv_sPassAcc == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_sPassAcc<=0:
                        #    csv_sPassAcc=1
                        #elif csv_sPassAcc>99:
                        #    csv_sPassAcc=99
                        #print(player_id, csv_sPassAcc)
                        set_value(of, player_id, 17, 0, 127, int(csv_sPassAcc))
                        
                    if 'SHORT PASS SPEED' in list_of_column_names:
                        csv_sPassSpe=(row[list_of_column_names.index('SHORT PASS SPEED')])
                        if csv_sPassSpe == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_sPassSpe<=0:
                        #    csv_sPassSpe=1
                        #elif csv_sPassSpe>99:
                        #    csv_sPassSpe=99
                        #print(player_id, csv_sPassSpe)
                        set_value(of, player_id, 17, 7, 127, int(csv_sPassSpe))
                        
                    if 'LONG PASS ACCURACY' in list_of_column_names:
                        csv_lPassAcc=(row[list_of_column_names.index('LONG PASS ACCURACY')])
                        if csv_lPassAcc == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_lPassAcc<=0:
                        #    csv_lPassAcc=1
                        #elif csv_lPassAcc>99:
                        #    csv_lPassAcc=99
                        #print(player_id, csv_lPassAcc)
                        set_value(of, player_id, 18, 6, 127, int(csv_lPassAcc))
                        
                    if 'LONG PASS SPEED' in list_of_column_names:
                        csv_lPassSpe=(row[list_of_column_names.index('LONG PASS SPEED')])
                        # Here we limit the stat to already know konami range
                        #if csv_lPassSpe<=0:
                        #    csv_lPassSpe=1
                        #elif csv_lPassSpe>99:
                        #    csv_lPassSpe=99
                        #print(player_id, csv_lPassSpe)
                        set_value(of, player_id, 19, 5, 127, int(csv_lPassSpe))
                        
                    if 'SHOT ACCURACY' in list_of_column_names:
                        csv_shotAcc=(row[list_of_column_names.index('SHOT ACCURACY')])
                        if csv_shotAcc == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_shotAcc<=0:
                        #    csv_shotAcc=1
                        #elif csv_shotAcc>99:
                        #    csv_shotAcc=99
                        #print(player_id, csv_shotAcc)
                        set_value(of, player_id, 21, 0, 127, int(csv_shotAcc))
                        
                    if 'SHOT POWER' in list_of_column_names:
                        csv_shotPow=(row[list_of_column_names.index('SHOT POWER')])
                        if csv_shotPow == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_shotPow<=0:
                        #    csv_shotPow=1
                        #elif csv_shotPow>99:
                        #    csv_shotPow=99
                        #print(player_id, csv_shotPow)
                        set_value(of, player_id, 21, 7, 127, int(csv_shotPow))
                        
                    if 'SHOT TECHNIQUE' in list_of_column_names:
                        csv_shotTec=(row[list_of_column_names.index('SHOT TECHNIQUE')])
                        if csv_shotTec == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_shotTec<=0:
                        #    csv_shotTec=1
                        #elif csv_shotTec>99:
                        #    csv_shotTec=99
                        #print(player_id, csv_shotTec)
                        set_value(of, player_id, 22, 6, 127, int(csv_shotTec))
                        
                    if 'FREE KICK ACCURACY' in list_of_column_names:
                        csv_fk=(row[list_of_column_names.index('FREE KICK ACCURACY')])
                        if csv_fk == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_fk<=0:
                        #    csv_fk=1
                        #elif csv_fk>99:
                        #    csv_fk=99
                        #print(player_id, csv_fk)
                        set_value(of, player_id, 23, 5, 127, int(csv_fk))
                        
                    if 'CURLING' in list_of_column_names:
                        csv_curling=(row[list_of_column_names.index('CURLING')])
                        if csv_curling == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_curling<=0:
                        #    csv_curling=1
                        #elif csv_curling>99:
                        #    csv_curling=99
                        #print(player_id, csv_curling)
                        set_value(of, player_id, 25, 0, 127, int(csv_curling))
                        
                    if 'HEADING' in list_of_column_names:
                        csv_heading=(row[list_of_column_names.index('HEADING')])
                        if csv_heading == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_heading<=0:
                        #    csv_heading=1
                        #elif csv_heading>99:
                        #    csv_heading=99
                        #print(player_id, csv_heading)
                        set_value(of, player_id, 25, 7, 127, int(csv_heading))
                        
                    if 'JUMP' in list_of_column_names:
                        csv_jump=(row[list_of_column_names.index('JUMP')])
                        if csv_jump == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_jump<=0:
                        #    csv_jump=1
                        #elif csv_jump>99:
                        #    csv_jump=99
                        #print(player_id, csv_jump)
                        set_value(of, player_id, 26, 6, 127, int(csv_jump))
                        
                    if 'TECHNIQUE' in list_of_column_names:
                        csv_tech=(row[list_of_column_names.index('TECHNIQUE')])
                        if csv_tech == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_tech<=0:
                        #    csv_tech=1
                        #elif csv_tech>99:
                        #    csv_tech=99
                        #print(player_id, csv_tech)
                        set_value(of, player_id, 29, 0, 127, int(csv_tech))
                        
                    if 'AGGRESSION' in list_of_column_names:
                        csv_aggress=(row[list_of_column_names.index('AGGRESSION')])
                        if csv_aggress == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_aggress<=0:
                        #    csv_aggress=1
                        #elif csv_aggress>99:
                        #    csv_aggress=99
                        #print(player_id, csv_aggress)
                        set_value(of, player_id, 29, 7, 127, int(csv_aggress))
                        
                    if 'MENTALITY' in list_of_column_names:
                        csv_mental=(row[list_of_column_names.index('MENTALITY')])
                        if csv_mental == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_mental<=0:
                        #    csv_mental=1
                        #elif csv_mental>99:
                        #    csv_mental=99
                        #print(player_id, csv_mental)
                        set_value(of, player_id, 30, 6, 127, int(csv_mental))
                        
                    if 'CONSISTENCY' in list_of_column_names:
                        csv_consistency=(row[list_of_column_names.index('CONSISTENCY')])
                        if csv_consistency == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_consistency<0:
                        #    csv_consistency=0
                        #elif csv_consistency>7:
                        #    csv_consistency=7
                        #print(player_id, csv_consistency)
                        set_value(of, player_id, 33, 7, 7, int(csv_consistency) - 1)
                        
                    if 'GOAL KEEPING' in list_of_column_names:
                        csv_gkAbil=(row[list_of_column_names.index('GOAL KEEPING')])
                        if csv_gkAbil == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_gkAbil<=0:
                        #    csv_gkAbil=1
                        #elif csv_gkAbil>99:
                        #    csv_gkAbil=99
                        #print(player_id, csv_gkAbil)
                        set_value(of, player_id, 31, 5, 127, int(csv_gkAbil))
                        
                    if 'TEAM WORK' in list_of_column_names:
                        csv_team=(row[list_of_column_names.index('TEAM WORK')])
                        if csv_team == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_team<=0:
                        #    csv_team=1
                        #elif csv_team>99:
                        #    csv_team=99
                        #print(player_id, csv_team)
                        set_value(of, player_id, 33, 0, 127, int(csv_team))
                        
                    if 'CONDITION / FITNESS' in list_of_column_names:
                        csv_condition=(row[list_of_column_names.index('CONDITION / FITNESS')])
                        if csv_condition == "": continue
                        # Here we limit the stat to already know konami range
                        #if csv_condition<0:
                        #    csv_condition=0
                        #elif csv_condition>7:
                        #    csv_condition=7
                        #print(player_id, csv_condition)
                        set_value(of, player_id, 34, 2, 7, int(csv_condition) - 1)
                        
                    if 'DRIBBLING' in list_of_column_names:
                        csv_drib=int(row[list_of_column_names.index('DRIBBLING')])
                        # Here we limit the stat to already know konami range
                        #if csv_drib<0:
                        #    csv_drib=0
                        #elif csv_drib>1:
                        #    csv_drib=1
                        #print(player_id, csv_drib)
                        set_value(of, player_id, 24, 4, 1, csv_drib)
                        
                    if 'TACTICAL DRIBBLE' in list_of_column_names:
                        csv_dribKeep=int(row[list_of_column_names.index('TACTICAL DRIBBLE')])
                        # Here we limit the stat to already know konami range
                        #if csv_dribKeep<0:
                        #    csv_dribKeep=0
                        #elif csv_dribKeep>1:
                        #    csv_dribKeep=1
                        #print(player_id, csv_dribKeep)
                        set_value(of, player_id, 24, 5, 1, csv_dribKeep)
                        
                    if 'POST PLAYER' in list_of_column_names:
                        csv_post=int(row[list_of_column_names.index('POST PLAYER')])
                        # Here we limit the stat to already know konami range
                        #if csv_post<0:
                        #    csv_post=0
                        #elif csv_post>1:
                        #    csv_post=1
                        #print(player_id, csv_post)
                        set_value(of, player_id, 32, 4, 1, csv_post)
                        
                    if 'POSITIONING' in list_of_column_names:
                        csv_posit=int(row[list_of_column_names.index('POSITIONING')])
                        # Here we limit the stat to already know konami range
                        #if csv_posit<0:
                        #    csv_posit=0
                        #elif csv_posit>1:
                        #    csv_posit=1
                        #print(player_id, csv_posit)
                        set_value(of, player_id, 24, 6, 1, csv_posit)
                        
                    if 'REACTION' in list_of_column_names:
                        csv_offside=int(row[list_of_column_names.index('REACTION')])
                        # Here we limit the stat to already know konami range
                        #if csv_offside<0:
                        #    csv_offside=0
                        #elif csv_offside>1:
                        #    csv_offside=1
                        #print(player_id, csv_offside)
                        set_value(of, player_id, 24, 7, 1, csv_offside)

                    if 'LINES' in list_of_column_names:
                        csv_linePos=int(row[list_of_column_names.index('LINES')])
                        # Here we limit the stat to already know konami range
                        #if csv_linePos<0:
                        #    csv_linePos=0
                        #elif csv_linePos>1:
                        #    csv_linePos=1
                        #print(player_id, csv_linePos)
                        set_value(of, player_id, 32, 5, 1, csv_linePos)

                    if 'MIDDLE SHOOTING' in list_of_column_names:
                        csv_midShot=int(row[list_of_column_names.index('MIDDLE SHOOTING')])
                        # Here we limit the stat to already know konami range
                        #if csv_midShot<0:
                        #    csv_midShot=0
                        #elif csv_midShot>1:
                        #    csv_midShot=1
                        #print(player_id, csv_midShot)
                        set_value(of, player_id, 32, 6, 1, csv_midShot)

                    if 'SCORING' in list_of_column_names:
                        csv_scorer=int(row[list_of_column_names.index('SCORING')])
                        # Here we limit the stat to already know konami range
                        #if csv_scorer<0:
                        #    csv_scorer=0
                        #elif csv_scorer>1:
                        #    csv_scorer=1
                        #print(player_id, csv_scorer)
                        set_value(of, player_id, 28, 6, 1, csv_scorer)

                    if 'PLAYMAKING' in list_of_column_names:
                        csv_play=int(row[list_of_column_names.index('PLAYMAKING')])
                        # Here we limit the stat to already know konami range
                        #if csv_play<0:
                        #    csv_play=0
                        #elif csv_play>1:
                        #    csv_play=1
                        #print(player_id, csv_play)
                        set_value(of, player_id, 28, 4, 1, csv_play)

                    if 'PASSING' in list_of_column_names:
                        csv_pass=int(row[list_of_column_names.index('PASSING')])
                        # Here we limit the stat to already know konami range
                        #if csv_pass<0:
                        #    csv_pass=0
                        #elif csv_pass>1:
                        #    csv_pass=1
                        #print(player_id, csv_pass)
                        set_value(of, player_id, 28, 5, 1, csv_pass)

                    if 'PENALTIES' in list_of_column_names:
                        csv_pk=int(row[list_of_column_names.index('PENALTIES')])
                        # Here we limit the stat to already know konami range
                        #if csv_pk<0:
                        #    csv_pk=0
                        #elif csv_pk>1:
                        #    csv_pk=1
                        #print(player_id, csv_pk)
                        set_value(of, player_id, 35, 6, 1, csv_pk)

                    if '1-1 SCORING' in list_of_column_names:
                        csv_k11=int(row[list_of_column_names.index('1-1 SCORING')])
                        # Here we limit the stat to already know konami range
                        #if csv_k11<0:
                        #    csv_k11=0
                        #elif csv_k11>1:
                        #    csv_k11=1
                        #print(player_id, csv_k11)
                        set_value(of, player_id, 28, 7, 1, csv_k11)

                    if 'LONG THROW' in list_of_column_names:
                        csv_longThrow=int(row[list_of_column_names.index('LONG THROW')])
                        # Here we limit the stat to already know konami range
                        #if csv_longThrow<0:
                        #    csv_longThrow=0
                        #elif csv_longThrow>1:
                        #    csv_longThrow=1
                        #print(player_id, csv_longThrow)
                        set_value(of, player_id, 36, 7, 1, csv_longThrow)

                    if '1-TOUCH PASS' in list_of_column_names:
                        csv_direct=int(row[list_of_column_names.index('1-TOUCH PASS')])
                        # Here we limit the stat to already know konami range
                        #if csv_direct<0:
                        #    csv_direct=0
                        #elif csv_direct>1:
                        #    csv_direct=1
                        #print(player_id, csv_direct)
                        set_value(of, player_id, 35, 7, 1, csv_direct)

                    if 'SIDE' in list_of_column_names:
                        csv_side=int(row[list_of_column_names.index('SIDE')])
                        # Here we limit the stat to already know konami range
                        #if csv_side<0:
                        #    csv_side=0
                        #elif csv_side>1:
                        #    csv_side=1
                        #print(player_id, csv_side)
                        set_value(of, player_id, 32, 7, 1, csv_side)

                    if 'CENTRE' in list_of_column_names:
                        csv_centre=int(row[list_of_column_names.index('CENTRE')])
                        # Here we limit the stat to already know konami range
                        #if csv_centre<0:
                        #    csv_centre=0
                        #elif csv_centre>1:
                        #    csv_centre=1
                        #print(player_id, csv_centre)
                        set_value(of, player_id, 35, 5, 1, csv_centre)

                    if 'OUTSIDE' in list_of_column_names:
                        csv_outside=int(row[list_of_column_names.index('OUTSIDE')])
                        # Here we limit the stat to already know konami range
                        #if csv_outside<0:
                        #    csv_outside=0
                        #elif csv_outside>1:
                        #    csv_outside=1
                        #print(player_id, csv_outside)
                        set_value(of, player_id, 36, 0, 1, csv_outside)

                    if 'MARKING' in list_of_column_names:
                        csv_man=int(row[list_of_column_names.index('MARKING')])
                        # Here we limit the stat to already know konami range
                        #if csv_man<0:
                        #    csv_man=0
                        #elif csv_man>1:
                        #    csv_man=1
                        #print(player_id, csv_man)
                        set_value(of, player_id, 36, 1, 1, csv_man)

                    if 'D-LINE CONTROL' in list_of_column_names:
                        csv_dLine=int(row[list_of_column_names.index('D-LINE CONTROL')])
                        # Here we limit the stat to already know konami range
                        #if csv_dLine<0:
                        #    csv_dLine=0
                        #elif csv_dLine>1:
                        #    csv_dLine=1
                        #print(player_id, csv_dLine)
                        set_value(of, player_id, 36, 4, 1, csv_dLine)

                    if 'SLIDING' in list_of_column_names:
                        csv_slide=int(row[list_of_column_names.index('SLIDING')])
                        # Here we limit the stat to already know konami range
                        #if csv_slide<0:
                        #    csv_slide=0
                        #elif csv_slide>1:
                        #    csv_slide=1
                        #print(player_id, csv_slide)
                        set_value(of, player_id, 36, 2, 1, csv_slide)

                    if 'COVERING' in list_of_column_names:
                        csv_cover=int(row[list_of_column_names.index('COVERING')])
                        # Here we limit the stat to already know konami range
                        #if csv_cover<0:
                        #    csv_cover=0
                        #elif csv_cover>1:
                        #    csv_cover=1
                        #print(player_id, csv_cover)
                        set_value(of, player_id, 36, 3, 1, csv_cover)

                    if 'PENALTY STOPPER' in list_of_column_names:
                        csv_keeperPK=int(row[list_of_column_names.index('PENALTY STOPPER')])
                        # Here we limit the stat to already know konami range
                        #if csv_keeperPK<0:
                        #    csv_keeperPK=0
                        #elif csv_keeperPK>1:
                        #    csv_keeperPK=1
                        #print(player_id, csv_keeperPK)
                        set_value(of, player_id, 36, 5, 1, csv_keeperPK)

                    if '1-ON-1 STOPPER' in list_of_column_names:
                        csv_keeper11=int(row[list_of_column_names.index('1-ON-1 STOPPER')])
                        # Here we limit the stat to already know konami range
                        #if csv_keeper11<0:
                        #    csv_keeper11=0
                        #elif csv_keeper11>1:
                        #    csv_keeper11=1
                        #print(player_id, csv_keeper11)
                        set_value(of, player_id, 36, 6, 1, csv_keeper11)

                    if 'FACE TYPE' in list_of_column_names:
                        csv_face_type = (row[list_of_column_names.index('FACE TYPE')])
                        #print(player_id, csv_face_type)
                        if csv_face_type == "BUILD": 
                            csv_face_type = 0
                        elif csv_face_type == "PRESET SPECIAL":
                            csv_face_type = 1
                        elif csv_face_type == "PRESET NORMAL":
                            csv_face_type = 2
                        else:
                            csv_face_type = 0
                        set_value(of, player_id, 60, 2, 3, csv_face_type)

                    if 'SKIN COLOUR' in list_of_column_names:
                        csv_skin_colour = int(row[list_of_column_names.index('SKIN COLOUR')]) - 1
                        #print(player_id, csv_skin_colour)
                        set_value(of, player_id, 91-48, 1, 3, csv_skin_colour)

                    if 'HEAD HEIGHT' in list_of_column_names:
                        csv_head_height = int(row[list_of_column_names.index('HEAD HEIGHT')]) + 7
                        #print(player_id, csv_head_height)
                        set_value(of, player_id, 43, 3, 15, csv_head_height)

                    if 'HEAD WIDTH' in list_of_column_names:
                        csv_head_width = int(row[list_of_column_names.index('HEAD WIDTH')]) + 7
                        #print(player_id, csv_head_width)
                        set_value(of, player_id, 43, 7, 15, csv_head_width)

                    if 'FACE ID' in list_of_column_names:
                        csv_face_id = int(row[list_of_column_names.index('FACE ID')]) - 1
                        #print(player_id, csv_face_id)
                        set_value(of, player_id, 53, 3, 0x1FF, csv_face_id)

                    if 'HEAD OVERALL POSITION' in list_of_column_names:
                        csv_head_ov_pos = int(row[list_of_column_names.index('HEAD OVERALL POSITION')]) + 3
                        #print(player_id, csv_head_ov_pos)
                        set_value(of, player_id, 124-48, 5, 7, csv_head_ov_pos)

                    # Brows menu
                    if 'BROWS TYPE' in list_of_column_names:
                        csv_brows_type = int(row[list_of_column_names.index('BROWS TYPE')]) - 1
                        #print(player_id, csv_brows_type)
                        set_value(of, player_id, 71, 5, 31, csv_brows_type)

                    if 'BROWS ANGLE' in list_of_column_names:
                        csv_brows_angle = (int(row[list_of_column_names.index('BROWS ANGLE')])* - 1) + 3
                        #print(player_id, csv_brows_angle)
                        set_value(of, player_id, 71, 2, 7, csv_brows_angle)

                    if 'BROWS HEIGHT' in list_of_column_names:
                        csv_brows_height = (int(row[list_of_column_names.index('BROWS HEIGHT')])* - 1) + 3
                        #print(player_id, csv_brows_height)
                        set_value(of, player_id, 70, 4, 7, csv_brows_height)

                    if 'BROWS SPACING' in list_of_column_names:
                        csv_brows_spacing = (int(row[list_of_column_names.index('BROWS SPACING')])* - 1) + 3
                        #print(player_id, csv_brows_spacing)
                        set_value(of, player_id, 70, 7, 7, csv_brows_spacing)

                    # Eyes menu
                    if 'EYES TYPE' in list_of_column_names:
                        csv_eyes_type = int(row[list_of_column_names.index('EYES TYPE')]) - 1
                        #print(player_id, csv_eyes_type)
                        set_value(of, player_id, 68, 3, 31, csv_eyes_type)

                    if 'EYES POSITION' in list_of_column_names:
                        csv_eyes_position = (int(row[list_of_column_names.index('EYES POSITION')])* - 1) + 3
                        #print(player_id, csv_eyes_position)
                        set_value(of, player_id, 69, 0, 7, csv_eyes_position)

                    if 'EYES ANGLE' in list_of_column_names:
                        csv_eyes_angle = (int(row[list_of_column_names.index('EYES ANGLE')])* - 1) + 3
                        #print(player_id, csv_eyes_angle)
                        set_value(of, player_id, 69, 3, 7, csv_eyes_angle)

                    if 'EYES LENGTH' in list_of_column_names:
                        csv_eyes_lenght = (int(row[list_of_column_names.index('EYES LENGTH')])* - 1) + 3
                        #print(player_id, csv_eyes_lenght)
                        set_value(of, player_id, 69, 6, 7, csv_eyes_lenght)

                    if 'EYES WIDTH' in list_of_column_names:
                        csv_eyes_width = (int(row[list_of_column_names.index('EYES WIDTH')])* - 1) + 3
                        #print(player_id, csv_eyes_width)
                        set_value(of, player_id, 70, 1, 7, csv_eyes_width)

                    if 'EYES COLOUR 1' in list_of_column_names:
                        csv_eyes_c1 = int(row[list_of_column_names.index('EYES COLOUR 1')]) - 1
                        #print(player_id, csv_eyes_c1)
                        set_value(of, player_id, 46, 9, 3, csv_eyes_c1)

                    if 'EYES COLOUR 2' in list_of_column_names:
                        csv_eyes_c2 = (row[list_of_column_names.index('EYES COLOUR 2')])
                        if csv_eyes_c2 == "BLACK 1": 
                            csv_eyes_c2 = 0
                        elif csv_eyes_c2 == "BLACK 2":
                            csv_eyes_c2 = 1
                        elif csv_eyes_c2 == "DARK GREY 1":
                            csv_eyes_c2 = 2
                        elif csv_eyes_c2 == "DARK GREY 2":
                            csv_eyes_c2 = 3
                        elif csv_eyes_c2 == "BROWN 1":
                            csv_eyes_c2 = 4
                        elif csv_eyes_c2 == "BROWN 2":
                            csv_eyes_c2 = 5
                        elif csv_eyes_c2 == "LIGHT BLUE 1":
                            csv_eyes_c2 = 6
                        elif csv_eyes_c2 == "LIGHT BLUE 2":
                            csv_eyes_c2 = 7
                        elif csv_eyes_c2 == "BLUE 1":
                            csv_eyes_c2 = 8
                        elif csv_eyes_c2 == "BLUE 2":
                            csv_eyes_c2 = 9
                        elif csv_eyes_c2 == "GREEN 1":
                            csv_eyes_c2 = 10
                        elif csv_eyes_c2 == "GREEN 2":
                            csv_eyes_c2 = 11
                        else:
                            csv_eyes_c2 = 0                        
                        #print(player_id, csv_eyes_c2)
                        set_value(of, player_id, 47, 3, 15, csv_eyes_c2)

                    # Nose menu
                    if 'NOSE TYPE' in list_of_column_names:
                        csv_nose_type = int(row[list_of_column_names.index('NOSE TYPE')]) - 1
                        #print(player_id, csv_nose_type)
                        set_value(of, player_id, 121-48, 0, 7, csv_nose_type)

                    if 'NOSE HEIGHT' in list_of_column_names:
                        csv_nose_height = (int(row[list_of_column_names.index('NOSE HEIGHT')])* - 1) + 3
                        #print(player_id, csv_nose_height)
                        set_value(of, player_id, 121-48, 6, 7, csv_nose_height)

                    if 'NOSE WIDTH' in list_of_column_names:
                        csv_nose_width = (int(row[list_of_column_names.index('NOSE WIDTH')])* - 1) + 3
                        #print(player_id, csv_nose_width)
                        set_value(of, player_id, 121-48, 3, 7, csv_nose_width)

                    # Cheecks menu
                    if 'CHEECKS TYPE' in list_of_column_names:
                        csv_cheecks_type = int(row[list_of_column_names.index('CHEECKS TYPE')]) - 1
                        #print(player_id, csv_cheecks_type)
                        set_value(of, player_id, 120-48, 2, 7, csv_cheecks_type)

                    if 'CHEECKS SHAPE' in list_of_column_names:
                        csv_cheecks_shape = (int(row[list_of_column_names.index('CHEECKS SHAPE')])* - 1) + 3
                        #print(player_id, csv_cheecks_shape)
                        set_value(of, player_id, 120-48, 5, 7, csv_cheecks_shape)

                    # Mouth menu
                    if 'MOUTH TYPE' in list_of_column_names:
                        csv_mouth_type = int(row[list_of_column_names.index('MOUTH TYPE')]) - 1
                        #print(player_id, csv_mouth_type)
                        set_value(of, player_id, 122-48, 1, 31, csv_mouth_type)

                    if 'MOUTH SIZE' in list_of_column_names:
                        csv_mouth_size = (int(row[list_of_column_names.index('MOUTH SIZE')])* - 1) + 3
                        #print(player_id, csv_mouth_size)
                        set_value(of, player_id, 123-48, 1, 7, csv_mouth_size)

                    if 'MOUTH POSITION' in list_of_column_names:
                        csv_mouth_position = (int(row[list_of_column_names.index('MOUTH POSITION')])* - 1) + 3
                        #print(player_id, csv_mouth_position)
                        set_value(of, player_id, 122-48, 6, 7, csv_mouth_position)

                    # Jaw menu
                    if 'JAW TYPE' in list_of_column_names:
                        csv_jaw_type = int(row[list_of_column_names.index('JAW TYPE')]) - 1
                        #print(player_id, csv_jaw_type)
                        set_value(of, player_id, 123-48, 4, 7, csv_jaw_type)

                    if 'JAW CHIN' in list_of_column_names:
                        csv_jaw_chin = (int(row[list_of_column_names.index('JAW CHIN')])* - 1) + 3
                        #print(player_id, csv_jaw_chin)
                        set_value(of, player_id, 123-48, 7, 7, csv_jaw_chin)

                    if 'JAW WIDTH' in list_of_column_names:
                        csv_jaw_width = (int(row[list_of_column_names.index('JAW WIDTH')])* - 1) + 3
                        #print(player_id, csv_jaw_width)
                        set_value(of, player_id, 124-48, 2, 7, csv_jaw_width)

                    # Hair
                    #if 'HAIR' in list_of_column_names:
                        #csv_hair = int(row[list_of_column_names.index('HAIR')])
                        #print(player_id, csv_hair)
                        #set_value(of, player_id, 45, 0, 2047, csv_hair)

                    # If we dont find any of those columns in our csv file we dont import the hair attributes
                    if (("HAIR TYPE" in list_of_column_names) and ("HAIR SHAPE" in list_of_column_names) and ("HAIR FRONT" in list_of_column_names) and ("HAIR VOLUME" in list_of_column_names) and ("HAIR DARKNESS" in list_of_column_names) and ("BANDANA" in list_of_column_names)):
                        csv_hair = 0
                        csv_hair_type = row[list_of_column_names.index('HAIR TYPE')]
                        csv_hair_shape = int(row[list_of_column_names.index('HAIR SHAPE')]) - 1
                        csv_hair_front = int(row[list_of_column_names.index('HAIR FRONT')]) - 1
                        csv_hair_volume = int(row[list_of_column_names.index('HAIR VOLUME')]) - 1
                        csv_hair_darkness = int(row[list_of_column_names.index('HAIR DARKNESS')]) - 1
                        csv_hair_bandana = int(row[list_of_column_names.index('BANDANA')])

                        if csv_hair_type == 'BALD':
                            csv_hair = csv_hair_shape

                        elif csv_hair_type == 'BUZZ CUT':
                            csv_hair = 4 + (csv_hair_darkness) + (csv_hair_front * 4) + (csv_hair_shape * 20)

                        elif csv_hair_type == 'VERY SHORT 1':
                            csv_hair = 84 + (csv_hair_front) + (csv_hair_shape * 6)

                        elif csv_hair_type == 'VERY SHORT 2':
                            if 0 <= csv_hair_shape <= 2:
                                csv_hair = 108 + (csv_hair_shape * 10) + (csv_hair_front)
                            else:
                                csv_hair = 138 + ((csv_hair_shape - 3) * 5) + (csv_hair_front)

                        elif csv_hair_type == 'STRAIGHT 1':
                            if 0 <= csv_hair_front <= 8:
                                csv_hair = 153 + csv_hair_bandana + csv_hair_volume * 3 + csv_hair_front * 9 + csv_hair_shape * 102
                            else:
                                csv_hair = 234 + csv_hair_volume + (csv_hair_front - 9) * 3 + csv_hair_shape * 102

                        elif csv_hair_type == 'STRAIGHT 2':
                            if 0 <= csv_hair_front <= 1:
                                csv_hair = 561 + csv_hair_bandana + csv_hair_volume * 3 + csv_hair_front * 9 + csv_hair_shape * 33
                            else:
                                csv_hair = 579 + csv_hair_volume + (csv_hair_front - 2) * 3 + csv_hair_shape * 33
                                
                        elif csv_hair_type == 'CURLY 1':
                            if 0 <= csv_hair_front <= 4:
                                csv_hair = 660 + csv_hair_bandana + csv_hair_volume * 3 + csv_hair_front * 9 + csv_hair_shape * 51
                            else:
                                csv_hair = 705 + csv_hair_volume + (csv_hair_front - 5) * 3 + csv_hair_shape * 51

                        elif csv_hair_type == 'CURLY 2':
                            csv_hair = 864 + csv_hair_volume + csv_hair_front * 2 + csv_hair_shape * 12

                        elif csv_hair_type == 'PONYTAIL 1':
                            csv_hair = 912 + csv_hair_volume + csv_hair_front * 3 + csv_hair_shape * 12

                        elif csv_hair_type == 'PONYTAIL 2':
                            csv_hair = 948 + csv_hair_volume + csv_hair_front * 3 + csv_hair_shape * 12

                        elif csv_hair_type == 'DREADLOCKS':
                            csv_hair = 984 + csv_hair_volume + csv_hair_front * 2 + csv_hair_shape * 8

                        elif csv_hair_type == 'PULLED BACK':
                            csv_hair = 1008 + csv_hair_front + csv_hair_shape * 6

                        elif csv_hair_type == 'SPECIAL HAIRSTYLES':
                            csv_hair = 1026 + csv_hair_shape

                        set_value(of, player_id, 93-48, 0, 2047, csv_hair)

                    if 'HAIR COLOUR CONFIG' in list_of_column_names:
                        csv_hair_colour_config = int(row[list_of_column_names.index('HAIR COLOUR CONFIG')]) - 1
                        #print(player_id, csv_hair_colour_config)
                        set_value(of, player_id, 94-48, 3, 63, csv_hair_colour_config)

                    if 'HAIR COLOUR RGB R' in list_of_column_names:
                        csv_hair_rgb_r = (int(row[list_of_column_names.index('HAIR COLOUR RGB R')]) * - 1) + 63
                        #print(player_id, csv_hair_rgb_r)
                        set_value(of, player_id, 102-48, 5, 63, csv_hair_rgb_r)

                    if 'HAIR COLOUR RGB G' in list_of_column_names:
                        csv_hair_rgb_g = (int(row[list_of_column_names.index('HAIR COLOUR RGB G')]) * - 1) + 63
                        #print(player_id, csv_hair_rgb_g)
                        set_value(of, player_id, 103-48, 3, 63, csv_hair_rgb_g)

                    if 'HAIR COLOUR RGB B' in list_of_column_names:
                        csv_hair_rgb_b = (int(row[list_of_column_names.index('HAIR COLOUR RGB B')]) * - 1) + 63
                        #print(player_id, csv_hair_rgb_b)
                        set_value(of, player_id, 104-48, 1, 63, csv_hair_rgb_b)

                    if 'BANDANA COLOUR' in list_of_column_names:
                        csv_hair_bandana_colour = int(row[list_of_column_names.index('BANDANA COLOUR')]) - 1
                        #print(player_id, csv_hair_bandana_colour)
                        set_value(of, player_id, 109-48, 2, 7, csv_hair_bandana_colour)

                    if 'CAP (ONLY GK)' in list_of_column_names:
                        csv_cap = int(row[list_of_column_names.index('CAP (ONLY GK)')])
                        #print(player_id, csv_cap)
                        set_value(of, player_id, 98-48, 6, 1, csv_cap)

                    if 'CAP COLOUR' in list_of_column_names:
                        csv_cap_colour = int(row[list_of_column_names.index('CAP COLOUR')]) - 1
                        #print(player_id, csv_cap_colour)
                        set_value(of, player_id, 114-48, 3, 7, csv_cap_colour)

                    if 'FACIAL HAIR TYPE' in list_of_column_names:
                        csv_facial_hair_type = int(row[list_of_column_names.index('FACIAL HAIR TYPE')])
                        #print(player_id, csv_facial_hair_type)
                        set_value(of, player_id, 95-48, 7, 127, csv_facial_hair_type)

                    if 'FACIAL HAIR COLOUR' in list_of_column_names:
                        csv_facial_hair_colour = int(row[list_of_column_names.index('FACIAL HAIR COLOUR')]) - 1
                        #print(player_id, csv_facial_hair_colour)
                        set_value(of, player_id, 97-48, 0, 63, csv_facial_hair_colour)

                    if 'SUNGLASSES TYPE' in list_of_column_names:
                        csv_sunglasses = int(row[list_of_column_names.index('SUNGLASSES TYPE')]) 
                        #print(player_id, csv_sunglasses)
                        set_value(of, player_id, 97-48, 6, 3, csv_sunglasses)

                    if 'SUNGLASSES COLOUR' in list_of_column_names:
                        csv_sunglasses_colour = int(row[list_of_column_names.index('SUNGLASSES COLOUR')]) - 1
                        #print(player_id, csv_sunglasses_colour)
                        set_value(of, player_id, 114-48, 0, 7, csv_sunglasses_colour)

                    # Physical settings
                    if 'HEIGHT' in list_of_column_names:
                        csv_height=int(row[list_of_column_names.index('HEIGHT')])-148
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_height)
                        set_value(of, player_id, 41, 0, 63, csv_height)

                    if 'WEIGHT' in list_of_column_names:
                        csv_weight=int(row[list_of_column_names.index('WEIGHT')])
                        # Here we limit the stat to already know konami range
                        #print(player_id, csv_weight)
                        set_value(of, player_id, 41, 6, 127, csv_weight)

                    if 'BODY TYPE' in list_of_column_names:
                        csv_body_type=(row[list_of_column_names.index('BODY TYPE')])
                        if csv_body_type == "Edited":

                            if 'NECK LENGTH' in list_of_column_names:
                                csv_neck_length = int(row[list_of_column_names.index('NECK LENGTH')]) + 7
                                #print(player_id, csv_neck_length)
                                set_value(of, player_id, 57, 2, 15, csv_neck_length)

                            if 'NECK WIDTH' in list_of_column_names:
                                csv_neck_width = int(row[list_of_column_names.index('NECK WIDTH')]) + 7
                                #print(player_id, csv_neck_width)
                                set_value(of, player_id, 44, 3, 15, csv_neck_width)

                            if 'SHOULDER HEIGHT' in list_of_column_names:
                                csv_shoulder_height = int(row[list_of_column_names.index('SHOULDER HEIGHT')]) + 7
                                #print(player_id, csv_shoulder_height)
                                set_value(of, player_id, 61, 5, 15, csv_shoulder_height)

                            if 'SHOULDER WIDTH' in list_of_column_names:
                                csv_should_width = int(row[list_of_column_names.index('SHOULDER WIDTH')]) + 7
                                #print(player_id, csv_should_width)
                                set_value(of, player_id, 62, 1, 15, csv_should_width)

                            if 'CHEST MEASUREMENT' in list_of_column_names:
                                csv_chest_measu = int(row[list_of_column_names.index('CHEST MEASUREMENT')]) + 7
                                #print(player_id, csv_chest_measu)
                                set_value(of, player_id, 57, 6, 15, csv_chest_measu)

                            if 'WAIST CIRCUMFERENCE' in list_of_column_names:
                                csv_waist_circu = int(row[list_of_column_names.index('WAIST CIRCUMFERENCE')]) + 7
                                #print(player_id, csv_waist_circu)
                                set_value(of, player_id, 58, 6, 15, csv_waist_circu)

                            if 'ARM CIRCUMFERENCE' in list_of_column_names:
                                csv_arm_circu = int(row[list_of_column_names.index('ARM CIRCUMFERENCE')]) + 7
                                #print(player_id, csv_arm_circu)
                                set_value(of, player_id, 58, 2, 15, csv_arm_circu)

                            if 'LEG CIRCUMFERENCE' in list_of_column_names:
                                csv_leg_circu = int(row[list_of_column_names.index('LEG CIRCUMFERENCE')]) + 7
                                #print(player_id, csv_leg_circu)
                                set_value(of, player_id, 59, 2, 15, csv_leg_circu)

                            if 'CALF CIRCUMFERENCE' in list_of_column_names:
                                csv_calf_circu = int(row[list_of_column_names.index('CALF CIRCUMFERENCE')]) + 7
                                #print(player_id, csv_calf_circu)
                                set_value(of, player_id, 59, 6, 15, csv_calf_circu)

                            if 'LEG LENGTH' in list_of_column_names:
                                csv_leg_length = int(row[list_of_column_names.index('LEG LENGTH')]) + 7
                                #print(player_id, csv_leg_length)
                                set_value(of, player_id, 60, 4, 15, csv_leg_length)
                        else:
                            csv_body_type=int(row[list_of_column_names.index('BODY TYPE')]) -1

                            #print(player_id, csv_neck_length)
                            set_value(of, player_id, 57, 2, 15, body_types[csv_body_type][0] + 7)

                            #print(player_id, csv_neck_width)
                            set_value(of, player_id, 44, 3, 15, body_types[csv_body_type][1] + 7)

                            #print(player_id, csv_shoulder_height)
                            set_value(of, player_id, 61, 5, 15, body_types[csv_body_type][2] + 7)

                            #print(player_id, csv_should_width)
                            set_value(of, player_id, 62, 1, 15, body_types[csv_body_type][3] + 7)

                            #print(player_id, csv_chest_measu)
                            set_value(of, player_id, 57, 6, 15, body_types[csv_body_type][4] + 7)

                            #print(player_id, csv_waist_circu)
                            set_value(of, player_id, 58, 6, 15, body_types[csv_body_type][5] + 7)

                            #print(player_id, csv_arm_circu)
                            set_value(of, player_id, 58, 2, 15, body_types[csv_body_type][6] + 7)

                            #print(player_id, csv_leg_circu)
                            set_value(of, player_id, 59, 2, 15, body_types[csv_body_type][7] + 7)

                            #print(player_id, csv_calf_circu)
                            set_value(of, player_id, 59, 6, 15, body_types[csv_body_type][8] + 7)

                            #print(player_id, csv_leg_length)
                            set_value(of, player_id, 60, 4, 15, body_types[csv_body_type][9] + 7)

                    # Boots/Acc.
                    if 'BOOT TYPE' in list_of_column_names:
                        csv_boot_type = int(row[list_of_column_names.index('BOOT TYPE')])
                        #print(player_id, csv_boot_type)
                        set_value(of, player_id, 51, 9, 15, csv_boot_type)

                    if 'BOOT COLOUR' in list_of_column_names:
                        csv_boot_colour = int(row[list_of_column_names.index('BOOT COLOUR')]) - 1
                        #print(player_id, csv_boot_colour)
                        set_value(of, player_id, 51, 13, 3, csv_boot_colour)

                    if 'NECK WARMER' in list_of_column_names:
                        csv_neck_warm = int(row[list_of_column_names.index('NECK WARMER')])
                        #print(player_id, csv_neck_warm)
                        set_value(of, player_id, 98-48, 0, 1, csv_neck_warm)

                    if 'NECKLACE TYPE' in list_of_column_names:
                        csv_necklace_type = int(row[list_of_column_names.index('NECKLACE TYPE')])
                        #print(player_id, csv_necklace_type)
                        set_value(of, player_id, 98-48, 1, 3, csv_necklace_type)

                    if 'NECKLACE COLOUR' in list_of_column_names:
                        csv_necklace_colour = int(row[list_of_column_names.index('NECKLACE COLOUR')]) - 1
                        #print(player_id, csv_necklace_colour)
                        set_value(of, player_id, 98-48, 3, 7, csv_necklace_colour)

                    if 'WISTBAND' in list_of_column_names:
                        csv_wistband = int(row[list_of_column_names.index('WISTBAND')])
                        #print(player_id, csv_wistband)
                        set_value(of, player_id, 98-48, 7, 3, csv_wistband)

                    if 'WISTBAND COLOUR' in list_of_column_names:
                        csv_wistband_colour = int(row[list_of_column_names.index('WISTBAND COLOUR')]) - 1
                        #print(player_id, csv_wistband_colour)
                        set_value(of, player_id, 99-48, 1, 7, csv_wistband_colour)

                    if 'FRIENDSHIP BRACELET' in list_of_column_names:
                        csv_friend_brace = int(row[list_of_column_names.index('FRIENDSHIP BRACELET')])
                        #print(player_id, csv_friend_brace)
                        set_value(of, player_id, 99-48, 4, 3, csv_friend_brace)

                    if 'FRIENDSHIP BRACELET COLOUR' in list_of_column_names:
                        csv_friend_brace_colour = int(row[list_of_column_names.index('FRIENDSHIP BRACELET COLOUR')]) - 1
                        #print(player_id, csv_friend_brace_colour)
                        set_value(of, player_id, 99-48, 6, 7, csv_friend_brace_colour)

                    if 'GLOVES' in list_of_column_names:
                        csv_gloves = int(row[list_of_column_names.index('GLOVES')])
                        #print(player_id, csv_gloves)
                        set_value(of, player_id, 104-48, 7, 1, csv_gloves)

                    if 'FINGER BAND' in list_of_column_names:
                        csv_finger_band = int(row[list_of_column_names.index('FINGER BAND')])
                        #print(player_id, csv_finger_band)
                        set_value(of, player_id, 109-48, 0, 3, csv_finger_band)

                    if 'SHIRT' in list_of_column_names:
                        csv_shirt = int(row[list_of_column_names.index('SHIRT')])
                        #print(player_id, csv_shirt)
                        set_value(of, player_id, 92-48, 7, 1, csv_shirt)

                    if 'SLEEVES' in list_of_column_names:
                        csv_sleeves = int(row[list_of_column_names.index('SLEEVES')])
                        #print(player_id, csv_sleeves)
                        set_value(of, player_id, 96-48, 6, 3, csv_sleeves)

                    if 'UNDER SHORT' in list_of_column_names:
                        csv_under_short = int(row[list_of_column_names.index('UNDER SHORT')])
                        #print(player_id, csv_under_short)
                        set_value(of, player_id, 100-48, 7, 1, csv_under_short)

                    if 'UNDER SHORT COLOUR' in list_of_column_names:
                        csv_under_short_colour = int(row[list_of_column_names.index('UNDER SHORT COLOUR')]) - 1
                        #print(player_id, csv_under_short_colour)
                        set_value(of, player_id, 101-48, 0, 7, csv_under_short_colour)

                    if 'SOCKS' in list_of_column_names:
                        csv_socks = int(row[list_of_column_names.index('SOCKS')]) - 1
                        #print(player_id, csv_socks)
                        set_value(of, player_id, 105-48, 0, 3, csv_socks)

                    if 'TAPE' in list_of_column_names:
                        csv_tape = int(row[list_of_column_names.index('TAPE')])
                        #print(player_id, csv_tape)
                        set_value(of, player_id, 102-48, 4, 1, csv_tape)

                    # Rare stats
                    if 'ASW ?' in list_of_column_names:
                        csv_cbwL=int(row[list_of_column_names.index('ASW ?')])
                        # Here we limit the stat to already know konami range
                        #if csv_cbwL<0:
                        #    csv_cbwL=0
                        #elif csv_cbwL>1:
                        #    csv_cbwL=1
                        #print(player_id, csv_cbwL)
                        set_value(of, player_id, 11, 14, 1, csv_cbwL)
                        
                    if 'STAT X' in list_of_column_names:
                        csv_statX=int(row[list_of_column_names.index('STAT X')]) - 1
                        # Here we limit the stat to already know konami range
                        #if csv_statX<=0:
                        #    csv_statX=1
                        #elif csv_statX>99:
                        #    csv_statX=99
                        #print(player_id, csv_statX)
                        set_value(of, player_id, 27, 5, 127, csv_statX)

                    if 'B F FEINT' in list_of_column_names:
                        csv_bff=int(row[list_of_column_names.index('B F FEINT')])
                        # Here we limit the stat to already know konami range
                        #if csv_bff<0:
                        #    csv_bff=0
                        #elif csv_bff>1:
                        #    csv_bff=1
                        #print(player_id, csv_bff)
                        set_value(of, player_id, 20, 6, 1, csv_bff)

                    if 'GK KICK' in list_of_column_names:
                        csv_gkKick=int(row[list_of_column_names.index('GK KICK')])
                        # Here we limit the stat to already know konami range
                        #if csv_gkKick<0:
                        #    csv_gkKick=0
                        #elif csv_gkKick>1:
                        #    csv_gkKick=1
                        #print(player_id, csv_gkKick)
                        set_value(of, player_id, 20, 7, 1, csv_gkKick)

                    if 'STAT EDITED' in list_of_column_names:
                        csv_statEdited=int(row[list_of_column_names.index('STAT EDITED')])
                        # Here we limit the stat to already know konami range
                        #if csv_statEdited<0:
                        #    csv_statEdited=0
                        #elif csv_statEdited>1:
                        #    csv_statEdited=1
                        #print(player_id, csv_statEdited)
                        set_value(of, player_id, 39, 7, 1, csv_statEdited)

                    # if 'PSD' in list_of_column_names:
                    #     csv_psd_link=(row[list_of_column_names.index('PSD')])
                    #     if csv_psd_link !="":
                    #         import_stats_from_psd(of, player_id, csv_psd_link)
                    # else:
                    #     csv_psd_link = ""
                    
                    # Here's a template in future case i need to add a new stat (which is very likely)
                    #if '' in list_of_column_names:
                        #csv_ = int(row[list_of_column_names.index('')])
                        #print(player_id, csv_)
                        #set_value(of, player_id, , , , csv_)

                    # breaking the loop after the 
                    # first iteration itself 
                    #break
                return True
    except Exception as e: 
        #messagebox.showerror(title="Error", message=e)
        print(e)
        print(traceback.format_exc())
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