# Check Point R80 Connector
## Overview
The Check Point R80 connector allows for streamlined security management and automation of threat prevention tasks within the Swimlane ecosystem.

Check Point R80 is a comprehensive security management solution that provides advanced threat prevention and security management capabilities. This connector enables Swimlane Turbine users to automate and streamline security operations by integrating with Check Point R80's robust API. Users can create, update, and manage security layers, access rules, application sites, domains, groups, hosts, networks, and retrieve logs directly within Swimlane Turbine, enhancing their security posture and response capabilities without the need for manual intervention.

## Prerequisites


To effectively utilize the Check Point R80 connector with Swimlane Turbine, ensure you have the following prerequisites in place:
- API Key Authentication:
  * URL: Endpoint for the Check Point R80 API.
  * API Key: Unique key provided by Check Point R80 for API access.
- HTTP Basic Authentication:
  * URL: Endpoint for the Check Point R80 API.
  * Username: Your Check Point R80 username.
  * Password: Your Check Point R80 password.


## Capabilities

The Check Point R80 connector has the following capabilities:

* Manage Access Layers
* Manage Access Rules
* Manage Domains
* Manage Groups
* Manage Hosts
* Manage Networks
* Manage Application Sites
* Manage Application Sites Categories
* Manage Logs

### Additional Information about Capabilities

- "Host - Create" and "Network - Create" tasks can be used to add a Host/Network to a Group on creation.
- "Group - Update" can be used to add a pre-existing Host/Network to a Group.
- To block objects, for example IPs or domains, an access rule must be created and assigned to a group where the objects to be blocked are located.
- In the case of applying or using "Show Logs" task, we have added the following two tasks in place:
 1. "Show Logs using New Query" task - takes `new-query` as input in the request body.
 2. "Show Logs using Query ID" task - takes `query-id` as input in the request body.

## Notes

* [Check Point R80 API Documentation](https://sc1.checkpoint.com/documents/latest/APIs/index.html#introduction~v1.6)
* [Show Logs Documentation](https://sc1.checkpoint.com/documents/latest/APIs/index.html#web/show-logs~v1.9%20)

This connector was last tested against product version: 1.6