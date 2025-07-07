# CyberArk
## Overview
The CyberArk connector facilitates secure privileged access management by automating user and account operations within the CyberArk Vault.

CyberArk is a leader in privileged access management, securing privileged credentials and secrets in an enterprise environment. The CyberArk Turbine Connector enables secure, automated credential management and privileged access within Swimlane Turbine's low-code security automation platform. By integrating with CyberArk, users can streamline privileged account operations, enhance security posture, and ensure compliance with industry regulations through centralized management of sensitive credentials.

## Prerequisites


To effectively utilize the CyberArk connector within Swimlane Turbine, ensure you have the following prerequisites:
- HTTP Basic Authentication with these parameters:
  * URL: Endpoint URL for the CyberArk Vault
  * Username: User name for authentication
  * Password: Password for authentication
- OAuth 2.0 Client Credentials with these parameters:
  * URL: Endpoint URL for the CyberArk Vault
  * Client ID: Unique identifier for the OAuth client
  * Client Secret: Secret key for the OAuth client
  * Identity Tenant ID: Identifier for the tenant in the identity platform


## Capabilities

The Cyberark connector provides the following capabilities:

* Add Account
* Add Account to Group
* Add User
* Add User to Group
* Change Account Credentials
* Delete Account
* Delete Account from Group
* Delete User
* Get Account Details
* Get Accounts
* Get All Safe Members
* Get All Safes
* Get Applications
* Get Password Value
* Get Security Events
* Get User Details
* Get User Groups
* Get Users
* Remove User from Group
* Reset User Password
* Update Account
* Update Security Event Status
* Update User
* Verify Account Credentials

### Notes

*  For More Information on API's refer [CyberArk Documentation](https://docs.cyberark.com/pam-self-hosted/Latest/en/Content/WebServices/Implementing%20Privileged%20Account%20Security%20Web%20Services%20.htm?tocpath=Developer%7CREST%20APIs%7C_____0)
* [OAuth Authentication](https://docs.cyberark.com/ispss-deployment/latest/en/Content/ISPSS/ISPSS-API-Authentication.htm)
* This connector was developed against product version: 14.0
