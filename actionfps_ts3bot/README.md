# ActionFPS TS3 Bot


## Prerequisite

##### Install pip
Pip is a better alternative to Easy Install for installing Python packages.
```
apt-get install python-pip
```

##### Install sseclient
This is a Python client library for iterating over http Server Sent Event (SSE) streams.
```
pip install sseclient
```

##### Install python-ts3
python-ts3 is a abstraction library around the Teamspeak 3 ServerQuery API.
```
git clone git://github.com/nikdoof/python-ts3.git
cd python-ts3
python setup.py install
```


## Installation Spam Bot 

##### Clone the script
```
git clone https://github.com/Paul255/actionfps_ts3bot.git
```

##### login & password
Make sure the user you are using can send global messages

Create a config.json file next to ts3bot.py and fill in your login/password

```json
{
	"login": "serveradmin",
	"password":"yourpassword"
}
```


## Getting started

##### Run the script
```
python ts3bot.py
```

![GitHub Logo](https://files.gitter.im/ScalaWilliam/ActionFPS/uIgf/inter.jpg)

