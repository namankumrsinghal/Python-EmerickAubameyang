import pandas as pd

#loading the datasets in variables
s_2016 = pd.read_csv(r'C:\Users\naman\Desktop\work\2016.csv')
s_2017 = pd.read_csv(r'C:\Users\naman\Desktop\work\2017.csv')
s_2018 = pd.read_csv(r'C:\Users\naman\Desktop\work\2018.csv')
s_2019 = pd.read_csv(r'C:\Users\naman\Desktop\work\2019.csv')
s_2020 = pd.read_csv(r'C:\Users\naman\Desktop\work\2020.csv')

class Team():
    def __init__(self, name, season = 2020):
        self.name = name
        self.season = season

    def __str__(self):
        return "Team: " + str(self.name) + "; Season: " + str(self.season)

    def home(self):
        """prints out the home record for the given team in the given season and returns home points"""
        w = 0       #count for wins
        d = 0       #count for draws
        l = 0       #count for losses
        
        #checking season, and if a valid value has been entered
        if self.season == 2016:
            x = s_2016
        elif self.season == 2017:
            x = s_2017
        elif self.season == 2018:
            x = s_2018
        elif self.season == 2019:
            x = s_2019
        elif self.season == 2020:
            x = s_2020
        else:
            print("Invalid value of season entered")
            return 0

        teams = set()           #set that will contain names of all teams(used a set since we wanted to take care of duplicate values)
        for e in x['HomeTeam']:
            teams.add(e)
        if self.name not in teams:              #checking if given team name is valid(ie, whether that team played in the league that season)
            print("Invalid value of team entered")
            return 0

        for i in range(len(x['HomeTeam'])):
            if x['HomeTeam'][i] == self.name:
                if x['FTR'][i] == 'H':
                    w +=1
                elif x['FTR'][i] == 'D':
                    d += 1
                else:
                    l += 1
        home_points = (w*3 + d*1)
        print("Home record for ", self)
        print("Wins: ", w)
        print("Draws: ", d)
        print("Losses: ", l)
        print("points", home_points, ";" , 100*home_points/((w+d+l)*3), "%")
        return home_points

    def away(self):
        """prints out the home record for the given team in the given season and returns home points"""
        w = 0       #count for wins
        d = 0       #count for draws
        l = 0       #count for loses

        #checking season, and if a valid value has been entered
        if self.season == 2016:
            x = s_2016
        elif self.season == 2017:
            x = s_2017
        elif self.season == 2018:
            x = s_2018
        elif self.season == 2019:
            x = s_2019
        elif self.season == 2020:
            x = s_2020
        else:
            print("Invalid value of season entered")
            return 0

        teams = set()           #set that will contain names of all teams(used a set since we wanted to take care of duplicate values)
        for e in x['HomeTeam']:
            teams.add(e)
        if self.name not in teams:              #checking if given team name is valid(ie, whether that team played in the league that season)
            print("Invalid value of team entered")
            return 0

        for i in range(len(x['HomeTeam'])):
            if x['AwayTeam'][i] == self.name:
                if x['FTR'][i] == 'A':
                    w +=1
                elif x['FTR'][i] == 'D':
                    d += 1
                else:
                    l += 1
        away_points = (w*3 + d*1)
        print("Away record for ", self )
        print("Wins: ", w)
        print("Draws: ", d)
        print("Loses: ", l)
        print("points", away_points, ";" , 100*(away_points)/((w+d+l)*3), "%")
        return away_points
