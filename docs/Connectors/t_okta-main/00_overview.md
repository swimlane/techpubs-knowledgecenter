# Okta Connector
## Overview
The Okta Identity Management connector allows seamless integration with Okta's services, enabling automated identity and access management operations.

Okta Identity Management is a comprehensive identity management service that simplifies user authentication, authorization, and lifecycle processes. The Swimlane Turbine Okta connector enables security teams to automate critical identity management tasks, such as user activation, group membership adjustments, application lifecycle management, and session control. By integrating with Okta, Swimlane Turbine users can enhance their security posture, streamline user and application management, and respond rapidly to identity-related incidents, all within a low-code automation environment.

## Prerequisites


Before you can utilize the Okta Identity Management connector for Turbine, ensure you have the following:
- API Key Authentication with the following parameters:
  * URL: The endpoint URL for the Okta API.
  * API Key: A valid API key to authenticate requests to the Okta API.


## Capabilities

The Okta Connector has the following capabilities:

* Activate User
* Deactivate User
* Suspend User
* Unsuspend User
* Unlock User
* Force User Password Reset
* Clear User Session
* Get Users: List All, filter, get by ID, search
* Get Events: List All, filter by keyword, filter by query string.
* Get Applications: List all or filter
* Get Application by ID
* Activate Application by ID
* Deactivate Application by ID
* Delete Application by ID
* List Groups
* Add or Remove User from Group
* Get User Event of Removed Apps
* Get Applications for User

## Notes

- Information for event actions including filter expressions, event types and correlations can be found at: https://developer.okta.com/docs/reference/api/system-log/#request-parameters
- Information for user actions including search examples, filter examples and name queries can be found at: https://developer.okta.com/docs/reference/api/users/#get-user-with-login-shortname
- Information for group actions including filtering expressions can be found at: https://developer.okta.com/docs/reference/api/groups/#group-rule-operations
- The complete documentation for the API is found at: https://developer.okta.com/docs/reference/