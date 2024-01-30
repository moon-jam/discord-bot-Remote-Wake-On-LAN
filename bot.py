import discord
from wakeonlan import send_magic_packet
import subprocess
import time
from config import ip_address, port, mac, discord_bot_token, state_keywords, on_keywords

intents = discord.Intents.all()
discord.Intents.message_content = True
client = discord.Client(intents=intents)

def is_host_up(ip, port):
    # Nmap command for a specific port scan
    command = ["nmap", "-p", str(port), "-Pn", ip]
    try:
        # Execute the command and capture the output
        output = subprocess.check_output(command, stderr=subprocess.STDOUT).decode()
        # Check if the port is open based on Nmap's output
        if "open" in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.output.decode()}")
        return False

@client.event
# bot has been active
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
# when the bot has received a message
async def on_message(message):
    # ignore messages from bot
    if message.author == client.user:
        return
    
    #check computer state
    if message.content.lower().startswith(state_keywords):
        if is_host_up(ip_address, port):
            await message.channel.send("The computer is on!")
        else:
            await message.channel.send("The computer is off!")
        return
    
    #turn on computer
    if message.content.lower().startswith(on_keywords):
        for i in range(15):
            if is_host_up(ip_address, port):
                break
            else :
                send_magic_packet(mac)
                await message.channel.send("Processing...")
                time.sleep(2)
        if is_host_up(ip_address, port):
            await message.channel.send("The computer has already started up!")
        else:
            await message.channel.send("The computer failed to start!")
        return
    
    await message.channel.send("The keywords is invalid!")
    await message.channel.send("Your message should start with one of these keywords to check the computer state: ```" + ', '.join(state_keywords) + "```")
    await message.channel.send("Your message should start with one of these keywords to turn on the computer: ```" + ', '.join(on_keywords) + "```")

client.run(discord_bot_token)
