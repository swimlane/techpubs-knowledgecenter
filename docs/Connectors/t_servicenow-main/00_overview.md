# ServiceNow Connector
## Overview
The ServiceNow connector facilitates the automation of IT service management tasks by enabling interaction with ServiceNow's digital workflow system through Swimlane.

ServiceNow is a cloud-based platform that provides solutions for IT service management (ITSM), IT operations management (ITOM), and IT business management (ITBM). This connector enables Swimlane Turbine users to automate incident response, service requests, and security incident management by integrating with ServiceNow's comprehensive suite of services. By leveraging this connector, users can streamline their workflows, enhance collaboration, and accelerate resolution times for IT and security-related incidents within their organization.

## Prerequisites


To effectively utilize the ServiceNow connector with Swimlane, ensure you have the following prerequisites:
- OAuth 2.0 Password authentication with these parameters:
  * URL: The endpoint URL for ServiceNow API access.
  * Client ID: The client identifier as registered in your ServiceNow application.
  * Client Secret: The secret key associated with your client ID for OAuth authentication.
  * OAuth2 Username: Your ServiceNow user account username.
  * OAuth2 Password: Your ServiceNow user account password.
- OAuth 2.0 Client Credentials authentication with these parameters:
  * URL: The endpoint URL for ServiceNow API access.
  * Client ID: The client identifier as registered in your ServiceNow application.
  * Client Secret: The secret key associated with your client ID for OAuth authentication.
  * Token URL: The URL to retrieve the OAuth token from ServiceNow.
- HTTP Basic authentication with these parameters:
  * URL: The endpoint URL for ServiceNow API access.
  * Username: Your ServiceNow user account username.
  * Password: Your ServiceNow user account password.


## Capabilities

The ServiceNow connector provides the following capabilities:

* Add Attachment to Table
* Create Incident
* Create Request
* Create Security Incident
* Create Table Row
* Delete Custom Endpoint
* Get all Incidents
* Get all Security Incidents
* Get Attachment
* Get Attachment Metadata
* Get Custom Endpoint
* Get Table
* Patch Custom Endpoint
* Post Custom Endpoint
* Put Custom Endpoint
* ServiceNow Get Custom Action
* ServiceNow Patch Custom Action
* ServiceNow Post Custom Action
* Update Incident
* Update Security Incident
* Update Table Row

## Task Setup

Use `Add a property` under `JSON Body` option in the action inputs screen, to add additional parameters like `state`, `close notes`, etc. for Creating/Updating Incidents or Security Incidents.

### Additional Information about Capabilities

* To close an incident from the update incident action, you must provide appropriate values for state, close notes, and close code.

* A ticket can be changed from the update ticket action just by changing the state.

* The Security Incident integrations will fail if the 'Security Incident' table is not created, see the
  [Service Now documentation](https://docs.servicenow.com/bundle/geneva-security-management/page/product/planning_and_policy/concept/c_GetStartedWithSIM.html).
* For **ServiceNow Query** inputs, you can use [this documentation](https://docs.servicenow.com/bundle/paris-platform-user-interface/page/use/common-ui-elements/reference/r_OpAvailableFiltersQueries.html)
to format your query correctly.
  
### Limitations

Currently the only action able to retrieve Work Notes is the 'Get Journal Field Information' action.

## Developer Notes

* [ServiceNow REST API](https://developer.servicenow.com/app.do#!/rest_api_doc?v=madrid)

This plugin was last tested against product version: Paris.