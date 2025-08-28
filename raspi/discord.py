import requests
import os
from raspi.logger import logger
from raspi.models.models import SHT30X

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
    
# The optimal humidity for storing cigars generally ranges between 62% and 70% relative humidity (RH).
# While 70% RH is often cited as the ideal, some prefer a slightly lower range, such as 65% to 68% RH.
def analyze(data: SHT30X):

    if data.humidity < 62 or data.humidity > 70:
        notify_discord_sync(f"**WARNING** - humidor is out of ideal humidity range\n- Temperature: {data.temperature}°F\n- Humidity: **{data.humidity}%** RH\n*ideal range is between 62%-70% @ 70°F*")

    else:
        notify_discord_sync(f"HI. humidor WITHIN ideal humidity range\n- Temperature: {data.temperature}°F\n- Humidity: **{data.humidity}%** RH\n*Light one up?*")
