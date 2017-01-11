const Discord = require('discord.js');
var client = new Discord.Client();
var EventSource = require('eventsource');

var cfgPath = require('confortable')('token.json', process.cwd());
if (!cfgPath) {
    throw new Error("Could not load token.json");
}
var cfg = require(cfgPath);
console.log(cfg.token);

client.login(cfg.token);

//var interSource = new EventSource("http://woop.ac:81/actionfps/inters/");

var interSource = new EventSource("https://actionfps.com/inters/");

var serverUpdateSource = new EventSource("https://actionfps.com/server-updates/");

var servers = new Array();

function countPlayers(server) {
  var players =  new Array();
  var index = 0;
  console.log('In countPlayers');
  //console.log(server);
  if( typeof server !== 'undefined') {
    if(typeof server.players !== 'undefined') {
      server.players.forEach(function(teams) {
        players[index] = teams.name;
        index++;
      });
    } else {
      //console.log(Object.keys(server.teams).length);
      server.teams.forEach(function(teams) {
        for (var i = 0; i < teams.players.length; i++) {
          players[index] = teams.players[i].name;
          index++;
        }
      });
    }
  }
  return players;
}

client.on('ready', () => {
  console.log('I am ready!');
  var channels = client.channels;
  var interChan = channels.find('name', 'inters');

  interSource.addEventListener('inter', function(e) {
    console.log("event inter");
    var inter = JSON.parse(e.data);
    var msg = '';
    //console.log(inter);
    var server = servers[inter.serverConnect];
    //console.log("Avant playercount");
    //console.log(server);
    var onlinePlayers = countPlayers(server);
    if( typeof servers[inter['serverConnect']] !== 'undefined') {
      var connect = servers[inter['serverConnect']].now.server.connectName;
      msg = '@everyone ' + inter.playerName + ' started an inter and is looking for players ```/connect ' + connect + '```' + onlinePlayers.length + ' players online';
      msg+='```';
      onlinePlayers.forEach(function(value){
        msg+=value + ' ';
      });
      msg+='```';
      console.log(msg);
      //interChan.sendMessage(msg)
      //   .then(message => console.log(`Bot : ${message.content}`))
      //   .catch(console.error);
    }
  }, false);

  serverUpdateSource.addEventListener('current-game-status', function(e) {
    var server = JSON.parse(e.data);
    //console.log('Received data for : ' + server.now.server.server);
    //console.log(server.now.server.server);
    servers[server.now.server.server] = server;
  }, false);

});
