import discord
import time
from colorama import Fore
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)

@client.event #Bot Online Status
async def on_ready():
    print(f'''{Fore.MAGENTA}
███████╗███████╗░█████╗░████████╗██╗░░██╗███████╗██████╗░██╗███╗░░██╗███████╗
██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔══██╗██║████╗░██║██╔════╝
█████╗░░█████╗░░███████║░░░██║░░░███████║█████╗░░██████╔╝██║██╔██╗██║█████╗░░
██╔══╝░░██╔══╝░░██╔══██║░░░██║░░░██╔══██║██╔══╝░░██╔══██╗██║██║╚████║██╔══╝░░
██║░░░░░███████╗██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║██║██║░╚███║███████╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝
    ''')
    time.sleep(1)
    print(f'''{Fore.MAGENTA} 
    Made By Featherine#3810
    Github : https://github.com/Featherineee
    Prefix : $ , $massdm
    ''')
    await client.change_presence(
    status=discord.Status.do_not_disturb,
    activity=discord.Game(name='https://github.com/Featherineee'))

@client.command() #Mass DM Command
async def massdm(ctx):
        msg = input('Input Message You Want To Send: ')
        members = ctx.guild.members
        for member in members:
            try:
                print(f'{Fore.GREEN}[+]{Fore.RESET}Direct Message Sent To {member}')
                await member.send(msg)
            except:
                print(f'{Fore.RED}[-]{Fore.RESET}Cant Send Direct Message {member}\n')
        


client.run('') #Input your discord bot token here
