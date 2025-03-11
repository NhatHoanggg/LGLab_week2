from scapy.all import *
from scapy.layers.inet6 import IPv6
from scapy.layers.l2 import Ether, Dot1Q
from scapy.layers.inet import TCP, UDP
from random import randint

# Interface mạng
IFACE = "Ethernet"  # Thay bằng ID của card mạng

# Địa chỉ MAC
SRC_MAC = "08:8F:C3:08:14:34"  # MAC nguồn
DST_MAC = "D8:3A:DD:A4:BE:B8"  # MAC đích

# VLAN ID
VLAN_ID = 1

# Địa chỉ IPv6 hợp lệ
VALID_SRC_IPv6 = "fd53:1111:111:5::10"
VALID_DST_IPv6 = "fd53:1111:111:5::14"

# Cổng hợp lệ
VALID_SPORT = 13400
VALID_DPORT = 13400

# Giao thức
pro_type = TCP  # Có thể đổi sang UDP nếu cần

# Payload mẫu
# payload_default = "fd53:1111:111:5::16"
payload_default = "A1:B2:C3:D4:D5:E6"

# Gói tin hợp lệ
PKT_Default_Receive = (
    Ether(src=SRC_MAC, dst=DST_MAC) /
    Dot1Q(vlan=VLAN_ID) /
    IPv6(src=VALID_SRC_IPv6, dst=VALID_DST_IPv6) /
    pro_type(sport=VALID_SPORT, dport=VALID_DPORT) /
    Raw(load=payload_default)
)

# Gói tin với UDP port không hợp lệ
PKT_Default_Send = (
    Ether(src=SRC_MAC, dst=DST_MAC) /
    Dot1Q(vlan=VLAN_ID) /
    IPv6(src=VALID_SRC_IPv6, dst=VALID_DST_IPv6) /
    pro_type(sport=VALID_SPORT, dport=12345) /
    Raw(load=payload_default)
)



# from scapy.all import *
# from scapy.layers.inet import *
# from scapy.layers.inet6 import *
# from random import randint
# from netaddr import *
# import binascii
# import sys
# import signal
# from threading import Thread

# from scapy.layers.l2 import Dot1Q
# from sqlalchemy import false

# # Interface
# IFACE = "Ethernet" #fill the ID of destination network card

# # Number of threads used
# PKT_COUNT = 5
# # Scan Ports
# FROM_PORT = 1
# TO_PORT = 65536

# # MAC Address

# SRC_MAC = "08:8F:C3:08:14:34"  # MAC nguồn
# DST_MAC = "D8:3A:DD:A4:BE:B8"  # MAC đích
# INVALID_SRC_MAC = "D1:D2:D3:D4:D5:D6" #Invalid MAC

# # VLAN ID
# VLAN_ID = 1

# # IPv6s
# INVALID_DST_IPv6 = "fd53:1111:111:4::14" #Invalid IPv6
# INVALID_SRC_IPv6 = "fd53:1111:111:4::10" #Invalid IPv6
# VALID_SRC_IPv6 = "fd53:1111:111:5::10"
# VALID_DST_IPv6 = "fd53:1111:111:5::14"
# VALID_DST_Multicast = "ff02::1"
# INVALID_DST_Multicast = "ff02::2"

# # Ports
# VALID_SPORT = 13400
# VALID_DPORT = 13400
# INVALID_DPORT = 13456
# INVALID_SPORT = 13456
# RANGE = (1000, 65535)
# pro_type = TCP

# # Layers
# dot1q = Dot1Q(vlan=VLAN_ID)

# # Payload
# payload_default ="fd53:1111:111:5::15"

# PKT_Default_Send = Ether(dst=SRC_MAC,src=DST_MAC)/dot1q/IPv6(src=VALID_DST_IPv6,dst=VALID_SRC_IPv6)/pro_type(sport=VALID_DPORT, dport=VALID_SPORT)/payload_default