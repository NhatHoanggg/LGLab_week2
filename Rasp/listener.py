import ipaddress
import subprocess
from scapy.all import *
from scapy.layers.inet6 import IPv6
from scapy.layers.l2 import Dot1Q

# Constants
INTERFACE = "eth0"
EXPECTED_SRC_IPv6 = "fd53:1111:111:5::10"
EXPECTED_DST_IPv6 = "fd53:1111:111:5::14"
EXPECTED_SPORT = 13400
EXPECTED_DPORT = 13400
EXPECTED_VLAN_ID = 1
IPv6_NETWORK = "fd53:1111:111:5::/64"

def update_ipv6(new_ip, interface, ipv6_network):
    try:
        ip_addr = ipaddress.IPv6Address(new_ip)
        network = ipaddress.IPv6Network(ipv6_network, strict=False)
        if ip_addr not in network:
            print(f"IPv6 address {new_ip} is outside the allowed range: {ipv6_network}.")
            return
    except ipaddress.AddressValueError:
        print(f"Invalid IPv6 address: {new_ip}.")
        return

    print(f"Updating IPv6 address to: {new_ip}")
    remove_command = f"ip -6 addr flush dev {interface}"
    try:
        subprocess.run(remove_command, shell=True, check=True)
        print("Successfully removed existing IPv6 addresses.")
    except subprocess.CalledProcessError as e:
        print(f"Error removing existing IPv6 addresses: {e}")

    command = f"ip -6 addr add {new_ip}/64 dev {interface}"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"IPv6 address successfully updated to: {new_ip}")
    except subprocess.CalledProcessError as e:
        print(f"Error updating IPv6 address: {e}")
def packet_callback(packet):                                       
    try:                                                      
        if Dot1Q in packet and packet[Dot1Q].vlan == EXPECTED_VLAN_ID:                   
            print("VLAN tag matches expected ID.")     
                                                                
        if IPv6 in packet and (TCP in packet or UDP in packet):    
            ipv6_layer = packet[IPv6]                         
            transport_layer = packet[TCP] if TCP in packet else packet[UDP]              
                                                       
            if (ipv6_layer.src == EXPECTED_SRC_IPv6 and            
                ipv6_layer.dst == EXPECTED_DST_IPv6 and               
                transport_layer.sport == EXPECTED_SPORT and                              
                transport_layer.dport == EXPECTED_DPORT):     
                                                               
                print(f"Received valid packet: {packet.summary()}")
                print(f"Payload: {bytes(transport_layer.payload)}")        
                packet.show()                                 
                                                              
                if Raw in packet:                              
                    try:                                        
                        new_ipv6 = packet[Raw].load.decode().strip()       
                        update_ipv6(new_ipv6, INTERFACE, IPv6_NETWORK)
                    except UnicodeDecodeError:                     
                        print("Failed to decode packet payload.")  
    except Exception as e:                                      
        print(f"Error processing packet: {e}")                             
                                                  
def main():                                                        
    print(f"Listening on interface {INTERFACE}...")                 
    sniff(iface=INTERFACE, prn=packet_callback, filter="ip6", store=False)
                                                                           
if __name__ == "__main__":                                       
    main()