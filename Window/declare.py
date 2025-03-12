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

# Payload
payload_default = "Default"
# payload_default = "A1:B2:C3:D4:D5:E6"

# Gói tin hợp lệ
PKT_Default_Receive = (
    Ether(src=SRC_MAC, dst=DST_MAC) /
    Dot1Q(vlan=VLAN_ID) /
    IPv6(src=VALID_SRC_IPv6, dst=VALID_DST_IPv6) /
    pro_type(sport=VALID_SPORT, dport=VALID_DPORT) /
    # Raw(load=payload_default)
    payload_default
)
















# Gói tin với UDP port không hợp lệ
# PKT_Default_Send = (
#     Ether(src=SRC_MAC, dst=DST_MAC) /
#     Dot1Q(vlan=VLAN_ID) /
#     IPv6(src=VALID_SRC_IPv6, dst=VALID_DST_IPv6) /
#     pro_type(sport=VALID_SPORT, dport=VALID_DPORT) /
#     Raw(load=payload_default)
# )
