# Fortinet Fortigate connector
## Overview
The Fortinet Fortigate connector enables automated interactions with Fortigate firewall appliances, facilitating advanced network security management.

Fortinet Fortigate is a comprehensive cybersecurity solution that provides advanced security through its firewall capabilities. This connector enables Swimlane Turbine users to automate critical security tasks such as creating and managing address objects, address groups, and firewall policies. By integrating with Fortinet Fortigate, users can streamline security configurations, enhance policy enforcement, and rapidly respond to network threats directly within the Swimlane platform.

## Prerequisites


To effectively utilize the Fortinet Fortigate connector with Swimlane Turbine, ensure you have the following:
- HTTP Bearer Token Authentication with these parameters:
  * URL: The endpoint URL for the Fortigate API.
  * API Token: A valid token to authenticate requests to the Fortigate API.


## Obtaining an API Key:

#### Step 1: Determine your Source Address
The source address is needed to ensure the API token can only be used from trusted hosts. This step can be skipped if the trusted host IP address is already known.

1. On the FortiGate GUI, select the **Status** dashboard and locate the **Administrators** widget.

2. Click **your-userid > Show active administrator sessions.**

3. Make note of the **Source Address** for **your-userid** as it will be needed to create the Trusted Host in Step 3: Create the REST API Admin.
#### Step 2: Create an Administrator profile

1. On the FortiGate GUI, select **System > Admin Profiles > Create New.**

2. Populate the following fields Security Fabric, FortiView, User & Device, Firewall, Log & Report, Network, System, Security Profile, VPN, WAN Opt & Cache and Wifi & Switch.

3. Click **OK.**
#### Step 3: Create the REST API Admin

1. On the FortiGate GUI, select **System > Administrators > Create New > REST API Admin.**

2. Populate the following fields Username, Administrator Profile, CORS and Trusted Hosts.

The **Trusted Host** must be specified to ensure that your local host can reach the FortiGate. For example, to restrict requests as coming from only 10.20.100.99, enter 10.20.100.99/32. The Trusted Host is created from the **Source Address** obtained in Step 1: Determine your Source Address.

3. Click **OK** and an API token will be generated.

4. Make note of the API token as it is only shown once and cannot be retrieved.

5. Click **Close** to complete creation of the REST API Admin.

## About filtering addresses, address groups and group members.

The following 3 fields are mandatory

1. Key, objects will be filtered on property with this name.
2. Pattern, objects will be filtered on property with this value.
3. Filter, see table below.

Operator | Description  
--- | --- 
== | Case insensitive match with pattern
!= | Does not match with pattern (case insensitive)
=@ | Pattern found in object value (case insensitive)
!@ | Pattern not﻿ found in object value (case insensitive)
<= | Value must be less than or equal to pattern
< | Value must be less than pattern
\>= | Value must be greater than or equal to pattern
\> | Value must be greater than pattern
Logical OR | Separate filters using commas ','
Logical AND | Filter strings can be combined to create logical AND queries by including multiple filters in the request
Combining AND and OR | You can combine AND and OR filters together to create more complex filters.

## Capabilities

The Fortinet Fortigate connector provides the following capabilities:

* Create Address
* Create Address Group
* Create IPV4 firewall Policy
* Create Policy
* Delete Address
* Get Addresses
* Get Group Members
* Update Address Group

This connector was last tested against product version: 7.