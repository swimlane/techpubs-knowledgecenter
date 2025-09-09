# Microsoft Azure Sentinel Connector

## Overview

The Azure Sentinel connector facilitates seamless integration with Azure Sentinel's SIEM and SOAR capabilities, enabling automated threat response and management.

Microsoft Azure Sentinel is a scalable, cloud-native security information event management (SIEM) and security orchestration automated response (SOAR) solution. This connector enables Swimlane Turbine users to automate incident response and management, streamline comment additions, rule creation, and updates directly within Azure Sentinel. By integrating with Azure Sentinel, users can enhance their security posture, reduce response times, and leverage a comprehensive view of their security landscape without leaving the Swimlane platform.

## Prerequisites

Before you can use the Microsoft Azure Sentinel connector for Turbine, ensure you have the following:

- OAuth 2.0 client credentials authentication with the following parameters:
  - URL: Endpoint for Azure Sentinel API
  - Client ID: Unique identifier for the registered Azure application
  - Client Secret: Confidential secret key for the registered Azure application
  - Token URL: Endpoint to retrieve the OAuth2 token

## Token URL

Use the following as the token URL,

- To run the Log Analytics Query action, use `https://login.microsoftonline.com/{tenant_id}/oauth2/token`.
- For all other actions, use `https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token`.

### Host URL

- To run the Log Analytics Query action, use `https://api.loganalytics.azure.com/`.
- For all other actions, use `https://management.azure.com/`.

## Action setup

To run the Incident management actions, you need a `Resource Group Name`, `Subscription ID` and `Workspace Name.`

## Steps to create the Azure app:

1. Go to the [App Registration page](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
   in the Azure portal.
2. Click `New Registration`.
3. Enter a name for your new application and choose `Accounts in this organizational directory only`,
   then click `Register` at the bottom.
4. Navigate to the `API permissions` tab on the left navigation menu.
5. Select `Add a permission`.
6. Add the following permissions.
   - Microsoft Graph / SecurityEvents.ReadWrite.All
   - WindowsDefenderATP / Alert.ReadWrite.All
7. Navigate to the `Certificates & Secrets` tab and select `New client secret`.
8. Fill out the description and expiration, then click the `Add` button at the bottom.
9. The `Value` of the secret you just created is the `Client Secret` needed for the Swimlane asset.
10. Navigate to the `Overview` tab on the left menu.
11. The `Client ID` and `Tenant ID` needed in the asset are shown on this page.
12. Go back to the main Azure portal windows, and click on your app overview. Copy the following values.

- Resource Group Name
- Subscription ID
- Workspace Name
- Workspace ID

## Capabilities

The Microsoft Azure Sentinel connector provides the following capabilities:

- Create or Update Fusion Alert Rule
- Create or Update Incident
- Create or Update MSSIC(MicrosoftSecurityIncidentCreation) Alert Rule
- Create or Update Saved Searches
- Create or Update Scheduled Alert Rule
- Delete Alert Rules
- Delete Incident
- Delete Incident Comments
- Delete Saved Searches
- Get Alert Entities
- Get Alert Rules by Rule ID
- Get Incident
- Get Incident Comment
- Get Saved Searches
- List Alert Rules
- List by Workspace Saved Searches
- List Incident Alerts
- List Incident Bookmarks
- List Incident Comments
- List Incident Entities
- List Incidents
- Run Analytics Query
- Update Incident Comment

## Known Issues

If you get a 403 HTTP error, you have to add that Azure app to the Sentinel workspace and assign the Contributor Role to it.

## Notes

[Incident Management API](https://learn.microsoft.com/en-us/rest/api/securityinsights/stable/incidents)

[Saved Searches API](https://learn.microsoft.com/en-us/rest/api/loganalytics/saved-searches)

[Analytics Query](https://learn.microsoft.com/en-us/rest/api/loganalytics/dataaccess/query/get?tabs=HTTP)

[Analytics Query Auth and Permissions](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/api/access-api)

[API Version Doc](https://learn.microsoft.com/en-us/rest/api/securityinsights/api-versions)
