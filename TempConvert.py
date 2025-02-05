#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  
  tempF = input("Enter your temperature in Farenheit: ")
  tempF = int(tempF)
  tempC = (tempF - 32) * 5/9


  tempC = tempF / 3
  
  tempC_Round = round(tempC, 1)
  print(tempF, "is ", tempC_Round, "degrees celsius.")

if __name__ == '__main__':
  main()
