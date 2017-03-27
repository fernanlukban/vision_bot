const Discord = require("discord.js");
const client = new Discord.Client();
const commandPrefix = '$';

client.on('ready', () => {
  console.log(`Logged in as ${client.user.username}!`);
});

client.on('message', msg => {
  if (msg.content.startsWith(commandPrefix)){
  	doAction(msg)
  }
});

function doAction(msg){

	content = msg.content.split(" ");
	command = content[0].slice(commandPrefix.length);
	args = content.slice(1);

	console.log(command, args);

	if (command === 'ping'){
		msg.reply('pong');
	} else if (command === '$init'){
		numOfTeams = args[0]
		startTournament(msg, numOfTeams);
	} else if (command === '$delete'){
		deleteAllChannels(msg);
	}
};


function startTournament(msg, numOfTeams){
	createChannels(msg, numOfTeams);
}

function createChannels(msg, numOfTeams){
	var channelsCreated = new Array();
	for (var channel of msg.guild.channels){
		//console.log(RegExp(`Team {1,${numOfTeams}}`).test(channel[1].name));
		//if (channel instanceof Discord.VoiceChannel){
			if (RegExp(`Team {1,${numOfTeams}}`).test(channel[1].name)){
				var number = Number(channel[1].name.split(" ")[1]);
				if (!channelsCreated.includes(number)){
					channelsCreated.push(number);
				}
				console.log(`Team ${number} channel found!`);
			}
		//}
	}
	//console.log(channelsCreated);
	for (var i = 1; i <= numOfTeams; i++){
		if (!channelsCreated.includes(i)){
			msg.guild.createChannel(`Team ${i}`, 'voice');
			console.log(`Team ${i} channel created!`);
		}
	}
}

function deleteAllChannels(msg){
	for (var channel of msg.guild.channels){
		//console.log(channel);
		channel[1].delete();
	}
}

client.login('MjkzMjU5NjQ4OTE0Njg1OTU0.C7oreg.8MWVuxlpgjU9hpU8290eYqHy-ZM');
