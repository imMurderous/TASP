==========================================
        Tyla's Auto Self Promo (TASP)
==========================================

WHAT IS TASP?
TASP (Tyla's Auto Self Promo) is a self-bot that automatically sends a message
in a specified Discord channel at set intervals.

WARNING:
Self-bots are against Discord's Terms of Service.
Use this at your own risk!

------------------------------------------
INSTALLATION:
------------------------------------------
1) Make sure you have Python 3.6.0 installed.  
   Download it here: https://www.python.org/downloads/release/python-360/

2) Open the "setup" folder and run "setup.bat" as Administrator  
   (Right-click → Run as administrator).  
   This will install the required dependencies.  
   If it doesn’t work, open a terminal in the "setup" folder and type:
   
      pip install -r requirements.txt

3) Open the ".env" file in the main TASP folder and edit this line:  
   
      DISCORD_TOKEN=your_token_here

   (Replace "your_token_here" with your actual Discord token.)

------------------------------------------
HOW TO USE:
------------------------------------------
Easiest Method:  
   Double-click "TASP.py" in the main folder, and it will start running!  

Or, Run it Manually:
1) Open a terminal in the TASP folder.  
2) Type the following command and press Enter:  

      python TASP.py  

3) The bot will prompt you to enter:
   - The Channel ID where messages should be sent.
   - The Message you want to send.
   - The Interval (in seconds) between messages.

4) The bot will then automatically send your message at the set interval.

------------------------------------------
SAVING SETTINGS:
------------------------------------------
- TASP will remember your last used settings so you don’t have to enter them again.
- If you want to reset the settings, delete "config.json" in the main folder and restart the bot.

------------------------------------------
TROUBLESHOOTING:
------------------------------------------
"ModuleNotFoundError: No module named 'discord'"
   - Run: pip install -r requirements.txt
   
"Invalid Token"
   - Make sure your Discord token is correct in ".env".
   - Your token should look like a long string of random characters.
   
"Message Not Sending"
   - Check if the Channel ID is correct.
   - Make sure your account has permission to send messages in that channel.

------------------------------------------
DISCLAIMER:
------------------------------------------
- This bot is for educational purposes only.
- Using self-bots violates Discord's Terms of Service and can get your account banned.
- Use this at your own risk!  
  
------------------------------------------
LICENSE:
------------------------------------------
Feel free to modify and improve this project.

