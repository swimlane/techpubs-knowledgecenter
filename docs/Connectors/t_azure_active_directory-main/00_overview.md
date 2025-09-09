# Azure Active Directory Connector
## Overview
The Azure Active Directory connector enables streamlined user account management and automation of identity-related tasks within the Azure ecosystem.

Azure Active Directory (Azure AD) is Microsoft's cloud-based identity and access management service, which helps employees sign in and access resources. This connector enables Swimlane Turbine users to manage user accounts and automate identity-related workflows directly within the platform. By integrating with Azure AD, users can create, delete, retrieve, list, and update user accounts, streamlining identity management and enhancing security automation within their organizations.

## Prerequisites


To utilize the Azure Active Directory connector with Swimlane Turbine, ensure you have the following:
- OAuth 2.0 client credentials for authentication with these parameters:
  * URL: The endpoint URL for Azure AD services.
  * Client ID: The application (client) ID registered in Azure AD.
  * Client Secret: The application secret that was generated for the app registration in Azure AD.
  * Token URL: The URL to retrieve the OAuth2 token from Azure AD.
  * Scope: The scope of the access request, which might include one or more permissions.


## Asset Setup

### Client Credential Flow Authentication
Authentication uses Azure application OAuth2.  You will need an admin account in Azure to create the application.


Recommended Application Permissions (feel free use custom permissions if you only use
certain actions):
* User.ReadWrite.All
* Directory.ReadWrite.All
* Directory.AccessAsUser.All
* User.ReadBasic.All
* Directory.Read.All
* User.ManageIdentities.All
* User.EnableDisableAccount.All
* User.EnableDisableAccount.All


In order to set up the asset, you need the following:
* Azure Application Client ID
* Azure Application Client Secret
* Azure Tenant ID


Steps to create the Azure app:
1. Go to the [App Registration page](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
   in the Azure portal.
2. Click __New Registration__.


3. Enter a name for your new application and choose __Accounts in this organizational directory only__,
   then click __Register__ at the bottom.


4. Navigate to the __API permissions__ tab on the left navigation menu.


5. Select __Add a permission__.



6. Select __Microsoft Graph__.


7. Select __Application permissions__, then mark all the permissions you need for the
actions you are using (See suggested permissions at the top of the asset setup section).



9. Click the __Add permissions__ button at the bottom of the page.
10. Select __Grant admin consent__ for your organization, then your permissions should look as below.

11. Navigate to the __Certificates & secrets__ tab and select __New client secret__.


12. Fill out the description and expiration, then click the __Add__ button at the bottom.
13. The __Value__ of the secret you just created is the __Client Secret__ needed for the Swimlane asset.


14. Navigate to the __Overview__ tab on the left menu.


15. The __Client ID__ and __Tenant ID__ needed in the asset are shown on this page.



The __Client ID__, __Tenant ID__, and __Client Secret__ described in the steps above are the credentials you
need for the asset.

## Notes:

* For more information refer to API documentation - [API Document](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)
* [Query Parameters Documentation - OData V4](https://docs.microsoft.com/en-us/graph/query-parameters)
* For more information about the use of ConsistencyLevel and $count, see [Advanced query capabilities on directory objects](https://learn.microsoft.com/en-us/graph/aad-advanced-queries?tabs=http)