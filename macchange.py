
import subprocess as sb
import random

def randmac():
   mac = ""
   counter = 0
   while True:
      if counter == 6:
         return mac
      number = str(random.randrange(10, 99))
      if counter == 5:
         mac = mac + number
      else:
         mac = mac + number + ":"
      counter += 1

def macchange():
   sb.call(f"ifconfig {interface} down ", shell=True)
   sb.call(f"ifconfig {interface} hw ether {mac}", shell=True)
   sb.call(f"ifconfig {interface} up", shell=True)

#checks for the correct MAC
def checkmac(interface):
   ifconfig_result = str(sb.check_output(f"ifconfig {interface}", shell=True))
   if mac in ifconfig_result:
      print("[+] MAC changed!")
      return True
   else:
      return False

interface = str(input("specify interface > "))
mac = str(input("type MAC or r for random MAC > "))

if mac == "r":
   mac = randmac()

print(f"[+] changing MAC to > {mac}")
macchange()

while not checkmac(interface):
   mac = randmac()
   print(f"changing mac to > {mac}")
   macchange()











