# Discord Bot for Remote Wake-On-LAN

## Overview

This project is a Discord bot that uses the Wake-on-LAN protocol to remotely wake up a computer via a small server. The bot listens to commands sent in Discord messages and uses the `nmap` tool to check the state of the target machine.

## Features

- Check the state of a remote computer (on/off).
- Remotely turn on a computer using the Wake-on-LAN protocol.
- Responds to commands sent via Discord messages.

## Setup

1. This application requires a small server, like a Raspberry Pi, that is always powered on to listen for commands and respond accordingly.
2. Clone the repository on your server.
3. Install the required Python packages using pip or pip3, depending on your system:

    ```bash
    # If pip is linked to Python 3 on your system
    pip install -r requirements.txt

    # If pip3 is linked to Python 3 on your system
    pip3 install -r requirements.txt
    ```

4. Install `nmap` on your system. Refer to the [official Nmap install guide](https://nmap.org/book/install.html) for instructions.
5. Run the bot with either python or python3, depending on your system:

    ```bash
    # If python is linked to Python 3 on your system
    python bot.py

    # If python3 is the command for Python 3 on your system
    python3 bot.py
    ```

## Configuration

Configuration variables are stored in `config.py`. You need to set the following:

- `ip_address`: The IP address of the target machine.
- `port`: The port to check for the machine's on/off state.
- `mac`: The MAC address of the target machine for Wake-on-LAN.
- `discord_bot_token`: The token of your Discord bot.
- `state_keywords`: The keywords that the bot responds to for checking the state of the machine.
- `on_keywords`: The keywords that the bot responds to for turning on the machine.

## FAQ

**Q: What is Wake-on-LAN?**  
A: Wake-on-LAN is a protocol that allows a computer to be turned on or awakened by a network message.

**Q: How do I get my Discord bot token?**  
A: You can get your Discord bot token from the Discord developer portal. Check out this [guide](https://www.writebots.com/discord-bot-token/) for more details.

**Q: The bot isn't responding to my commands. What's wrong?**  
A: Make sure that the bot has the necessary permissions in your Discord server and you have enabled 'Privileged Gateway Intents' for your bot in the Discord developer portal.  
![Access Privileged Gateway Intents](./pictures/Access%20Privileged%20Gateway%20Intents.png)
Also, check that your keywords in `config.py` are set correctly.

**Q: Where should I run this script?**  
A: This script is designed to be run on a device that's always powered on, like a Raspberry Pi or a dedicated server. This ensures that the script can always listen for commands and respond accordingly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
