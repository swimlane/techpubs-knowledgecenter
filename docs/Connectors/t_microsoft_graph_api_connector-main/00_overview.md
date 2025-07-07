# Microsoft Graph API Connector
## Overview
The Microsoft Graph API connector facilitates seamless integration with various Microsoft services, enabling comprehensive access and control over data and functions within the Microsoft ecosystem.

Microsoft Graph API is a unified gateway to data and intelligence in Microsoft 365, providing secure access to a wealth of resources including users, mail, files, and more. This connector enables seamless integration with third-party tools, allowing users to automate tasks within Swimlane Turbine. By leveraging this connector, users can enhance their security automation workflows, streamline data retrieval, and perform actions across various Microsoft services without manual intervention.

## Configuration

### Prerequisites


To utilize the Microsoft Graph API connector with Swimlane Turbine, ensure you have the following prerequisites:
- Delegated Flow Authentication with these parameters:
  * URL: Endpoint for Microsoft Graph API
  * Tenant ID: Unique identifier of your Azure AD tenant
  * Username: User's account username in Azure AD
  * Password: Corresponding password for the Azure AD account
  * Client ID: Application ID registered in Azure AD
  * Client Secret: Secret generated for the application in Azure AD
- Asset Authentication with these parameters:
  * URL: Endpoint for Microsoft Graph API
  * Client ID: Application ID registered in Azure AD
  * Client Secret: Secret generated for the application in Azure AD
  * Tenant ID: Unique identifier of your Azure AD tenant
  * Scope: Permissions the app requires
- OAuth2 Client Credentials with these parameters:
  * URL: Endpoint for Microsoft Graph API
  * Client ID: Application ID registered in Azure AD
  * Client Secret: Secret generated for the application in Azure AD
  * Token URL: URL to retrieve the oauth2 token
  * Scope: Permissions the app requires


## Authentication Methods

#### OAuth 2.0 client credentials authentication with these parameters:
  * url: Endpoint for Microsoft Graph API.
  * client_id: Application (client) ID registered in Azure AD.
  * client_secret: Client secret (key) generated for the application in Azure AD.
  * token_url: URL to retrieve the OAuth token.
  * scope: Permissions the app requires.

#### Password Grant (Delegated Authentication) for acting on behalf of a user:
  * url: Endpoint for Microsoft Graph API.
  * tenant_id: Directory ID of the Azure AD tenant.
  * oauth_un: User's username to authenticate.
  * oauth_pwd: User's password to authenticate.
  * oauth_cl_id: Application (client) ID registered in Azure AD.
  * oauth_cl_secret: Client secret (key) generated for the application in Azure AD.
  * login_url: Login URL. Default value is https://login.microsoftonline.com. (Optional).
  * scope: Permissions the app requires. Optional field. (Optional).

#### Asset credentials specific to your organization (Microsoft Graph API Asset - Tenant ID):
  * url: Endpoint for Microsoft Graph API.
  * client_ID: Application (client) ID registered in Azure AD.
  * client_Secret: Client secret (key) generated for the application in Azure AD.
  * tenant_id: Directory ID of the Azure AD tenant.
  * scope: Permissions the app requires.

## Capabilities

The Microsoft Graph API connector gives the ability to get and update security alerts, and modify user licenses and sessions.

* Add Group Member
* Add Group Owner
* Add Identity Directory Device Registered User
* Add Identity Directory Role Member
* Add Incident Comment
* Add member to Directory Administrative Unit
* Add Members
* Assign and Remove License
* Audit Logs Get SignIn
* Audit Logs List SignIns
* Cancel Security Action
* Create Contact
* Create Event
* Create rejectedSender
* Create Group
* Create Identity Directory Device
* Create Identity Directory Domain
* Create Identity Directory Role Management
* Create Security Action
* Create Threat Intelligence Indicator for Azure Sentinel
* Create Threat Intelligence Indicator for Microsoft Defender
* Create User Mail Rule
* Delete Directory Administrative Unit Member
* Delete Email
* Delete Email Authentication Method
* Delete FIDO2 Authentication Method
* Delete Identity Directory Device
* Delete Identity Directory Device Registered User
* Delete Identity Directory Domain
* Delete Identity Directory Role Management
* Delete Identity Directory Role Member
* Delete Microsoft Authenticator Auth Method
* Delete Phone Authentication Method
* Delete Profile Email
* Delete Software OATH Authentication Method
* Delete Temporary Access Pass Auth Method
* Delete Threat Intelligence Indicator
* Delete User Mail Rule
* Delete Windows Hello For Business Auth Method
* Expand and Get Item Properties Attached to Message
* Forward Email
* Get Alert
* Get Control Profile
* Get Directory Administrative Unit
* Get Directory Administrative Unit List
* Get Directory Administrative Unit Member
* Get Directory Administrative Unit Member List
* Get Documents Shared
* Get Documents Used or Viewed
* Get Email Attachments
* Get Emails
* Export Email as EML
* Get File Metadata
* Get Folders
* Get Group
* Get Group Member List
* Get Group Owners List
* Get Group Rejected Senders List
* Get Groups List
* Get Identity Directory Device
* Get Identity Directory Device Group List
* Get Identity Directory Device List
* Get Identity Directory Domain
* Get Identity Directory Domain List
* Get Identity Directory Object
* Get Identity Directory Objects by IDs List
* Get Identity Directory Registered Users List
* Get Identity Directory Role
* Get Identity Directory Role Assignment
* Get Identity Directory Role Management
* Get Identity Directory Role Management List
* Get Identity Directory Role Members List
* Get Identity Directory Roles Assignment List
* Get Identity Directory Roles Assignment List
* Get License Details
* Get List of Child Folders
* Get Manager Root Level
* Get Profile Email
* Get Profile Email List
* Get Risk Detections
* Get Secure Control Profiles List
* Get Secure Score
* Get Secure Scores List
* Get Security Action
* Get Security Action List
* Get Security Get Incident
* Get Security Get Repeat Offenders
* Get Security Get Simulation
* Get Security Get Simulation Automations
* Get Security Get Simulation Coverage For Users
* Get Security Get Simulation Overview
* Get Security Get Training Coverage Users
* Get Security List Incident
* Get Security List Simulation
* Get Security List Simulation Automations
* Get Security List Simulation Users
* Get Security Run Hunting Query
* Get Security eDiscovery Get Case
* Get Security eDiscovery List Case Custodians
* Get Security eDiscovery List Case Operations
* Get Security eDiscovery List Case Review Sets
* Get Security eDiscovery List Case Searches
* Get Security eDiscovery List Case Tags
* Get Security eDiscovery List Cases
* Get Site Drives
* Get Threat Assessment
* Get Threat Assessment List
* Get Threat Intelligence Indicator
* Get Threat Intelligence Indicators List
* Get Trending Documents
* Get User Collaborators List
* Get User Mail Rule
* Get User Mail Rules List
* Get User by ID
* List a Users Direct Membership
* List Alerts
* List Analyzed Emails
* List riskyUsers
* List Password Authentication Methods
* Move Email
* Post Group Rejected Sender
* Post Threat Assessment Email
* Post Threat Assessment File
* Post Threat Assessment URI
* Post Threat Assessment URL
* Remove Directory Role Member
* Remove Group Rejected Sender
* Reply to Email
* Reset User Password
* Revoke User Signin Session
* Send Email
* SharePoint Add or Update File
* SharePoint Checkin File
* Sharepoint Checkout File
* Sharepoint Create List
* Sharepoint Create List Item
* Sharepoint Create list column
* Sharepoint Delete List
* Sharepoint Delete List Column
* Sharepoint Delete List Item
* Sharepoint Get File
* Sharepoint Get List
* Sharepoint Get List Columns
* Sharepoint Get List Columns
* Sharepoint Get Site
* Sharepoint Update List Item
* Update Alert
* Update Incident
* Update User
* Retrieve Authentication Methods

## Asset Setup

### Client Credential Flow Authentication
Authentication uses Azure application OAuth2.  You will need an admin account in Azure to create the application.

Recommended Application Permissions (feel free use custom permissions if you only use
certain actions):
* User.ReadWrite.All
* Calendars.ReadWrite
* Directory.ReadWrite.All
* Directory.AccessAsUser.All
* SecurityEvents.Read.All
* SecurityEvents.ReadWrite.All
* Mail.ReadWrite
* Mail.Send
* Sites.ReadWrite.All
* Files.ReadWrite.All
* AuditLog.Read.All
* Mail.ReadBasic.All
* SecurityAnalyzedMessage.ReadWrite.All
* SecurityAlert.ReadWrite.All
* User.ManageIdentities.All,
* User.EnableDisableAccount.All,
* User.ReadWrite.All
* SecurityIncident.ReadWrite.All
* UserAuthenticationMethod.Read.All
* UserAuthenticationMethod.ReadWrite.All
* Group.ReadWrite.All	
* IdentityRiskyUser.Read.All

Sites.ReadWrite.All is needed by Sharepoint actions only.

In order to set up the asset, you need the following:
* Azure Application Client ID
* Azure Application Client Secret
* Azure Tenant ID

Steps to create the Azure app:
1. Go to the [App Registration page](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
   in the Azure portal.
2. Click `New Registration`.
3. Enter a name for your new application and choose `Accounts in this organizational directory only`,
   then click `Register` at the bottom.
4. Navigate to the `API permissions` tab on the left navigation menu.
5. Select `Add a permission`.
6. Select `Microsoft Graph`.
7. Select `Application permissions`, then mark all the permissions you need for the
actions you are using (See suggested permissions at the top of the asset setup section).
9. Click the `Add permissions` button at the bottom of the page.
10. Select `Grant admin consent` for your organization, then your permissions should look as below.
11. Navigate to the `Certificates & secrets` tab and select `New client secret`.
12. Fill out the description and expiration, then click the `Add` button at the bottom.
13. The `Value` of the secret you just created is the `Client Secret` needed for the Swimlane asset.
14. Navigate to the `Overview` tab on the left menu.
15. The `Client ID` and `Tenant ID` needed in the asset are shown on this page.

The `Client ID`, `Tenant ID`, and `Client Secret` described in the steps above are the credentials you
need for the asset.

### Password Flow (Delegated Auth)

* Use Delegated Permissions, instead of Application Permissions, and generate `Client ID`, `Tenant ID`, and `Client Secret` as described in the above Client Credential Flow Authentication.
* We also need an `Username` and a `Password` for this authentication.

### Limit Access to specific mailboxes

Administrators who want to limit app access to specific mailboxes can create an application access policy by using
the __New-ApplicationAccessPolicy__ PowerShell cmdlet.
For more information please see the article [Limiting application permissions to specific Exchange Online mailboxes](https://docs.microsoft.com/en-us/graph/auth-limit-mailbox-access).

## Action Setup

### OData filters

Information on the filter input formatting can be found [here](https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter).

Keep in mind that not specifying a folder as an input will result in the query affecting all possible folders.
Example:
If we want to ingest only unread emails, and we don't set the input "folder", we will ingest all unread emails from all folders, including "Deleted Items", "Junk", etc.

### Well Known Folders

Well known folders can be used instead of Folder IDs for email actions.  All well known folder names can be found
[here](https://docs.microsoft.com/en-us/graph/api/resources/mailfolder?view=graph-rest-1.0).

### Sites Get Site

All the Sites actions require the site ID to be executed. The site ID can be obtained using the action Sites Get Site, in
order to run the action the `site_hostname` and `site_name` are needed. This two values can be found in a site URL:

```
https://{site_hostname}.sharepoint.com/sites/{site_name}
```

For example if our site URL is `https://swimlaneintegrations.sharepoint.com/sites/IntegrationsSite` we should use:

- `site_hostname`: `swimlaneintegrations`
- `site_name`: `IntegrationsSite`

After the action execution you can find the Site ID on the `ID` output field.

### Sites Create List

In order to create a list with its columns, use the input `Columns`. You can find all the possible values with
its configuration on the following table.

| Property name         | Type                        | Description                                                                                                             |
|-----------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------|
| boolean               | [booleanColumn](https://docs.microsoft.com/en-us/graph/api/resources/booleancolumn?view=graph-rest-1.0)               | This column stores boolean values.                                                                                      |
| calculated            | [calculatedColumn](https://docs.microsoft.com/en-us/graph/api/resources/calculatedcolumn?view=graph-rest-1.0)            | This column's data is calculated based on other columns.                                                                |
| choice                | [choiceColumn](https://docs.microsoft.com/en-us/graph/api/resources/choicecolumn?view=graph-rest-1.0)                | This column stores data from a list of choices.                                                                         |
| currency              | [currencyColumn](https://docs.microsoft.com/en-us/graph/api/resources/currencycolumn?view=graph-rest-1.0)              | This column stores currency values.                                                                                     |
| dateTime              | [dateTimeColumn](https://docs.microsoft.com/en-us/graph/api/resources/datetimecolumn?view=graph-rest-1.0)              | This column stores DateTime values.                                                                                     |
| geolocation           | [geolocationColumn](https://docs.microsoft.com/en-us/graph/api/resources/geolocationcolumn?view=graph-rest-1.0)           | This column stores a geolocation.                                                                                       |
| lookup                | [lookupColumn](https://docs.microsoft.com/en-us/graph/api/resources/lookupcolumn?view=graph-rest-1.0)                | This column's data is looked up from another source in the site.                                                        |
| number                | [numberColumn](https://docs.microsoft.com/en-us/graph/api/resources/numbercolumn?view=graph-rest-1.0)                | This column stores number values.                                                                                       |
| personOrGroup         | [personOrGroupColumn](https://docs.microsoft.com/en-us/graph/api/resources/personorgroupcolumn?view=graph-rest-1.0)         | This column stores Person or Group values.                                                                              |
| text                  | [textColumn](https://docs.microsoft.com/en-us/graph/api/resources/textcolumn?view=graph-rest-1.0)                  | This column stores text values.                                                                                         |
| validation            | [columnValidation](https://docs.microsoft.com/en-us/graph/api/resources/columnvalidation?view=graph-rest-1.0)            | This column stores validation formula and message for the column.                                                       |
| hyperlinkOrPicture    | [hyperlinkOrPictureColumn](https://docs.microsoft.com/en-us/graph/api/resources/hyperlinkorpicturecolumn?view=graph-rest-1.0)    | This column stores hyperlink or picture values.                                                                         |
| term                  | [termColumn](https://docs.microsoft.com/en-us/graph/api/resources/termcolumn?view=graph-rest-1.0)                  | This column stores taxonomy terms.                                                                                      |
| thumbnail             | [thumbnailColumn](https://docs.microsoft.com/en-us/graph/api/resources/thumbnailcolumn?view=graph-rest-1.0)             | This column stores thumbnail values.                                                                                    |
| contentApprovalStatus | [contentApprovalStatusColumn](https://docs.microsoft.com/en-us/graph/api/resources/contentapprovalstatuscolumn?view=graph-rest-1.0) | This column stores content approval status.                                                                             |

For a complete version of this table please see [the official column definition table.](https://docs.microsoft.com/en-us/graph/api/resources/columndefinition?view=graph-rest-1.0#properties)

### Create List Column

Refer to the above table to get the `Type properties` and `Column type` input. The `Type properties` are
documented within the links in the `Type` column.

### Get list items

In order to use the filter input please refer to the [OData filters](#odata-filters) section.

The column used to filter the output must be indexed, see the [Microsoft documentation](https://support.microsoft.com/en-us/office/add-an-index-to-a-list-or-library-column-f3f00554-b7dc-44d1-a2ed-d477eac463b0?ui=en-us&rs=en-us&ad=us) to add an index to a list.

## Limitations

When using `$filter` and `$orderby` in the same query to get messages, make sure to specify properties in the following ways:

* Properties that appear in `$orderby` must also appear in $filter.
* Properties that appear in `$orderby` are in the same order as in $filter.
* Properties that are present in `$orderby` appear in `$filter` before any properties that aren't.

Failing to do this results in the following error:

* Error code: InefficientFilter
* Error message: The restriction or sort order is too complex for this operation.

The Assign/Remove User License requires either the disabled plans and accompanying SKU IDs to assign licenses or the
SKU ID of the license you want to remove.

The Get Security Alert has additional information it can return. There are a large number of fields that don't
relate to many alerts, so they are not mapped; you can add them if desired.

## Notes

- [An Introduction to Microsoft Graph API](https://social.technet.microsoft.com/wiki/contents/articles/33525.an-introduction-to-microsoft-graph-api.aspx)
- [Microsoft Graph Security API Homepage](https://www.microsoft.com/en-us/security/intelligence-security-api)
- [Microsoft Graph REST API v1.0 reference](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0)
- [Query Parameters Documentation - OData V4](https://docs.microsoft.com/en-us/graph/query-parameters)
- [Microsoft Graph Security API v1.0 refrence](https://docs.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-beta)
- [Azure AD OAuth2 flow](https://docs.microsoft.com/en-us/azure/active-directory/develop/v1-protocols-oauth-code)
- [oauthlib Legacy Application client](https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#legacy-application-flow), this is sort of a hack to bypass manual login (typically required)
- [Limiting application permissions to specific Exchange Online mailboxes](https://docs.microsoft.com/en-us/graph/auth-limit-mailbox-access)
- [Microsoft Graph Reports Audit Logs API reference](https://learn.microsoft.com/en-us/graph/api/resources/azure-ad-auditlog-overview?view=graph-rest-1.0)