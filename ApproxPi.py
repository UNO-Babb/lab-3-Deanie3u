#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  decimal_percision = int(input("How many decimal points to compute (0-10): "))
    
  
 

  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
  approxPi = 4/1
  sign = -1
  denom = 3


  while round (approxPi, decimal_percision) != round(realPi, decimal_percision):
    #print(approxPi)
    approxPi = approxPi + (sign * 4 / denom)
    denom += 2
    sign = sign * - 1
    
  
  end = time.time()

  elapsedTime = end - start
  #print(elapsedTime)
  print("Pi:", round(realPi, decimal_percision))
  print("Calculated in", elapsedTime, "seconds")
  

if __name__ == '__main__':
  main()
