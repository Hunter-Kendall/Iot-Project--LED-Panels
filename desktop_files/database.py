import sqlite3
conn = sqlite3.connect('led_lights.db')
c = conn.cursor()

instructions = str([["Fade",range(0, 13), [[255, 0, 0], [0, 0, 255]], [255, 0, 0], [0, 1], 7],
                    ["Fade", range(13, 22),[[0, 255, 0], [0, 0, 255], [255,122,4]], [0, 255, 0], [0,2], 7],
                    ["Static", range(22, 31), [25, 183, 205]],
                    ["Strobe", range(31, 40), [[0, 255, 0], [0, 0, 255], [255,122,4]],[0,2], 3],
                    ["Fade", range(40, 49),[[0, 255, 0], [0, 60, 255], [255,122,4]], [0, 255, 0], [0,2], 7],
                    ["Fade", range(49, 58),[[204, 255, 0], [0, 204, 255], [255,122,4]], [0, 255, 0], [0,2], 7],
                    ["Strobe", range(58, 67), [[0, 255, 111], [179, 0, 255], [255,122,4]],[0,2], 3],
                    ["Fade", range(67, 76),[[19, 255, 203], [45, 77, 255], [255,122,4]], [0, 255, 0], [0,2], 7],
                    ["Strobe", range(76, 89), [[92, 255, 0], [0, 36, 255], [255,122,4]],[0,2], 3]])
instruct = str([['Static', range(0, 13), [0, 0, 0]],
            ['Static', range(13, 22), [0, 0, 0]],
            ['Static', range(22, 31), [0, 0, 0]],
            ['Static', range(31, 40), [0, 0, 0]],
            ['Static', range(40, 49), [0, 0, 0]],
            ['Static', range(49, 58), [0, 0, 0]],
            ['Static', range(58, 67), [0, 0, 0]],
            ['Static', range(67, 76), [0, 0, 0]],
            ['Static', range(76, 89), [0, 0, 0]]])

# c.execute('''CREATE TABLE Profiles
#             (profile TEXT PRIMARY KEY,
#              instructions TEXT)''')

# c.execute('''CREATE TABLE Last
#             (last_light TEXT PRIMARY KEY,
#            instructions TEXT,
#           CONSTRAINT FK_profile FOREIGN KEY (last_light)
#            REFERENCES Profiles(profile)
#            ON DELETE NO ACTION ON UPDATE NO ACTION)''')


# ins1 = f'''INSERT INTO Profiles VALUES("Last", {repr(instructions)})'''
# ins2 = f'''INSERT INTO Last VALUES("Last", {repr(instructions)})'''
# ins3 = f'''INSERT INTO Profiles VALUES("Off", {repr(instruct)})'''
# c.execute(ins1)
# c.execute(ins2)
# c.execute(ins3)
# conn.commit()
c.execute("""SELECT * FROM Profiles""")
row = c.fetchall()
for i in row:
    print(i)