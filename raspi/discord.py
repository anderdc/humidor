import requests
import os
from raspi.logger import logger

HUMIDOR_DISCORD_WEBHOOK = os.getenv('HUMIDOR_DISCORD_WEBHOOK')
assert HUMIDOR_DISCORD_WEBHOOK, "webhook for discord not found :/"

def notify_discord_sync(message: str, webhook: str = HUMIDOR_DISCORD_WEBHOOK):
    try:
        response = requests.post(webhook, json={"content": message})
        if response.status_code == 204:
            logger.info(f"Discord notification sent: {message}")
        else:
            logger.error(f"Discord notification failed: {response.status_code}")
        return message
    except Exception as e:
        logger.error(f"Discord notification exception thrown: {e}")
        return ""