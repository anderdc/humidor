import json
import paho.mqtt.client as mqtt
from raspi.models.models import SHT30X
from raspi.discord import analyze, notify_discord_sync
from raspi.logger import logger
from pydantic import ValidationError

'''
    MQTT subscriber (like a RabbitMQ consumer) that receives ESP32 sensor data
    TODO: NOT DONE bc solution requires also running an MQTT broker like mosquitto
'''

MQTT_BROKER = "0.0.0.0" 
MQTT_PORT = 1883
MQTT_TOPIC = "humidor/data"

def on_connect(client, userdata, flags, rc):
    logger.info("Connected to MQTT broker with code %s", rc)
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        data_dict = json.loads(msg.payload.decode())
        payload = SHT30X(**data_dict)
        logger.info("MQTT message received: %s", payload.model_dump())
        analyze(payload)

    except ValidationError as e:
        logger.warning("Validation failed: %s", e.json())

    except Exception as e:
        logger.error("Unexpected error: %s", str(e))

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT)
    client.loop_forever()
