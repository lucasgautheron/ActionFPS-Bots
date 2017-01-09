import ts3
import urllib, json

print "Channel creation bot started"

try:
	with open('config.json') as config:
		config = json.load(config)
	login = config['login']
	password = config['password']
	clanChannelID = config['clanChannelID']

except Exception:
	print "Could not load config.json, make sure it is present"
	exit(1)

url = "https://actionfps.com/clans/?format=json"
response = urllib.urlopen(url)
data = json.loads(response.read())

server = ts3.TS3Server('127.0.0.1', 10011)
server.login(login, password)
server.use(1)

print "Bot connected"

for clan in data:
	clanName = clan["fullName"]
	createChannel = True
	try: clan["teamspeak"]
	except KeyError:
		createChannel = False
	
	try: clan["website"]
	except KeyError:
		clan["website"] = ""

	if createChannel == False:
		#print "No teamspeak3 adress defined for clan "+clanName
		pass
	else:
		if "woop.ac" in clan["teamspeak"]:
			#print "Creating teamspeak3 channels for clan "+clanName
			if server.send_command('channelcreate', keys={'channel_name': clanName, 'channel_flag_permanent' : '1', 'cpid': clanChannelID, 'channel_description': '[img]'+clan["logo"]+'[/img]\n[url='+clan["website"]+']Website[/url]\n[url=https://actionfps.com/clan/?id='+clan["id"]+']Action FPS Clan Page[/url]'}).is_successful:
				for channel in server.send_command('channellist').data:
        				if channel['channel_name'] == clanName:
	                			channel_id = channel['cid']

				server.send_command('channelcreate', keys={'channel_name': 'Public', 'cpid': channel_id, 'channel_flag_permanent' : '1'})	
				server.send_command('channelcreate', keys={'channel_name': 'Private', 'cpid': channel_id, 'channel_flag_password': '1', 'channel_password': 'match', 'channel_flag_permanent' : '1'})
				print 'Created channel '+clanName+' and sub channels'
			else:
				pass
				#print 'Channel '+clanName+' already exists'
		else:
			pass
			#print "teamspeak3 server not in domain woop.ac"

if server.send_command('quit').is_successful:
	print 'Bot disconnected'
