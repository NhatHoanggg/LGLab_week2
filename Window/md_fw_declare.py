#md_fw_declare.py

from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.inet6 import *
from random import randint
from netaddr import *
import binascii
import sys
import signal
from threading import Thread

from scapy.layers.l2 import Dot1Q
from sqlalchemy import false

# Interface
IFACE = "Ethernet" #fill the ID of destination network card

# Number of threads used
PKT_COUNT = 5
# Scan Ports
FROM_PORT = 1
TO_PORT = 65536

# MAC Address
SRC_MAC = "90:0F:0C:1A:FF:9F"	#fill your MAC Address here
DST_MAC = "D8:3A:DD:A4:C1:42" #fill the destination MAC
INVALID_SRC_MAC = "D1:D2:D3:D4:D5:D6" #Invalid MAC

# VLAN ID
VLAN_ID = 1

# IPv6s
INVALID_DST_IPv6 = "fd53:abcd:123:3::14" #Invalid IPv6
INVALID_SRC_IPv6 = "fd53:abcd:123:3::10" #Invalid IPv6
VALID_SRC_IPv6 = "fd53:1111:111:5::10"
VALID_DST_IPv6 = "fd53:1111:111:5::14"
VALID_DST_Multicast = "ff02::1"
INVALID_DST_Multicast = "ff02::2"

# Ports
VALID_SPORT = 13400
VALID_DPORT = 13400
INVALID_DPORT = 13456
INVALID_SPORT = 13456
RANGE = (1000, 65535)
pro_type = TCP

# Layers
dot1q = Dot1Q(vlan=VLAN_ID)

# Payload
payload_default ="Default"
PKT_Default_Receive = Ether()/dot1q/IPv6(src=VALID_SRC_IPv6,dst=VALID_DST_IPv6)/pro_type(sport=VALID_SPORT, dport=VALID_DPORT)/payload_default

PKT_Default_Send = Ether(dst=SRC_MAC,src=DST_MAC)/dot1q/IPv6(src=VALID_DST_IPv6,dst=VALID_SRC_IPv6)/pro_type(sport=VALID_DPORT, dport=VALID_SPORT)/payload_default