# Rapid7 InsightIDR V2
## Overview
The Rapid7 InsightIDR V2 connector enables seamless integration with Swimlane Turbine, providing users with the ability to automate and orchestrate security operations tasks.

Rapid7 InsightIDR V2 is a powerful security analytics and incident detection platform that enables teams to detect and investigate security incidents quickly. This connector allows Swimlane Turbine users to automate key security operations tasks such as assigning users to investigations, closing multiple investigations, managing saved queries, and updating investigation statuses. By integrating with Rapid7 InsightIDR V2, users can streamline their incident response process, reduce manual workload, and accelerate threat detection and resolution within the Swimlane Turbine platform.

## Prerequisites


To effectively utilize the Rapid7 InsightIDR V2 connector within Swimlane Turbine, ensure you have the following prerequisites:
- API Key Authentication:
  * URL: The base endpoint URL for the Rapid7 InsightIDR API.
  * API Key: A valid API key provided by Rapid7 to authenticate API requests.


## Capabilities
This connector provides the following capabilities:

* Assign User to Investigation
* Bulk Close Investigations
* Create a Saved Query
* Create investigation
* Delete a Saved Query
* Get Investigation
* Get Product List Alerts by Investigation
* List Alerts Investigation
* List All Saved Queries
* List Investigations
* Retrieve Evidence for Alert
* Run Saved Query
* Search investigations
* Set Disposition Investigation
* Set Priority Investigation
* Set Status Investigation
* Update Investigation

## Asset Setup
Fill in the region parameter with the data center used for your account. To find the data center, log in to your insightIDR account, then look at the URL of the home page. The URL should look similar to this:

[REGION](http://REGION.idr.insight.rapid7.com) indicates your data center. Enter that as the value in the region parameter.

## Actions Setup
You need a threat key in order to use actions that manage threats. If you do not have a threat to use, follow the instructions here to create a new threat.

For actions that take datetime inputs, you can use any standard datetime format.

## Notes
* [All API documentation](https://docs.rapid7.com/insightidr/insightidr-rest-api/)