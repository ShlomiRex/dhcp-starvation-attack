#!/bin/bash
sudo service isc-dhcp-server stop
sudo rm /var/lib/dhcp/dhcpd.leases /var/lib/dhcp/dhcpd.leases~ 
sudo service isc-dhcp-server restart