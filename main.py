import requests
from datetime import datetime
import smtplib
import time
MY_LAT = -37.586449 # Your latitude
MY_LONG =145.033340 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
while True:
    time.sleep(60)
    if(MY_LAT-5  <= iss_latitude <= MY_LAT+5 )and(MY_LONG-5 <= iss_longitude <= MY_LONG+5):
        if(time_now.hour >= sunset) or (time_now.hour <= sunrise):
            EMAIL="tazeen.fatima.khan.1986@gmail.com"
            PASSWORD="orguobjwdqexxrzq"

            with smtplib.SMTP("smtp.gmail.com") as conn:
                conn.starttls()
                conn.login(user=EMAIL,password=PASSWORD)
                conn.sendmail(from_addr=EMAIL,
                to_addrs="tazeenfatimakhan1986@yahoo.com",
                msg=f"Subject:ISS is Overhead\n\n It's night time and ISS is overhead.Look Up.")
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.



