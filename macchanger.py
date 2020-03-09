import subprocess as sb
import random



interface = input("napis interfce ktoreho menis mac\n")
mac = str(input("napis mac adresu na ktoru chces zmenit alebo random(r):\n"))

#random mac gen
if mac == "r":
    mac = ""
    counter = 0
    while True:
        if counter == 6:
            break
        cislo = str(random.randrange(10,99))
        if counter == 5:
            mac = mac + cislo
        else:
            mac = mac + cislo + ":"
        counter += 1

print(f"mac = {mac}")


sb.call(f"ifconfig {interface} down ", shell=True)
sb.call(f"ifconfig {interface} hw ether {mac}", shell=True)
sb.call(f"ifconfig {interface} up", shell=True)