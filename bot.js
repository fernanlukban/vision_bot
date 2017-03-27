const Discord = require("discord.js");
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.username}!`);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('Pong!');
  }
  if (msg.content.startsWith('$')){
  	doAction(msg)
  }
});

function doAction(msg){
	if (msg.content.startsWith('$hello')){
		msg.reply('lol')
	}
};

client.login('MjkzMjU5NjQ4OTE0Njg1OTU0.C7oreg.8MWVuxlpgjU9hpU8290eYqHy-ZM');
