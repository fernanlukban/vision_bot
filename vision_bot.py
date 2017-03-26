import discord
from discord.ext.commands import Bot
import praw

vision_bot = Bot(command_prefix='$')

reddit_bot = praw.Reddit(client_id='viEg-tLBWjn2iw',
                     client_secret='KYgB2k8cH7n056nHdDqwQ4VbLcQ',
                     username='vision_bot',
                     password='ayylmao',
                     user_agent='/u/opsadboys')

reddit_bot.read_only = True

QUERY_SEARCH_TYPE = {'hot': lambda sub, lim: reddit_bot.subreddit(sub).hot(limit=lim),
               'top': lambda sub, lim: reddit_bot.subreddit(sub).top(limit=lim),
               'new': lambda sub, lim: reddit_bot.subreddit(sub).new(limit=lim),
               'controversial': lambda sub, lim: reddit_bot.subreddit(sub).controversial(limit=lim)
               }

#print(vision_bot.command

@vision_bot.event
async def on_ready(*args):
    print('VISION BOT\n----------------------------\nFucking with the vision!\n----------------------------\nREADY')
    #print(vision_bot.commands)

@vision_bot.command()
async def hello(*args):
    return await vision_bot.say('Let\'s link up man I\'m tryna build!')

@vision_bot.event
async def on_message(message):
    #print(message, type(message), message.author)
    if message.content.startswith(vision_bot.command_prefix):
        if message.content.startswith(vision_bot.command_prefix + 'help'):
            await vision_bot.send_message(message.author, help_text)
        elif message.content.split()[0][1:] not in vision_bot.commands:
            await vision_bot.send_message(message.channel, 'I don\'t think you fuck with the vision! The command "{}" was not found!'.format(message.content.split()[0][1:]))
        else:
            await vision_bot.process_commands(message)

@vision_bot.command()
async def vision(*args):
    await vision_bot.say('```VVV        VVV  III    SSSSSSSS    III   OOOOOOOOO   NNN    NN\n\
 VVV      VVV   III   SSS    SSS   III   OO     OO   NNNN   NN\n\
  VVV    VVV    III     SSS        III   OO     OO   NN NN  NN\n\
   VVV  VVV     III        SSS     III   OO     OO   NN  NN NN\n\
    VVVVVV      III   SSS    SSS   III   OO     OO   NN   NNNN\n\
     VVVV       III    SSSSSSSS    III   OOOOOOOOO   NN    NNN```')

@vision_bot.command()
async def reddit(*args):
    lim = 5 if len(args) < 3 else int(args[-1])
    sub = args[0]
    order = 'hot' if len(args) < 2 else args[1]
    search_type = QUERY_SEARCH_TYPE.get(order, reddit_bot.subreddit(sub).hot(limit=lim))(sub, lim)
    if lim > 15:
        print(f'Failed to search {sub} for {order} {lim} posts')
        await vision_bot.say("Looking for too many posts!")
    else:
        print(f'Successfully searched {sub} for {order} {lim} posts')
        await vision_bot.say(" ".join([f"{submission_num+1}. {submission.title} -- {submission.url}\n\n" for submission_num, submission in enumerate(search_type)]))

@vision_bot.command()
async def henlo(*args):
    await reddit('clopclop', 'hot', '10')

#vision_bot.add_listener(lambda x: print(3), )
help_text = '\n'.join([f'Commands: {len(vision_bot.commands)}']+list(vision_bot.commands.keys()))
vision_bot.run('MjkzMjU5NjQ4OTE0Njg1OTU0.C7D-4A.I89_lvqP9bkwwNl8pzyXpbwFo8A')