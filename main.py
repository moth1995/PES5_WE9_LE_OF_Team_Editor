from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import traceback

from COFPES_OF_Editor_5.editor.option_file import OptionFile
from COFPES_OF_Editor_5.editor.utils.common_functions import resource_path

from getnames import get_of_names
from swap_teams import swap_teams_data, swap_nations_data
from swap_teams import encrypt_and_save
from player_data import get_stats
from export_csv import write_csv
from import_csv import load_csv
from of_crypt import of_encrypter, of_decrypter
from teams import get_players_nations, get_players_clubs, get_formation_generic, set_formation_generic

def export_formation_btn_action():
    try:
        root.temp_file = filedialog.asksaveasfile(initialdir=".",title="Save formation", mode='wb', filetypes=(("Bin files","*.bin"),("All files", "*")), defaultextension=".bin")
        if root.temp_file is None:
            return
        with open(root.temp_file.name, "wb") as binary_file:
            binary_file.write(get_formation_generic(of, teamform_cmb.current()))
        messagebox.showinfo(title=appname,message="Formation file created!")
    except Exception as err:
        #print("OS error: {0}".format(err))
        messagebox.showerror(title=appname,message="OS error: {0}".format(err))

def import_formation_btn_action():
    try:
        root.temp_file = filedialog.askopenfilename(initialdir=".",title="Select your formation file", filetypes=(("Bin files","*.bin"),("All files", "*")))
        if root.temp_file is None:
            return
        with open(root.temp_file, "rb") as binary_file:
            set_formation_generic(of, teamform_cmb.current(), bytearray(binary_file.read()))
        messagebox.showinfo(title=appname,message="Formation imported!")
        save_btn_action()
    except Exception as err:
        #print("OS error: {0}".format(err))
        messagebox.showerror(title=appname,message="OS error: {0}".format(err))



def decrypt_btn_action():
    root.temp_file = filedialog.asksaveasfile(initialdir=".",title="Create your decrypted OF", mode='wb', filetypes=(("Bin files","*.bin"),("All files", "*")), defaultextension=".bin")
    if of_decrypter(of, root.temp_file.name):
        messagebox.showinfo(title=appname,message="Decrypted OF created!")
    else:
        messagebox.showerror(title=appname,message="Error while creating file, please run as admin")

def encrypt_btn_action():
    messagebox.showinfo(title=appname,message="Please take in mind that this will overwrite the data from the OF selected at start with the data from decrypted OF!")
    root.temp_file = filedialog.askopenfilename(initialdir=".",title="Select your decrypted OF", filetypes=(("Bin files","*.bin"),("All files", "*")))
    if root.temp_file!="":
        if of_encrypter(root.temp_file, of):
            messagebox.showinfo(title=appname,message="OF encrypted!")
        else:
            messagebox.showerror(title=appname,message="Error while reading file, please run as admin")


def export_all_to_csv():
    #print(csv_team_cmb.current())
    option_selected = csv_team_cmb.current()
    if option_selected ==0:
        #print(extra_players_check.get())
        players_ids=[*range(1, 4896, 1)]
        if extra_players_check.get():
            players_ids=[*range(1, 5000, 1)]+[*range(32768, 32952, 1)]
        all_data=[]
        for player in players_ids:
            all_data.append(get_stats(player, of, extra_stats_check.get()))
        root.new_file = filedialog.asksaveasfile(initialdir=".",title="Create your CSV file", mode='w', filetypes=(("CSV files","*.csv"),("All files", "*")), defaultextension=".csv")
        if root.new_file is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        if write_csv(root.new_file.name, all_data, extra_stats_check.get()):
            messagebox.showinfo(title=appname,message="CSV file created!")
        else:
            messagebox.showerror(title=appname,message="Error while creating CSV file, please run as admin")
    elif 1<= option_selected <= 64:
        players_ids=get_players_nations(of,option_selected-1)
        all_data=[]
        for player in players_ids:
            if player==0:
                continue
            all_data.append(get_stats(player, of, extra_stats_check.get()))
        root.new_file = filedialog.asksaveasfile(initialdir=".",title="Create your CSV file", mode='w', filetypes=(("CSV files","*.csv"),("All files", "*")), defaultextension=".csv")
        if root.new_file is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        if write_csv(root.new_file.name, all_data, extra_stats_check.get()):
            messagebox.showinfo(title=appname,message="CSV file created!")
        else:
            messagebox.showerror(title=appname,message="Error while creating CSV file, please run as admin")
    elif 65<= option_selected <= 202:
        players_ids=get_players_clubs(of,option_selected-1)
        #print(players_ids)
        all_data=[]
        for player in players_ids:
            if player==0:
                continue
            all_data.append(get_stats(player, of, extra_stats_check.get()))
        root.new_file = filedialog.asksaveasfile(initialdir=".",title="Create your CSV file", mode='w', filetypes=(("CSV files","*.csv"),("All files", "*")), defaultextension=".csv")
        if root.new_file is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        if write_csv(root.new_file.name,all_data, extra_stats_check.get()):
            messagebox.showinfo(title=appname,message="CSV file created!")
        else:
            messagebox.showerror(title=appname,message="Error while creating CSV file, please run as admin")
    else:
        messagebox.showerror(title=appname,message="Please select an option!")

def import_all_from_csv():
    root.csv_file = filedialog.askopenfilename(initialdir=".",title="Select your CSV file", filetypes=(("CSV files","*.csv"),("All files", "*")))
    if root.csv_file!="":
        if load_csv(of, root.csv_file):
            of.save_option_file()
            messagebox.showinfo(title=appname,message="CSV file imported and saved!")
        else:
            messagebox.showerror(title=appname,message="Error while importing CSV file")


#this is a function to update the list in the combobox
def swap_list_positions(teams_list, pos1, pos2): 
    teams_list[pos1], teams_list[pos2] = teams_list[pos2], teams_list[pos1] 
    return teams_list

def swap_btn_action():
    global teams_list
    if ((0 <= team_a_cmb.current() <= 63) and (0 <= team_b_cmb.current() <= 63)):
        if swap_nations_data(of.data, team_a_cmb.current(), team_b_cmb.current(), swap_kits_check.get()):
            teams_list=swap_list_positions(teams_list, team_a_cmb.current(), team_b_cmb.current())
            team_a_cmb.config(values=teams_list)
            team_b_cmb.config(values=teams_list)
            messagebox.showinfo(title=appname,message="Nations swapped!")        
        else:
            messagebox.showerror(title=appname,message="Can't swap the same team!!!")
    elif ((64 <= team_a_cmb.current() <= 201) and (64 <= team_b_cmb.current() <= 201)):
        if swap_teams_data(of.data, team_a_cmb.current(), team_b_cmb.current(), swap_kits_check.get()):
            teams_list=swap_list_positions(teams_list, team_a_cmb.current(), team_b_cmb.current())
            team_a_cmb.config(values=teams_list)
            team_b_cmb.config(values=teams_list)
            messagebox.showinfo(title=appname,message="Teams swapped!")        
        else:
            messagebox.showerror(title=appname,message="Can't swap the same team!!!")
    else:
        messagebox.showerror(title=appname,message="Can't swap Nations and Club teams!!!")
    
def save_btn_action():
    if encrypt_and_save(of):
        messagebox.showinfo(title=appname,message="All changes saved")
    else:
        messagebox.showerror(title=appname,message="Error while saving, please run as admin")

def load_team_kit_config():
    import struct
    team_id = team_kit_name_cmb.current() # team id
    address = 845468 + 544 * (team_id - first_club_team_id) + 57
    if team_id < first_club_team_id:
        address = 822940 + 352 * team_id + 57
    for i in range(4):
        kit_license, _, model, _ =struct.unpack("<4B", of.data[address + 62 * i : address + 62 * i + 4])
        print(kit_license, model)
    print(address)
    kit_license, _, model, _ = struct.unpack("<4B", of.data[address : address + 4])
    print(kit_license, model)
    team_license_cmb.current(kit_license)
    team_model_cmb.current(model)

def apply_team_kit_config():
    kit_license = team_license_cmb.current()
    model = team_model_cmb.current()
    team_id = team_kit_name_cmb.current() # team id
    address = 845468 + 544 * (team_id - first_club_team_id) + 57 # license offset
    if team_id < first_club_team_id:
        address = 822940 + 352 * team_id + 57
    for i in range(4):
        of.data[address + 62 * i] = kit_license
        of.data[address + 62 * i + 2] = model


def report_callback_exception(*args):
    err = traceback.format_exception(*args)
    messagebox.showerror(appname + " Error Message", " ".join(err))

if __name__ == "__main__":
    appname='PES5/WE9/LE OF Team Editor'
    root = Tk()
    root.title(appname)
    w = 800 # width for the Tk root
    h = 600 # height for the Tk root
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    # set the dimensions of the screen 
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #Once it start it will ask to select the option file
    root.iconbitmap(default=resource_path("pes_indie.ico"))
    root.report_callback_exception = report_callback_exception
    root.filename=""
    #temp_file=""
    root.filename = filedialog.askopenfilename(initialdir=".",title="Select your option file", filetypes=(("KONAMI-WIN32PES5OPT","KONAMI-WIN32PES5OPT"),("KONAMI-WIN32WE9UOPT","KONAMI-WIN32WE9UOPT"),("KONAMI-WIN32WE9KOPT","KONAMI-WIN32WE9KOPT")))
    #root.filename = "KONAMI-WIN32PES5OPT"
    #root.filename = r"C:\Users\marco\Documents\KONAMI\Pro Evolution Soccer 5\save\folder1\KONAMI-WIN32PES5OPT"
    first_club_team_id = 64
    if root.filename!="":
        of = OptionFile(root.filename)
        '''
        # No need anymore to create a temporary file, we just use the bytearray
        temp_file = "temp.bin"
        with open(temp_file, "wb") as binary_file:
            binary_file.write(of.data)
            #print("Temporary file created")
        '''

        # CODE BELOW WAS DONE ONLY FOR DEBUGGING, IF YOU WANT TO FIND THE SHIFT AND MASK FOR A STAT
        # YOU JUST NEED TO PASS PLAYER IDS THAT YOU WILL USE TO COMPARE AND WRITE THE POSSIBLE VALUES IN THE LIST CALLED TEST

        '''
        players_ids=[*range(1, 5000, 1)]+[*range(32768, 32952, 1)]
        all_data=[]
        for player_id in players_ids:
            all_data.append(int(get_value(of,player_id,12, 6, 1, "Head overall position")))


        #validate=[*range(0, 8, 1)]#+[*range(0, 6, 1)]
        #validate = [0,1,2,3,4,5,6]
        #validate = [6,5,4,3,2,1,0]
        validate = [0, 0, 1, 0, 0, 1, 1, 1]
        #validate = [63,62,0]
        print(validate)
        test=[]

        for shift in range(0,65536):
            #print (f"the mask is {mask}")
            for mask in range(0,65536):
                #if mask==2047:
                #    print("llegamos al punto conocido")
                #mask=12
                offset = 12
                stat_name = ""
                test.append((get_value(of,1,offset, shift, mask, stat_name) ))
                test.append((get_value(of,2,offset, shift, mask, stat_name) ))
                test.append((get_value(of,3,offset, shift, mask, stat_name) ))
                
                test.append((get_value(of,4,offset, shift, mask, stat_name) ))
                
                test.append((get_value(of,5,offset, shift, mask, stat_name) ))
                test.append((get_value(of,6,offset,shift, mask, stat_name) ))
                
                

                test.append((get_value(of,7,offset, shift, mask, stat_name) ))
                test.append((get_value(of,8,offset, shift, mask, stat_name) ))
                
                #test.append((get_value(of,690,offset, shift, mask, stat_name) ))
                #test.append((get_value(of,4473,offset, shift, mask, stat_name) ))
                #test.append((get_value(of,1485,offset, shift, mask, stat_name) ))
                
                #test.append((get_value(of,4521,offset, shift, mask, stat_name) ))
                #test.append((get_value(of,1229,offset, shift, mask, stat_name) ))
                #test.append((get_value(of,690,offset, shift, mask, stat_name) ))
                #test.append((get_value(of,4029,offset, shift, mask, stat_name) ))

                if test == validate:
                    print(shift, mask)
                test=[]
        '''


        tabs_container=ttk.Notebook(root)
        swap_teams_tab=Frame(tabs_container, width=w, height=h)
        csv_tab=Frame(tabs_container, width=w, height=h)
        extra_tab=Frame(tabs_container, width=w, height=h)
        kits_tab=Frame(tabs_container, width=w, height=h)
        copyright_lbl=Label(root, text="By PES Indie Team")
        thanks_lbl=Label(root, text="Thanks to PeterC10 for python de/encrypt code for OF\nand also mattmid who help me with many player attributes")


        #Swap teams tab 

        teams_list=[
        "Austria", "Belgium", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "England", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", 
        "Netherlands", "Northern Ireland", "Norway", "Poland", "Portugal", "Romania", "Russia", "Scotland", "Serbia and Montenegro", "Slovakia", "Slovenia", "Spain", "Sweden", 
        "Switzerland", "Turkey", "Ukraine", "Wales", "Cameroon", "Cote d'Ivoire", "Morocco", "Nigeria", "Senegal", "South Africa", "Tunisia", "Costa Rica", "Mexico", "USA", 
        "Argentina", "Brazil", "Chile", "Colombia", "Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela", "China", "Iran", "Japan", "Saudi Arabia", "South Korea", "Australia",
        "Classic Argentina", "Classic Brazil", "Classic England", "Classic France", "Classic Germany", "Classic Italy", "Classic Netherlands"
        ]
        #print(len(teams_list))
        teams_list+=get_of_names(of)
        #print(len(teams_list))
        csv_team_list = ["---ALL PLAYERS---"] + teams_list
        #print(csv_team_list)



        team_a_lbl=Label(swap_teams_tab, text="Team A")
        team_b_lbl=Label(swap_teams_tab, text="Team B")
        team_a_cmb=ttk.Combobox(swap_teams_tab, state="readonly", value=teams_list, width=30)
        team_b_cmb=ttk.Combobox(swap_teams_tab, state="readonly", value=teams_list, width=30)
        swap_kits_check = IntVar()
        swap_kits_check.set(0)
        swap_kits_check_btn = Checkbutton(swap_teams_tab, text="Swap OF kits", variable=swap_kits_check)
        swap_teams_btn=Button(swap_teams_tab, text="Swap teams", command=lambda: swap_btn_action())
        save_changes_btn=Button(swap_teams_tab, text="Save changes", command=lambda: save_btn_action())

        #CSV tab

        csv_team_cmb = ttk.Combobox(csv_tab, state="readonly", value=csv_team_list, width=30)
        csv_team_cmb.current(0)
        extra_players_check = IntVar()
        extra_players_check.set(1)
        extra_players = Checkbutton(csv_tab, text="Include Unused and Edited players", variable=extra_players_check)
        extra_stats_check = IntVar()
        extra_stats_check.set(0)
        extra_stats_check_btn = Checkbutton(csv_tab, text="Include extra/unknow stats (only for testing)", variable=extra_stats_check)
        create_csv_btn = Button(csv_tab, text="Create CSV", command=lambda: export_all_to_csv())
        import_csv_btn = Button(csv_tab, text="Import CSV", command=lambda: import_all_from_csv())

        #Extra tab

        stat_test_entry = Entry (extra_tab) 
        #test_print_btn=Button(extra_tab, text="Print stat test!", command=lambda: print(all_data[int(stat_test_entry.get())-1]))
        test_print_btn=Button(extra_tab, text="Print stat test!", command=lambda: None)
        crypt_lbl=Label(extra_tab, text="Option File cryptology", font = "bold")
        decrypt_of_btn=Button(extra_tab, text="Decrypt", command=lambda: decrypt_btn_action())
        encrypt_of_btn=Button(extra_tab, text="Encrypt", command=lambda: encrypt_btn_action())
        teamform_lbl=Label(extra_tab, text="Formations options", font = "bold")
        teamform_cmb = ttk.Combobox(extra_tab, state="readonly", value=teams_list, width=30)
        teamform_cmb.current(0)
        exp_formation_btn = Button(extra_tab, text="Export team\nformation", command=lambda: export_formation_btn_action())
        imp_formation_btn = Button(extra_tab, text="Import team\nformation", command=lambda: import_formation_btn_action())

        #kits tab 
        KIT_TAB_PADX = 50
        KIT_TAB_PADY = 20
        team_kit_name_lbl=Label(kits_tab, text="Team")
        team_kit_name_lbl.grid(row=0, column=0, padx=KIT_TAB_PADX, pady=KIT_TAB_PADY)
        team_kit_name_cmb=ttk.Combobox(kits_tab, state="readonly", value=teams_list, width=30)
        team_kit_name_cmb.bind("<<ComboboxSelected>>", lambda e : load_team_kit_config() )
        team_kit_name_cmb.grid(row=0, column=1)
        team_license_lbl=Label(kits_tab, text="License Type")
        team_license_lbl.grid(row=1, column=0, padx=KIT_TAB_PADX, pady=KIT_TAB_PADY)
        team_license_cmb = ttk.Combobox(kits_tab, state="readonly", value = ["No License", "License", "License + Edit"], width=14)
        team_license_cmb.grid(row=1, column=1)
        team_model_lbl=Label(kits_tab, text="Model")
        team_model_lbl.grid(row=2, column=0, padx=KIT_TAB_PADX, pady=KIT_TAB_PADY)
        team_model_cmb = ttk.Combobox(kits_tab, state="readonly", value = list(range(256)), width=14)
        team_model_cmb.grid(row=2, column=1)
        apply_kits_changes_btn=Button(kits_tab, text="Apply", command=lambda: apply_team_kit_config())
        apply_kits_changes_btn.grid(row=3, column=0, columnspan=2, padx=KIT_TAB_PADX, pady=KIT_TAB_PADY)
        save_kits_changes_btn=Button(kits_tab, text="Save to OF", command=lambda: save_btn_action())
        save_kits_changes_btn.grid(row=4, column=0, columnspan=2, padx=KIT_TAB_PADX, pady=KIT_TAB_PADY)


        #Swap team tab placing

        team_a_lbl.place(x=200, y=60)
        team_b_lbl.place(x=420, y=60)
        team_a_cmb.place(x=200, y=100)
        team_b_cmb.place(x=420, y=100)
        swap_kits_check_btn.place(x=460, y=160)
        swap_teams_btn.place(x=380, y=160)
        save_changes_btn.place(x=376, y=200)
        copyright_lbl.place(x=0, y=570)
        thanks_lbl.place(x=480, y=560)

        #CSV tab placing

        csv_team_cmb.place(x=280, y=120)
        extra_players.place(x=280, y=150)
        extra_stats_check_btn.place(x=280, y=170)
        create_csv_btn.place(x=300, y=200)
        import_csv_btn.place(x=380, y=200)
        # Extra tab placing

        #stat_test_entry.place(x=200, y=70)
        #test_print_btn.place(x=200, y=100)
        teamform_lbl.place(x=280, y=70)
        teamform_cmb.place(x=280, y=120)
        exp_formation_btn.place(x=300, y=150)
        imp_formation_btn.place(x=380, y=150)
        crypt_lbl.place(x=280,y=220)
        decrypt_of_btn.place(x=300, y=280)
        encrypt_of_btn.place(x=380, y=280)


        #Placing tabs and container in the root

        tabs_container.pack()
        swap_teams_tab.pack(fill="both", expand=1)
        csv_tab.pack(fill="both", expand=1)
        extra_tab.pack(fill="both", expand=1)
        kits_tab.pack(fill="both", expand=1)

        tabs_container.add(swap_teams_tab, text="Swap Teams")
        tabs_container.add(csv_tab, text="Export/Import CSV")
        tabs_container.add(extra_tab, text="Extra")
        tabs_container.add(kits_tab, text="Kits")

        root.resizable(False, False)
        root.mainloop() 
    else:
        root.destroy()

