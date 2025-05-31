from flask import Flask, request, jsonify
from pydantic import ValidationError
from raspi.models.models import SHT30X
from raspi.discord import notify_discord_sync
from raspi.logger import logger
import waitress

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "hello this is the backend for my humidor :)"

@app.route('/humidor', methods=['POST'])
def humidor():
    try:
        payload = SHT30X(**request.get_json())
        logger.info("POST request called with: %s", payload.model_dump())

        analyze(payload)
        return 'success', 200
    
    except ValidationError as e:
        logger.warning("Validation failed: %s", e.json())
        return jsonify({'error': e.errors()}), 400
    

# The optimal humidity for storing cigars generally ranges between 62% and 70% relative humidity (RH).
# While 70% RH is often cited as the ideal, some prefer a slightly lower range, such as 65% to 68% RH.
def analyze(data: SHT30X):

    # notify_discord_sync(f"Hi\n- Temperature: {payload.temperature}F\n- Humidity: {payload.humidity}% RH")

    if data.humidity < 62 or data.humidity > 70:
        notify_discord_sync(f"**WARNING** - humidor is out of ideal humidity range\n- Temperature: {data.temperature}°F\n- Humidity: **{data.humidity}%** RH\n*ideal range is between 62%-70% @ 70°F*")

if __name__ == '__main__':
    waitress.serve(app, host="0.0.0.0", port=5001)
