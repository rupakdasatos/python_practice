''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import numpy as np

class Error(Exception):
   """Base class for other exceptions"""
   pass

class QRErr(Error):
   """Raised when the quantity required number list length is less or more than required length"""
   pass

class QPErr(Error):
   """Raised when the quantity present number list length is less or more than required length"""
   pass

def main():

   try:

      N = int(input())
      QR = np.array([int(x) for x in input().split()])
      QP = np.array([int(y) for y in input().split()])


      if QR.size != N:
         raise QRErr
      elif QP.size != N:
         raise QPErr

      #print(min(list(map(floordiv, QP, QR))))
      print(np.amin(np.floor_divide(QP, QR)))


   except ZeroDivisionError:
      print("Please enter non zero value in quantity required.")
   except QRErr:
      print("Please provide proper quantity required inputs.")
   except QPErr:
      print("Please provide proper quantity present inputs.")
   except ValueError:
      print("Please provide numeric values in each input")      

main()
