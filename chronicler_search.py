import requests
import blaseball
import ast
import time

args = {'season':'-1'}
keyword = input('Enter keyword: ')
out = blaseball.searchChronicler(args, keyword)
game = ''
for i in out:
	d = i['data']
	if i['gameId'] != game:
		season = d['season']
		day = d['day']
		home = d['homeTeamName']
		away = d['awayTeamName']
		print('\n{}/{} {} VS. {}'.format(season,day,home,away).upper())
		game = i['gameId']
	print(d['lastUpdate'])

input()
