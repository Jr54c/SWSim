import pandas
import csv

wb = pandas.read_excel('CustomStarshipTool_v109 (stats for all vehicles and starships).xls', sheet_name='StarshipInfo')
#print(wb.items)
"""
for I in wb.items(): #reads column by column
    print(I[0])
BOOK, PAGE, WEB, STARSHIP, CL, Ship CL, Size, Class, HP, DR, SR, STR, DEX, INT, Armor, Speed (C), Speed (S), Max, Velocity (km/h), Crew, C. Quality, Passeng., Astromech, Availability, Cost (new), Cost (used), MANUFACTURER, COMMENTS, Cargo, Consumables, Hyperdrive, Backup Hyperdrive, Wpn#1, Ion? (1 = yes, blank = no), Wpn#1 Pilot/Copilot/Gunner, Wpn#1 Battery?, Wpn#1 #Gunners, Wpn#1 #ofDmgDie, Wpn#1 Dmg die type, Wpn#1 Dmg Mulitplier, Wpn#2, Ion? (1 = yes, blank = no).1, Wpn#2 Pilot/Copilot/Gunner, Wpn#2 Battery?, Wpn#2 #Gunners, Wpn#2 #ofDmgDie, Wpn#2 Dmg die type, Wpn#2 Dmg Mulitplier, Wpn#3, Ion? (1 = yes, blank = no).2, Wpn#3 Pilot/Copilot/Gunner, Wpn#3 Battery?, Wpn#3 #Gunners, Wpn#3 #ofDmgDie, Wpn#3 Dmg die type, Wpn#3 Dmg Mulitplier, Wpn#4, Ion? (1 = yes, blank = no).3, Wpn#4 Pilot/Copilot/Gunner, Wpn#4 Battery?, Wpn#4 #Gunners, Wpn#4 #ofDmgDie, Wpn#4 Dmg die type, Wpn#4 Dmg Mulitplier, Wpn#5, Ion? (1 = yes, blank = no).4, Wpn#5 Pilot/Copilot/Gunner, Wpn#5 Battery?, Wpn#5 #Gunners, Wpn#5 #ofDmgDie, Wpn#5 Dmg die type, Wpn#5 Dmg Mulitplier, Wpn#6, Ion? (1 = yes, blank = no).5, Wpn#6 Pilot/Copilot/Gunner, Wpn#6 Battery?, Wpn#6 #Gunners, Wpn#6 #ofDmgDie, Wpn#6 Dmg die type, Wpn#6 Dmg Mulitplier, Wpn#7, Ion? (1 = yes, blank = no).6, Wpn#7 Pilot/Copilot/Gunner, Wpn#7 Battery?, Wpn#7 #Gunners, Wpn#7 #ofDmgDie, Wpn#7 Dmg die type, Wpn#7 Dmg Mulitplier, Wpn#8, Ion? (1 = yes, blank = no).7, Wpn#8 Pilot/Copilot/Gunner, Wpn#8 Battery?, Wpn#8 #Gunners, Wpn#8 #ofDmgDie, Wpn#8 Dmg die type, Wpn#8 Dmg Mulitplier, Terrain, Cover, Equip. Bonus to Pilot skill, Cargo units, Wpn#1Qty, (1=sngl,2=dbl,3=trpl,4=quad,5=Autoblaster), Wpn#1, Grade (1=Lt,2-Med,3=Hvy), Wpn#1, PtDfns?, Wpn#1, Fr-lnkd?, Wpn#1, Enhanced? (1 = Enh,2=AdvEnh), Wpn#1, Basic Name, Wpn#2Qty, (1=sngl,2=dbl,3=trpl,4=quad), Wpn#2, Grade (1=Lt,2-Med,3=Hvy), Wpn#2, PtDfns?, Wpn#2, Fr-lnkd?, Wpn#2, Enhanced? (1 = Enh,2=AdvEnh), Wpn#2, Basic Name, Wpn#3Qty, (1=sngl,2=dbl,3=trpl,4=quad), Wpn#3, Grade (1=Lt,2-Med,3=Hvy), Wpn#3, PtDfns?, Wpn#3, Fr-lnkd?, Wpn#3, Enhanced? (1 = Enh,2=AdvEnh), Wpn#3, Basic Name, Wpn#4Qty, (1=sngl,2=dbl,3=trpl,4=quad), Wpn#4, Grade (1=Lt,2-Med,3=Hvy), Wpn#4, PtDfns?, Wpn#4, Fr-lnkd?, Wpn#4, Enhanced? (1 = Enh,2=AdvEnh), Wpn#4, Basic Name, Wpn#5Qty, (1=sngl,2=dbl,3=trpl,4=quad), Wpn#5, Grade (1=Lt,2-Med,3=Hvy), Wpn#5, PtDfns?, Wpn#5, Fr-lnkd?, Wpn#5, Enhanced? (1 = Enh,2=AdvEnh), Wpn#5, Basic Name, Wpn#6Qty, (1=sngl,2=dbl,3=trpl,4=quad), Wpn#6, Grade (1=Lt,2-Med,3=Hvy), Wpn#6, PtDfns?, Wpn#6, Fr-lnkd?, Wpn#6, Enhanced? (1 = Enh,2=AdvEnh), Wpn#6, Basic Name, Wpn#7Qty, (1=sngl,2=dbl,3=trpl,4=quad), Wpn#7, Grade (1=Lt,2-Med,3=Hvy), Wpn#7, PtDfns?, Wpn#7, Fr-lnkd?, Wpn#7, Enhanced? (1 = Enh,2=AdvEnh), Wpn#7, Basic Name, Wpn#8Qty, (1=sngl,2=dbl,3=trpl,4=quad), Wpn#8, Grade (1=Lt,2-Med,3=Hvy), Wpn#8, PtDfns?, Wpn#8, Fr-lnkd?, Wpn#8, Enhanced? (1 = Enh,2=AdvEnh), Wpn#8, Basic Name, Units for consumables, Navicomputer / Astromech (A = Astromech, N = Navicomputer, LN = Limited Navicomputer, AN = (Advanced Navicomputer), Free EP, Combat Thrusters?, Carried Craft, ship, Has booster ring? (1=yes)
"""
ships = []
for I in wb['STARSHIP'][1:]:
    ships.append([I.replace('"', "").replace(',', ".")])


counter = 0

for I in ['HP', 'SR', 'Armor', 'Speed (S)', 'Hyperdrive', 'Cargo', 'Crew', 'C. Quality']:
    for II in wb[I][1:]:
        ships[counter].append(0) if II != II or II == 'none' else ships[counter].append(II) if I != 'Hyperdrive' else ships[counter].append(float(II.replace('x','')))
        counter += 1
    counter = 0

weapons = []
rows = len(wb['STARSHIP'])
for I in range(rows-1):
    I += 1
    weapons.append(['',0])
    for II in range(1,7):
        lst = ['']
        string = 'Wpn#'+str(II)
        name = wb[string][I]
        if name == name: #checking for nan
            lst = [name]
            for III in [' #Gunners', ' #ofDmgDie', ' Dmg die type', ' Dmg Mulitplier']:
                num = wb[string+III][I]
                if num == 'none':
                    lst.append(0)
                elif num == num: #checking for nan
                    if num == '6 + 4':
                        lst.append(eval(num))
                    else:
                        lst.append(num)
                else:
                    lst.append(1)
            weapons[-1][0] += lst[0] + '-'
            weapons[-1][1] += int(lst[1]*lst[2]*lst[3]*lst[4])
    if len(weapons[-1][0]) > 0: weapons[-1][0] = weapons[-1][0][:-1]


with open("shipList.csv",'w+') as resultFile:
    writr = csv.writer(resultFile, dialect='excel')
    for I in range(rows-1):
        ships[I].append(weapons[I][0])
        ships[I].append(weapons[I][1])
        print(ships[I])
        writr.writerow(ships[I])

#for I in ships:
 #   print(I)

#
# [print(I) for I in ships]
#
# print('\n'.join(ships))