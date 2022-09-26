import time
import random

while True:
  temperature,humidity=random.randint(-50,138),random.randint(0,99)
  print("Temperature: "+str(temperature)+"°F"+"\tHumidity: "+str(humidity)+"%",sep="")
  if temperature>106:
    print('-'*5,"Alert!!! Too Hot",'-'*5,"\n\n")
  time.sleep(1)
