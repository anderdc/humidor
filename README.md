## Humidor
The premise of this project is to build my own humidor notification system for a cigar box. 

### Why do this instead of buying one?
1. I like cigars and want to be able to store a small collection at my house.
2. This would be a great way to get my hands back into hobbyist electronics and *inventing*.
3. I'll be able to *implement creativity* with novel solutions to a problem and *acquisition of knowledge*.
4. I'll (re)learn the basics of working with microcontrollers, sensors, wiring, soldering, prototyping, and (perhaps) IoT.

### Checkpoints Towards Solution 
- Phase 1
Use an ESP-32 dev kit module to read data from an SHT3X humidity sensor. The sensor will post data (JSON) to a (self-hosted?) flask server. The server will ping a discord channel and notify me of my humidor's current state. 

- Phase 2 
Using everything from phase 1, I will put my circuit in a box (a normal cigar box) and continue monitoring. I will manually intervene when the humidity is not at an appropriate level.
At this stage I will add another discord alert to check if the power source for the circuit is low.

- Phase 3
I was going to have a solution using a mini humidifier/water atomizer to inject water into the air in the box, but it might get too wet + that type of solution will require more maintenance than I want for this project. 
Instead, I'll add an OLED display to show the current sensor reading, I think that'd be neat to see whenever I grab a cigar.

#### Deliverables
- A circuit using an ESP32 with capabilities to: **read SHT3X output**, **display temp/humidity on an OLED display**, **display power level on OLED**, **send an alert over wifi for low humidity**, **send an alert over wifi for low battery/power**
- A flask backend (preferably self hosted on raspberry pi).

#### Getting Started with Flask & Waitress
- Install requirements using a venv

```bash
pip install -r requirements.txt
```

- your environment needs to have these variables exported

```bash
HUMIDOR_DISCORD_WEBHOOK="your_webhook"
```

- run the server on port `5001` with

```
python -m raspi.backend
```


**Notes**
I2C is a communication protocol used to connect sensors and peripherals to microcontrollers
Serial Data (SDA) The data line — sends/receives data between the microcontroller and sensor
Serial Clock (SCL) The clock line — keeps everything in sync by pulsing with timing signals
For the ESP32
SDA	- GPIO 21
SCL	- GPIO 22
