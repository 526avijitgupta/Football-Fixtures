from lxml import html
from datetime import datetime
import requests
from titlecase import titlecase

# Function to find the user input team


def find(hometeam, awayteam, length, find_by):
    flag = False
    for i in range(0, length):
        if(hometeam[i] == find_by or awayteam[i] == find_by):
            print ("%s Vs %s" % (hometeam[i], awayteam[i]))
            convert_to_standard_time(real_date[i])
            flag = True
    print "\n"
    if(not flag):
        print "Your input did not match any fixtures!"

# Function to find the important fixtures


def important(hometeam, awayteam, length, topTeams):
    flag = False
    print "The list of important fixtures of the selected league (involving top teams) :\n"
    for i in range(0, length):
        if (hometeam[i] in topTeams and awayteam[i] in topTeams):
            print ("%s Vs %s" % (hometeam[i], awayteam[i]))
            convert_to_standard_time(real_date[i])
            flag = True
    print "\n"
    if(not flag):
        print "Your input did not match any fixtures!"

# Function to correct the user input to make it usable


def chop(userinput):
    for i in range(0, 5):
        userinput[i] = userinput[i].replace('AS ', '')
        userinput[i] = userinput[i].replace('FC ', '')
        userinput[i] = userinput[i].replace(' FC', '')
        userinput[i] = userinput[i].replace('EA ', '')

# Function to correct the date and time of the found fixture


def convert_to_standard_time(date):
    print date['day'],

    date['month'] = int(date['month'])
    if (date['month'] == 1):
        print "January",
    elif (date['month'] == 2):
        print "February",
    elif (date['month'] == 3):
        print "March",
    elif (date['month'] == 4):
        print "April",
    elif (date['month'] == 5):
        print "May",
    elif (date['month'] == 6):
        print "June",
    elif (date['month'] == 7):
        print "July",
    elif (date['month'] == 8):
        print "August",
    elif (date['month'] == 9):
        print "September",
    elif (date['month'] == 10):
        print "October",
    elif (date['month'] == 11):
        print "November",
    elif (date['month'] == 12):
        print "December",

    print ", ",

    print date['year'],
    print "-",

    # print "\n"

    hrs = date['time'].split(":")[0]
    mins = date['time'].split(":")[1]

    if (int(hrs) <= 12):
        print date['time'] + "AM"
    else:
        hrs = str(int(hrs) - 12)
        print hrs + ":" + mins + "PM"

    print "\n"

flag = False

# In case the user enters an invalid input, display this message
INVALID_MSG = 'Please enter a valid input!'

# Getting the user input for choosing the league
main = int(raw_input("""
    Select the league for which the fixtures for the current calendar year have to be displayed:
    1. UEFA Champions League
    2. English Premier League(EPL)
    3. La Liga
    4. Bundesliga
    5. French Ligue 1
    6. Italian Serie A
    """))

# Checking for the validity of user input
if (main <= 6 and main > 0):

    print "Loading.."

    FIXTURES_URL = 'http://www.goal.com/en-india/fixtures/'

    UCL_FIXED = 'uefa-champions-league/10'
    EPL_FIXED = 'premier-league/8'
    LL_FIXED = 'primera-divisi%C3%B3n/7'
    BL_FIXED = 'bundesliga/9'
    L1_FIXED = 'ligue-1/16'
    SA_FIXED = 'serie-a/13'

    if(main == 1):
        page = requests.get(FIXTURES_URL + UCL_FIXED)
    elif(main == 2):
        page = requests.get(FIXTURES_URL + EPL_FIXED)
    elif(main == 3):
        page = requests.get(FIXTURES_URL + LL_FIXED)
    elif(main == 4):
        page = requests.get(FIXTURES_URL + BL_FIXED)
    elif(main == 5):
        page = requests.get(FIXTURES_URL + L1_FIXED)
    elif(main == 6):
        page = requests.get(FIXTURES_URL + SA_FIXED)

    tree = html.fromstring(page.text)

    HOME_TEAM_XPATH = '//div[@class="module module-team simple home"]/span/text()'
    AWAY_TEAM_XPATH = '//div[@class="module module-team simple away"]/span/text()'

    if(main == 1):
        uclhome = tree.xpath(HOME_TEAM_XPATH)
        uclaway = tree.xpath(AWAY_TEAM_XPATH)
        total_teams = len(uclhome)

    else:
        team_home = tree.xpath(HOME_TEAM_XPATH)
        team_away = tree.xpath(AWAY_TEAM_XPATH)
        total_teams = len(team_home)

    # Getting the user input for the functionality needed
    choice = int(raw_input("""
        Enter one of the choices from below:
        1. Print the only important fixtures of the current league
        2. Print the fixtures by team
        3. Print the standings for the league
        """))

    # Checking for the validity of user input
    if (choice <= 3 and choice > 0):

        print "Loading.."

        date_list = tree.xpath('//th[@class="comp-date"]/text()')
        time_list = tree.xpath('//@data-match-time')
        real_date = []
        for time in time_list:
            match_details = datetime.fromtimestamp(int(time))
            temp = {
                'month': match_details.month,
                'day': match_details.day,
                'year': match_details.year,
                'time': match_details.strftime('%H:%M')
            }
            real_date.append(temp)

        TABLES_FIXED = 'http://www.goal.com/en-india/tables/'

        if (choice == 1 or choice == 3):

            if(main == 1):
                page = requests.get(TABLES_FIXED + UCL_FIXED)
            elif(main == 2):
                page = requests.get(TABLES_FIXED + EPL_FIXED)
            elif(main == 3):
                page = requests.get(TABLES_FIXED + LL_FIXED)
            elif(main == 4):
                page = requests.get(TABLES_FIXED + BL_FIXED)
            elif(main == 5):
                page = requests.get(TABLES_FIXED + L1_FIXED)
            elif(main == 6):
                page = requests.get(TABLES_FIXED + SA_FIXED)

            tree = html.fromstring(page.text)

            TEAM_RANKWISE_XPATH = '//td[@class="legend team short"]'
            UCL_HREF_CONTAINS_XPATH = '/a[starts-with(@href, "/en-india/teams/")]/text()'
            EPL_HREF_CONTAINS_XPATH = '/a[starts-with(@href, "/en-india/teams/england/")]/text()'
            LL_HREF_CONTAINS_XPATH = '/a[starts-with(@href, "/en-india/teams/spain/")]/text()'
            BL_HREF_CONTAINS_XPATH = '/a[starts-with(@href, "/en-india/teams/germany/")]/text()'
            L1_HREF_CONTAINS_XPATH = '/a[starts-with(@href, "/en-india/teams/france/")]/text()'
            SA_HREF_CONTAINS_XPATH = '/a[starts-with(@href, "/en-india/teams/italy/")]/text()'

            if (main == 1):
                tempTeamName = tree.xpath(
                    TEAM_RANKWISE_XPATH + UCL_HREF_CONTAINS_XPATH)
            elif (main == 2):
                standings = tree.xpath(
                    TEAM_RANKWISE_XPATH + EPL_HREF_CONTAINS_XPATH)
            elif (main == 3):
                standings = tree.xpath(
                    TEAM_RANKWISE_XPATH + LL_HREF_CONTAINS_XPATH)
            elif (main == 4):
                standings = tree.xpath(
                    TEAM_RANKWISE_XPATH + BL_HREF_CONTAINS_XPATH)
            elif (main == 5):
                standings = tree.xpath(
                    TEAM_RANKWISE_XPATH + L1_HREF_CONTAINS_XPATH)
            elif (main == 6):
                standings = tree.xpath(
                    TEAM_RANKWISE_XPATH + SA_HREF_CONTAINS_XPATH)

            UCL_TEAMRANK_XPATH = '//td[@class="legend position"]/text()'

            if (main == 1):
                teamRank = tree.xpath('//td[@class="legend position"]/text()')
                teamName = []
                for temp_team in tempTeamName:
                    teamName += [temp_team[1:][:-1]]
                topTeams = [teamName[i]
                            for i in range(0, len(teamRank)) if(int(teamRank[i]) <= 3)]
                topTeamDates = [real_date[i] for i in range(0, 3)]
                if (choice == 1):
                    important(uclhome, uclaway, total_teams, topTeams)

            else:
                ln = len(standings)
                for i in range(0, ln):
                    standings[i] = standings[i].split("\n")[1][:-1]
                topTeams = [standings[i] for i in range(0, 5)]
                topTeamDates = [real_date[i] for i in range(0, 5)]
                if (choice == 1):
                    important(team_home, team_away, total_teams, topTeams)

            if (choice == 3):

                print "\nThe league standings are as follows:\n"

                if (main == 1):
                    for team in teamName:
                        print str(teamName.index(team) + 1) + ". " + team

                else:
                    for team in standings:
                        print str(standings.index(team) + 1) + ". " + team

                print "\n"

        elif (choice == 2):

            # Never thought converting to title case would be so easy!
            find_by = titlecase(
                str(raw_input("Enter the team name(omit words like FC, AS, CF etc.):\n")))
            print(
                "\nThe fixtures for the team you entered for the current season are:\n")

            if (main == 1):
                find(uclhome, uclaway, total_teams, find_by)
            else:
                find(team_home, team_away, total_teams, find_by)

    else:
        print INVALID_MSG

else:
    print INVALID_MSG
