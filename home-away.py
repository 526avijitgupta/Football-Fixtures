from lxml import html
import requests

def checkflag():
    if(not flag):
        print "Your input did not match any fixtures!"

def find(hometeam, awayteam , length , find_by):
    for i in range(0,length):
        if(hometeam[i] == find_by or awayteam[i] == find_by):
            print ("%s Vs %s" % (hometeam[i] , awayteam[i]))
            flag = True

def important(hometeam, awayteam, length, topTeams):
        print "The list of important fixtures of the selected league (involving top teams) :\n"
        for i in range(0,length):
            if(hometeam[i] and awayteam[i]) in topTeams:            
                print  ("%s Vs %s" % (hometeam[i] , awayteam[i]))
                flag = True 

#This will create a list of home teams:

#This will create a list of away teams


#This will create a list of the dates of the fixtures
#pldate = tree.xpath('//div[@class="module module-team simple home"]/parent::td[@class="team"]/parent::tr[@class="clickable "]/parent::tbody/parent::table[@class="match-table "]/thead/tr[@class="subheader"]/th[@class="comp-date"]/text()')
#This will create a list of the times of the fixtures
#pltime = tree.xpath('//td[@class="status"]/text() ')

flag = False

main = int(raw_input("Select the league for which the fixtures for the current calendar year have to be displayed:\n1.UEFA Champions League\n2.English Premier League(EPL)\n3.La Liga\n3.Bundesliga\n4.French Ligue 1\n5.Italian Series A\n"))

if(main == 1):
    print "Loading.."
    page = requests.get('http://www.goal.com/en-india/fixtures/uefa-champions-league/10?ICID=FX')
    tree = html.fromstring(page.text)
    uclhome = tree.xpath('//div[@class="module module-team simple home"]/span/text()')
    uclaway = tree.xpath('//div[@class="module module-team simple away"]/span/text()')
    b = len(uclhome)
    choice = int(raw_input("Enter one of the choics from below:\n1.Print the only important fixtures of UCL \n2.Print the UCL fixtures by team\n"))
    if(choice == 1):
           print "Loading.."
           page = requests.get('http://www.goal.com/en-india/live-scores/standings/date/2014-07-21/tab/all?ICID=OP')
           tree = html.fromstring(page.text)
           teamName = tree.xpath('//td[@class="teamName"]/text() ')
           teamRank = tree.xpath('//td[@class="teamRank"]/text() ')
           c = len(teamRank)
           topTeams =[teamRank[i] for i in range(0,c) if(teamRank[i] == "1" or teamRank[i] == "2" or teamRank[i] == "3")]

           #print ("The length of the top teams is: %d " % (len(topTeams)))  

           important(uclhome,uclaway,b,topTeams)
           checkflag()

    if(choice == 2):
           print "Loading.."
           find_by = raw_input("Enter the team name(starting with a capital letter):\n")
           print("\nThe fixtures for the team you entered for the current season are:\n")
           find(uclhome,uclaway,b,find_by)
           checkflag()
        
if(main == 2):
    print "Loading.."
    page = requests.get('http://www.goal.com/en-india/fixtures/premier-league/8')
    tree = html.fromstring(page.text)
    plhome = tree.xpath('//div[@class="module module-team simple home"]/span/text()')
    plaway = tree.xpath('//div[@class="module module-team simple away"]/span/text()')
    a=len(plhome)
    choice = int(raw_input("Enter one of the choics from below:\n1.Print the important fixtures of EPL for the calendar year 2014-2015\n2.Print the EPL fixtures by team\n"))
    if(choice == 1):
        print "Loading.."
        page = requests.get('http://www.goal.com/en-india/results-standings/64/english-premier-league-epl/table?ICID=FX_TN_103')
        tree = html.fromstring(page.text)
        #Get the standings in an array
        standings = tree.xpath('//a[starts-with(@href, "/en-india/teams/england/")]/text()')
        topTeams = [standings[i] for i in range(0,5)]
        important(plhome,plaway,a,topTeams)
        checkflag()

    if(choice == 2):    
        find_by = raw_input("Enter the team name(starting with a capital letter):\n")
        print("\nThe fixtures for the team you entered for the current season are:\n")
        find(plhome,plaway,a,find_by)
        checkflag()
