import json
import ts3
from sseclient import SSEClient
from TS3Escape import TS3Escape

print "Bot started"

try:
	with open('config.json') as config:
		config = json.load(config)
	login = config['login']
	password = config['password']
except Exception:
	print "Could not load config.json, make sure it is present"
	exit(1)

print "Config loaded"

while True:
	messages = SSEClient('http://actionfps.com/inters/')
	for message in messages:
		if message.data:
			server = ts3.TS3Server('127.0.0.1', 10011)
			server.login(login, password)
			server.use(1)
			print 'Bot connected'
			data = json.loads(message.data)
	                serverName = str(data['serverName'])
	                playerName = data['playerName']
        	        serverConnect = data['serverConnect']
                	event = message.event
	                msg = playerName + ' started an ' + event + ' and is looking for players on '
			msg = str(msg)
			msg = TS3Escape.escape(msg)
			msg = msg + '[url='+serverConnect+']'+TS3Escape.escape(serverName)+'[/url]'
			if server.send_command('gm msg='+msg).is_successful:
				print str(message.id) + msg
			if server.send_command('quit').is_successful:
				print 'Bot disconnected'

