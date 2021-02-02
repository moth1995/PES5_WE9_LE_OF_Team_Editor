import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import sys
from COFPES_OF_Editor_5.editor.option_file import OptionFile
from getnames import get_of_names
from swap_teams import swap_teams_data
from swap_teams import encrypt_and_save

#this is a function to update the list in the combobox
def swap_list_positions(teams_list, pos1, pos2): 
    teams_list[pos1], teams_list[pos2] = teams_list[pos2], teams_list[pos1] 
    return teams_list

def swap_btn_action():
    if swap_teams_data(temp_file,team_a_cmb.current(),team_b_cmb.current()):
        global teams_list
        teams_list=swap_list_positions(teams_list, team_a_cmb.current(), team_b_cmb.current())
        team_a_cmb.config(values=teams_list)
        team_b_cmb.config(values=teams_list)
        messagebox.showinfo(title=appname,message="Teams swapped!")        
    else:
        messagebox.showerror(title=appname,message="Can't swap the same team!!!")

def save_btn_action():
    if encrypt_and_save(temp_file,of):
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
filename=""
temp_file=""
filename = filedialog.askopenfilename(initialdir=".",title="Select your option file", filetypes=(("KONAMI-WIN32PES5OPT","KONAMI-WIN32PES5OPT"),("KONAMI-WIN32WE9UOPT","KONAMI-WIN32WE9UOPT"),("KONAMI-WIN32WE9KOPT","KONAMI-WIN32WE9KOPT")))
#filename = "KONAMI-WIN32PES5OPT"
if filename!="":
    of = OptionFile(filename)
    temp_file = "temp.bin"
    with open(temp_file, "wb") as binary_file:
        binary_file.write(of.data)
        #print("Temporary file created")
else:
    root.destroy()


tabs_container=ttk.Notebook(root)
swap_teams_tab=Frame(tabs_container, width=w, height=h)
export_team_tab=Frame(tabs_container, width=w, height=h)

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

#Export team tab

wip_lbl=Label(export_team_tab, text="Still working on this section, soon there will be something to test")


#Swap team tab placing

team_a_lbl.place(x=200, y=60)
team_b_lbl.place(x=420, y=60)
team_a_cmb.place(x=200, y=100)
team_b_cmb.place(x=420, y=100)
swap_teams_btn.place(x=380, y=160)
save_changes_btn.place(x=376, y=200)
copyright_lbl.place(x=0, y=555)
thanks_lbl.place(x=500, y=555)

#Export team tab placing

wip_lbl.place(x=280, y=160)

#Placing tabs and container in the root

tabs_container.pack()
swap_teams_tab.pack(fill="both", expand=1)
export_team_tab.pack(fill="both", expand=1)
tabs_container.add(swap_teams_tab, text="Swap Teams")
tabs_container.add(export_team_tab, text="Export Team")

root.resizable(False, False)
root.mainloop() 