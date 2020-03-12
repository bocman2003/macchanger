
import subprocess as sb
import random

def randmac():
   mac = ""
   counter = 0
   while True:
      if counter == 6:
         return mac
      cislo = str(random.randrange(10, 99))
      if counter == 5:
         mac = mac + cislo
      else:
         mac = mac + cislo + ":"
      counter += 1

def macchange():
   sb.call(f"ifconfig {interface} down ", shell=True)
   sb.call(f"ifconfig {interface} hw ether {mac}", shell=True)
   sb.call(f"ifconfig {interface} up", shell=True)

interface = str(input("specify interface > "))
mac = str(input("type MAC or r for random MAC > "))

#random mac gen
if mac == "r":
   mac = randmac()



print(f"[+] changing MAC to > {mac}")
macchange()


#checks for the correct MAC
ifconfig_result = str(sb.check_output(f"ifconfig {interface}", shell=True))
if (mac in ifconfig_result) == True:

   print("[+] MAC changed!")








