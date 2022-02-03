import tkinter as tk
#import time
from tkinter import colorchooser
import socket
import subprocess
import sqlite3
root=tk.Tk()
# setting up database
conn = sqlite3.connect('led_lights.db')
c = conn.cursor()

def insert_db(name, instructions):
    print("insert ins", instructions)
    ex1 = f"""INSERT INTO Profiles VALUES('{name}', {repr(instructions)})"""
    c.execute(ex1)
    ex2 = f"""UPDATE Last SET instructions = {repr(instructions)} WHERE last_light = 'Last' """
    c.execute(ex2)
    ex3 = f"""UPDATE Profiles SET instructions = {repr(instructions)} WHERE Profile = 'Last' """
    c.execute(ex3)
    conn.commit()

def update_last(instructions):
    ex1 = f"""UPDATE Last SET instructions = {repr(instructions)} WHERE last_light = 'Last' """
    c.execute(ex1)
    ex2 = f"""UPDATE Profiles SET instructions = {repr(instructions)} WHERE Profile = 'Last' """
    c.execute(ex2)
    conn.commit()
# setting up websocket

proc = subprocess.Popen(["ping", "csci226-hdk", "-4"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
splitw = out.split()
ip = str(splitw[2])
ip = ip.replace("b","")
ip = ip.replace("'","")
ip = ip.replace("[","")
ip = ip.replace("]","")
print(ip)

HOST = str(ip)
PORT = 5051

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

def send(ins):

    #socket.connect((HOST, PORT))
    socket.send(str(ins).encode())
    don = socket.recv(1024).decode('UTF - 8')
    print(don)

# setting the windows size
root.geometry("1920x1500")
# panel 1 variables
p1var = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]
p1rgb = [[],[],[],[],[]]
p1c = [tk.Checkbutton(root, variable=p1var[0], \
                 onvalue=1, offvalue=0, height=5, \
                 width=20),
       tk.Checkbutton(root, variable=p1var[1], \
                 onvalue=1, offvalue=0, height=5,\
                 width=20),
       tk.Checkbutton(root, variable=p1var[2], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p1var[3], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p1var[4], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20)
       ]

# pannel 1 variables
p2var = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]
p2rgb = [[],[],[],[],[]]
p2c = [tk.Checkbutton(root, variable=p2var[0], \
                 onvalue=1, offvalue=0, height=5, \
                 width=20),
       tk.Checkbutton(root, variable=p2var[1], \
                 onvalue=1, offvalue=0, height=5,\
                 width=20),
       tk.Checkbutton(root, variable=p2var[2], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p2var[3], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p2var[4], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20)
       ]
# pannel 3 variables
p3var = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]
p3rgb = [[],[],[],[],[]]
p3c = [tk.Checkbutton(root, variable=p3var[0], \
                 onvalue=1, offvalue=0, height=5, \
                 width=20),
       tk.Checkbutton(root, variable=p3var[1], \
                 onvalue=1, offvalue=0, height=5,\
                 width=20),
       tk.Checkbutton(root, variable=p3var[2], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p3var[3], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p3var[4], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20)
       ]
p4var = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]
p4rgb = [[],[],[],[],[]]
p4c = [tk.Checkbutton(root, variable=p4var[0], \
                 onvalue=1, offvalue=0, height=5, \
                 width=20),
       tk.Checkbutton(root, variable=p4var[1], \
                 onvalue=1, offvalue=0, height=5,\
                 width=20),
       tk.Checkbutton(root, variable=p4var[2], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p4var[3], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p4var[4], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20)
       ]

p5var = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]
p5rgb = [[],[],[],[],[]]
p5c = [tk.Checkbutton(root, variable=p5var[0], \
                 onvalue=1, offvalue=0, height=5, \
                 width=20),
       tk.Checkbutton(root, variable=p5var[1], \
                 onvalue=1, offvalue=0, height=5,\
                 width=20),
       tk.Checkbutton(root, variable=p5var[2], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p5var[3], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p5var[4], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20)
       ]
p6var = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]
p6rgb = [[],[],[],[],[]]
p6c = [tk.Checkbutton(root, variable=p6var[0], \
                 onvalue=1, offvalue=0, height=5, \
                 width=20),
       tk.Checkbutton(root, variable=p6var[1], \
                 onvalue=1, offvalue=0, height=5,\
                 width=20),
       tk.Checkbutton(root, variable=p6var[2], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p6var[3], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p6var[4], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20)
       ]
p7var = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]
p7rgb = [[],[],[],[],[]]
p7c = [tk.Checkbutton(root, variable=p7var[0], \
                 onvalue=1, offvalue=0, height=5, \
                 width=20),
       tk.Checkbutton(root, variable=p7var[1], \
                 onvalue=1, offvalue=0, height=5,\
                 width=20),
       tk.Checkbutton(root, variable=p7var[2], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p7var[3], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p7var[4], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20)
       ]
p8var = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]
p8rgb = [[],[],[],[],[]]
p8c = [tk.Checkbutton(root, variable=p8var[0], \
                 onvalue=1, offvalue=0, height=5, \
                 width=20),
       tk.Checkbutton(root, variable=p8var[1], \
                 onvalue=1, offvalue=0, height=5,\
                 width=20),
       tk.Checkbutton(root, variable=p8var[2], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p8var[3], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p8var[4], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20)
       ]
p9var = [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]
p9rgb = [[],[],[],[],[]]
p9c = [tk.Checkbutton(root, variable=p9var[0], \
                 onvalue=1, offvalue=0, height=5, \
                 width=20),
       tk.Checkbutton(root, variable=p9var[1], \
                 onvalue=1, offvalue=0, height=5,\
                 width=20),
       tk.Checkbutton(root, variable=p9var[2], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p9var[3], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20),
       tk.Checkbutton(root, variable=p9var[4], \
                      onvalue=1, offvalue=0, height=5, \
                      width=20)
       ]
def anim_update(choice):
    print("updating")
    global p1c, p2c, p3c

    for i, r, pc, d in [[panel_1[0], 3, p1c, drop1], [panel_2[0],4, p2c, drop2], [panel_3[0], 5, p3c, drop3] , [panel_4[0], 6, p4c, drop4], [panel_5[0], 7, p5c, drop5], [panel_6[0], 8, p6c, drop6], [panel_7[0], 9, p7c, drop7], [panel_8[0], 10, p8c, drop8], [panel_9[0], 11, p9c, drop9]]:



            if i.get() == "Static":
                d[1].grid_forget()
                d[2].grid_forget()
                pc[0].grid(row=r, column=4 )
                pc[1].grid_forget()
                pc[2].grid_forget()
                pc[3].grid_forget()
                pc[4].grid_forget()

            elif i.get() == "Fade":
                d[1].grid(row=r, column=2)
                d[2].grid(row=r, column=3)
                pc[0].grid(row=r, column=4)
                pc[1].grid(row=r, column=5)
            elif i.get() == "Strobe":
                d[1].grid(row=r, column=2)
                d[2].grid(row=r, column=3)
                pc[0].grid(row=r, column=4)
                pc[1].grid(row=r, column=5)

def colornum(choice):
    print("numcolor")
    for i, r, pc in [[panel_1[2],3,p1c], [panel_2[2],4,p2c], [panel_3[2],5,p3c], [panel_4[2],6,p4c], [panel_5[2],7,p5c], [panel_6[2],8,p6c], [panel_7[2],9,p7c], [panel_8[2],10,p8c], [panel_9[2],11,p9c]]:
        if i.get() == "3":
            pc[2].grid(row=r, column=6, columnspan=1)
            pc[3].grid_forget()
            pc[4].grid_forget()
        elif i.get() == "4":
            pc[2].grid(row=r, column=6)
            pc[3].grid(row=r, column=7)
            pc[4].grid_forget()
        elif i.get() == "5":
            pc[2].grid(row=r, column=6)
            pc[3].grid(row=r, column=7)
            pc[4].grid(row=r, column=8)
        else:
            pc[2].grid_forget()
            pc[3].grid_forget()
            pc[4].grid_forget()

# defining a function that will get lighting profiles
def get_profiles(light):
    global profiles
    c.execute("""SELECT profile FROM Profiles""")
    rows = c.fetchall()

    profiles = []
    for i in rows:
        profiles.append(i[0])
    print(profiles)

# declaring string variable
# for profile name
profile_name = tk.StringVar()
#panels
profiles = []
options = ["Static", "Fade", "Strobe"]
speed_control = ["1","2","3","4","5","6","7","8","9","10"]
num_colors = ["2","3","4","5"]
panel_1 = [tk.StringVar(),tk.StringVar(),tk.StringVar()]
panel_2 = [tk.StringVar(),tk.StringVar(),tk.StringVar()]
panel_3 = [tk.StringVar(),tk.StringVar(),tk.StringVar()]
panel_4 = [tk.StringVar(),tk.StringVar(),tk.StringVar()]
panel_5 = [tk.StringVar(),tk.StringVar(),tk.StringVar()]
panel_6 = [tk.StringVar(),tk.StringVar(),tk.StringVar()]
panel_7 = [tk.StringVar(),tk.StringVar(),tk.StringVar()]
panel_8 = [tk.StringVar(),tk.StringVar(),tk.StringVar()]
panel_9 = [tk.StringVar(),tk.StringVar(),tk.StringVar()]
#Option
#panel_1[0].set("Static")
#panel_1[2].set("Static")
#panel_2[2].set("Static")
#panel_3[2].set("Static")
#speed_control
panel_1[1].set("1")
panel_2[1].set("1")
panel_3[1].set("1")
panel_4[1].set("1")
panel_5[1].set("1")
panel_6[1].set("1")
panel_7[1].set("1")
panel_8[1].set("1")
panel_9[1].set("1")
#num_colors
panel_1[2].set("2")
panel_2[2].set("2")
panel_3[2].set("2")
panel_4[2].set("2")
panel_5[2].set("2")
panel_6[2].set("2")
panel_7[2].set("2")
panel_8[2].set("2")
panel_9[2].set("2")

dbprofile = tk.Label(root, text='use from database:', font=('calibre', 10, 'bold'))
dbvalue = tk.StringVar()
get_profiles(1)
dbdrop = tk.OptionMenu(root, dbvalue, *profiles, command= get_profiles)

drop1 = [tk.OptionMenu(root, panel_1[0], *options, command=anim_update), tk.OptionMenu(root, panel_1[1], *speed_control), tk.OptionMenu(root, panel_1[2], *num_colors, command=colornum)]
drop2 = [tk.OptionMenu(root, panel_2[0], *options, command=anim_update), tk.OptionMenu(root, panel_2[1], *speed_control), tk.OptionMenu(root, panel_2[2], *num_colors, command=colornum)]
drop3 = [tk.OptionMenu(root, panel_3[0], *options, command=anim_update), tk.OptionMenu(root, panel_3[1], *speed_control), tk.OptionMenu(root, panel_3[2], *num_colors, command=colornum)]
drop4 = [tk.OptionMenu(root, panel_4[0], *options, command=anim_update), tk.OptionMenu(root, panel_4[1], *speed_control), tk.OptionMenu(root, panel_4[2], *num_colors, command=colornum)]
drop5 = [tk.OptionMenu(root, panel_5[0], *options, command=anim_update), tk.OptionMenu(root, panel_5[1], *speed_control), tk.OptionMenu(root, panel_5[2], *num_colors, command=colornum)]
drop6 = [tk.OptionMenu(root, panel_6[0], *options, command=anim_update), tk.OptionMenu(root, panel_6[1], *speed_control), tk.OptionMenu(root, panel_6[2], *num_colors, command=colornum)]
drop7 = [tk.OptionMenu(root, panel_7[0], *options, command=anim_update), tk.OptionMenu(root, panel_7[1], *speed_control), tk.OptionMenu(root, panel_7[2], *num_colors, command=colornum)]
drop8 = [tk.OptionMenu(root, panel_8[0], *options, command=anim_update), tk.OptionMenu(root, panel_8[1], *speed_control), tk.OptionMenu(root, panel_8[2], *num_colors, command=colornum)]
drop9 = [tk.OptionMenu(root, panel_9[0], *options, command=anim_update), tk.OptionMenu(root, panel_9[1], *speed_control), tk.OptionMenu(root, panel_9[2], *num_colors, command=colornum)]



# submit all info
def submit():
    p_name = profile_name.get()
    instructions = []
    #formatting instructions
    for pandat, pan, rgb in [[panel_1, range(0,13), p1rgb], [panel_2, range(13,22), p2rgb], [panel_3, range(22,31), p3rgb], [panel_4, range(31,40), p4rgb], [panel_5, range(40,49), p5rgb], [panel_6, range(49,58), p6rgb], [panel_7, range(58,67), p7rgb], [panel_8, range(67,76), p8rgb], [panel_9, range(76,89), p9rgb]]:
        if pandat[0].get() == "Static":
            instructions.append([pandat[0].get(), pan, rgb[0]])
        elif pandat[0].get() == "Fade":
            try:
                while True:
                    rgb.remove([0,0,0])
            except ValueError:
                pass

            instructions.append([pandat[0].get(), pan, rgb, rgb[0], [0, len(rgb) - 1], int(pandat[1].get())])
        elif pandat[0].get() == "Strobe":
            try:
                while True:
                    rgb.remove([0,0,0])
            except ValueError:
                pass

            instructions.append([pandat[0].get(), pan, rgb, [0, len(rgb) - 1], int(pandat[1].get())])
    print("Profile Name: " + p_name)
    print("ins", instructions)
    print("dbvalue", dbvalue.get())
    profile_name.set("")

    #whether to insert from db or use from db or neither
    if tobeins.get() == 1:
        insert_db(p_name, str(instructions))
        send(instructions)
    #does nothing
    elif tobeins.get() == 1 and touse.get() ==1:
         get_profiles(1)
    elif touse.get() ==1:
        c.execute(f"""SELECT instructions FROM Profiles WHERE profile = {repr(dbvalue.get())} """)
        r = c.fetchone()[0]
        update_last(str(r))

        print(r)
        send(eval(r))
    else:
        update_last(str(instructions))
        send(instructions)

    print("sent")
    get_profiles(1)
    dbdrop.grid_forget()
    dbdrop.grid(row=0, column=5)

def choose_color():
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")

    for i, r, c in [[p1var, p1rgb, p1c], [p2var, p2rgb, p2c], [p3var, p3rgb, p3c], [p4var, p4rgb, p4c], [p5var, p5rgb, p5c], [p6var, p6rgb, p6c], [p7var, p7rgb, p7c], [p8var, p8rgb, p8c], [p9var, p9rgb, p9c]]:

        for n in range(0, 5):
            #print(n)
            if i[n].get() == 1:
                c[n].configure(bg=color_code[1])
                #print(color_code[1])
                r[n].clear()
                for j in color_code[0]:
                    r[n].append(j)
                #print(r)
            elif r[n] == []:
                r[n] = [0,0,0]





# creating a label for
# name using widget Label
name_label = tk.Label(root, text='Profile Name', font=('calibre', 10, 'bold'))

# creating a entry for input
# profile name using widget Entry
name_entry = tk.Entry(root, textvariable=profile_name, font=('calibre', 10, 'normal'))

panel_1_label = tk.Label(root, text='panel 1', font=('calibre', 10, 'bold'))
panel_2_label = tk.Label(root, text='panel 2', font=('calibre', 10, 'bold'))
panel_3_label = tk.Label(root, text='panel 3', font=('calibre', 10, 'bold'))
panel_4_label = tk.Label(root, text='panel 4', font=('calibre', 10, 'bold'))
panel_5_label = tk.Label(root, text='panel 5', font=('calibre', 10, 'bold'))
panel_6_label = tk.Label(root, text='panel 6', font=('calibre', 10, 'bold'))
panel_7_label = tk.Label(root, text='panel 7', font=('calibre', 10, 'bold'))
panel_8_label = tk.Label(root, text='panel 8', font=('calibre', 10, 'bold'))
panel_9_label = tk.Label(root, text='panel 9', font=('calibre', 10, 'bold'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

color_picker1 = tk.Button(root, text="Select color",command=choose_color)
#to be inserted into db
tobeins =tk.IntVar()
tbi = tk.Checkbutton(root, variable=tobeins, \
                 onvalue=1, offvalue=0, height=5, \
                 width=20)
insert_label = tk.Label(root, text='Add to Database:', font=('calibre', 10, 'bold'))

touse = tk.IntVar()
tu = tk.Checkbutton(root, variable=touse, \
                 onvalue=1, offvalue=0, height=5, \
                 width=20)

dbuse_label = tk.Label(root, text='Use from Database:', font=('calibre', 10, 'bold'))
# placing the label and entry in
# the required position using grid
# method

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
tbi.grid(row=0, column=3)
insert_label.grid(row=0, column=2)
dbprofile.grid(row=0, column=4)
dbdrop.grid(row=0, column=5)
dbuse_label.grid(row=0, column=6)
tu.grid(row=0, column=7)
sub_btn.grid(row=2, column=1)
panel_1_label.grid(row=3, column=0)
panel_2_label.grid(row=4, column=0)
panel_3_label.grid(row=5, column=0)
panel_4_label.grid(row=6, column=0)
panel_5_label.grid(row=7, column=0)
panel_6_label.grid(row=8, column=0)
panel_7_label.grid(row=9, column=0)
panel_8_label.grid(row=10, column=0)
panel_9_label.grid(row=11, column=0)
drop1[0].grid(row=3, column=1, columnspan=1)
drop2[0].grid(row=4, column=1, columnspan=1)
drop3[0].grid(row=5, column=1, columnspan=1)
drop4[0].grid(row=6, column=1, columnspan=1)
drop5[0].grid(row=7, column=1, columnspan=1)
drop6[0].grid(row=8, column=1, columnspan=1)
drop7[0].grid(row=9, column=1, columnspan=1)
drop8[0].grid(row=10, column=1, columnspan=1)
drop9[0].grid(row=11, column=1, columnspan=1)
color_picker1.grid(row=2, column=2)
#c1.grid(row=3, column=2)
#c2.grid(row=3, column=3)
#c3.grid(row=3, column=4)
#c1.grid_forget()
#c2.grid_forget()
#c3.grid_forget()
# performing an infinite loop
# for the window to display
root.mainloop()
