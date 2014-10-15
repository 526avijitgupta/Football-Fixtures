from lxml import html
from datetime import datetime
import requests

teamName = []

# Function to 
def find(hometeam, awayteam , length , find_by):
    flag = False
    for i in range(0,length):
        if(hometeam[i] == find_by or awayteam[i] == find_by):
            print ("%s Vs %s" % (hometeam[i] , awayteam[i]))
            flag = True
    print "\n"
    if(not flag):
        print "Your input did not match any fixtures!"

def important(hometeam, awayteam, length, topTeams):
    flag = False
    print "The list of important fixtures of the selected league (involving top teams) :\n"
    for i in range(0,length):
        if(hometeam[i] and awayteam[i]) in topTeams:            
            print  ("%s Vs %s" % (hometeam[i] , awayteam[i]))
            flag = True
    print "\n"
    if(not flag):
        print "Your input did not match any fixtures!"

def chop(userinput):
    for i in range(0,5):
        userinput[i] = userinput[i].replace('AS ','')
        userinput[i] = userinput[i].replace('FC ','')
        userinput[i] = userinput[i].replace(' FC','')
        userinput[i] = userinput[i].replace('EA ','')
        
#This will create a list of home teams:

#This will create a list of away teams

#This will create a list of the dates of the fixtures
#pldate = tree.xpath('//div[@class="module module-team simple home"]/parent::td[@class="team"]/parent::tr[@class="clickable "]/parent::tbody/parent::table[@class="match-table "]/thead/tr[@class="subheader"]/th[@class="comp-date"]/text()')
#This will create a list of the times of the fixtures
#pltime = tree.xpath('//td[@class="status"]/text() ')

flag = False

main = int(raw_input("\nSelect the league for which the fixtures for the current calendar year have to be displayed:\n1.UEFA Champions League\n2.English Premier League(EPL)\n3.La Liga\n4.Bundesliga\n5.French Ligue 1\n6.Italian Serie A\n"))

#Comment -try this
#
# main = int(raw_input("""
#    \nSelect the league for which the fixtures for the current calendar year have to be displayed:\n
#    1.UEFA Champions League\n
#    2.English Premier League(EPL)\n
#    3.La Liga\n
#    4.Bundesliga\n
#    5.French Ligue 1\n
#    6.Italian Serie A\n
# """
if(main == 1):
    print "Loading.."
    page = requests.get('http://www.goal.com/en-india/fixtures/uefa-champions-league/10?ICID=FX')
    tree = html.fromstring(page.text)
    uclhome = tree.xpath('//div[@class="module module-team simple home"]/span/text()')
    uclaway = tree.xpath('//div[@class="module module-team simple away"]/span/text()')
    b = len(uclhome)
    choice = int(raw_input("Enter one of the choices from below:\n1.Print the only important fixtures of UCL \n2.Print the UCL fixtures by team\n"))
    if(choice == 1):
           print "Loading.."
           page = requests.get('http://www.goal.com/en-india/tables/uefa-champions-league/10')
           tree = html.fromstring(page.text)
           tempTeamName = tree.xpath('//td[@class="legend team short"]/a[starts-with(@href, "/en-india/teams/")]/text()')
           teamRank = tree.xpath('//td[@class="legend position"]/text()')
           for temp_team in tempTeamName:
                teamName += [temp_team[1:][:-1]]
           c = len(teamRank)
           topTeams =[teamName[i] for i in range(0,c) if(teamRank[i] == "1" or teamRank[i] == "2" or teamRank[i] == "3")]
           important(uclhome,uclaway,b,topTeams)

    if(choice == 2):
           print "Loading.."
           find_by = raw_input("Enter the team name(starting with a capital letter):\n")
           print("\nThe fixtures for the team you entered for the current season are:\n")
           find(uclhome,uclaway,b,find_by)
        
if(main == 2):
    print "Loading.."
    page = requests.get('http://www.goal.com/en-india/fixtures/premier-league/8')
    tree = html.fromstring(page.text)
    plhome = tree.xpath('//div[@class="module module-team simple home"]/span/text()')
    plaway = tree.xpath('//div[@class="module module-team simple away"]/span/text()')
    a=len(plhome)
    choice = int(raw_input("Enter one of the choices from below:\n1.Print the important fixtures of EPL for the current calendar year.\n2.Print the EPL fixtures by team\n"))
    if(choice == 1):
        print "Loading.."
        page = requests.get('http://www.goal.com/en-india/results-standings/64/english-premier-league-epl/table?ICID=FX_TN_103')
        tree = html.fromstring(page.text)
        #Get the standings in an array
        standings = tree.xpath('//td[@class="legend team short"]/a[starts-with(@href, "/en-india/teams/england/")]/text()')
        ln=len(standings)
        for i in range(0,ln):
            standings[i] = standings[i].split("\n")[1][:-1]
        print standings
        topTeams = [standings[i] for i in range(0,5)]
        important(plhome,plaway,a,topTeams)

    if(choice == 2):    
        find_by = raw_input("Enter the team name(starting with a capital letter):\n")
        print("\nThe fixtures for the team you entered for the current season are:\n")
        find(plhome,plaway,a,find_by)

if(main == 3):
    print "Loading.."
    page = requests.get('http://www.goal.com/en-india/fixtures/primera-divisi%C3%B3n/7')
    tree = html.fromstring(page.text)
    llhome = tree.xpath('//div[@class="module module-team simple home"]/span/text()')
    llaway = tree.xpath('//div[@class="module module-team simple away"]/span/text()')
    d = len(llhome)
    choice = int(raw_input("Enter one of the choices from below:\n1.Print the important fixtures of La Liga for the current calendar year.\n2.Print the La Liga fixtures by team\n"))
    if(choice == 1):
        print "Loading.."
        page = requests.get('http://www.goal.com/en-india/tables/primera-divisi%C3%B3n/7')
        tree = html.fromstring(page.text)
        #Get the standings in an array
        standings = tree.xpath('//td[@class="legend team short"]/a[starts-with(@href, "/en-india/teams/spain/")]/text()')
        ln = len(standings)
        for i in range(0,ln):
            standings[i] = standings[i].split("\n")[1][:-1]
        topTeams = [standings[i] for i in range(0,5)]
        important(llhome,llaway,d,topTeams)

    if(choice == 2):    
        find_by = raw_input("Enter the team name(starting with a capital letter):\n")
        print("\nThe fixtures for the team you entered for the current season are:\n")
        find(llhome,llaway,d,find_by)

if(main == 4):
    print "Loading.."
    page = requests.get('http://www.goal.com/en-india/fixtures/bundesliga/9')
    tree = html.fromstring(page.text)
    blhome = tree.xpath('//div[@class="module module-team simple home"]/span/text()')
    blaway = tree.xpath('//div[@class="module module-team simple away"]/span/text()')
    e = len(blhome)
    choice = int(raw_input("Enter one of the choices from below:\n1.Print the important fixtures of BundesLiga for the current calendar year.\n2.Print the BundesLiga fixtures by team\n"))
    if(choice == 1):
        print "Loading.."
        page = requests.get('http://www.goal.com/en-india/tables/bundesliga/9')
        tree = html.fromstring(page.text)
        #Get the standings in an array
        standings = tree.xpath('//td[@class="legend team short"]/a[starts-with(@href, "/en-india/teams/germany/")]/text()')
        ln = len(standings)
        for i in range(0,ln):
            standings[i] = standings[i].split("\n")[1][:-1]
        topTeams = [standings[i] for i in range(0,5)]
        chop(topTeams)
        important(blhome,blaway,e,topTeams)

    if(choice == 2):    
        find_by = raw_input("Enter the team name(starting with a capital letter):\n")
        print("\nThe fixtures for the team you entered for the current season are:\n")
        find(blhome,blaway,e,find_by)

if(main == 5):
    print "Loading.."
    page = requests.get('http://www.goal.com/en-india/fixtures/ligue-1/16')
    tree = html.fromstring(page.text)
    l1home = tree.xpath('//div[@class="module module-team simple home"]/span/text()')
    l1away = tree.xpath('//div[@class="module module-team simple away"]/span/text()')
    f = len(l1home)
    choice = int(raw_input("Enter one of the choices from below:\n1.Print the important fixtures of Ligue 1 for the current calendar year.\n2.Print the Ligue 1 fixtures by team\n"))
    if(choice == 1):
        print "Loading.."
        page = requests.get('http://www.goal.com/en-india/tables/ligue-1/16')
        tree = html.fromstring(page.text)
        #Get the standings in an array
        standings = tree.xpath('//td[@class="legend team short"]/a[starts-with(@href, "/en-india/teams/france/")]/text()')
        ln = len(standings)
        for i in range(0,ln):
            standings[i] = standings[i].split("\n")[1][:-1]
        topTeams = [standings[i] for i in range(0,5)]
        chop(topTeams)
        important(l1home,l1away,f,topTeams)

    if(choice == 2):    
        find_by = raw_input("Enter the team name(starting with a capital letter):\n")
        print("\nThe fixtures for the team you entered for the current season are:\n")
        find(l1home,l1away,f,find_by)

if(main == 6):
    print "Loading.."
    page = requests.get('http://www.goal.com/en-india/fixtures/serie-a/13')
    tree = html.fromstring(page.text)
    sahome = tree.xpath('//div[@class="module module-team simple home"]/span/text()')
    saaway = tree.xpath('//div[@class="module module-team simple away"]/span/text()')
    g = len(sahome)
    choice = int(raw_input("Enter one of the choices from below:\n1.Print the important fixtures of Serie A for the current calendar year.\n2.Print the Serie A fixtures by team\n"))
    if(choice == 1):
        print "Loading.."
        page = requests.get('http://www.goal.com/en-india/tables/serie-a/13')
        tree = html.fromstring(page.text)
        #Get the standings in an array
        standings = tree.xpath('//td[@class="legend team short"]/a[starts-with(@href, "/en-india/teams/italy/")]/text()')
        ln = len(standings)
        for i in range(0,ln):
            standings[i] = standings[i].split("\n")[1][:-1]
        topTeams = [standings[i] for i in range(0,5)]
        chop(topTeams)
        important(sahome,saaway,g,topTeams)

    if(choice == 2):    
        find_by = raw_input("Enter the team name(starting with a capital letter):\n")
        print("\nThe fixtures for the team you entered for the current season are:\n")
        find(sahome,saaway,g,find_by)

# Yash trials
page = requests.get('http://www.goal.com/en-india/fixtures/premier-league/8?ICID=TA_TN_133')
tree = html.fromstring(page.text)
date_list = tree.xpath('//th[@class="comp-date"]/text()')
home_list = tree.xpath('//div[@class="module module-team simple home"]/span/text()')
time_list = tree.xpath('//@data-match-time')
print date_list
print home_list
print time_list
print "Length of date list is %d" % len(date_list)
print "Length of home list is %d" % len(home_list)
print "Length of time list is %d" % len(time_list)
real_date = []
for time in time_list:
    match_details = datetime.fromtimestamp(int(time))
    temp = {
        'month':match_details.month,
        'day':match_details.day,
        'year':match_details.year,
        'time':match_details.strftime('%H:%M')
    }
    real_date.append(temp)

# The real_date is a list , each index of this list contains a dictionary regarding match timing details , convert numerical month to normal
# month later ( ie . 10 -- October)
# The for loop is where all the magic happens
# @avijit - Challenge Accepted and Completed

# Notes for refactoring
# All urls can be made modular by converting into constants
# Better variable names
# Better Function names
# An option to show the standings


#for time in time_list:
#    if time >= prev_time and time != time_list[0]:
#        real_date.append(date_list[counter_date])
#        real_date_counter += 1
#        prev_time = time
#    elif time != time_list[0]:
#        counter_date += 1
#        real_date.append(date_list[counter_date])
#        real_date_counter += 1
#        prev_time = time

print real_date
print len(real_date)
