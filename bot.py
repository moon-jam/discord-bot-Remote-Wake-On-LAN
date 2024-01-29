import discord
from wakeonlan import send_magic_packet
import subprocess
import time

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

# Example usage
ip_address = "Your local IP"  # Replace with the target IP address
port = 3389  # Replace with a port you expect to be open

intents = intents = discord.Intents.all()

intents.messages = True
discord.Intents.message_content = True

client = discord.Client(intents=intents)

# 調用event函式庫
@client.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {client.user}")

@client.event
# 當頻道有新訊息
async def on_message(message):
    # 排除機器人本身的訊息，避免無限循環
    if message.author == client.user:
        return
    if message.content == "state":
        if is_host_up(ip_address, port):
            await message.channel.send("The computer is on!")
        else:
            await message.channel.send("The computer is off!")
        return
    
    for i in range(15):
        if is_host_up(ip_address, port):
            break
        else :
            send_magic_packet('Your Mac Address')
            await message.channel.send("Processing...")
            time.sleep(2)
    if is_host_up(ip_address, port):
        await message.channel.send("The computer has already started up!")
    else:
        await message.channel.send("The computer failed to start!")

client.run('Your Discord Bot token')

