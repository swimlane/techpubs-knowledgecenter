# SentinelOne Connector
## Overview
The SentinelOne connector enables automated interaction with SentinelOne's endpoint protection capabilities, facilitating real-time threat detection and response.

SentinelOne delivers autonomous endpoint protection through a single agent that successfully prevents, detects, responds, and hunts attacks across all major vectors. The SentinelOne Turbine Connector for Swimlane Turbine enables security teams to automate threat detection and response actions, such as adding notes to threats, broadcasting messages to agents, and managing blacklist items. By integrating with SentinelOne, users can streamline their security operations, reduce response times, and enhance their overall security posture within the Swimlane Turbine platform.

## Prerequisites


To effectively utilize the SentinelOne connector within the Swimlane Turbine platform, ensure you have the following prerequisites:
- API Key Authentication:
  * URL: Endpoint URL for the SentinelOne Management API.
  * API Token: A valid API token from SentinelOne to authenticate requests.


## Obtaining an API Token
1. Navigate to the Sentinel One Portal. Select your user in the upper right corner of the menu.
2. Select the menu by your user account name, then select `My User`.
3. A modal will pop up displaying your account information.
4. Select `Generate` to generate a new API Token and copy the value into the Swimlane asset.

## Capabilities

The SentinelOne integration provides the following capabilities:

* Add Threat Note
* Broadcast Message
* Connect Agents
* Create Blacklist Item
* Create Exclusion
* Create Power Query And Get Query ID
* Deep Visibility Create Query and Get Query ID
* Deep Visibility Get Events By Query ID
* Delete Blocklist Item
* Delete Threat Note
* Disconnect Agents
* Download From Cloud
* Fetch Files
* Fetch Threat File
* Get Activities
* Get Agent Applications
* Get Agents
* Get Alerts
* Get Blocklist Items
* Get Groups
* Get Hash
* Get Rogues Settings
* Get Sites
* Get Threat Analysis
* Get Threat Appearences
* Get Threat Events
* Get Threat Notes
* Get Threat Timeline
* Get Threats
* Initiate Scan
* Mitigate Threats
* New Firewall Rule
* Ping A Power Query
* Update Alert Analyst Verdict
* Update Alert Incident
* Update Threat Analyst Verdict
* Update Threat External Ticket ID
* Update Threat Incident
* Update Threat Note

#### Initiate Scan Action
* Full Disk Scan finds dormant suspicious activity, threats, and compliance violations, that are then mitigated according to the policy. It scans the local file system.
* Full Disk Scan does not inspect drives that require user credentials (such as network drives) or external drives.
* Full Disk Scan does not work on hashes. It does not check each file against the blacklist.
* If the Static AI determines a file is suspicious, the Agent calculates its hash and sees if the hash is in the blacklist. If a file is executed, all aspects of the process are inspected, including hash-based analysis and blacklist checks. Full Disk Scan can run when the endpoint is offline, but when it is connected to the Management, it can use the most updated Cloud data to improve detection.

#### Create Firewall Rule
To keep it simple for the user, this action currently only supports adding remote hosts to a firewall rule.
Should this action need to be expanded to support others, please contact Swimlane Support.

### About Deep Visibility Queries

For complete query syntax, see Query Syntax in the [Knowledge Base](support.sentinelone.com) or the Console Help.

## Notes
The API documentation can be found on your Sentinel One Instance by doing the following:
1. Select the arrow next to your user in the top right of the navigation bar.
2. Select __API Doc__ and a new tab of the API documentation will open.

This connector was last tested against product version: API v2.1