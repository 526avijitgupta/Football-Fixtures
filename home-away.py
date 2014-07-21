from lxml import html
import requests

def find(hometeam, awayteam , length , find_by):
    for i in range(0,length):
        if(hometeam[i] == find_by or awayteam[i] == find_by):
            print ("%s Vs %s" % (hometeam[i] , awayteam[i]))
            flag = True
    if(not flag):
        print "Your input did not match any fixtures!"

def important(hometeam, awayteam, length, topTeams):
    print "The list of important fixtures of the selected league (involving top teams) :\n"
    for i in range(0,length):
        if(hometeam[i] and awayteam[i]) in topTeams:            
            print  ("%s Vs %s" % (hometeam[i] , awayteam[i]))
            flag = True
    if(not flag):
        print "Your input did not match any fixtures!"
        
#This will create a list of home teams:

#This will create a list of away teams


#This will create a list of the dates of the fixtures
#pldate = tree.xpath('//div[@class="module module-team simple home"]/parent::td[@class="team"]/parent::tr[@class="clickable "]/parent::tbody/parent::table[@class="match-table "]/thead/tr[@class="subheader"]/th[@class="comp-date"]/text()')
#This will create a list of the times of the fixtures
#pltime = tree.xpath('//td[@class="status"]/text() ')

flag = False

main = int(raw_input("Select the league for which the fixtures for the current calendar year have to be displayed:\n1.UEFA Champions League\n2.English Premier League(EPL)\n3.La Liga\n4.Bundesliga\n5.French Ligue 1\n6.Italian Serie A\n"))

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
           page = requests.get('http://www.goal.com/en-india/live-scores/standings/date/2014-07-21/tab/all?ICID=OP')
           tree = html.fromstring(page.text)
           teamName = tree.xpath('//td[@class="teamName"]/text() ')
           teamRank = tree.xpath('//td[@class="teamRank"]/text() ')
           c = len(teamRank)
           topTeams =[teamRank[i] for i in range(0,c) if(teamRank[i] == "1" or teamRank[i] == "2" or teamRank[i] == "3")]

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
        standings = tree.xpath('//td[@class="fcName"]/a[starts-with(@href, "/en-india/teams/england/")]/text()')
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
        page = requests.get('http://www.goal.com/en-india/results-standings/61/la-liga/table')
        tree = html.fromstring(page.text)
        #Get the standings in an array
        standings = tree.xpath('//td[@class="fcName"]/a[starts-with(@href, "/en-india/teams/spain/")]/text()')
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
        page = requests.get('http://www.goal.com/en-india/results-standings/47/1-bundesliga/table?ICID=OP')
        tree = html.fromstring(page.text)
        #Get the standings in an array
        standings = tree.xpath('//td[@class="fcName"]/a[starts-with(@href, "/en-india/teams/germany/")]/text()')
        topTeams = [standings[i] for i in range(0,5)]
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
        page = requests.get('http://www.goal.com/en-india/results-standings/60/ligue-1/table?ICID=OP')
        tree = html.fromstring(page.text)
        #Get the standings in an array
        standings = tree.xpath('//td[@class="fcName"]/a[starts-with(@href, "/en-india/teams/france/")]/text()')
        topTeams = [standings[i] for i in range(0,5)]
        print topTeams
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
        page = requests.get('http://www.goal.com/en-india/results-standings/69/serie-a/table?ICID=OP')
        tree = html.fromstring(page.text)
        #Get the standings in an array
        standings = tree.xpath('//td[@class="fcName"]/a[starts-with(@href, "/en-india/teams/italy/")]/text()')
        topTeams = [standings[i] for i in range(0,5)]
        print topTeams
        important(sahome,saaway,g,topTeams)

    if(choice == 2):    
        find_by = raw_input("Enter the team name(starting with a capital letter):\n")
        print("\nThe fixtures for the team you entered for the current season are:\n")
        find(sahome,saaway,g,find_by)
