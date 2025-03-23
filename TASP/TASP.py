import discord
import os
import asyncio
import json
import platform
from dotenv import load_dotenv
from colorama import init, Fore, Style

# Initialize colorama for cross-platform support
init(autoreset=True)

CONFIG_FILE = "config.json"

# Load token from .env
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

def clear_console():
    """Clears the console based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Displays the startup banner with perfect alignment."""
    clear_console()
    print(Fore.MAGENTA + "=" * 59)
    print(Fore.CYAN + r"""
  _____  _    ____  ____  
 |_   _|/ \  / ___||  _ \ 
   | | / _ \ \___ \| |_) |
   | |/ ___ \ ___) |  __/ 
   |_/_/   \_\____/|_|    

  Tyla's Auto Self Promo (TASP)
""" + Fore.MAGENTA + "=" * 59 + "\n")

def load_config():
    """Loads saved config if available and valid."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(Fore.RED + "\n[ERROR] Config file is corrupted. Resetting...\n")
            os.remove(CONFIG_FILE)  # Delete broken config
    return None

def save_config(config):
    """Saves user settings to config.json."""
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

def get_user_input():
    """Gets new settings from the user."""
    display_banner()
    print(Fore.CYAN + "\n[CONFIG SETUP] Enter new settings:\n" + "=" * 50)
    
    channel_id = input(Fore.YELLOW + ">> Enter Channel ID: ").strip()
    message = input(Fore.YELLOW + ">> Enter Message: ").strip()
    interval = input(Fore.YELLOW + ">> Enter Interval (seconds): ").strip()

    if not channel_id.isdigit():
        print(Fore.RED + "\n[ERROR] Invalid Channel ID. It must be numbers only.\n")
        return None
    try:
        interval = int(interval)
    except ValueError:
        print(Fore.RED + "\n[ERROR] Interval must be a number.\n")
        return None

    config = {"channel_id": channel_id, "message": message, "interval": interval}
    save_config(config)
    print(Fore.GREEN + "\n[INFO] Config saved successfully!\n")
    return config

class SelfBot(discord.Client):
    async def on_ready(self):
        display_banner()
        print(Fore.GREEN + f"[INFO] Logged in as: {self.user}")
        print(Fore.MAGENTA + "-" * 59)

        # Load or create config
        config = load_config()

        if not config:
            print(Fore.YELLOW + "\n[INFO] No saved settings found. Starting setup...\n")
            config = get_user_input()
        else:
            print(Fore.BLUE + "\n[LAST USED SETTINGS]")
            print(Fore.WHITE + f"  - Channel ID : {config['channel_id']}")
            print(Fore.WHITE + f"  - Message    : {config['message']}")
            print(Fore.WHITE + f"  - Interval   : {config['interval']} seconds")
            print(Fore.BLUE + "=" * 50)
            use_last = input(Fore.YELLOW + ">> Would you like to use these settings? (yes/no): ").strip().lower()
            if use_last != "yes":
                config = get_user_input()

        if not config:
            print(Fore.RED + "\n[ERROR] Invalid settings. Exiting...\n")
            await self.close()
            return

        clear_console()
        display_banner()
        print(Fore.GREEN + "\n[INFO] Now sending messages with the following settings:")
        print(Fore.WHITE + f"  - Channel ID : {config['channel_id']}")
        print(Fore.WHITE + f"  - Message    : {config['message']}")
        print(Fore.WHITE + f"  - Interval   : {config['interval']} seconds")
        print(Fore.YELLOW + "\n(Press CTRL+C to stop)\n")

        # Start messaging loop
        try:
            await self.send_messages(config["channel_id"], config["message"], config["interval"])
        except asyncio.CancelledError:
            print(Fore.RED + "\n[INFO] Messaging loop stopped.\n")

    async def send_messages(self, channel_id, message, interval):
        """Sends messages at the specified interval."""
        while True:
            channel = self.get_channel(int(channel_id))
            if channel:
                try:
                    await channel.send(message)
                    print(Fore.GREEN + f"[SENT] Message sent to {channel_id}")
                except discord.Forbidden:
                    print(Fore.RED + f"\n[ERROR] Cannot send messages in {channel_id}. Check permissions.\n")
                    return
                except discord.HTTPException as e:
                    print(Fore.RED + f"\n[ERROR] Failed to send message: {e}\n")
            else:
                print(Fore.RED + f"\n[ERROR] Invalid Channel ID: {channel_id}. Message not sent.\n")
            await asyncio.sleep(interval)

client = SelfBot()

try:
    client.run(token, bot=False)
except KeyboardInterrupt:
    print(Fore.RED + "\n[INFO] Bot stopped by user.\n")
except discord.LoginFailure:
    print(Fore.RED + "\n[ERROR] Invalid token. Check your .env file.\n")
