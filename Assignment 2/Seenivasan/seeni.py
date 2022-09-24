import time
import random

def getTemperature():
  return random.randint(-60,140)
def getHumidity():
  return random.randint(0,99)

while True:
  time.sleep(1)
  temperature,humidity=getTemperature(),getHumidity()
  print("Temperature: "+str(temperature)+"°F"+"\tHumidity: "+str(humidity)+"%",sep="")
  if temperature>100:
    print('-'*6,"Alert!!! Too Hot",'-'*6,"\n\n")