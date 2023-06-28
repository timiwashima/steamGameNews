# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:43:27 2023
Steam Game News
@author: tiwashima
"""
import requests
import datetime

gameName=input("What game do you want news on? ")
gameName=gameName.lower()

steamDBdictionary={
    'ace combat 7':502500,'ace combat 7: skies unknown':502500,
    'alone in the dark':1310410,
    'cities: skylines':255710,'cities:skylines':255710,'cities skylines':255710,'cities: sky lines':255710, 'cities:sky lines':255710,
    'cities: skylines 2':949230,'cities:skylines2':949230,'cities:skylines 2':949230,'cities skylines 2':949230,'cities sky lines 2':949230,'cities skylines ii':949230,'cities sky lines ii':949230,
    'counterstrike':10,'counter strike':10,'counter-strike':10,
    'cult of the lamb':1313140,
    'dead or alive xtreme venus vacation':958260,'doa xtreme venus vacation':958260,'doaxvv':958260,'dead or alive: xtreme venus vacation':958260,'dead or alive:xtreme venus vacation':958260,'dead or alive:xvv':958260,'doa:xtreme venus vacation':958260,'doa: '
    'elder scrolls iii morrowind':22320,'the elder scrolls iii morrowind':22320,'the elder scrolls iii: morrowind':22320,'elder scrolls 3':22320,'elder scrolls iii':22320,'tesiii':22320,'tes3':22320,'tes3:morrowind':22320,'morrowind':22320,
    'elder scrolls v skyrim':72850,'the elder scrolls v skyrim':72850,'the elder scrolls v: skyrim':72850,'elder scrolls 5':72850,'elder scrolls v':72850,'the elder scrolls 5':72850,'tesv:skyrim':72850,'skyrim':72850,'tes5':72850,'tesv':72850,
    'factorio':427520,
    'fall guys':1097150,'fallguys':1097150,
    'half life 2':220,'half-life 2':220,'half life: 2':220,'half-life:2':220,
    'lost ark':1599340,'lostark':1599340,
    'mass effect':1328670,'mass effect legendary edition':1328670,'mass effect: legendary edition':1328670,
    'monster hunter rise':1446780,'monster hunter: rise':1446780,'monsterhunter rise':1446780,'monsterhunter: rise':1446780,
    'monster hunter rise sunbreak':1880360,'monster hunter rise: sunbreak':1880360,'monsterhunter rise: sunbreak':1880360,'monster hunter rise sun break':1880360,'monsterhunter rise: sun break':1880360,'monsterhunter rise sunbreak':1880360,
    'monster hunter stories 2':1277400,'monster hunter stories 2: wings of ruin':1277400,'monsterhunter stories 2: wings of ruin':1277400,'monster hunter stories 2 wings of ruin':1277400,
    'monster hunter world':582010,'monster hunter: world':582010,'mhw':582010,'monsterhunter world':582010,
    'monster hunter world iceborne':1118010,'monster hunter world: iceborne':1118010,'monsterhunter world iceborne':582010,'monsterhunter world: iceborne':582010,
    'nickelodeon all star brawl':1414850,'nickelodeon: all star brawl':1414850,'nickelodeon all-star brawl':1414850,'nickelodeon: all-star brawl':1414850,
    'street fighter 4':45760,'street fighter iv':45760,'sf4':45760,'sfiv':45760,'ultra street fighter iv':45760,'ultra street fighter 4':45760,
    'street fighter 5':310950,'street fighter v':310950,'sf5':310950,'sfv':310950,
    'street fighter 6':1364780,'street fighter vi':1364780,'sf6':1364780,'sfvi':1364780,
    'stardew valley': 413150,'star dew valley': 413150,
    'starfield':1716740,'star field':1716740,
    'tactics ogre reborn':1451090,'tactics ogre: reborn':1451090,'tactics ogre':1451090,
    'team fortress 2':440,'tf2':440,'teamfortress2':440,
    'tekken 7':389730,'tekken7':389730,
    'tekken 8':1778820,'tekken8':1778820,
    'witcher 3':292030,'witcher iii':292030,'the witcher 3':292030,'the witcher iii':292030,'the witcher 3: wild hunt':292030,'the witcher iii: wild hunt':292030,'the witcher 3 wild hunt':292030,'the witcher iii wild hunt':292030,'wild hunt':292030,'wildhunt':292030,
            }

appID=steamDBdictionary[gameName]
    
url='http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=' + str(appID) + '&count=5&maxlength=300&format=json'
r=requests.get(url)

#print(r.status_code)

responseDict=r.json()

responseNews=responseDict['appnews']
newsItems=responseNews['newsitems']

for news in range(0,len(newsItems)):
    newsDict=newsItems[news]
    time=datetime.datetime.fromtimestamp(newsDict['date']).strftime('%A, %B %d, %Y, %H:%M')
    print(newsDict['title'])
    print(time)
    print('by ' + newsDict['author'])
    print(newsDict['contents'])
    print(newsDict['url'])
    print()
