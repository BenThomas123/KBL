# @Author Benjamin Thomas
# @Version 1.0

# imports
import random
import time


# global utility functions


# this global functions gets the season number.txt which
# might be the most important digit to the program
def read_season_number():
    with open("season number.txt", "r") as contents:
        s = contents.readlines()
        return int(s[0])


# this exits an option
def exit_program():
    input("any key to exit: ")
    return


def read_individual_awards():
    for player in range(len(league_list)):
        league_list[player].read_awards()


# classes for the programs

# player class

class Player:

    # declare all class attributes, integers ratings of these attributes
    # the lst_... attributes represents the years they have won an award
    def __init__(self, name, consistency, takeover, explosiveness, threatening, big_play,
                 play_making, shot_tendency, range_tendency, draw_foul, block, steal, fg_percentage, g, ppg,
                 apg, orb, drb, bpg, spg, p, a, o, d, b, s, c, mvp, dpoy, opoy, pt, at, rt, st, bt, ct,
                 lst_mvp, lst_dpoy, lst_opoy, lst_pt, lst_at, lst_rt, lst_st, lst_bt, lst_ct):
        self.name = name
        self.consistency = consistency
        self.takeover = takeover
        self.shot_tendency = shot_tendency
        self.range_tendency = range_tendency
        self.explosiveness = explosiveness
        self.threatening = threatening
        self.big_play = big_play
        self.play_making = play_making
        self.draw_foul = draw_foul
        self.g = g
        self.block = block
        self.steal = steal
        self.fg_percentage = fg_percentage
        self.ppg = ppg
        self.apg = apg
        self.orb = orb
        self.drb = drb
        self.bpg = bpg
        self.spg = spg
        self.p = p
        self.a = a
        self.o = o
        self.d = d
        self.b = b
        self.s = s
        self.c = c
        self.mvp = mvp
        self.dpoy = dpoy
        self.opoy = opoy
        self.pt = pt
        self.at = at
        self.rt = rt
        self.st = st
        self.bt = bt
        self.ct = ct
        self.lst_mvp = lst_mvp
        self.lst_dpoy = lst_dpoy
        self.lst_opoy = lst_opoy
        self.lst_pt = lst_pt
        self.lst_at = lst_at
        self.lst_rt = lst_rt
        self.lst_st = lst_st
        self.lst_bt = lst_bt
        self.lst_ct = lst_ct

    def overall(self):
        return (self.takeover + self.explosiveness + self.threatening
                + self.big_play + self.play_making + self.draw_foul + self.block + self.steal) / 9

    def display_stats(self):

        # declare the empty string
        stats_string = ""

        # if there aren't any game played return N/A
        if self.g == 0:
            stats_string += self.name + " N/A"

        # otherwise, build the string
        else:
            stats_string += self.name + " G: " + str(self.g) + " PPG: " + str(self.p / self.g) + " APG: " + str(
                self.a / self.g) + " OPG: " + str(self.o / self.g) + " DPG: " + str(self.d / self.g) + " BPG: " + str(
                self.b / self.g) + " SPG: " + str(self.s / self.g) + " CPG: " + str(self.c / self.g) + " "
        print(stats_string)

    # this function creates a string of a players awards and years won for each stat
    def display_awards(self):
        print(self.name + "'s accolades")
        awards_str = ""
        awards_str += "MVP: " + str(self.mvp // 2) + " |" + str(list(set(self.lst_mvp))) + "| "
        awards_str += "DPOY: " + str(self.dpoy // 2) + " |" + str(list(set(self.lst_dpoy))) + "| "
        awards_str += "OPOY: " + str(self.opoy // 2) + " |" + str(list(set(self.lst_opoy))) + "| "
        awards_str += "Scoring Titles: " + str(self.pt // 2) + " |" + str(list(set(self.lst_pt))) + "| "
        awards_str += "Assist Titles: " + str(self.at // 2) + " |" + str(list(set(self.lst_at))) + "| "
        awards_str += "Rebound Titles: " + str(self.rt // 2) + " |" + str(list(set(self.lst_rt))) + "| "
        awards_str += "Steals Title: " + str(self.st // 2) + " |" + str(list(set(self.lst_st))) + "| "
        awards_str += "Blocks title: " + str(self.bt // 2) + " |" + str(list(set(self.lst_bt))) + "| "
        awards_str += "Contest titles: " + str(self.ct // 2) + " |" + str(list(set(self.lst_ct))) + "| "
        print(awards_str)

    # construct the string
    def write_awards(self):
        print_string = (self.name + " " + str(self.mvp) + " " + str(self.dpoy) + " " + str(self.opoy)
                        + " " + str(self.pt) + " " + str(self.at) + " " + str(self.rt) + " "
                        + str(self.st) + " " + str(self.bt) + " " + str(self.ct) + "\n")
        return print_string

    def find_awards_seasons(self):

        # loop each season
        for n in range(1, read_season_number()):

            # search each text file
            file = "seasonAwards" + str(n) + ".txt"
            with open(file, "r") as contents:

                # create a list of each line
                lst = contents.readlines()

                # loop through that list
                for element in range(len(lst)):

                    # split each line in the list
                    line_lst = lst[element].split(" ")

                    # count by 2 for each word in the line and if it
                    # equals name add the season number.txt to the list
                    if ''.join(line_lst[0]) + " " + ''.join(line_lst[1]) == self.name:
                        self.lst_mvp.append(n)
                    if ''.join(line_lst[2]) + " " + ''.join(line_lst[3]) == self.name:
                        self.lst_dpoy.append(n)
                    if ''.join(line_lst[4]) + " " + ''.join(line_lst[5]) == self.name:
                        self.lst_opoy.append(n)
                    if ''.join(line_lst[6]) + " " + ''.join(line_lst[7]) == self.name:
                        self.lst_pt.append(n)
                    if ''.join(line_lst[8]) + " " + ''.join(line_lst[9]) == self.name:
                        self.lst_at.append(n)
                    if ''.join(line_lst[10]) + " " + ''.join(line_lst[11]) == self.name:
                        self.lst_rt.append(n)
                    if ''.join(line_lst[12]) + " " + ''.join(line_lst[13]) == self.name:
                        self.lst_st.append(n)
                    if ''.join(line_lst[14]) + " " + ''.join(line_lst[15]) == self.name:
                        self.lst_bt.append(n)
                    if ''.join(line_lst[16]) + " " + ''.join(line_lst[17]) == self.name:
                        self.lst_ct.append(n)

    def read_awards(self):

        # open the text file
        with open("PlayerAccolades.txt", "r") as contents:

            # create a list of each line
            lst = contents.readlines()

            # if the list is 1 it's not valid then break out of the function
            if len(lst) == 1:
                return

            # loop through each line
            for line in range(len(lst)):

                # split each line by the delimiter
                here_lst = lst[line].split(" ")

                # if first 2 words equal the name it corresponds to the player
                if here_lst[0] + " " + here_lst[1] == self.name:

                    # line up text file delimitation to award counts
                    self.mvp = int(here_lst[2])
                    self.dpoy = int(here_lst[3])
                    self.opoy = int(here_lst[4])
                    self.pt = int(here_lst[5])
                    self.at = int(here_lst[6])
                    self.rt = int(here_lst[7])
                    self.st = int(here_lst[8])

                    # handles a specific bug
                    if here_lst[9] == "[]":
                        self.bt = int(0)
                        self.ct = int(0)
                    else:
                        self.bt = int(here_lst[9])
                        self.ct = int(here_lst[10])

    # reset all stats to 0
    def reset_stats(self):

        # reset every stat to 0
        self.g = 0
        self.p = 0
        self.a = 0
        self.o = 0
        self.d = 0
        self.b = 0
        self.s = 0
        self.c = 0


# team class
class Team:
    def __init__(self, name, roster, wins, losses, conference, games, rhc, championships, rhc_seasons,
                 championship_seasons):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.conference = conference
        self.games = games
        self.roster = roster
        self.rhc = rhc
        self.championships = championships
        self.championship_seasons = championship_seasons
        self.rhc_seasons = rhc_seasons

    def get_record_holders_cup_count(self):

        # loop through each season
        for season in range(1, read_season_number()):

            # declare a text file and open it
            file = "seasonAwards" + str(season) + ".txt"
            with open(file, "r") as contents:

                # get the text content and split each line into a list
                body = contents.readline()
                lst = body.split(" ")

                # if the very last "word" that means that the team won the rhc that year
                if lst[-1][:-1] == self.name:
                    self.rhc += 1
                    self.rhc_seasons.append(season)

    # this function is the same idea as the function above
    def get_team_championship_count(self):
        for i in range(1, read_season_number()):
            file = "seasonAwards" + str(i) + ".txt"
            with open(file, "r") as contents:
                body = contents.readline()
                lst = body.split(" ")
                if lst[-2] == self.name:
                    self.championships += 1
                    self.championship_seasons.append(i)

    def display_championships(self):
        self.get_team_championship_count()
        print("Championships: " + self.name + ":", str(len(set(self.championship_seasons))), self.championship_seasons)

    def display_rhcs(self):
        self.get_record_holders_cup_count()
        print("Record Holders cups: " + self.name + ":", str(len(set(self.rhc_seasons))), self.rhc_seasons)

    def display_awards(self):
        self.display_championships()
        self.display_rhcs()

    def reset_team_stats(self):
        self.wins = 0
        self.losses = 0
        self.games = 0

    def overall(self):

        # set the overall counter
        overall = 0

        # loop through each player in the roster and add there overall
        for player in range(len(self.roster)):
            overall += self.roster[player].overall()

        # find and return the average overall
        overall = overall / len(self.roster)
        return overall

    def print_roster(self):

        # initial message
        print_string = self.name + "'s roster" + "\n"

        # build and return the string
        for team in range(len(self.roster)):
            print_string += (self.roster[team].name + " " + str(self.roster[team].overall()) + "\n")
        return print_string


# season class
def write_season_number(number):
    with open("season number.txt", "w") as contents:
        contents.write(str(number))


class Season:
    def __init__(self, schedule, teams, standings_east, standingsWest, allKBL, mvp, opoy, dpoy, mip, champion, number,
                 pt, at, rt, st, bt, ct, record_holders_cup):
        self.schedule = schedule
        self.teams = teams
        self.standings_east = standings_east
        self.standings_west = standingsWest
        self.allKBL = allKBL
        self.mvp = mvp
        self.dpoy = dpoy
        self.opoy = opoy
        self.mip = mip
        self.pt = pt
        self.at = at
        self.rt = rt
        self.st = st
        self.bt = bt
        self.ct = ct
        self.champion = champion
        self.number = number
        self.record_holders_cup = record_holders_cup

    def handle_awards(self):
        print("your record holders cup champion is: " + Season1.determine_record_holders_cup().name)
        print("your MVP is: ", self.determine_mvp().name)
        print("your DPOY is: ", self.determine_dpoy().name)
        print("your OPOY is: ", self.determine_opoy().name)
        print("Your scoring champ is: ", self.determine_scoring_champion().name)
        print("Your assist champ is: ", self.determine_assist_champion().name)
        print("Your rebound champ is: ", self.determine_rebound_champion().name)
        print("Your steals champ is: ", self.determine_steal_champion().name)
        print("Your blocks champ is: ", self.determine_block_champion().name)
        print("Your contest champ is: ", self.determine_contest_champion().name)

    def determine_record_holders_cup(self):
        win_count = boston.wins
        cup_holders_index = 0
        for i in range(len(self.teams)):
            if self.teams[i].wins > win_count:
                win_count = self.teams[i].wins
                cup_holders_index = i
        self.teams[cup_holders_index].rhc += 1
        self.record_holders_cup = self.teams[cup_holders_index]
        return self.teams[cup_holders_index]

    def new_season(self):
        self.write_season_awards()
        season_string = ""
        for i in range(len(self.teams)):
            self.teams[i].reset_team_stats()
            for j in range(len(self.teams[i].roster)):
                self.teams[i].roster[j].reset_stats()
                season_string += self.teams[i].roster[j].write_awards()
        with open("playerAccolades.txt", "w") as contents:
            contents.write(season_string)

    def save_player_awards(self):
        player_awards_string = ""
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].roster)):
                player_awards_string += self.teams[i].roster[j].write_awards()
        with open("playerAccolades.txt", "w") as contents:
            contents.write(player_awards_string)

    def write_season_awards(self):
        n = "seasonAwards" + str(self.number) + ".txt"
        season_awards_string = (self.mvp.name + " " + self.dpoy.name + " " + self.opoy.name + " "
                                + self.pt.name + " " + self.at.name + " " + self.rt.name + " " +
                                self.st.name + " " + self.bt.name + " " + self.ct.name + " " +
                                self.champion.name + " " + self.record_holders_cup.name + "\n")
        with open(n, "w") as contents:
            contents.write(season_awards_string)

    def read_team_awards(self):
        for i in range(len(self.teams)):
            self.teams[i].get_team_championship_count()
            self.teams[i].get_record_holders_cup_count()

    def read_season_awards(self):

        # open the file
        n = "seasonAwards" + str(self.number) + ".txt"
        with open(n, "r") as contents:
            # make the contents a list
            lst = contents.readlines()

            # loop through the content
            for i in range(len(lst)):
                # make each line a list
                lines_lst = lst[i].split(" ")

                # set all the values to a string
                self.mvp = ''.join(lines_lst[0]) + " " + ''.join(lines_lst[1])
                self.dpoy = ''.join(lines_lst[2]) + " " + ''.join(lines_lst[3])
                self.opoy = ''.join(lines_lst[4]) + " " + ''.join(lines_lst[5])
                self.pt = ''.join(lines_lst[6]) + " " + ''.join(lines_lst[7])
                self.at = ''.join(lines_lst[8]) + " " + ''.join(lines_lst[9])
                self.rt = ''.join(lines_lst[10]) + " " + ''.join(lines_lst[11])
                self.st = ''.join(lines_lst[12]) + " " + ''.join(lines_lst[13])
                self.bt = ''.join(lines_lst[14]) + " " + ''.join(lines_lst[15])
                self.ct = ''.join(lines_lst[16]) + " " + ''.join(lines_lst[17])
                self.champion = ''.join(lines_lst[-2])
                self.record_holders_cup = ''.join(lines_lst[-1])

    def display_season_awards(self):
        season_awards_string = (self.mvp + " " + self.dpoy +
                                " " + " " + self.opoy + " " + self.pt +
                                " " + self.at + " " + self.rt + " " +
                                self.st + " " + self.bt + " " + self.ct
                                + " " + self.champion + " " + self.record_holders_cup)
        print(season_awards_string)

    # all the determine_x award functions do the same thing they take
    # the stats and whoever has the most stats wins the awards
    def determine_mvp(self):
        x = 0
        y = 0
        toBeat = self.teams[0].roster[0].c + self.teams[0].roster[0].s + self.teams[0].roster[0].b + \
                 self.teams[0].roster[0].d + self.teams[0].roster[0].p + self.teams[0].roster[0].a + \
                 self.teams[0].roster[0].o
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].roster)):
                total = self.teams[i].roster[j].c + self.teams[i].roster[j].s + self.teams[i].roster[j].b + \
                        self.teams[i].roster[j].d + self.teams[i].roster[j].p + self.teams[i].roster[j].a + \
                        self.teams[i].roster[j].o
                if total > toBeat:
                    toBeat = total
                    x = i
                    y = j
        self.mvp = self.teams[x].roster[y]
        self.teams[x].roster[y].mvp += 1
        self.teams[x].roster[y].lst_mvp.append(read_season_number())
        return self.mvp

    def determine_dpoy(self):
        x = 0
        y = 0
        toBeat = self.teams[0].roster[0].c + self.teams[0].roster[0].s + self.teams[0].roster[0].b + \
                 self.teams[0].roster[0].d + self.teams[0].roster[0].p + self.teams[0].roster[0].a + \
                 self.teams[0].roster[0].o
        self.dpoy = self.teams[0].roster[0]
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].roster)):
                total = self.teams[i].roster[j].c + self.teams[i].roster[j].s + self.teams[i].roster[j].b + \
                        self.teams[i].roster[j].d
                if total > toBeat:
                    toBeat = total
                    self.dpoy = self.teams[i].roster[j]
                    x = i
                    y = j
        self.teams[x].roster[y].dpoy += 1
        self.dpoy = self.teams[x].roster[y]
        self.teams[x].roster[y].lst_dpoy.append(read_season_number())
        return self.dpoy

    def determine_opoy(self):
        x = 0
        y = 0
        toBeat = self.teams[0].roster[0].p + self.teams[0].roster[0].a + self.teams[0].roster[0].o
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].roster)):
                total = self.teams[i].roster[j].p + self.teams[i].roster[j].a + self.teams[i].roster[j].o
                if total > toBeat:
                    toBeat = total
                    x = i
                    y = j
        self.teams[x].roster[y].opoy += 1
        self.opoy = self.teams[x].roster[y]
        self.teams[x].roster[y].lst_opoy.append(read_season_number())
        return self.opoy

    def determine_scoring_champion(self):
        x = 0
        y = 0
        toBeat = self.teams[0].roster[0].p
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].roster)):
                total = self.teams[i].roster[j].p
                if total > toBeat:
                    toBeat = total
                    x = i
                    y = j
        self.teams[x].roster[y].pt += 1
        self.pt = self.teams[x].roster[y]
        self.teams[x].roster[y].lst_pt.append(read_season_number())
        return self.pt

    def determine_assist_champion(self):
        x = 0
        y = 0
        toBeat = self.teams[0].roster[0].a
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].roster)):
                total = self.teams[i].roster[j].a
                if total > toBeat:
                    toBeat = total
                    x = i
                    y = j
        self.teams[x].roster[y].at += 1
        self.at = self.teams[x].roster[y]
        self.teams[x].roster[y].lst_at.append(read_season_number())
        return self.at

    def determine_rebound_champion(self):
        x = 0
        y = 0
        toBeat = self.teams[0].roster[0].o + self.teams[0].roster[0].d
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].roster)):
                total = self.teams[i].roster[j].o + self.teams[i].roster[j].d
                if total > toBeat:
                    toBeat = total
                    x = i
                    y = j
        self.teams[x].roster[y].rt += 1
        self.rt = self.teams[x].roster[y]
        self.teams[x].roster[y].lst_rt.append(read_season_number())
        return self.rt

    def determine_steal_champion(self):
        x = 0
        y = 0
        toBeat = self.teams[0].roster[0].s
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].roster)):
                total = self.teams[i].roster[j].s
                if total > toBeat:
                    toBeat = total
                    x = i
                    y = j
        self.teams[x].roster[y].st += 1
        self.st = self.teams[x].roster[y]
        self.teams[x].roster[y].lst_st.append(read_season_number())
        return self.st

    def determine_block_champion(self):
        x = 0
        y = 0
        toBeat = self.teams[0].roster[0].b
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].roster)):
                total = self.teams[i].roster[j].b
                if total > toBeat:
                    toBeat = total
                    x = i
                    y = j
        self.teams[x].roster[y].bt += 1
        self.bt = self.teams[x].roster[y]
        self.teams[x].roster[y].lst_bt.append(read_season_number())
        return self.bt

    def determine_contest_champion(self):
        x = 0
        y = 0
        toBeat = self.teams[0].roster[0].c
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].roster)):
                total = self.teams[i].roster[j].c
                if total > toBeat:
                    toBeat = total
                    x = i
                    y = j
        self.ct = self.teams[x].roster[y]
        self.teams[x].roster[y].ct += 1
        self.teams[x].roster[y].lst_ct.append(read_season_number())
        return self.ct

    def get_champion(self, champ):
        self.champion = champ

    def display_stats(self):

        # print the title
        print("Season " + str(self.number) + " stats")

        # loop through each team
        for team in range(len(team_lst)):

            # show the head for each team
            print("Stats for", team_lst[team].name)

            # loop through each player
            for player in range(len(team_lst[team].roster)):
                # display the stat of each player
                team_lst[team].roster[player].display_stats()

    def display_standings(self):

        # make the standing are ordered
        self.standings_order()

        # declare the heading
        print("Season:", self.number, "standings")
        print("Eastern Conference:")

        # print the standings
        for team_iteration in range(3):
            team = self.standings_east[team_iteration][1]
            if team.games == 0:
                print(str(1 + team_iteration) + ".", team.name, "GP:", team.games, " Wins:", team.wins,
                      " Losses:", team.losses, " Percentage: ", "N/A")
            else:
                print(str(1 + team_iteration) + ".", team.name, "GP:", team.games, " Wins:", team.wins,
                      " Losses:", team.losses, " Percentage:", team.wins / team.games)

        # header
        print("Western Conference:")

        # declare the team
        for team_iteration in range(3):
            team = self.standings_west[team_iteration][1]
            if team.games == 0:
                print(team_iteration + 1, ".", team.name, "GP:", team.games, " Wins:", team.wins,
                      " Losses:", team.losses, " Percentage: ", "N/A")
            else:
                print(team_iteration + 1, ".", team.name, "GP:", team.games, " Wins:", team.wins,
                      " Losses:", team.losses, " Percentage:", team.wins / team.games)

    def generate_schedule(self):

        # loop through each team and compare each
        # team as long as they are not the same
        for home_team in range(len(self.teams)):
            for road_team in range(len(self.teams)):
                if home_team != road_team:

                    # add the appropriate amount of games between the road and home teams
                    if self.teams[home_team].conference == self.teams[road_team].conference:
                        lst = []
                        for game in range(12):
                            lst.append((self.teams[home_team], self.teams[road_team]))
                        self.schedule.append(lst)
                    else:
                        lst = []
                        for game in range(6):
                            lst.append((self.teams[home_team], self.teams[road_team]))
                        self.schedule.append(lst)

        lst = []

        # placeholder to replace schedule
        place_holder_schedule = []

        # set up the list with the numbers 0 to 29
        nums = []
        for home_team in range(0, 30):
            nums.append(home_team)

        # mix the schedule up
        while len(nums) > 0:
            number = random.randint(0, len(nums) - 1)
            lst.append(nums[number])
            nums.remove(nums[number])
        for home_team in range(len(lst)):
            place_holder_schedule.append(self.schedule[lst[home_team]])
        self.schedule = place_holder_schedule

        # save the schedule to a text file
        name = "Schedule" + str(self.number) + ".txt"
        with open(name, 'w') as file:
            for home_team in range(len(self.schedule)):
                for road_team in range(len(self.schedule[home_team])):
                    file.write(
                        self.schedule[home_team][road_team][0].name + " vs " + self.schedule[home_team][road_team][
                            1].name + "\n")
        file.close()

    def display_schedule(self, game_index):

        # find how many games in we are and print from the game_index
        Index = 0
        for game_group in range(len(self.schedule)):
            for game in range(len(self.schedule[game_set])):
                if Index < game_index:
                    Index += 1
                else:
                    Index += 1
                    print(self.schedule[game_set][game][0].name + " vs " + self.schedule[game_set][game][1].name)

    def write_stats(self):
        stats_string = ""
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].roster)):
                player = self.teams[i].roster[j]
                if player.g == 0:
                    stats_string += "N/A" + "\n"
                else:
                    stats_string += " G: " + str(player.g) + " PPG: " + str(player.p / player.g) + " APG: " + str(
                        player.a / player.g) + " OPG: " + str(player.o / player.g) + " DPG: " + str(
                        player.d / player.g) + " BPG: " + str(player.b / player.g) + " SPG: " + str(
                        player.s / player.g) + " CPG: " + str(player.c / player.g) + "\n"
        name = "stats" + str(self.number) + ".txt"
        with open(name, "w") as contents:
            contents.write(stats_string)

    def read_stats(self, player):

        # try to open the file
        name = "stats" + str(self.number) + ".txt"
        try:
            with open(name, "r") as file:

                # take the contents and make it a list of lines than
                contents = file.readlines()

                # make each line a list of words
                lt = [line.strip() for line in contents]

                # loop through each line
                for j in range(len(lt)):

                    # split each line and make each piece of data a float
                    line_data = lt[j].split(" ")
                    if line_data[0] != "N/A":
                        player[j].g = int(line_data[1])
                        player[j].p = float(line_data[3]) * player[j].g
                        player[j].a = float(line_data[5]) * player[j].g
                        player[j].o = float(line_data[7]) * player[j].g
                        player[j].d = float(line_data[9]) * player[j].g
                        player[j].b = float(line_data[11]) * player[j].g
                        player[j].s = float(line_data[13]) * player[j].g
                        player[j].c = float(line_data[15]) * player[j].g

        except FileNotFoundError:
            return

    def write_standings(self):

        # exact same as display_standings()
        # except we add the data to a string
        # then we write it to a file
        self.standings_order()
        collection_string = ""
        collection_string += "Season " + str(self.number) + ": " + " standings" + " \n"
        collection_string += "Eastern Conference:" + "\n"
        for teams in range(3):
            team = self.standings_east[teams][1]
            if team.games == 0:
                collection_string += str(teams + 1) + ". " + str(team.name) + " GP: " + str(
                    team.games) + " Wins: " + str(
                    team.wins) + " Losses: " + str(team.losses) + " Percentage: " + " N/A " + " \n" + "e"
            else:
                collection_string += str(teams + 1) + ". " + str(team.name) + " GP: " + str(
                    team.games) + " Wins: " + str(
                    team.wins) + " Losses: " + str(team.losses) + " Percentage: " + str(
                    team.wins / team.games) + " \n"

        collection_string += "Western Conference: \n"
        for teams in range(3):
            team = self.standings_west[teams][1]
            if team.games == 0:
                collection_string += str(teams + 1) + ". " + str(team.name) + " GP: " + str(
                    team.games) + " Wins: " + str(
                    team.wins) + " Losses: " + str(team.losses) + " Percentage: " + " N/A " + " \n" + "w"
            else:
                collection_string += str(teams + 1) + ". " + str(team.name) + " GP: " + str(
                    team.games) + " Wins: " + str(
                    team.wins) + " Losses: " + str(team.losses) + " Percentage: " + str(
                    team.wins / team.games) + " \n"
        standing = "standings" + str(self.number) + ".txt"
        with open(standing, "w") as file:
            file.write(collection_string)

    def read_standings(self):
        try:
            name = "standings" + str(self.number) + ".txt"
            with open(name, "r") as file:

                # create a list of each team
                contents = file.readlines()
                lt = [line.strip() for line in contents]

                # get each teams stats
                lst = lt[2:5] + lt[6:]

                # list to gather how many games each team has won
                wins_games_east = []
                wins_games_west = []

                # loop through each team in the teams list and each set of team stats
                for team in range(len(self.teams)):
                    for team_stats in range(len(lst)):

                        # if the teams are in the first 3 they are in the east so act appropriately
                        if self.teams[team].name in lst[team_stats] and team_stats < len(team_lst) / 2:
                            for comparison_team in range(len(self.teams)):
                                if self.teams[comparison_team].name == self.teams[team].name:
                                    # split the list and extract and add the necessary data to the master list
                                    team_data = lst[team_stats].split(" ")
                                    wins_games_east.append([int(team_data[3]), int(team_data[5])])
                                    self.standings_east.append(self.teams[team])

                        # do the same thing for the west
                        elif self.teams[team].name in lst[team_stats] and team_stats >= len(team_lst) / 2:
                            for comparison_team in range(len(self.teams)):
                                if self.teams[comparison_team].name == self.teams[team].name:
                                    team_data = lst[team_stats].split(" ")
                                    wins_games_west.append([int(team_data[3]), int(team_data[5])])
                                    self.standings_west.append(self.teams[team])

            # loop through wins for east and west
            total = 0
            for team in range(len(wins_games_east)):
                # extract the games played, won and lost for
                # each team east and west of same index
                self.standings_east[team].games = wins_games_east[team][0]
                total += wins_games_east[team][0]
                self.standings_east[team].wins = wins_games_east[team][1]
                self.standings_east[team].losses = abs(wins_games_east[team][0] - wins_games_east[team][1])
                self.standings_west[team].games = wins_games_west[team][0]
                total += wins_games_west[team][0]
                self.standings_west[team].wins = wins_games_west[team][1]
                self.standings_west[team].losses = abs(wins_games_west[team][0] - wins_games_west[team][1])

            # return the amount of game that have been played
            # in the season // 2 because it always gives 2
            return total // 2

        # if the file doesn't exist return 0
        except FileNotFoundError:
            return 0

    def determine_all_kbl_team(self):
        x = 0
        team_collection = []
        allStars = []
        for i in range(len(self.teams)):
            for j in range(len(self.teams[i].roster)):
                team_collection.append(self.teams[i].roster[j])
        while len(allStars) < 10:
            toBeat = (team_collection[0].c + team_collection[0].s + team_collection[0].b +
                      team_collection[0].d +
                      team_collection[0].p + team_collection[0].a + team_collection[0].o)
            MVP = team_collection[0]
            for i in range(len(team_collection)):
                total = (team_collection[i].c + team_collection[i].s + team_collection[i].b +
                         team_collection[i].d + team_collection[i].p + team_collection[i].a +
                         team_collection[i].o)
                if total > toBeat:
                    toBeat = total
                    x = i
                    MVP = team_collection[i]
            allStars.append(team_collection[x])
            self.allKBL.append(team_collection[x])
            team_collection.remove(MVP)
        return allStars

    def load_schedule(self):

        # collection containers
        lst1 = []
        lst2 = []
        names = []
        cities = []

        # collect the team name
        for team_name in range(len(self.teams)):
            cities.append(self.teams[team_name].name)

        # read in the schedule data
        file = "Schedule" + str(self.number) + ".txt"
        with open(file, "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(" ")
                names.append([data[0], data[2]])

        # add each match
        for match in range(len(names) - 1):
            lst1.append(names[match])

            # if the next match does not equal the current match
            # add copy of list 1 to lst 2 make sure lst 1 is empty
            if names[match] != names[match + 1] or match == len(names) - 2:
                lst2.append(lst1.copy())
                lst1 = []

        # handle the bug exception
        lst2[-1].append(names[-1])

        # loop through each game and teams and add it to the schedule
        for match_set in range(len(lst2)):
            for game in range(len(lst2[match_set])):
                for team in range(len(cities)):
                    if lst2[match_set][game][0] == cities[team]:
                        lst2[match_set][game][0] = self.teams[team]
                    elif lst2[match_set][game][1] == cities[team]:
                        lst2[match_set][game][1] = self.teams[team]

        # make list 2 the new schedule
        self.schedule = lst2

    def standings_order(self):

        # make sure to empty the current list and declare the new list
        east_substitute = []
        west_substitute = []
        self.standings_east.clear()
        self.standings_west.clear()

        # add each teams win percentage and handle exceptions

        # east teams
        for teams in range(3):
            team = self.teams[teams]
            if team.games == 0:
                east_substitute.append([0, team])
            else:
                east_substitute.append([team.wins / team.games, team])

        # west teams
        for teams in range(3, 6):
            team = self.teams[teams]
            if team.games == 0:
                west_substitute.append([0, team])
            else:
                west_substitute.append([team.wins / team.games, team])

        # get the list in the correct order and set
        # the substitute to the actual class attribute
        self.standings_east = sorted(east_substitute, key=lambda x: x[0], reverse=True)
        self.standings_west = sorted(west_substitute, key=lambda x: x[0], reverse=True)


# game class
class Game:
    def __init__(self, home_team, road_team, home_team_score, road_team_score):
        self.current_offense = None
        self.home_team = home_team
        self.road_team = road_team
        self.home_team_score = home_team_score
        self.road_team_score = road_team_score

    def display_score(self):
        print(self.home_team.name, " ", self.home_team_score, " ", self.road_team.name, " ", self.road_team_score)

    def run_game(self):

        # loop 200 possessions if 1 team scores the other team gets the ball repeat 200 times
        possessions = 0
        current_offense = self.home_team
        while possessions <= 200:
            if current_offense == self.home_team:
                current_offense_scored = self.home_team_offense()
                current_offense = self.road_team if current_offense_scored else self.home_team
            else:
                current_offense_scored = self.road_team_offense()
                current_offense = self.home_team if current_offense_scored else self.road_team

            # add each possession
            possessions += 1
            self.display_score()
            time.sleep(0.5)

        # decide who won
        if self.home_team_score > self.road_team_score:
            return self.home_team
        elif self.home_team_score < self.road_team_score:
            return self.road_team
        else:
            return self.home_team

    def simulate_game(self):
        possessions = 0
        current_offense = self.road_team
        while possessions <= 200:
            if current_offense == self.home_team:
                current_offense_scored = self.home_team_offense_sim()
                current_offense = self.road_team if current_offense_scored else self.home_team
            else:
                current_offense_scored = self.road_team_offense_sim()
                current_offense = self.home_team if current_offense_scored else self.road_team
            possessions += 1
        if self.home_team_score > self.road_team_score:
            return self.home_team
        elif self.home_team_score < self.road_team_score:
            return self.road_team
        else:
            return self.home_team

    def home_team_offense(self):
        player = None
        tracker = 0
        divs = []
        index = 0
        for i in range(len(self.home_team.roster)):
            divs.append(int(tracker))
            tracker += int(self.home_team.roster[i].shot_tendency)
        select_player = random.randint(1, tracker)
        for i in range(len(divs)):
            if select_player < divs[i]:
                player = self.home_team.roster[i]
                index = i
                break
        if player is None:
            player = self.home_team.roster[-1]
        shotChance = player.range_tendency
        Steal = 3
        StealOdds = random.randint(1, 20)
        if Steal == StealOdds:
            player_5 = None
            tracker5 = 0
            divs5 = []
            index5 = 0
            for i in range(len(self.road_team.roster)):
                divs5.append(int(tracker5))
                tracker5 += int(self.road_team.roster[i].steal)
            select_player2 = random.randint(1, tracker5)
            for i in range(len(divs5)):
                if select_player2 < divs5[i]:
                    player_5 = self.road_team.roster[i]
                    index5 = i
                    break
            if player_5 is None:
                index5 = 0
            self.road_team.roster[index5].s += 1
            print(self.road_team.roster[index5].name, "Steals it")
            return True
        player_6 = None
        tracker6 = 0
        divs6 = []
        index6 = 0
        for i in range(len(self.road_team.roster)):
            divs6.append(int(tracker6))
            tracker6 += int(self.road_team.roster[i].draw_foul)
        select_player2 = random.randint(1, tracker6)
        for i in range(len(divs6)):
            if select_player2 < divs6[i]:
                player_6 = self.road_team.roster[i]
                index6 = i
                break
        if player_6 is None:
            player_6 = self.road_team.roster[0]
            index6 = 0
        odds = random.randint(1, tracker6)
        self.road_team.roster[index6].c += 1

        if odds < shotChance:
            shotValue = 3
            add = player.consistency + player.takeover + player.explosiveness
            add //= (len(self.home_team.roster) * 2) * 2
            divisor = random.randint(1, 101)
            block = random.randint(1, 100)
            block_odds = 3
            if block == block_odds:
                Player4 = None
                tracker4 = 0
                divs4 = []
                index4 = 0
                for i in range(len(self.road_team.roster)):
                    divs4.append(int(tracker4))
                    tracker4 += int(self.road_team.roster[i].block)
                select_player2 = random.randint(1, tracker4)
                for i in range(len(divs4)):
                    if select_player2 < divs4[i] and i != index:
                        Player4 = self.road_team.roster[i]
                        index4 = i
                        break
                if Player4 is None:
                    Player4 = self.road_team.roster[0]
                    index4 = 0
                print(player.name, "three pointer is blocked by", Player4.name)
                self.road_team.roster[index4].b += 1
                return False

            if divisor < add + 75:
                index3 = 0
                Player3 = None
                tracker3 = 0
                divs3 = []
                for i in range(len(self.home_team.roster)):
                    divs3.append(tracker3)
                    tracker3 += int(self.home_team.roster[i].play_making)
                select_player = random.randint(1, tracker3)
                for i in range(len(divs3)):
                    if select_player < divs3[i]:
                        Player3 = self.home_team.roster[i]
                        index3 = i
                        break
                if Player3 is None:
                    Player3 = self.home_team.roster[-1]
                    index3 = 0
                if Player3 != player:
                    self.home_team.roster[index3].a += 1
                    print(player.name, "For Three! Assisted by", Player3.name, "Contested by", player_6.name)
                    self.home_team_score += shotValue
                    self.home_team.roster[index].p += shotValue
                else:
                    print(player.name, "For Three! Contested by", player_6.name)
                    self.home_team_score += shotValue
                    self.home_team.roster[index].p += shotValue
                return True
            else:
                total = 0
                print(player.name, "no good from three", "Contested by", player_6.name)
                for i in range(len(self.home_team.roster)):
                    total += self.home_team.roster[i].drb
                reboundChance = total // len(self.home_team.roster) * .75
                odds = random.randint(1, 21)
                if odds > reboundChance:
                    index2 = 0
                    Player2 = None
                    tracker2 = 0
                    divs2 = []
                    for i in range(len(self.home_team.roster)):
                        divs2.append(tracker2)
                        tracker2 += int(self.home_team.roster[i].draw_foul)
                    select_player = random.randint(1, tracker2)
                    for i in range(len(divs2)):
                        if select_player < divs2[i]:
                            Player2 = self.home_team.roster[i]
                            index2 = i
                            break
                    if Player2 is None:
                        index2 = 0
                    self.home_team.roster[index2].o += 1
                    print("Offensive rebound secured by", self.home_team.roster[index2].name)
                    return False
                else:
                    Player2 = None
                    tracker2 = 0
                    divs2 = []
                    index2 = 0
                    for i in range(len(self.road_team.roster)):
                        divs2.append(tracker2)
                        tracker2 += int(self.road_team.roster[i].draw_foul)
                    select_player = random.randint(1, tracker2)
                    for i in range(len(divs2)):
                        if select_player < divs2[i]:
                            Player2 = self.road_team.roster[i]
                            index2 = i
                            break
                    if Player2 is None:
                        index2 = 0
                    self.road_team.roster[index2].d += 1
                    print("Defensive rebound secured by", self.road_team.roster[index2].name)
                    return True
        else:
            shotValue = 2
            add = player.consistency + player.takeover + player.explosiveness
            add //= (len(self.home_team.roster) * 3)
            divisor = random.randint(1, 101)
            block = random.randint(1, 20)
            block_odds = 3
            if block == block_odds:
                Player4 = None
                tracker4 = 0
                divs4 = []
                index4 = 0
                for i in range(len(self.home_team.roster)):
                    divs4.append(int(tracker4))
                    tracker4 += int(self.home_team.roster[i].block)
                select_player2 = random.randint(1, tracker4)
                for i in range(len(divs4)):
                    if select_player2 < divs4[i] and i != index:
                        Player4 = self.home_team.roster[i]
                        index4 = i
                        break
                if Player4 is None:
                    Player4 = self.home_team.roster[0]
                    index4 = 0
                print(player.name, "two pointer is blocked by", Player4.name)
                self.home_team.roster[index4].b += 1
                return False
            if divisor < add + 75:
                index3 = 0
                Player3 = None
                tracker3 = 0
                divs3 = []
                for i in range(len(self.home_team.roster)):
                    divs3.append(tracker3)
                    tracker3 += int(self.home_team.roster[i].play_making)
                select_player = random.randint(1, tracker3)
                for i in range(len(divs3)):
                    if select_player < divs3[i]:
                        Player3 = self.home_team.roster[i]
                        index3 = i
                        break
                if Player3 is None:
                    Player3 = self.home_team.roster[-1]
                    index3 = 0
                if Player3 != player:
                    self.home_team.roster[index3].a += 1
                    print(player.name, "For Two! Assisted by", Player3.name, "Contested by", player_6.name)
                    self.home_team_score += shotValue
                    self.home_team.roster[index].p += shotValue
                else:
                    print(player.name, "For two! Contested by", player_6.name)
                    self.home_team_score += shotValue
                    self.home_team.roster[index].p += shotValue
                return True
            else:
                total = 0
                print(player.name, "no good from two", "Contested by", player_6.name)
                for i in range(len(self.home_team.roster)):
                    total += self.home_team.roster[i].drb
                reboundChance = total // len(self.home_team.roster) * .5
                odds = random.randint(1, 21)
                if odds > reboundChance:
                    index2 = 0
                    Player2 = None
                    tracker2 = 0
                    divs2 = []
                    for i in range(len(self.road_team.roster)):
                        divs2.append(tracker2)
                        tracker2 += int(self.road_team.roster[i].draw_foul)
                    select_player = random.randint(1, tracker2)
                    for i in range(len(divs2)):
                        if select_player < divs2[i]:
                            Player2 = self.road_team.roster[i]
                            index2 = i
                            break
                    if Player2 is None:
                        index2 = 0
                    self.road_team.roster[index2].d += 1
                    print("Defensive rebound secured by", self.road_team.roster[index2].name)
                    return True
                else:
                    index2 = 0
                    Player2 = None
                    tracker2 = 0
                    divs2 = []
                    for i in range(len(self.home_team.roster)):
                        divs2.append(tracker2)
                        tracker2 += int(self.home_team.roster[i].draw_foul)
                    select_player = random.randint(1, tracker2)
                    for i in range(len(divs2)):
                        if select_player < divs2[i]:
                            Player2 = self.home_team.roster[i]
                            index2 = i
                            break
                    if Player2 is None:
                        index2 = 0
                    self.home_team.roster[index2].o += 1
                    print("Offensive rebound secured by", self.home_team.roster[index2].name)
                    return False

    def home_team_offense_sim(self):
        player = None
        tracker = 0
        divs = []
        index = 0
        for i in range(len(self.home_team.roster)):
            divs.append(int(tracker))
            tracker += int(self.home_team.roster[i].shot_tendency)
        select_player = random.randint(1, tracker)
        for i in range(len(divs)):
            if select_player < divs[i]:
                player = self.home_team.roster[i]
                index = i
                break
        if player is None:
            player = self.home_team.roster[-1]
        shot_chance = player.range_tendency
        steal = 3
        steal_odds = random.randint(1, 20)
        if steal == steal_odds:
            player_5 = None
            tracker_5 = 0
            divs_5 = []
            index_5 = 0
            for i in range(len(self.road_team.roster)):
                divs_5.append(int(tracker_5))
                tracker_5 += int(self.road_team.roster[i].steal)
            select_player_2 = random.randint(1, tracker_5)
            for i in range(len(divs_5)):
                if select_player_2 < divs_5[i]:
                    player_5 = self.road_team.roster[i]
                    index_5 = i
                    break
            if player_5 is None:
                index_5 = 0
            self.road_team.roster[index_5].s += 1
            return True
        player_6 = None
        tracker_6 = 0
        divs_6 = []
        index_6 = 0
        for i in range(len(self.road_team.roster)):
            divs_6.append(int(tracker_6))
            tracker_6 += int(self.road_team.roster[i].draw_foul)
        select_player_2 = random.randint(1, tracker_6)
        for i in range(len(divs_6)):
            if select_player_2 < divs_6[i]:
                player_6 = self.road_team.roster[i]
                index_6 = i
                break
        if player_6 is None:
            index_6 = 0
        odds = random.randint(1, tracker_6)
        self.road_team.roster[index_6].c += 1

        if odds < shot_chance:
            shot_value = 3
            add = player.threatening + player.big_play
            add //= (len(self.home_team.roster) * 2) * 2
            divisor = random.randint(1, 101)
            block = random.randint(1, 100)
            block_odds = 3
            if block == block_odds:
                player_4 = None
                tracker_4 = 0
                divs_4 = []
                index_4 = 0
                for i in range(len(self.road_team.roster)):
                    divs_4.append(int(tracker_4))
                    tracker_4 += int(self.road_team.roster[i].block)
                select_player_2 = random.randint(1, tracker_4)
                for i in range(len(divs_4)):
                    if select_player_2 < divs_4[i] and i != index:
                        player_4 = self.road_team.roster[i]
                        index_4 = i
                        break
                if player_4 is None:
                    index_4 = 0
                self.road_team.roster[index_4].b += 1
                return False
            if divisor < add + 75:
                index_3 = 0
                player_3 = None
                tracker_3 = 0
                divs_3 = []
                for i in range(len(self.home_team.roster)):
                    divs_3.append(tracker_3)
                    tracker_3 += int(self.home_team.roster[i].play_making)
                select_player = random.randint(1, tracker_3)
                for i in range(len(divs_3)):
                    if select_player < divs_3[i]:
                        player_3 = self.home_team.roster[i]
                        index_3 = i
                        break
                if player_3 is None:
                    player_3 = self.home_team.roster[-1]
                    index_3 = 0
                if player_3 != player:
                    self.home_team.roster[index_3].a += 1
                    self.home_team_score += shot_value
                    self.home_team.roster[index].p += shot_value
                else:
                    self.home_team_score += shot_value
                    self.home_team.roster[index].p += shot_value
                return True
            else:
                total = 0
                for i in range(len(self.home_team.roster)):
                    total += self.home_team.roster[i].drb
                rebound_chance = total // len(self.home_team.roster) * .75
                odds = random.randint(1, 21)
                if odds > rebound_chance:
                    index_2 = 0
                    player_2 = None
                    tracker_2 = 0
                    divs_2 = []
                    for i in range(len(self.home_team.roster)):
                        divs_2.append(tracker_2)
                        tracker_2 += int(self.home_team.roster[i].draw_foul)
                    select_player = random.randint(1, tracker_2)
                    for i in range(len(divs_2)):
                        if select_player < divs_2[i]:
                            player_2 = self.home_team.roster[i]
                            index_2 = i
                            break
                    if player_2 is None:
                        index_2 = 0
                    self.home_team.roster[index_2].o += 1
                    return False
                else:
                    player_2 = None
                    tracker_2 = 0
                    divs_2 = []
                    index_2 = 0
                    for i in range(len(self.road_team.roster)):
                        divs_2.append(tracker_2)
                        tracker_2 += int(self.road_team.roster[i].draw_foul)
                    select_player = random.randint(1, tracker_2)
                    for i in range(len(divs_2)):
                        if select_player < divs_2[i]:
                            player_2 = self.road_team.roster[i]
                            index_2 = i
                            break
                    if player_2 is None:
                        index_2 = 0
                    self.road_team.roster[index_2].d += 1
                    return True
        else:
            shot_value = 2
            add = player.consistency + player.takeover + player.explosiveness
            add //= (len(self.home_team.roster) * 3)
            divisor = random.randint(1, 101)
            block = random.randint(1, 20)
            block_odds = 3
            if block == block_odds:
                player_4 = None
                tracker_4 = 0
                divs_4 = []
                index_4 = 0
                for i in range(len(self.road_team.roster)):
                    divs_4.append(int(tracker_4))
                    tracker_4 += int(self.road_team.roster[i].block)
                select_player_2 = random.randint(1, tracker_4)
                for i in range(len(divs_4)):
                    if select_player_2 < divs_4[i] and i != index:
                        player_4 = self.road_team.roster[i]
                        index_4 = i
                        break
                if player_4 is None:
                    index_4 = 0
                self.road_team.roster[index_4].b += 1
                return False
            if divisor < add + 75:
                index_3 = 0
                player_3 = None
                tracker_3 = 0
                divs_3 = []
                for i in range(len(self.home_team.roster)):
                    divs_3.append(tracker_3)
                    tracker_3 += int(self.home_team.roster[i].play_making)
                select_player = random.randint(1, tracker_3)
                for i in range(len(divs_3)):
                    if select_player < divs_3[i]:
                        player_3 = self.home_team.roster[i]
                        index_3 = i
                        break
                if player_3 is None:
                    player_3 = self.home_team.roster[-1]
                    index_3 = 0
                if player_3 != player:
                    self.home_team.roster[index_3].a += 1
                    self.home_team_score += shot_value
                    self.home_team.roster[index].p += shot_value
                else:
                    self.home_team_score += shot_value
                    self.home_team.roster[index].p += shot_value
                return True
            else:
                total = 0
                for i in range(len(self.home_team.roster)):
                    total += self.home_team.roster[i].drb
                rebound_chance = total // len(self.home_team.roster) * .5
                odds = random.randint(1, 21)
                if odds > rebound_chance:
                    index_2 = 0
                    player_2 = None
                    tracker_2 = 0
                    divs_2 = []
                    for i in range(len(self.road_team.roster)):
                        divs_2.append(tracker_2)
                        tracker_2 += int(self.road_team.roster[i].draw_foul)
                    select_player = random.randint(1, tracker_2)
                    for i in range(len(divs_2)):
                        if select_player < divs_2[i]:
                            player_2 = self.road_team.roster[i]
                            index_2 = i
                            break
                    if player_2 is None:
                        index_2 = 0
                    self.road_team.roster[index_2].d += 1
                    return True
                else:
                    index_2 = 0
                    player_2 = None
                    tracker_2 = 0
                    divs_2 = []
                    for i in range(len(self.home_team.roster)):
                        divs_2.append(tracker_2)
                        tracker_2 += int(self.home_team.roster[i].draw_foul)
                    select_player = random.randint(1, tracker_2)
                    for i in range(len(divs_2)):
                        if select_player < divs_2[i]:
                            player_2 = self.home_team.roster[i]
                            index_2 = i
                            break
                    if player_2 is None:
                        index_2 = 0
                    self.home_team.roster[index_2].o += 1
                    return False

    def road_team_offense_sim(self):
        player = None
        tracker = 0
        divs = []
        index = 0
        steal = 3
        steal_odds = random.randint(1, 20)
        if steal == steal_odds:
            player_5 = None
            tracker_5 = 0
            divs_5 = []
            index_5 = 0
            for player_or_team in range(len(self.home_team.roster)):
                divs_5.append(int(tracker_5))
                tracker_5 += int(self.home_team.roster[player_or_team].steal)
            select_player_2 = random.randint(1, tracker_5)
            for player_or_team in range(len(divs_5)):
                if select_player_2 < divs_5[player_or_team]:
                    player_5 = self.home_team.roster[player_or_team]
                    index_5 = player_or_team
                    break
            if player_5 is None:
                index_5 = 0
            self.home_team.roster[index_5].s += 1
            return True

        player_6 = None
        tracker_6 = 0
        divs_6 = []
        index_6 = 0
        for player_or_team in range(len(self.home_team.roster)):
            divs_6.append(int(tracker_6))
            tracker_6 += int(self.home_team.roster[player_or_team].draw_foul)
        select_player_2 = random.randint(1, tracker_6)
        for player_or_team in range(len(divs_6)):
            if select_player_2 < divs_6[player_or_team]:
                player_6 = self.home_team.roster[player_or_team]
                index_6 = player_or_team
                break
        if player_6 is None:
            index_6 = 0
        self.home_team.roster[index_6].c += 1

        for player_or_team in range(len(self.road_team.roster)):
            divs.append(int(tracker))
            tracker += int(self.home_team.roster[player_or_team].shot_tendency)
        select_player = random.randint(1, tracker)
        for player_or_team in range(len(divs) - 1):
            if select_player < divs[player_or_team]:
                player = self.road_team.roster[player_or_team]
                index = player_or_team
                break
        if player is None:
            player = self.road_team.roster[-1]
        odds = random.randint(1, tracker)
        shot_chance = player.range_tendency
        if odds < shot_chance:
            shot_value = 3
            add = 0
            for player_or_team in range(len(self.road_team.roster)):
                add += (self.road_team.roster[player_or_team].threatening
                        + self.road_team.roster[player_or_team].big_play)
            add //= (len(self.road_team.roster) * 2)
            divisor = random.randint(1, 101)
            block = random.randint(1, 100)
            block_odds = 3
            if block == block_odds:
                player_4 = None
                tracker_4 = 0
                divs_4 = []
                index_4 = 0
                for player_or_team in range(len(self.home_team.roster)):
                    divs_4.append(int(tracker_4))
                    tracker_4 += int(self.home_team.roster[player_or_team].block)
                select_player_2 = random.randint(1, tracker_4)
                for player_or_team in range(len(divs_4)):
                    if select_player_2 < divs_4[player_or_team]:
                        player_4 = self.home_team.roster[player_or_team]
                        index_4 = player_or_team
                        break
                if player_4 is None:
                    index_4 = 0
                self.road_team.roster[index_4].b += 1
                return False
            if divisor < add:
                index_3 = 0
                player_3 = None
                tracker_3 = 0
                divs_3 = []
                for player_or_team in range(len(self.road_team.roster)):
                    divs_3.append(tracker_3)
                    tracker_3 += int(self.road_team.roster[player_or_team].play_making)
                select_player = random.randint(1, tracker_3)
                for player_or_team in range(len(divs_3)):
                    if select_player < divs_3[player_or_team]:
                        player_3 = self.road_team.roster[player_or_team]
                        index_3 = player_or_team
                        break
                if player_3 is None:
                    player_3 = self.road_team.roster[-1]
                    index_3 = 0
                if player_3 == player:
                    self.road_team_score += shot_value
                    self.road_team.roster[index].p += shot_value
                else:
                    self.road_team.roster[index_3].a += 1
                    self.road_team_score += shot_value
                    self.road_team.roster[index].p += shot_value
                return True
            else:
                total = 0
                for player_or_team in range(len(self.road_team.roster)):
                    total += self.road_team.roster[player_or_team].draw_foul
                rebound_chance = total // len(self.road_team.roster) * .75
                odds = random.randint(1, 21)
                if odds > rebound_chance:
                    index_2 = 0
                    tracker_2 = 0
                    divs_2 = []
                    player_2 = None
                    for player_or_team in range(len(self.road_team.roster)):
                        divs_2.append(tracker_2)
                        tracker_2 += int(self.road_team.roster[player_or_team].draw_foul)

                    select_player = random.randint(1, tracker_2)
                    for player_or_team in range(len(divs_2)):
                        if select_player < divs_2[player_or_team]:
                            player_2 = self.road_team.roster[player_or_team]
                            index_2 = player_or_team
                            break
                    if player_2 is None:
                        index_2 = 0
                    self.road_team.roster[index_2].o += 1
                    return False
                else:
                    player_2 = None
                    tracker_2 = 0
                    divs_2 = []
                    index_2 = 0
                    for player_or_team in range(len(self.home_team.roster)):
                        divs_2.append(tracker_2)
                        tracker_2 += int(self.home_team.roster[player_or_team].draw_foul)
                    select_player = random.randint(1, tracker_2)
                    for player_or_team in range(len(divs_2)):
                        if select_player < divs_2[player_or_team]:
                            player_2 = self.home_team.roster[player_or_team]
                            index_2 = player_or_team
                            break
                    if player_2 is None:
                        index_2 = 0
                    self.home_team.roster[index_2].d += 1
                    return True
        else:
            shot_value = 2
            add = 0
            for player_or_team in range(len(self.road_team.roster)):
                add += (self.road_team.roster[player_or_team].consistency +
                        self.road_team.roster[player_or_team].takeover +
                        self.road_team.roster[player_or_team].explosiveness)
            add //= (len(self.road_team.roster) * 3)
            divisor = random.randint(1, 101)
            block = random.randint(1, 20)
            block_odds = 3
            if block == block_odds:
                player_4 = None
                tracker_4 = 0
                divs_4 = []
                index_4 = 0
                for player_or_team in range(len(self.home_team.roster)):
                    divs_4.append(int(tracker_4))
                    tracker_4 += int(self.home_team.roster[player_or_team].block)
                select_player_2 = random.randint(1, tracker_4)
                for player_or_team in range(len(divs_4)):
                    if select_player_2 < divs_4[player_or_team]:
                        player_4 = self.home_team.roster[player_or_team]
                        index_4 = player_or_team
                        break
                if player_4 is None:
                    index_4 = 0
                self.road_team.roster[index_4].b += 1
                return False
            if divisor + 20 < add:
                index_3 = 0
                player_3 = None
                tracker_3 = 0
                divs_3 = []
                for player_or_team in range(len(self.road_team.roster)):
                    divs_3.append(tracker_3)
                    tracker_3 += int(self.road_team.roster[player_or_team].play_making)
                select_player = random.randint(1, tracker_3)
                for player_or_team in range(len(divs_3)):
                    if select_player < divs_3[player_or_team]:
                        player_3 = self.road_team.roster[player_or_team]
                        index_3 = player_or_team
                        break
                if player_3 is None:
                    player_3 = self.road_team.roster[-1]
                    index_3 = 0
                if player_3 == player:
                    self.road_team_score += shot_value
                    self.road_team.roster[index].p += shot_value
                else:
                    self.road_team.roster[index_3].a += 1
                    self.road_team_score += shot_value
                    self.road_team.roster[index].p += shot_value
                return True
            else:
                total = 0
                for player_or_team in range(len(self.road_team.roster)):
                    total += self.road_team.roster[player_or_team].draw_foul
                rebound_chance = total // len(self.road_team.roster) * .5
                odds = random.randint(1, 21)
                if odds > rebound_chance:
                    player_2 = None
                    tracker_2 = 0
                    divs_2 = []
                    index_2 = 0
                    for player_or_team in range(len(self.home_team.roster)):
                        divs_2.append(tracker_2)
                        tracker_2 += int(self.home_team.roster[player_or_team].draw_foul)
                    select_player = random.randint(1, tracker_2)
                    for player_or_team in range(len(divs_2)):
                        if select_player < divs_2[player_or_team]:
                            player_2 = self.home_team.roster[player_or_team]
                            index_2 = player_or_team
                            break
                    if player_2 is None:
                        index_2 = 0
                    self.home_team.roster[index_2].d += 1
                    return True
                else:
                    index_2 = 0
                    player_2 = None
                    tracker_2 = 0
                    divs_2 = []
                    for player_or_team in range(len(self.road_team.roster)):
                        divs_2.append(tracker_2)
                        tracker_2 += int(self.road_team.roster[player_or_team].draw_foul)
                    select_player = random.randint(1, tracker_2)
                    for player_or_team in range(len(divs_2)):
                        if select_player < divs_2[player_or_team]:
                            player_2 = self.road_team.roster[player_or_team]
                            index_2 = player_or_team
                            break
                    if player_2 is None:
                        index_2 = -1
                    self.road_team.roster[index_2].o += 1
                    return False

    def road_team_offense(self):
        player = None
        tracker = 0
        divs = []
        index = 0
        steal = 3
        steal_odds = random.randint(1, 20)
        if steal == steal_odds:
            player_5 = None
            tracker_5 = 0
            divs_5 = []
            index_5 = 0
            for i in range(len(self.home_team.roster)):
                divs_5.append(int(tracker_5))
                tracker_5 += int(self.home_team.roster[i].steal)
            select_player_2 = random.randint(1, tracker_5)
            for i in range(len(divs_5)):
                if select_player_2 < divs_5[i]:
                    player_5 = self.home_team.roster[i]
                    index_5 = i
                    break
            if player_5 is None:
                index_5 = 0
            self.home_team.roster[index_5].s += 1
            return True

        player_6 = None
        tracker_6 = 0
        divs_6 = []
        index_6 = 0
        for i in range(len(self.home_team.roster)):
            divs_6.append(int(tracker_6))
            tracker_6 += int(self.home_team.roster[i].draw_foul)
        select_player_2 = random.randint(1, tracker_6)
        for i in range(len(divs_6)):
            if select_player_2 < divs_6[i]:
                player_6 = self.home_team.roster[i]
                index_6 = i
                break
        if player_6 is None:
            index_6 = 0
        self.home_team.roster[index_6].c += 1

        for i in range(len(self.road_team.roster)):
            divs.append(int(tracker))
            tracker += int(self.home_team.roster[i].shot_tendency)
        select_player = random.randint(1, tracker)
        for i in range(len(divs) - 1):
            if select_player < divs[i]:
                player = self.road_team.roster[i]
                index = i
                break
        if player is None:
            player = self.road_team.roster[-1]
        odds = random.randint(1, tracker)
        shot_chance = player.range_tendency
        if odds < shot_chance:
            shot_value = 3
            add = 0
            for i in range(len(self.road_team.roster)):
                add += self.road_team.roster[i].threatening + self.road_team.roster[i].big_play
            add //= (len(self.road_team.roster) * 2)
            divisor = random.randint(1, 101)
            block = random.randint(1, 100)
            block_odds = 3
            if block == block_odds:
                player_4 = None
                tracker_4 = 0
                divs_4 = []
                index_4 = 0
                for i in range(len(self.home_team.roster)):
                    divs_4.append(int(tracker_4))
                    tracker_4 += int(self.home_team.roster[i].block)
                select_player_2 = random.randint(1, tracker_4)
                for i in range(len(divs_4)):
                    if select_player_2 < divs_4[i]:
                        player_4 = self.home_team.roster[i]
                        index_4 = i
                        break
                if player_4 is None:
                    index_4 = 0
                self.road_team.roster[index_4].b += 1
                return False
            if divisor < add:
                index_3 = 0
                player_3 = None
                tracker_3 = 0
                divs_3 = []
                for i in range(len(self.road_team.roster)):
                    divs_3.append(tracker_3)
                    tracker_3 += int(self.road_team.roster[i].play_making)
                select_player = random.randint(1, tracker_3)
                for i in range(len(divs_3)):
                    if select_player < divs_3[i]:
                        player_3 = self.road_team.roster[i]
                        index_3 = i
                        break
                if player_3 is None:
                    player_3 = self.road_team.roster[-1]
                    index_3 = 0
                if player_3 == player:
                    self.road_team_score += shot_value
                    self.road_team.roster[index].p += shot_value
                else:
                    self.road_team.roster[index_3].a += 1
                    self.road_team_score += shot_value
                    self.road_team.roster[index].p += shot_value
                return True
            else:
                total = 0
                for i in range(len(self.road_team.roster)):
                    total += self.road_team.roster[i].draw_foul
                rebound_chance = total // len(self.road_team.roster) * .75
                odds = random.randint(1, 21)
                if odds > rebound_chance:
                    index_2 = 0
                    tracker_2 = 0
                    divs_2 = []
                    player_2 = None
                    for i in range(len(self.road_team.roster)):
                        divs_2.append(tracker_2)
                        tracker_2 += int(self.road_team.roster[i].draw_foul)

                    select_player = random.randint(1, tracker_2)
                    for i in range(len(divs_2)):
                        if select_player < divs_2[i]:
                            player_2 = self.road_team.roster[i]
                            index_2 = i
                            break
                    if player_2 is None:
                        index_2 = 0
                    self.road_team.roster[index_2].o += 1
                    return False
                else:
                    player_2 = None
                    tracker_2 = 0
                    divs_2 = []
                    index_2 = 0
                    for i in range(len(self.home_team.roster)):
                        divs_2.append(tracker_2)
                        tracker_2 += int(self.home_team.roster[i].draw_foul)
                    select_player = random.randint(1, tracker_2)
                    for i in range(len(divs_2)):
                        if select_player < divs_2[i]:
                            player_2 = self.home_team.roster[i]
                            index_2 = i
                            break
                    if player_2 is None:
                        index_2 = 0
                    self.home_team.roster[index_2].d += 1
                    return True
        else:
            shot_value = 2
            add = 0
            for i in range(len(self.road_team.roster)):
                add += self.road_team.roster[i].consistency + self.road_team.roster[i].takeover + \
                       self.road_team.roster[
                           i].explosiveness
            add //= (len(self.road_team.roster) * 3)
            divisor = random.randint(1, 101)
            block = random.randint(1, 20)
            block_odds = 3
            if block == block_odds:
                player_4 = None
                tracker_4 = 0
                divs_4 = []
                index_4 = 0
                for i in range(len(self.home_team.roster)):
                    divs_4.append(int(tracker_4))
                    tracker_4 += int(self.home_team.roster[i].block)
                select_player_2 = random.randint(1, tracker_4)
                for i in range(len(divs_4)):
                    if select_player_2 < divs_4[i]:
                        player_4 = self.home_team.roster[i]
                        index_4 = i
                        break
                if player_4 is None:
                    index_4 = 0
                self.road_team.roster[index_4].b += 1
                return False
            if divisor + 20 < add:
                index_3 = 0
                player_3 = None
                tracker_3 = 0
                divs_3 = []
                for i in range(len(self.road_team.roster)):
                    divs_3.append(tracker_3)
                    tracker_3 += int(self.road_team.roster[i].play_making)
                select_player = random.randint(1, tracker_3)
                for i in range(len(divs_3)):
                    if select_player < divs_3[i]:
                        player_3 = self.road_team.roster[i]
                        index_3 = i
                        break
                if player_3 is None:
                    player_3 = self.road_team.roster[-1]
                    index_3 = 0
                if player_3 == player:
                    self.road_team_score += shot_value
                    self.road_team.roster[index].p += shot_value
                else:
                    self.road_team.roster[index_3].a += 1
                    self.road_team_score += shot_value
                    self.road_team.roster[index].p += shot_value
                return True
            else:
                total = 0
                for i in range(len(self.road_team.roster)):
                    total += self.road_team.roster[i].draw_foul
                rebound_chance = total // len(self.road_team.roster) * .5
                odds = random.randint(1, 21)
                if odds > rebound_chance:
                    player_2 = None
                    tracker_2 = 0
                    divs_2 = []
                    index_2 = 0
                    for i in range(len(self.home_team.roster)):
                        divs_2.append(tracker_2)
                        tracker_2 += int(self.home_team.roster[i].draw_foul)
                    select_player = random.randint(1, tracker_2)
                    for i in range(len(divs_2)):
                        if select_player < divs_2[i]:
                            player_2 = self.home_team.roster[i]
                            index_2 = i
                            break
                    if player_2 is None:
                        index_2 = 0
                    self.home_team.roster[index_2].d += 1
                    return True
                else:
                    index_2 = 0
                    player_2 = None
                    tracker_2 = 0
                    divs_2 = []
                    for i in range(len(self.road_team.roster)):
                        divs_2.append(tracker_2)
                        tracker_2 += int(self.road_team.roster[i].draw_foul)
                    select_player = random.randint(1, tracker_2)
                    for i in range(len(divs_2)):
                        if select_player < divs_2[i]:
                            player_2 = self.road_team.roster[i]
                            index_2 = i
                            break
                    if player_2 is None:
                        index_2 = -1
                    self.road_team.roster[index_2].o += 1
                    return False


# playoff class
class Playoffs:
    saved_road_wins = 0
    saved_home_wins = 0

    def __init__(self, east_playoffs, west_playoffs, season, teams, champion, save_string):
        self.east_playoffs = east_playoffs
        self.west_playoffs = west_playoffs
        self.season = season
        self.teams = teams
        self.champion = champion
        self.save_string = save_string

    def save_series_score(self, home_team, road_team, home_wins, road_wins):
        file = "playoffs" + str(read_season_number()) + ".txt"
        with open(file, "w") as contents:
            contents.write(self.save_string)
            contents.write(road_team.name + " " + str(road_wins) + "\n" + home_team.name + " " + str(home_wins) + "\n")

    def initialize_playoffs(self):
        file = "playoffs" + str(read_season_number()) + ".txt"
        east_organizer = []
        west_organizer = []
        try:
            with open(file, "r") as contents:
                lst = contents.readlines()
                for i in range(len(lst)):
                    if lst[i][:-2].strip() in teamNames[0:3]:
                        east_organizer.append([lst[i][:-2].strip(), int(lst[i].strip()[-1])])
                    elif lst[i][:-2].strip() in teamNames[3:]:
                        west_organizer.append([lst[i][:-2].strip(), int(lst[i].strip()[-1])])
                    if i % 2 != 0:
                        if "4" in lst[i] or "4" in lst[i - 1] or i == len(lst) - 1:
                            self.save_string += (lst[i - 1] + lst[i])
                teaml = [team for team in self.east_playoffs if [team[1].name, 4] in east_organizer]
                if len(teaml) == 1:
                    self.east_playoffs = teaml
                teaml = [team for team in self.west_playoffs if [team[1].name, 4] in west_organizer]
                if len(teaml) == 1:
                    self.west_playoffs = teaml
                self.saved_home_wins = int(lst[-1][-2])
                self.saved_road_wins = int(lst[-2][-2])
        except FileNotFoundError:
            return

    def run_playoff_series(self, home_team, road_team, conference):

        # get the saved wins
        road_wins = self.saved_road_wins
        home_wins = self.saved_home_wins
        self.save_series_score(home_team, road_team, home_wins, road_wins)

        # while neither team has hit 4 wins
        while road_wins < 4 and home_wins < 4:

            # print out the game preview
            game_count = home_wins + road_wins + 1
            choice_playoff_series = input("Enter 's' to simulate the game, enter 'p' to play: ")
            if game_count > 0:
                if road_wins > home_wins and game_count > 0:
                    print("Game", game_count, road_team.name, "leads series", road_wins, " - ", home_wins)
                elif road_wins < home_wins:
                    print("Game", game_count, home_team.name, "leads series", home_wins, " - ", road_wins)
                else:
                    print("Game", game_count, "series tied", home_wins, " - ", road_wins)
            else:
                print("Game", game_count, home_team.name, "vs", road_team.name)

            # initialize the game object.
            g = Game(home_team, road_team, 0, 0)

            # simulate the game
            if choice_playoff_series == "p":
                if game_count < 3 or game_count == 5 or game_count == 7:
                    print(road_team.name, "@", home_team.name)
                    match = g.run_game()
                    if match == home_team:
                        home_wins += 1
                    else:
                        road_wins += 1
                else:
                    print(home_team.name, "@", road_team.name)
                    match = g.run_game()
                    if match == road_team:
                        road_wins += 1
                    else:
                        home_wins += 1
            else:
                if game_count == 2 or game_count == 1 or game_count == 5 or game_count == 7:
                    print(road_team.name, "@", home_team.name)
                    match = g.simulate_game()
                    if match == home_team:
                        home_wins += 1
                    else:
                        road_wins += 1
                elif game_count == 3 or game_count == 4 or game_count == 6:
                    print(home_team.name, "@", road_team.name)
                    match = g.simulate_game()
                    if match == road_team:
                        road_wins += 1
                    else:
                        home_wins += 1
            self.save_series_score(home_team, road_team, home_wins, road_wins)
        self.saved_road_wins = 0
        self.saved_home_wins = 0
        if road_wins == 4:
            print(road_team.name, "Wins Series ", road_wins, " - ", home_wins)
            if conference == "east":
                if home_team in self.east_playoffs:
                    self.east_playoffs.remove(home_team)
            if conference == "west":
                if home_team in self.west_playoffs:
                    self.west_playoffs.remove(home_team)
            self.save_string += road_team.name + " " + str(road_wins) + "\n" + home_team.name + " " + str(
                home_wins) + "\n"
            return road_team
        else:
            print(home_team.name, "Wins Series ", home_wins, " - ", road_wins)
            if conference == "east":
                if road_team in self.east_playoffs:
                    self.east_playoffs.remove(road_team)
            if conference == "west":
                if road_team in self.west_playoffs:
                    self.west_playoffs.remove(road_team)
            self.save_string += road_team.name + " " + str(road_wins) + "\n" + home_team.name + " " + str(
                home_wins) + "\n"
            return home_team

    def run_playoffs(self):
        if len(self.east_playoffs) != 1:
            while len(self.east_playoffs) > 1:
                self.run_playoff_series(self.east_playoffs[1][1], self.east_playoffs[0][1], "east")
                break
        if len(self.west_playoffs) != 1:
            while len(self.west_playoffs) > 1:
                self.run_playoff_series(self.west_playoffs[1][1], self.west_playoffs[0][1], "west")
                break
        if self.east_playoffs[0][-1].wins > self.west_playoffs[0][-1].wins:
            home = self.east_playoffs[0][-1]
            road = self.west_playoffs[0][-1]
        else:
            home = self.west_playoffs[0][-1]
            road = self.east_playoffs[0][-1]
        champion = self.run_playoff_series(road, home, "")
        print("Your champion is: ", champion.name)
        return champion


# Players
# Boston
johnWhite = Player("John White", 45, 54, 93, 99, 99, 99, 99, 99, 99, 99, 99, 99, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
jamesJohnson = Player("James Johnson", 99, 99, 99, 93, 65, 65, 85, 90, 80, 95, 90, 90, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
michaelDavis = Player("Michael Davis", 98, 98, 60, 85, 65, 50, 30, 10, 80, 70, 10, 50, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
robertHarris = Player("Robert Harris", 80, 99, 70, 83, 99, 60, 95, 50, 40, 80, 90, 90, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
williamSmith = Player("William Smith", 80, 95, 98, 80, 93, 88, 93, 90, 89, 87, 90, 93, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
BostonRoster = (johnWhite, jamesJohnson, michaelDavis, robertHarris, williamSmith)

# NewYork
davidJackson = Player("David Jackson", 85, 90, 90, 95, 80, 90, 90, 50, 99, 60, 50, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [], [], [])
joesphBrown = Player("Joesph Brown", 99, 85, 99, 75, 60, 80, 90, 99, 60, 55, 65, 90, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
charlesRobinson = Player("Charles Robinson", 90, 95, 80, 90, 90, 90, 85, 87, 75, 60, 70, 80, 0, 0.0, 0.0, 0.0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
thomasLee = Player("Thomas Lee", 90, 80, 95, 85, 85, 60, 50, 40, 10, 60, 30, 50, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
danielWilson = Player("Daniel Wilson", 90, 80, 70, 78, 83, 90, 82, 90, 60, 80, 40, 50, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
NewYorkRoster = (davidJackson, joesphBrown, charlesRobinson, thomasLee, danielWilson)

# Miami
richardThompson = Player("Richard Thompson", 90, 99, 90, 90, 90, 90, 90, 99, 99, 99, 99, 78, 0, 0.0, 0.0, 0.0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
georgeAnderson = Player("George Anderson", 70, 80, 76, 56, 60, 50, 89, 80, 70, 75, 90, 58, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
kennethHall = Player("Kenneth Hall", 60, 80, 87, 80, 70, 90, 87, 90, 80, 78, 50, 93, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
paulMoore = Player("Paul Moore", 50, 90, 80, 90, 80, 90, 84, 40, 87, 40, 90, 85, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
edwardGreen = Player("Edward Green", 80, 90, 78, 85, 99, 99, 84, 99, 90, 90, 80, 90, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
MiamiRoster = (richardThompson, georgeAnderson, kennethHall, paulMoore, edwardGreen)

# Phoenix
frankTaylor = Player("Frank Taylor", 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
markWright = Player("Mark Wright", 95, 90, 93, 92, 90, 90, 99, 93, 96, 98, 90, 96, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
anthonyMartin = Player("Anthony Martin", 99, 90, 87, 89, 89, 90, 98, 90, 92, 94, 95, 90, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
stevenLewis = Player("Steven Lewis", 80, 70, 60, 65, 90, 99, 50, 40, 50, 40, 99, 95, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
brianAdams = Player("Brian Adams", 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 10, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
PhoenixRoster = [frankTaylor, markWright, anthonyMartin, stevenLewis, brianAdams]

# LA
kevinTurner = Player("Kevin Turner", 99, 89, 65, 99, 99, 76, 99, 76, 99, 99, 99, 99, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
ronaldKing = Player("Ronald King", 89, 99, 95, 95, 99, 99, 95, 76, 99, 99, 87, 90, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
ericScott = Player("Eric Scott", 80, 80, 60, 76, 98, 76, 50, 40, 80, 99, 99, 90, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
jerryCarter = Player("Jerry Carter", 90, 90, 0, 40, 90, 40, 40, 40, 90, 90, 90, 90, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
stephenParker = Player("Stephen Parker", 70, 90, 80, 60, 70, 80, 70, 80, 50, 60, 70, 60, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
LosAngelesRoster = (kevinTurner, ronaldKing, ericScott, jerryCarter, stephenParker)

# Denver
larryEvans = Player("Larry Evans", 90, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
jefferyAllen = Player("Jeffrey Allen", 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
scottYoung = Player("Scott Young", 99, 92, 90, 93, 93, 99, 90, 90, 99, 99, 99, 99, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
tyroneWashington = Player("Tyrone Washington", 50, 60, 70, 80, 50, 90, 60, 70, 50, 80, 70, 70, 0, 0, 0.0, 0.0, 0.0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [])
darnellMitchell = Player("Darnell Mitchell", 50, 60, 80, 70, 60, 50, 60, 80, 90, 60, 75, 90, 0, 0.0, 0.0, 0.0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], [])
DenverRoster = (larryEvans, jefferyAllen, scottYoung, tyroneWashington, darnellMitchell)

# Teams
boston = Team("Boston", BostonRoster, 0, 0, "East", 0, 0, 0, [], [])
new_york = Team("NewYork", NewYorkRoster, 0, 0, "East", 0, 0, 0, [], [])
Miami = Team("Miami", MiamiRoster, 0, 0, "East", 0, 0, 0, [], [])
Phoenix = Team("Phoenix", PhoenixRoster, 0, 0, "West", 0, 0, 0, [], [])
LosAngeles = Team("LosAngeles", LosAngelesRoster, 0, 0, "West", 0, 0, 0, [], [])
Denver = Team("Denver", DenverRoster, 0, 0, "West", 0, 0, 0, [], [])
team_lst = (boston, new_york, Miami, Phoenix, LosAngeles, Denver)
league_list = (
    johnWhite, jamesJohnson, michaelDavis, robertHarris, williamSmith, davidJackson, joesphBrown, charlesRobinson,
    thomasLee, danielWilson,
    richardThompson, georgeAnderson, kennethHall, paulMoore, edwardGreen, frankTaylor, markWright, anthonyMartin,
    stevenLewis, brianAdams,
    kevinTurner, ronaldKing, ericScott, jerryCarter, stephenParker, larryEvans, jefferyAllen, scottYoung,
    tyroneWashington,
    darnellMitchell)
east = (boston, new_york, Miami)
west = (Phoenix, LosAngeles, Denver)
teamNames = (boston.name, new_york.name, Miami.name, Phoenix.name, LosAngeles.name, Denver.name)
num = read_season_number()


def read_player_season_awards():
    for player in range(len(league_list)):
        league_list[player].find_awards_seasons()


read_player_season_awards()
season_number = read_season_number()
first_iteration = True
Season1 = Season([], team_lst, [], [], [], None, None, None, None, None, num, None, None, None, None, None, None, None)
stop = Season1.read_standings()
read_individual_awards()
Season1.read_stats(league_list)
Season1.read_team_awards()
if stop == 0:
    Season1.generate_schedule()
else:
    Season1.load_schedule()
iterationRunning = True
while iterationRunning:

    # configure the season
    game_set = 0
    game = 0
    index = 0
    if first_iteration is False and stop == 0:
        Season1.new_season()
        Season1 = Season([], team_lst, [], [], [], None, None, None, None, None, num, None, None, None, None, None,
                         None,
                         None)
        Season1.generate_schedule()

    # loop through each game
    while game_set < len(Season1.schedule):
        while game < len(Season1.schedule[game_set]):
            if index >= stop:
                print(Season1.schedule[game_set][game][0].name, " vs ", Season1.schedule[game_set][game][1].name)
                choice = input("Season " + str(Season1.number) + " day: " + str(
                    index) + " What would you like to do? press enter to simulate the game from the schedule. "
                             "press 'p' to play the game. enter 's' to view more enter e to exit"
                             "\ninformation about the present season. if you want to look at records enter 'r'."
                             "if you want to look at the profile of a player or team enter 'pr': ")
                game_setup = Game(Season1.schedule[game_set][game][0], Season1.schedule[game_set][game][1], 0, 0)
                if choice.upper() == "E":
                    print("exiting KBL...")
                    exit()

                # viewing the current season
                if choice == "s":
                    Season1.number = read_season_number()
                    choiceInside = input(
                        "If you would like to view the standings type 'st'. \nIf you would like to view the remaining "
                        "schedule press 'sh'. \nIf you would like to view the stats of every player type 'ss'.\n to "
                        "go back to the season page hit enter: ")
                    if choiceInside == "st":
                        Season1.display_standings()
                        exit_program()
                        continue
                    elif choiceInside == "sh":
                        Season1.display_schedule(index)
                        exit_program()
                        continue
                    elif choiceInside == "ss":
                        Season1.display_stats()
                        exit_program()
                        continue
                    else:
                        continue

                # viewing the records
                elif choice == "r":
                    try:
                        numberChoice = int(input("Enter which Season's records you would like to see: "))
                        while numberChoice >= read_season_number():
                            numberChoice = int(input("Enter which Season's records you would like to see: "))
                    except ValueError:
                        numberChoice = int(input("Enter which Season's records you would like to see: "))

                    insideChoice = input(
                        "Enter what you would like to see for your seasonNumber. If you would to view stats from your "
                        "season type sa.\nif you would like to view standings type st.\nIf you would like to view sh "
                        "schedule type sh.\nif you would like view award winners type 'aw'.\nto change you season "
                        "click enter: ")
                    SeasonRequested = Season([], team_lst, [], [], [], None, None, None, None, None, numberChoice, None,
                                             None, None, None,
                                             None, None, None)
                    if insideChoice == "sa":
                        SeasonRequested.read_stats(league_list)
                        SeasonRequested.display_stats()
                        exit_program()
                        SeasonRequested = None
                        continue
                    elif "st" == insideChoice:
                        SeasonRequested.read_standings()
                        SeasonRequested.display_standings()
                        exit_program()
                        SeasonRequested = None
                        continue
                    elif insideChoice == "sh":
                        SeasonRequested.load_schedule()
                        SeasonRequested.display_schedule(0)
                        exit_program()
                        SeasonRequested = None
                        continue
                    elif insideChoice == "aw":
                        SeasonRequested.read_season_awards()
                        SeasonRequested.display_season_awards()
                        exit_program()
                        SeasonRequested = None
                        continue
                    else:
                        continue

                # viewing particular records
                elif choice == "pr":
                    choiceInside = input(
                        "would you like to view a particular team or player? 'p' for player 't' for team: ")
                    if choiceInside == "p":
                        print("type the corresponding number to the player you would like to see in detail: ")
                        for game_set in range(len(league_list)):
                            print(game_set + 1, league_list[game_set].name)
                        player_choice = int(input("Enter the number: "))
                        league_list[player_choice - 1].display_awards()
                        continue

                    if choiceInside == "t":
                        for game_set in range(len(team_lst)):
                            print(game_set + 1, team_lst[game_set].name)
                        teamChoice = int(input("Enter the number corresponding to your desired team:"))
                        team_lst[teamChoice - 1].display_awards()
                        print(team_lst[teamChoice - 1].print_roster())
                        continue

                # playing the game
                elif choice == 'p':

                    # run game and do necessary operations
                    sim_result = game_setup.run_game()
                    if sim_result == Season1.schedule[game_set][game][0]:
                        Season1.schedule[game_set][game][0].games += 1
                        Season1.schedule[game_set][game][1].games += 1
                        Season1.schedule[game_set][game][0].wins += 1
                        Season1.schedule[game_set][game][1].losses += 1
                    else:
                        Season1.schedule[game_set][game][0].games += 1
                        Season1.schedule[game_set][game][1].games += 1
                        Season1.schedule[game_set][game][1].wins += 1
                        Season1.schedule[game_set][game][0].losses += 1
                    for x in range(len(Season1.schedule[game_set][game][0].roster)):
                        Season1.schedule[game_set][game][0].roster[x].g += 1
                    for x in range(len(Season1.schedule[game_set][game][1].roster)):
                        Season1.schedule[game_set][game][1].roster[x].g += 1
                    Season1.write_standings()
                    Season1.write_stats()
                    Season1.save_player_awards()
                else:
                    sim_result = game_setup.simulate_game()
                    if sim_result == Season1.schedule[game_set][game][0]:
                        Season1.schedule[game_set][game][0].games += 1
                        Season1.schedule[game_set][game][1].games += 1
                        Season1.schedule[game_set][game][0].wins += 1
                        Season1.schedule[game_set][game][1].losses += 1
                    else:
                        Season1.schedule[game_set][game][0].games += 1
                        Season1.schedule[game_set][game][1].games += 1
                        Season1.schedule[game_set][game][1].wins += 1
                        Season1.schedule[game_set][game][0].losses += 1
                    for x in range(len(Season1.schedule[game_set][game][0].roster)):
                        Season1.schedule[game_set][game][0].roster[x].g += 1
                    for x in range(len(Season1.schedule[game_set][game][1].roster)):
                        Season1.schedule[game_set][game][1].roster[x].g += 1
                    Season1.write_standings()
                    Season1.write_stats()
                    Season1.save_player_awards()
            game += 1
            index += 1
        game = 0
        game_set += 1
    Season1.display_stats()
    Season1.display_standings()
    Season1.handle_awards()
    string = ""
    string2 = ""
    for game_set in range(len(Season1.determine_all_kbl_team())):
        if game_set % 2 == 0:
            string += Season1.determine_all_kbl_team()[game_set].name + " "
        else:
            string2 += Season1.determine_all_kbl_team()[game_set].name + " "
    print("all KBL teams")
    print("First Team " + " " + string)
    print("Second Team " + " " + string2)
    input("Enter when ready: ")
    playoff = Playoffs(Season1.standings_east[0:-1], Season1.standings_west[0:-1], Season1, team_lst, None, "")
    playoff.initialize_playoffs()
    Season1.get_champion(playoff.run_playoffs())
    Season1.new_season()
    stop = 0
    num += 1
    write_season_number(num)
    first_iteration = False
