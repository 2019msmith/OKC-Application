import csv
import math
with open('shots_data.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     team_A_2pt_attempts = 0
     team_A_2pt_attempts_list = []

     team_B_2pt_attempts = 0
     team_B_2pt_attempts_list = []

     team_A_nc3_attempts = 0
     team_A_nc3_attempts_list = []

     team_B_nc3_attempts = 0
     team_B_nc3_attempts_list = []

     team_A_c3_attempts = 0
     team_A_c3_attempts_list = []

     team_B_c3_attempts = 0
     team_B_c3_attempts_list = []

     team_A_shot_total = 0
     team_B_shot_total = 0

     team_A_made_2pt_total = 0
     team_B_made_2pt_total = 0

     team_A_made_nc3_total = 0
     team_B_made_nc3_total = 0

     team_A_made_c3_total = 0
     team_B_made_c3_total = 0
     for row in reader:
        #2pt
        if float(row['y']) >= -1.6 and float(row['y']) <= 7.8 and -22 <= float(row['x']) <= 22: # rectangle
            if row['team'] == "Team A":
                team_A_2pt_attempts +=1
                team_A_2pt_attempts_list.append(row)
                team_A_shot_total +=1
            else:
                team_B_2pt_attempts +=1
                team_B_2pt_attempts_list.append(row)
                team_B_shot_total +=1
        if abs(float(row['x'])**2 < 23.75**2):
            if math.sqrt(23.75**2 - float(row['x'])**2) > float(row['y']) > 7.8 and -22 <= float(row['x']) <= 22:
                if row['team'] == "Team A":
                    team_A_2pt_attempts +=1
                    team_A_2pt_attempts_list.append(row)
                    team_A_shot_total +=1
                else:
                    team_B_2pt_attempts +=1
                    team_B_2pt_attempts_list.append(row)
                    team_B_shot_total +=1
        #3nc
        if 23.75**2 - float(row['x'])**2 < float(row['y'])**2 and float(row['y']) > 7.8:
            if row['team'] == "Team A":
                team_A_nc3_attempts +=1
                team_A_nc3_attempts_list.append(row)
                team_A_shot_total +=1
            else:
                team_B_nc3_attempts +=1
                team_B_nc3_attempts_list.append(row)
                team_B_shot_total +=1
        #3c
        if abs(float(row['x'])) > 22 and float(row['y']) <= 7.8:
            if row['team'] == "Team A":
                team_A_c3_attempts +=1
                team_A_c3_attempts_list.append(row)
                team_A_shot_total +=1
            else:
                team_B_c3_attempts +=1
                team_B_c3_attempts_list.append(row)
                team_B_shot_total +=1

for row in team_A_2pt_attempts_list:
    if float(row['fgmade']) == 1.0: #made 2pt shot
        team_A_made_2pt_total +=1
for row in team_A_c3_attempts_list:
    if float(row['fgmade']) == 1.0: #made corner 3 shot
        team_A_made_c3_total +=1
for row in team_A_nc3_attempts_list:
    if float(row['fgmade']) == 1.0: #made non-corner 3 shot
        team_A_made_nc3_total +=1

for row in team_B_2pt_attempts_list:
    if float(row['fgmade']) == 1.0: #made 2pt shot
        team_B_made_2pt_total +=1
for row in team_B_c3_attempts_list:
    if float(row['fgmade']) == 1.0: #made corner 3 shot
        team_B_made_c3_total +=1
for row in team_B_nc3_attempts_list:
    if float(row['fgmade']) == 1.0: #made non-corner 3 shot
        team_B_made_nc3_total +=1

a_2pt_pct = team_A_2pt_attempts/team_A_shot_total
b_2pt_pct = team_B_2pt_attempts/team_B_shot_total
a_nc3_pct = team_A_nc3_attempts/team_A_shot_total
b_nc3_pct = team_B_nc3_attempts/team_B_shot_total
a_c3_pct = team_A_c3_attempts/team_A_shot_total
b_c3_pct = team_B_c3_attempts/team_B_shot_total

a_2pt_efg = team_A_made_2pt_total/len(team_A_2pt_attempts_list)
a_nc3_efg = (team_A_made_nc3_total + (team_A_made_nc3_total*0.5))/len(team_A_nc3_attempts_list)
a_c3_efg = (team_A_made_c3_total + (team_A_made_c3_total*0.5))/len(team_A_c3_attempts_list)
team_A_tot_eFG = ((team_A_made_2pt_total+team_A_made_c3_total+team_A_made_nc3_total)+((team_A_made_c3_total+team_A_made_nc3_total)*0.5))/team_A_shot_total

b_2pt_efg = team_B_made_2pt_total/len(team_B_2pt_attempts_list)
b_nc3_efg = (team_B_made_nc3_total + (team_B_made_nc3_total*0.5))/len(team_B_nc3_attempts_list)
b_c3_efg = (team_B_made_c3_total + (team_B_made_c3_total*0.5))/len(team_B_c3_attempts_list)
team_B_tot_eFG = ((team_B_made_2pt_total+team_B_made_c3_total+team_B_made_nc3_total)+((team_B_made_c3_total+team_B_made_nc3_total)*0.5))/team_B_shot_total

#print("A total percent", a_2pt_pct + a_nc3_pct + a_c3_pct)
#print("B total percent", b_2pt_pct + b_nc3_pct + b_c3_pct)
print("Shot Distribution:")
print("Team A 2pt %", a_2pt_pct)
print("Team A Non-Corner 3 %", a_nc3_pct)
print("Team A Corner 3 %", a_c3_pct)
print("Team A 2pt eFG: ", a_2pt_efg)
print("Team A Non-Corner 3 eFG: ", a_nc3_efg)
print("Team A Corner 3 eFG: ", a_c3_efg)
print()
print("Team B 2pt %", b_2pt_pct)
print("Team B Non-Corner 3 %", b_nc3_pct)
print("Team B Corner 3 %", b_c3_pct)
print("Team B 2pt eFG: ", b_2pt_efg)
print("Team B Non-Corner 3 eFG: ", b_nc3_efg)
print("Team B Corner 3 eFG: ", b_c3_efg)
print()
print("Team A Total eFG: ", team_A_tot_eFG)
print("Team B Total eFG: ", team_B_tot_eFG)