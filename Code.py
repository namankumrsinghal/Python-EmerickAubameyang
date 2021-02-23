import pandas as pd

#loading the datasets in variables
s_2016 = pd.read_csv(r'C:\Users\naman\Desktop\work\2016.csv')
s_2017 = pd.read_csv(r'C:\Users\naman\Desktop\work\2017.csv')
s_2018 = pd.read_csv(r'C:\Users\naman\Desktop\work\2018.csv')
s_2019 = pd.read_csv(r'C:\Users\naman\Desktop\work\2019.csv')
s_2020 = pd.read_csv(r'C:\Users\naman\Desktop\work\2020.csv')

from Teams import Team          #importing the class(Team) we created in Teams.py

#testing the working of the above class be taking the input from the user
a = Team(input("Enter team name: "), int(input("Enter the season(year): ")))

b = a.home() + a.away()

print(b)

#writing total points of the team in the given season into a text file
import os
dir_name = os.getcwd()
file_name = os.path.join(dir_name, 'output.txt')
text_file = open(file_name, 'w')
text_file.write(str(a.name) + '\n')
text_file.write('Total points for season ' + str(a.season) + ' are: ' + str(b))

#making emplty lists to store respective values
team_name = []
home_total_ratio = []
better_at_home = list()           #stores the teams for whom home points are greater than or equal to away points
better_away = list()

def best_home_ratio_team(d):
    """Takes a dictionary and returns the key with highest value"""
    try:
        a = ""
        b = 0
        for k, v in d.items():
            if v > b:
                b = v
                a = k
        return a
    except AttributeError:
        print("Function did not receive a dictionary input")
        pass

year = int(input("Enter the year to print out the record"))
c = 0               #counter to check if a valid value of year is entered(0 if valid, 1 if invalid)
if year == 2016:
    x = s_2016
elif year == 2017:
    x = s_2017
elif year == 2018:
    x = s_2018
elif year == 2019:
    x = s_2019
elif year == 2020:
    x = s_2020
else:
    print("Invalid value of season entered")
    c = 1

if c == 0:
    y = set()           #set that will contain names of all teams(used a set since we wanted to take care of duplicate values)
    for e in x['HomeTeam']:
        y.add(e)

    for e in y:
        a = Team(e, year)
        p_h = a.home()      #this prints the home record of the team in the season, as well as stores home points in p_h
        p_a = a.away()      #this prints the away record of the team in the season, as well as stores away points in p_a

        print("\n Total Points: ", p_h + p_a, "\n")
        if p_h >= p_a : 
            better_at_home.append(e)
        else: 
            better_away.append(e)
        team_name.append(e)
        home_total_ratio.append(p_h/(p_h+p_a))

    d = dict(zip(team_name, home_total_ratio))       
    print(d)

    result  = list(x['FTR'])

    home = result.count('H')
    draw = result.count('D')
    away = result.count('A')

    print("total home wins in the season ", home)
    print("total draws in the season ", draw)
    print("total away wins in the season ", away)

    print("The number of teams with better home record are: ", len(better_at_home))
    print(better_at_home)
    print(better_away)
    print("The team with the best home to total points ratio is: ", best_home_ratio_team(d))

    #Now, we will run the above algorithm to every team in the last 5 seasons(2016-17 through 2020-21) and plot a comparison
    plot_or_not = input("Do you want to run the algorithm for every team in the last 5 seasons and make a comparison plot?(Y/N)")
    if plot_or_not == 'Y':
        print("Running the code for all the seasons and plotting them at the end")

        record = []
        for year in range(2016, 2021):
            team_name = []
            home_total_ratio = []
            better_at_home = list()           #stores the teams for whom home points are greater than or equal to away points
            better_away = list()
            if year == 2016:
                x = s_2016
            elif year == 2017:
                x = s_2017
            elif year == 2018:
                x = s_2018
            elif year == 2019:
                x = s_2019
            elif year == 2020:
                x = s_2020
            
            y = set()           #set that will contain names of all teams(used a set since we wanted to take care of duplicate values)
            for e in x['HomeTeam']:
                y.add(e)

            for e in y:
                a = Team(e, year)
                p_h = a.home()      #this prints the home record of the team in the season, as well as stores home points in p_h
                p_a = a.away()      #this prints the away record of the team in the season, as well as stores away points in p_a

                print("\n Total Points: ", p_h + p_a, "\n")
                if p_h >= p_a : 
                    better_at_home.append(e)
                else: 
                    better_away.append(e)
                team_name.append(e)
                home_total_ratio.append(p_h/(p_h+p_a))

            d = dict()
            d = dict(zip(team_name, home_total_ratio))       
            print(d)

            result  = list(x['FTR'])

            home = result.count('H')
            draw = result.count('D')
            away = result.count('A')
            if year != 2020:
                record.append((home/380, draw/380, away/380, len(better_at_home)/20))
            elif year == 2020:
                record.append((home/98, draw/98, away/98, len(better_at_home)/20))

            print("total home wins in the season ", home)
            print("total draws in the season ", draw)
            print("total away wins in the season ", away)

            print("The number of teams with better home record are: ", len(better_at_home))
            print(better_at_home)
            print(better_away)

        print("Record list of tuples: ")
        print(record)



        #plotting the season records(% home wins, away wins...) using matplotlib. The code is learnt and modified from this(open source) tutorial https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
        import matplotlib
        import matplotlib.pyplot as plt
        import numpy as np


        labels = ['2016', '2017', '2018', '2019', '2020']
        home_win = list()
        draw = list()
        away_win = list()
        teams_better_home = list()
        for e in record:
            home_win.append(e[0])
            draw.append(e[1])
            away_win.append(e[2])
            teams_better_home.append(e[3])

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, home_win, width, label='HOME')
        rects2 = ax.bar(x - width/4, away_win, width, label='AWAY')
        rects3 = ax.bar(x + width/4, draw, width, label='DRAW')
        rects4 = ax.bar(x + width/2, teams_better_home, width, label='TEAMS BETTER AT HOME')



        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Proportion')
        ax.set_title('Premier League: Comparison of Home and Away record for Season 2016-17 to 2020-21')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()


        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')


        autolabel(rects1)
        autolabel(rects2)
        autolabel(rects3)
        autolabel(rects4)

        fig.tight_layout()

        plt.show()

    else:
        pass