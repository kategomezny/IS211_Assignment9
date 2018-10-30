#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CBS Football Stats"""

import urllib2
import bs4 as bs

sauce = urllib2.urlopen("https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns")
html = sauce.read()

soup = bs.BeautifulSoup(html,"lxml")


touchdowns_table = soup.findAll("table", attrs={"class":"data"})[0].findAll('tr', attrs={"valign":"top"})

def Twenty_Players():
    """Finds the first 20 players with the most touchdowns and prints them"""
    touchdowns = 0
    print "The first 20 players with the most touchdowns are: "
    for i in touchdowns_table:
        player_name = i.findAll('td')[0].findAll('a')[0].contents[0]
        position_player = i.findAll('td')[1].contents[0]
        team =  i.findAll('td')[2].findAll('a')[0].contents[0]
        Number_of_touchdowns = i.findAll('td')[6].contents[0]
        touchdowns += 1
        print ("Player rank: {}, Player Name: {}, Position: {}, "
               "Team: {}, TDs: {}").format(touchdowns, player_name, position_player, team, Number_of_touchdowns)
        if touchdowns >= 20:
            break

def main():
    Twenty_Players()

if __name__ == '__main__':
    main()
