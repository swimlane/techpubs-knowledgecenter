## HaloPSA Connector

## Overview

The HaloPSA connector enables automated interactions with the HaloPSA ticketing system, facilitating efficient ticket management and incident resolution.

HaloPSA is a comprehensive Professional Services Automation (PSA) solution that streamlines ticket management and incident tracking for IT service management. This connector enables Swimlane Turbine users to automate ticket operations, such as adding, updating, retrieving, and deleting tickets within HaloPSA. By integrating with HaloPSA, security teams can efficiently manage service requests, incidents, and changes directly from the Swimlane platform, enhancing response times and operational efficiency.

### Limitations

None to date.

### Supported Versions

This connector supports the latest version of the HaloPSA REST API.

## Additional Docs

* [HaloPSA Authentication Link](https://swimlane.halopsa.com/apidoc/authentication/client)
* [HaloPSA API Docs](https://swimlane.halopsa.com/apidoc/resources/tickets)

### Configuration

## Prerequisites


To effectively utilize the HaloPSA connector within the Swimlane Turbine platform, ensure you have the following prerequisites:
- OAuth2 Password Credentials with the following parameters:
  * URL: The endpoint URL for the HaloPSA API.
  * HaloPSA Username: Your HaloPSA account username.
  * HaloPSA Password: Your HaloPSA account password.
  * Client ID: The client identifier as registered in HaloPSA.
  * Scopes: The scope of access requested from HaloPSA.
- OAuth2 Client Credentials with the following parameters:
  * URL: The endpoint URL for the HaloPSA API.
  * Client ID: The client identifier as registered in HaloPSA.
  * Client Secret: The secret key associated with your client ID in HaloPSA.
  * Scopes: The scope of access requested from HaloPSA.


## Authentication Methods

To effectively utilize the HaloPSA connector within Swimlane Turbine, ensure you have the following prerequisites:

- OAuth 2.0 Client Credentials for authentication with these parameters:

  * URL: Endpoint for HaloPSA API access.
  * Client ID: Unique identifier for the application making the request.
  * Client Secret: A secret known only to the application and the authorization server.
  * Scopes: Permissions the application needs to function correctly.

- OAuth 2.0 Password Credentials for authentication with these parameters:

  * URL: Endpoint for HaloPSA API access.
  * HaloPSA Username: Your HaloPSA user account name.
  * HaloPSA Password: Your HaloPSA user account password.
  * Client ID: Unique identifier for the application making the request.
  * Scopes: Permissions the application needs to function correctly.

## Capabilities

This Connector provides the following capabilities:

* Add or Update Ticket
* Delete Ticket by ID
* Get Ticket by ID
* Get Tickets

### Add or Update Ticket

Adds or updates one or more tickets. If ID is included then updates, if not included then creates new.

HaloPSA's Documentation for this action can be found [here](https://swimlane.halopsa.com/apidoc/resources/tickets).

### Delete Ticket by ID

Deletes the ticket and related objects with the specified ID.

HaloPSA's Documentation for this action can be found [here](https://swimlane.halopsa.com/apidoc/resources/tickets).

### Get Ticket by ID

Returns a single ticket object.

HaloPSA's Documentation for this action can be found [here](https://swimlane.halopsa.com/apidoc/resources/tickets).

### Get Tickets

Returns an object containing the count of tickets, and an array of ticket objects.

HaloPSA's Documentation for this action can be found [here](https://swimlane.halopsa.com/apidoc/resources/tickets).
