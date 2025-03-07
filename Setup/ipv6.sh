#!/bin/sh

# C?u hình d?a ch? IPv6 cho eth0 v?i scope link
ip -6 addr add fd53:abcd:123:5::14/64 dev vlan5

# B?t giao di?n eth0 (n?u chua b?t)
ip link set eth0 up

# Ki?m tra l?i c?u hình d?a ch? IPv6
ip -6 addr show dev eth0
