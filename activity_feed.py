import blaseball
import requests
import os.path
import time

url = 'https://www.blaseball.com/database'

#If a file for tracked games does not exist, get game IDs from blaseball API
if not os.path.exists('tracked_games.txt'):
	seasonNum = input('Game IDs not saved. Enter season to track: ')
	#Get round IDs from season playoffs
	endpoint = '/playoffs?number={}'.format(seasonNum)
	playoffs = blaseball.evalResponse(requests.get(url+endpoint))
	print('Playoff data recieved...')
	time.sleep(0.5)
	rounds = [r for r in playoffs['rounds']]
	#Get game IDs from playoff rounds
	for r in rounds:
		endpoint = 