import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import sys
import os

from COFPES_OF_Editor_5.editor.option_file import OptionFile
from COFPES_OF_Editor_5.editor.utils.common_functions import bytes_to_int, zero_fill_right_shift, to_int, to_byte

from getnames import get_of_names
from swap_teams import swap_teams_data
from swap_teams import encrypt_and_save
from player_data import get_stats, set_value, get_value
from export_csv import write_csv
from import_csv import load_csv
from of_crypt import of_encrypter, of_decrypter

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
    players_ids=[*range(1, 5000, 1)]+[*range(32768, 32952, 1)]
    all_data=[]
    for player in players_ids:
        all_data.append(get_stats(player,of))
    root.new_file = filedialog.asksaveasfile(initialdir=".",title="Create your CSV file", mode='w', filetypes=(("CSV files","*.csv"),("All files", "*")), defaultextension=".csv")
    if root.new_file is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    if write_csv(root.new_file.name,all_data):
        messagebox.showinfo(title=appname,message="CSV file created!")
    else:
        messagebox.showerror(title=appname,message="Error while creating CSV file, please run as admin")

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
    if swap_teams_data(of.data,team_a_cmb.current(),team_b_cmb.current()):
        global teams_list
        teams_list=swap_list_positions(teams_list, team_a_cmb.current(), team_b_cmb.current())
        team_a_cmb.config(values=teams_list)
        team_b_cmb.config(values=teams_list)
        messagebox.showinfo(title=appname,message="Teams swapped!")        
    else:
        messagebox.showerror(title=appname,message="Can't swap the same team!!!")
def save_btn_action():
    if encrypt_and_save(of):
        messagebox.showinfo(title=appname,message="All changes saved")
    else:
        messagebox.showerror(title=appname,message="Error while saving, please run as admin")

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
root.filename=""
#temp_file=""
#root.filename = filedialog.askopenfilename(initialdir=".",title="Select your option file", filetypes=(("KONAMI-WIN32PES5OPT","KONAMI-WIN32PES5OPT"),("KONAMI-WIN32WE9UOPT","KONAMI-WIN32WE9UOPT"),("KONAMI-WIN32WE9KOPT","KONAMI-WIN32WE9KOPT")))
#root.filename = "KONAMI-WIN32PES5OPT"
root.filename = r"C:\Users\marco\Documents\KONAMI\Pro Evolution Soccer 5\save\folder1\KONAMI-WIN32PES5OPT"
if root.filename!="":
    of = OptionFile(root.filename)
    '''
    # No need anymore to create a temporary file, we just use the bytearray
    temp_file = "temp.bin"
    with open(temp_file, "wb") as binary_file:
        binary_file.write(of.data)
        #print("Temporary file created")
    '''
else:
    root.destroy()

#below is how to read the value for all players, i compare this to the mdb file exported from dkz studio

#get_value(of,player,86-48, 0, 127, "GOAL CELEBRATION 2")
#get_value(of,player,85-48, 1, 127, "GOAL CELEBRATION 1")


players_ids=[*range(1, 5000, 1)]+[*range(32768, 32952, 1)]
all_data=[]
for player in players_ids:
    ##all_data.append(player)
    all_data.append(get_value(of,player,91-48,1, 3, "skin colour")+1)

#print (all_data[1228])

#get_value(of, 1, 0, 0 , 10, "boot type") #could be 12 boots maybe 51 offset

#print(get_value(of, 1, 7, 0, 127, "Attack"))
#set_value(of, 1, 7, 0, 127, 31)
#print(get_value(of, 1, 7, 0, 127, "Attack"))

#load_csv(of, 'players.csv')
#print(get_value(of, 1, 7, 0, 127, "Attack"))
#print(of.file_location)
#of.save_option_file()


tabs_container=ttk.Notebook(root)
swap_teams_tab=Frame(tabs_container, width=w, height=h)
csv_tab=Frame(tabs_container, width=w, height=h)
extra_tab=Frame(tabs_container, width=w, height=h)

#Swap teams tab 

teams_list=[]
teams_list=get_of_names(of)

team_a_lbl=Label(swap_teams_tab, text="Team A")
team_b_lbl=Label(swap_teams_tab, text="Team B")
team_a_cmb=ttk.Combobox(swap_teams_tab, state="readonly", value=teams_list, width=30)
team_b_cmb=ttk.Combobox(swap_teams_tab, state="readonly", value=teams_list, width=30)

swap_teams_btn=Button(swap_teams_tab, text="Swap teams", command=lambda: swap_btn_action())
save_changes_btn=Button(swap_teams_tab, text="Save changes", command=lambda: save_btn_action())

copyright_lbl=Label(swap_teams_tab, text="By PES Indie Team")
thanks_lbl=Label(swap_teams_tab, text="Thanks to PeterC10 for python de/encrypt code for OF")

#CSV tab

#wip_lbl=Label(csv_tab, text="Still working on this section, soon there will be something to test")
create_csv_btn=Button(csv_tab, text="Create CSV", command=lambda: export_all_to_csv())
import_csv_btn=Button(csv_tab, text="Import CSV", command=lambda: import_all_from_csv())

#extra tab

decrypt_of_btn=Button(extra_tab, text="Decrypt", command=lambda: decrypt_btn_action())
encrypt_of_btn=Button(extra_tab, text="Encrypt", command=lambda: encrypt_btn_action())
stat_test_entry = Entry (extra_tab) 
test_print_btn=Button(extra_tab, text="Print stat test!", command=lambda: print(all_data[int(stat_test_entry.get())+1]))


#Swap team tab placing

team_a_lbl.place(x=200, y=60)
team_b_lbl.place(x=420, y=60)
team_a_cmb.place(x=200, y=100)
team_b_cmb.place(x=420, y=100)
swap_teams_btn.place(x=380, y=160)
save_changes_btn.place(x=376, y=200)
copyright_lbl.place(x=0, y=555)
thanks_lbl.place(x=500, y=555)

#CSV tab placing

#wip_lbl.place(x=280, y=160)
create_csv_btn.place(x=240, y=160)
import_csv_btn.place(x=320, y=160)

# Extra tab placing

decrypt_of_btn.place(x=240, y=160)
encrypt_of_btn.place(x=320, y=160)
stat_test_entry.place(x=200, y=70)
test_print_btn.place(x=200, y=100)

#Placing tabs and container in the root




tabs_container.pack()
swap_teams_tab.pack(fill="both", expand=1)
csv_tab.pack(fill="both", expand=1)
extra_tab.pack(fill="both", expand=1)

tabs_container.add(swap_teams_tab, text="Swap Teams")
tabs_container.add(csv_tab, text="Export/Import CSV")
tabs_container.add(extra_tab, text="Extra")

root.resizable(False, False)
root.mainloop() 