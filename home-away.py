from lxml import html
from datetime import datetime
import requests
from titlecase import titlecase

# defines the number of teams to be taken into consideration for topTeams
NO_OF_TEAMS_FROM_TOP = 5

# defines the number of teams to be taken for each group for topTeams for UCL
UCL_NO_OF_TEAMS_GROUP = 2


# Function to search for user input team
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
    print "\nThe important fixtures of this league (involving top teams): \n"
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
    userinput = userinput
    .replace('AS ', '')
    .replace('FC ', '')
    .replace(' FC', '')
    .replace('EA ', '')


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

    hrs = date['time'].split(":")[0]
    mins = date['time'].split(":")[1]

    if (int(hrs) <= 12):
        print date['time'] + "AM"
    else:
        hrs = str(int(hrs) - 12)
        print hrs + ":" + mins + "PM"

    print "\n"


if __name__ == "__main__":
    # flag value to check whether user input matches any existing teams or not
    flag = False

    # In case the user enters an invalid input, display this message
    INVALID_MSG = 'Please enter a valid input!'

    # Getting the user input for choosing the league
    main = int(raw_input("""
    Select the league to display the fixtures for the current calendar year:
        1. UEFA Champions League
        2. English Premier League(EPL)
        3. La Liga
        4. Bundesliga
        5. French Ligue 1
        6. Italian Serie A
    """))

    # Checking for the validity of user input
    if (main <= 6 and main > 0):
        print "Loading..",

        FIXTURES_URL = 'http://www.goal.com/en-india/fixtures/'
        UCL_FIXED = 'uefa-champions-league/10'
        EPL_FIXED = 'premier-league/8'
        LL_FIXED = 'primera-divisi%C3%B3n/7'
        BL_FIXED = 'bundesliga/9'
        L1_FIXED = 'ligue-1/16'
        SA_FIXED = 'serie-a/13'

        if(main == 1):
            url_league = UCL_FIXED
        elif(main == 2):
            url_league = EPL_FIXED
        elif(main == 3):
            url_league = LL_FIXED
        elif(main == 4):
            url_league = BL_FIXED
        elif(main == 5):
            url_league = L1_FIXED
        elif(main == 6):
            url_league = SA_FIXED

        page = requests.get(FIXTURES_URL + url_league)
        tree = html.fromstring(page.text)

        HOME_TEAM_XPATH =
        '//div[@class="module module-team simple home"]/span/text()'
        AWAY_TEAM_XPATH =
        '//div[@class="module module-team simple away"]/span/text()'

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
            print "Loading..",

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
                page = requests.get(TABLES_FIXED + url_league)
                tree = html.fromstring(page.text)

                TEAM_RANKWISE_XPATH =
                '//td[@class="legend team short"]'
                UCL_HREF_CONTAINS_XPATH =
                '/a[starts-with(@href, "/en-india/teams/")]/text()'
                EPL_HREF_CONTAINS_XPATH =
                '/a[starts-with(@href, "/en-india/teams/england/")]/text()'
                LL_HREF_CONTAINS_XPATH =
                '/a[starts-with(@href, "/en-india/teams/spain/")]/text()'
                BL_HREF_CONTAINS_XPATH =
                '/a[starts-with(@href, "/en-india/teams/germany/")]/text()'
                L1_HREF_CONTAINS_XPATH =
                '/a[starts-with(@href, "/en-india/teams/france/")]/text()'
                SA_HREF_CONTAINS_XPATH =
                '/a[starts-with(@href, "/en-india/teams/italy/")]/text()'

                if (main == 1):
                    xpath_teams_list = UCL_HREF_CONTAINS_XPATH
                elif (main == 2):
                    xpath_teams_list = EPL_HREF_CONTAINS_XPATH
                elif (main == 3):
                    xpath_teams_list = LL_HREF_CONTAINS_XPATH
                elif (main == 4):
                    xpath_teams_list = BL_HREF_CONTAINS_XPATH
                elif (main == 5):
                    xpath_teams_list = L1_HREF_CONTAINS_XPATH
                elif (main == 6):
                    xpath_teams_list = SA_HREF_CONTAINS_XPATH

                if (main == 1):
                    tempTeamName = tree.xpath(
                        TEAM_RANKWISE_XPATH + xpath_teams_list)
                else:
                    standings = tree.xpath(
                        TEAM_RANKWISE_XPATH + xpath_teams_list)

                if (main == 1):
                    teamRank = tree.xpath(
                        '//td[@class="legend position"]/text()')
                    teamName = []

                    for temp_team in tempTeamName:
                        teamName += [temp_team.split("\n")[1]]

                    topTeams = [teamName[i]
                                for i in range(0, len(teamRank))
                                if(int(teamRank[i]) <= UCL_NO_OF_TEAMS_GROUP)]
                    topTeamDates = [real_date[i] for i in range(
                        0, UCL_NO_OF_TEAMS_GROUP)]

                    if (choice == 1):
                        important(uclhome, uclaway, total_teams, topTeams)

                else:
                    ln = len(standings)
                    for i in range(0, ln):
                        standings[i] = standings[i].split("\n")[1]

                    topTeams = [standings[i] for i in range(
                        0, NO_OF_TEAMS_FROM_TOP)]
                    topTeamDates = [real_date[i] for i in range(
                        0, NO_OF_TEAMS_FROM_TOP)]

                    if (choice == 1):
                        important(team_home, team_away, total_teams, topTeams)

                if (choice == 3):
                    print "\nThe league standings are as follows:"
                    if (main == 1):
                        for team in teamName:
                            print str(teamName.index(team) + 1) + ". " + team
                    else:
                        for team in standings:
                            print str(standings.index(team) + 1) + ". " + team

            elif (choice == 2):
                # Never thought converting to title case would be so easy!
                find_by = titlecase(
                    str(raw_input(
                        "Enter the team name(omit words like FC, CF ..):\n")))
                chop(find_by)
                print(
                    "\nThe fixtures for this team for the current season are:")
                if (main == 1):
                    find(uclhome, uclaway, total_teams, find_by)
                else:
                    find(team_home, team_away, total_teams, find_by)

        else:
            print INVALID_MSG

    else:
        print INVALID_MSG

    print "=" * 100
