const Discord = require("discord.js");
const client = new Discord.Client();
const commandPrefix = '$';


console.log(client.guilds);

client.on('ready', () => {
  console.log(`Logged in as ${client.user.username}!`);
});

client.on('message', msg => {
  if (msg.content.startsWith(commandPrefix)){
  	doAction(msg)
  }
});

function doAction(msg){
	if (msg.content.startsWith(commandPrefix + 'hello')){
		msg.reply('lol')
	}
};

client.login('MjkzMjU5NjQ4OTE0Njg1OTU0.C7oreg.8MWVuxlpgjU9hpU8290eYqHy-ZM');
