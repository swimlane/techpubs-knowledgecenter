# Symantec DLP Connector
## Overview

The Symantec DLP connector allows for seamless integration with Swimlane Turbine to automate responses to data loss prevention incidents and manage data security policies.

Symantec DLP (Data Loss Prevention) is a comprehensive data security solution that helps organizations prevent data breaches and secure sensitive information. The Symantec DLP Turbine Connector enables users to automate incident response and policy management tasks within the Swimlane Turbine platform. By integrating with Symantec DLP, users can retrieve detailed incident data, manage policy enforcement, and streamline compliance processes, enhancing the overall security posture and reducing manual workload.

### Limitations
None to date.

### Supported Versions
This connector uses version 16.1 Symantec DLP.

### Additional Docs

* [Authentication](https://apidocs.securitycloud.symantec.com/#/doc?id=introduction)
* [API Documentation](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)

## Configuration

### Prerequisites


To effectively utilize the Symantec DLP connector within Swimlane Turbine, ensure you have the following prerequisites:
- HTTP Basic Authentication with the following parameters:
  * URL: Endpoint URL for the Symantec DLP API.
  * Username: Your Symantec DLP account username.
  * Password: Your Symantec DLP account password.


## Authentication Methods

#### Basic Authentication
  * URL: The base endpoint for the Symantec DLP API.
  * Username: Your Symantec DLP account username.
  * Password: Your Symantec DLP account password.


## Capabilities

This Symantec DLP Connector provides the following capabilities:

* Get All Component Matches
* Get Component Data
* Get Editable Incident Details
* Get Form Image
* Get Incident Components
* Get Incident Correlations
* Get Incident History
* Get Incident Message Body
* Get Incident Original Message
* Get Policy Matches
* Get Static Incident Details
* Update a Policy

### Get All Component Matches
* Retrieves all the matches of the components for an incident ([Click here](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)).

### Get Component Data
* Retrieves the data of a specified incident component based on the component ID ([Click here](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)).


### Get Editable Incident Details
* Retrieves editable attributes of the specified incident. The API only returns the attributes that the user has permissions to read ([Click here](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)).

### Get Form Image
* Retrieves the form image from the database or an external disk based on the message ID and violation ID ([Click here](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)).

### Get Incident Components
* Retrieves a list of all incident components. The list contains the ID, name and MIME-type of the components ([Click here](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)).

### Get Incident Correlations
* Retrieves the correlations of the specified incident ([Click here](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)).

### Get Incident History
* Retrieves the history and notes of the specified incident ([Click here](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)).

### Get Incident Message Body
* Retrieves the message body of the specified incident. The message body is available for download if required permissions are satisfied ([Click here](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)).

### Get Incident Original Message
* Retrieves the original message of the specified incident. The original message is available for download if required permissions are satisfied ([Click here](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)).

### Get Policy Matches
* Retrieves information of the other violated policies for the specified incident ([Click here](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)).

### Get Static Incident Details
* Retrieves static attributes of the specified incident. Only returns the attributes that the user has permissions to read ([Click here](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)).

### Update a Policy
* Enables or disables policies specified by the policy ID ([Click here](https://apidocs.securitycloud.symantec.com/#/doc?id=16-1-incidentdetails)).