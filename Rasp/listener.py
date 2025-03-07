from scapy.all import *
from scapy.layers.inet6 import *
from scapy.layers.l2 import Dot1Q

# Constants
INTERFACE = "vlan5"  # Replace with your VLAN interface
EXPECTED_SRC_IPv6 = "fd53:abcd:123:5::10"
EXPECTED_DST_IPv6 = "fd53:abcd:123:5::14"
EXPECTED_SPORT = 13400
EXPECTED_DPORT = 13400
EXPECTED_VLAN_ID = 5

def packet_callback(packet):
    """
    Callback function to handle each sniffed packet.
    """
    try:
         # Check for VLAN tag
        if Dot1Q in packet and packet[Dot1Q].vlan == EXPECTED_VLAN_ID:
            # Check for IPv6 and transport layer (TCP/UDP)
            if IPv6 in packet and (TCP in packet or UDP in packet):
                ipv6_layer = packet[IPv6]
                transport_layer = packet[TCP] if TCP in packet else packet[UDP]
                
                # Check for expected source/destination addresses and ports
                if (ipv6_layer.src == EXPECTED_SRC_IPv6 and 
                    ipv6_layer.dst == EXPECTED_DST_IPv6 and
                    transport_layer.sport == EXPECTED_SPORT and
                    transport_layer.dport == EXPECTED_DPORT):
                    
                    print(f"Received valid packet: {packet.summary()}")
                    print(f"Payload: {bytes(transport_layer.payload)}")
                    packet.show()
                    return
    except Exception as e:
        print(f"Error processing packet: {e}")

def main():
    """
    Main function to start sniffing on the VLAN interface.
    """
    print(f"Listening on interface {INTERFACE}...")
    sniff(iface=INTERFACE, prn=packet_callback, filter="ip6", store=False)

if __name__ == "__main__":
    main()