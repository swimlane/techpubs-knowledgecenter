# Proofpoint Connector
## Overview
The ProofPoint connector enables automated interactions with ProofPoint's security services, facilitating threat detection and response activities.

ProofPoint is a leading cybersecurity and compliance company that protects organizations' people, data, and brand against advanced threats and compliance risks. The ProofPoint connector for Swimlane Turbine enables users to automate the decoding of URLs, retrieval of forensic data, and extraction of SIEM events. By integrating with ProofPoint, Swimlane Turbine users can enhance their security operations with streamlined threat intelligence and incident response capabilities, leveraging ProofPoint's advanced email protection and targeted attack analysis.

## Prerequisites


To effectively utilize the ProofPoint connector with Swimlane Turbine, ensure you have the following prerequisites:
- HTTP Basic Authentication with the following parameters:
  * URL: The endpoint URL for the ProofPoint API.
  * Principal: Your ProofPoint account username.
  * Secret: Your ProofPoint account password.


## Capabilities

The Proofpoint integration provides the following capabilities:

* Decode URLs
* Decode URLs - Offline (This uses a local script to decode the URLs.)
* Forensics Campaign Lookup
* Forensics Threat Lookup
* SIEM All
* SIEM Messages Blocked
* SIEM Messages Delivered
* SIEM Clicks Blocked
* SIEM Clicks Delivered

## Limitations

The URLs passed to the decode tasks are case sensitive.

Proofpoint encodes the URLs with base64, if you are passing extracted IOCs from the Swilane Utilites plugin with the IOC Parser task, 
please make sure that you have the input `To Lower` marked as False. 

## Notes

In the case of using SIEM API action, we must have to pass the one of the following fields in query parameters 

* Interval
* Since Seconds
* Since Time


`interval`

A string containing an ISO8601-formatted interval. If this interval overlaps with previous requests for data, records from the previous request may be duplicated. The minimum interval is thirty seconds. The maximum interval is one hour.

Example

* 2016-05-01T12:00:00Z/2016-05-01T13:00:00Z - an hour interval, beginning at noon UTC on 05-01-2016
* PT30M/2016-05-01T12:30:00Z - the thirty minutes beginning at noon UTC on 05-01-2016 and ending at 12:30pm UTC
* 2016-05-01T05:00:00-0700/PT30M - the same interval as above, but using -0700 as the time zone

`sinceSeconds`

An integer representing a time window in seconds from the current API server time. The start of the window is the current API server time, rounded to the nearest minute, less the number of seconds provided. The end of the window is the current API server time rounded to the nearest minute. If JSON output is selected, the end time is included in the returned result.

`sinceTime`

A string containing an ISO8601 date. It represents the start of the data retrieval period. The end of the period is determined by current API server time rounded to the nearest minute. If JSON output is selected, the end time is included in the returned result.

`format`
A string specifying the format in which response data is returned. If no format is specified, syslog will be used as the default. The following values are accepted:
* syslog
* JSON


## Notes

* [Proofpoint API Documentation](https://help.proofpoint.com/Threat_Insight_Dashboard/API_Documentation)