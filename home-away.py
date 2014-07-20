from lxml import html
import requests

def manu(plhome, plaway, a):
    for i in range(0,a):
        if(plhome[i] == "Manchester United" or plaway[i] == "Manchester United"):
            print  ("%s Vs %s" % (plhome[i] , plaway[i]))

def mancity(plhome, plaway, a):
    for i in range(0,a):
        if(plhome[i] == "Manchester City" or plaway[i] == "Manchester City"):
            print  ("%s Vs %s" % (plhome[i] , plaway[i]))

def liverpool(plhome, plaway, a):
    for i in range(0,a):
        if(plhome[i] == "Liverpool" or plaway[i] == "Liverpool"):
            print  ("%s Vs %s" % (plhome[i] , plaway[i]))

def arsenal(plhome, plaway, a):
    for i in range(0,a):
        if(plhome[i] == "Arsenal" or plaway[i] == "Arsenal"):
            print  ("%s Vs %s" % (plhome[i] , plaway[i]))

def chelsea(plhome, plaway, a):
    for i in range(0,a):
        if(plhome[i] == "Chelsea" or plaway[i] == "Chelsea"):
            print  ("%s Vs %s" % (plhome[i] , plaway[i]))

def important(plhome, plaway, a):
        print "The list of important fixtures of EPL (involving top teams) :\n"
        for i in range(0,a):
            if(plhome[i] == standings[0] or plhome[i] == standings[1] or plhome[i] == standings[2] or plhome[i] == standings[3] or plhome[i] == standings[4] or plhome[i] == standings[5]):
                if(plaway[i] == standings[0] or plaway[i] == standings[1] or plaway[i] == standings[2] or plaway[i] == standings[3] or plaway[i] == standings[4] or plaway[i] == standings[5]):
                    print  ("%s Vs %s" % (plhome[i] , plaway[i]))

    
page = requests.get('http://www.goal.com/en-india/fixtures/premier-league/8')
tree = html.fromstring(page.text)

#This will create a list of home teams:
plhome = tree.xpath('//div[@class="module module-team simple home"]/span/text()')
#This will create a list of away teams
plaway = tree.xpath('//div[@class="module module-team simple away"]/span/text()')

#This will create a list of the dates of the fixtures
#pldate = tree.xpath('//div[@class="module module-team simple home"]/parent::td[@class="team"]/parent::tr[@class="clickable "]/parent::tbody/parent::table[@class="match-table "]/thead/tr[@class="subheader"]/th[@class="comp-date"]/text()')
#This will create a list of the times of the fixtures
#pltime = tree.xpath('//td[@class="status"]/text() ')

a=len(plhome)

choice = int(raw_input("Enter one of the choics from below:\n1.Print the important fixtures of EPL for the calendar year 2014-2015\n2.Print the EPL fixtures by team\n"))

if(choice == 1):
    print "Loading.."
    page = requests.get('http://www.goal.com/en-india/results-standings/64/english-premier-league-epl/table?ICID=FX_TN_103')
    tree = html.fromstring(page.text)
    #Get the standings in an array
    standings = tree.xpath('//a[starts-with(@href, "/en-india/teams/england/")]/text()')
    important(plhome,plaway,a)

if(choice ==2):
    team = int(raw_input("Select one of the teams from below\n1.Manchester United\n2.Manchester City\n3.Liverpool\n4.Arsenal\n5.Chelsea\n"))
    if(team == 1):
        print ("The Manchester United Premier League fixtures are as follows:\n")
        manu(plhome,plaway,a)
    if(team == 2):
        print ("\n The Manchester City Premier League fixtures are as follows: \n")
        mancity(plhome,plaway,a)
    if(team == 3):
        print ("\n The Liverpool Premier League fixtures are as follows: \n")
        liverpool(plhome,plaway,a)
    if(team == 4):
        print ("\n The Arsenal Premier League fixtures are as follows: \n")
        arsenal(plhome,plaway,a)
    if(team == 5):
        print ("\n The Chelsea Premier League fixtures are as follows: \n")
        chelsea(plhome,plaway,a)

