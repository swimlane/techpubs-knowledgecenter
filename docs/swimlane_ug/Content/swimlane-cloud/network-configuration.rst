Network Configuration
=====================

This topic contains specific information about network configuration for
Swimlane Cloud.

Network Address Translation (NAT)
---------------------------------

Network address translation (NAT) is a method of mapping an IP address
space into another by modifying network address information in the IP
header of packets while they are in transit across a traffic routing
device.

For Swimlane Cloud, you configure NAT in a way that the Swimlane
infrastructure can communicate to your private integrations using NAT'ed
IPs in a reduced subnet range that you set up. This prevents the
entirety of the Swimlane cloud's respective IP ranges from needing to be
routable to one another and helps prevent future IP range conflicts if
additional IP ranges are added as routable by your infrastructure that
may conflict with Swimlane's IP range.

Public DNS with VPN Connection
------------------------------

Swimlane Cloud is unable to use private DNS servers for DNS resolution.
Any DNS records that need to be resolved must be available in public DNS
zones.
