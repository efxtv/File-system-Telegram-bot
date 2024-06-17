# File-system-Telegram-bot
Telegram bot generates NGROK Link to access remote file systems of an OS
# File System Access Telegram Bot

File System Access Telegram Bot allows you to access your filesystem remotely using ngrok link sent to a Telegram bot from a remote device.

## Overview

This Python script sets up a Telegram bot that, when executed on a compatible system, starts ngrok tunnel and sends the public URL to a Telegram chat. This allows remote access to the filesystem of the device where the script is running.

## Dependencies

- Python 3.x
- requests library (`pip install requests`)

## Usage

1. **Configure Telegram Bot:**
   - Create a Telegram bot using BotFather and obtain the API token (`BOT_TOKEN`) and your Telegram user ID (`USER_ID`).

2. **Install Dependencies:**
```
   pip install requests
```

## Service commands
```
$ pip install -r requirements.txt
```

```
$ python3 run.py
```

```
$ sudo systemctl daemon-reload
```

```
$ sudo systemctl start ngrok-monitor.service
```

```
$ sudo service nm status
```

```
$ sudo systemctl daemon-reload
```

```
$ sudo systemctl restart nm.service
```

```
$ sudo journalctl -u nm.service -f
```

## How to setup?
Contact [EFXTv](https://t.me/efxtv) to know more
