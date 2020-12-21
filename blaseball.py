import ast
import time
import requests

def evalResponse(response):
	t = response.text
	t = t.replace('false','False')
	t = t.replace('true','True')
	t = t.replace('null','None')
	d = eval(t)
	#d = d['data'] <- commented out because the blaseball api doesn't put everything inside another array, although the chronicler api does
	return d

def getAllUpdates(args):
	delay = 0.5
	url = 'https://api.sibr.dev/chronicler/v1'
	if 'season' not in args or 'game' in args:
		print('Invalid arguments. Do not call getAllUpdates with a game ID argument or without a season argument.')
		return []
	if 'day' in args:
		day = args['day']
		dayLimit = day+1
	else:
		dayLimit = 150
		day = 0
	args['count'] = 16
	gameIDs = []
	for i in range(day,dayLimit):
		args['day'] = str(i)
		games = evalResponse(requests.get(url+'/games', args))['data']
		if games == []:
			break
		for j in games:
			gameIDs.append(j['data']['id'])
		print('Games recieved for day {}'.format(i+1))
		time.sleep(delay)

	out = []
	count = 0
	total = len(gameIDs)
	args.pop('day')
	args.pop('season')
	args['count'] = 500
	for g in gameIDs:
		args['game'] = g
		updates = evalResponse(requests.get(url+'/games/updates', args))['data']
		for k in updates:
			out.append(k)
		count += 1
		print('Updates recieved for {}/{} games'.format(count,total))
		time.sleep(delay)
	return out

def searchChronicler(args, keyword=''):
	if 'season' in args:
		updates = getAllUpdates(args)
	else:
		updates = evalResponse(requests.get('https://api.sibr.dev/chronicler/v1/games/updates',args))['data']
	out = []
	for u in updates:
		if keyword == '' or u['data']['lastUpdate'].lower().find(keyword) >= 0:
			out.append(u)
	return out