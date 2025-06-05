from flask import Flask, request, jsonify
from pydantic import ValidationError
from raspi.models.models import SHT30X
from raspi.discord import notify_discord_sync
from raspi.logger import logger
import waitress

'''
    flask server to receive post requests from ESP-32
'''

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
    

if __name__ == '__main__':
    waitress.serve(app, host="0.0.0.0", port=5001)
