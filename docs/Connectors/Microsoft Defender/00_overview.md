# Microsoft Defender Advanced Threat Protection Connector
## Overview
The Microsoft Defender connector allows for seamless integration with Swimlane Turbine, enabling automated security incident response and threat management.

Microsoft Defender is a comprehensive endpoint security solution that provides real-time protection against a wide range of threats such as malware, phishing, and ransomware. The Microsoft Defender Turbine Connector enables users to automate and orchestrate security workflows, enhancing threat detection and response capabilities within the Swimlane Turbine platform. By leveraging this integration, security teams can streamline incident management, perform in-depth investigations, and enforce security controls across their digital environment without manual intervention.

## Prerequisites


Before you can use the Microsoft Defender connector for Turbine, ensure you have the following prerequisites:
- OAuth 2.0 client credentials authentication with these parameters:
  * URL: Endpoint URL for Microsoft Defender API
  * Client ID: Application (client) ID registered in Azure AD
  * Client Secret: Secret key generated for the application in Azure AD
  * Scope: The scope of the access request, which specifies the resources that the application should access
- Delegated flow authentication with these parameters:
  * URL: Endpoint URL for Microsoft Defender API
  * Tenant ID: Directory (tenant) ID in Azure AD
  * Username: The username of the user on behalf of whom the application is authenticating
  * Password: The password for the specified username
  * Client ID: Application (client) ID registered in Azure AD
  * Client Secret: Secret key generated for the application in Azure AD


## Authentication Methods

#### OAuth 2.0 client credentials authentication with these parameters:
  * URL: Endpoint for Microsoft Defender API
  * Client ID: Application ID registered in Azure AD
  * Client Secret: Key generated for the application in Azure AD
  * Tenant ID or Token URL: At least one of these parameters is required for authentication:
      * Tenant ID: Identifier for the Azure AD tenant
      * Token URL: Token URL for Azure AD. Must start with https://login.microsoftonline.com/, followed by the tenant_id, and appended with /oauth2/v2.0/token.
  * Scope: Permissions the application requires

#### Delegated Flow Authentication with these parameters:
  * URL: Endpoint for Microsoft Defender API
  * Tenant ID: Identifier for the Azure AD tenant
  * Username: The username for delegated access
  * Password: The password for delegated access
  * Client ID: Application ID registered in Azure AD
  * Client Secret: Key generated for the application in Azure AD
  * Login URL: Login URL. Default value is https://login.microsoftonline.com. (Optional).
  * scope: Permissions the app requires. Optional field. (Optional).

## Additional Notes about Asset

* Please make sure to pass atleast one of the __Tenant ID__ or __Token URL__ in the inputs for the asset.

## Asset and Permissions Setup

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

6. Select __APIs my organization uses__ tab or any __Permissions__ relevant tab.

7. Select the relevant options or permissions for the action you want to test or run, then mark all the permissions you need for the actions you are using (See suggested permissions at the top of the asset setup section).

9. Click the __Add permissions__ button at the bottom of the page.
10. Select __Grant admin consent__ for your organization, then your permissions should look as below.

11. Navigate to the __Certificates & secrets__ tab and select __New client secret__.

12. Fill out the description and expiration, then click the __Add__ button at the bottom.
13. The __Value__ of the secret you just created is the __Client Secret__ needed for the Swimlane asset.

14. Navigate to the __Overview__ tab on the left menu.

15. The __Client ID__ and __Tenant ID__ needed in the asset are shown on this page.

The __Client ID__, __Tenant ID__, and __Client Secret__ described in the steps above are the credentials you
need for the asset.


## Capabilities

The Microsoft Defender Advanced Threat Protection integration provides the following capabilities:

* Cancel Machine Action
* Create Alert
* Decode Generated Bearer Token
* Delete Indicator by ID
* Get Alert
* Get Alert Domains
* Get Alert Files
* Get Alert IPs
* Get Alert Machine Information
* Get Alert User Information
* Get Alerts
* Get Domain Related Alerts
* Get Domain Related Machines
* Get Domain Seen Organization
* Get Domain Statistics
* Get File Information
* Get File Related Alerts
* Get File Related Machines
* Get File Statistics
* Get Incident
* Get Incidents List
* Get Indicators
* Get Investigation
* Get Investigation Collection Package
* Get IP Related Alerts
* Get IP Related Machines
* Get IP Seen Organization
* Get IP Statistics
* Get Machine
* Get Machine Action
* Get Machine Logon Users
* Get Machine Related Alerts
* Get Machines
* Get User Related Alerts
* Get User Related Machines
* Get Vulnerability by ID
* Import Indicators
* Invoke Collection Of Investigation Package
* Isolate Machine
* List All Remediation Activities
* List Devices by Vulnerability
* List Vulnerabilities
* List Vulnerabilities by Machine and Software
* Offboard Machine
* Query Advanced Hunting
* Remove App Restriction
* Restrict App Execution 
* Run Antivirus Scan
* Run Query
* Start Investigation
* Stop And Quarantine File
* Submit Indicator
* UnIsolate Machine
* Update Alert
* Update Incident by ID

## Notes

*  Use these scopes in the asset as per the action requirement 
  * https://api.securitycenter.microsoft.com/.default
  * https://security.microsoft.com/mtp/.default

* Whenever you are using a particular action, please make sure you visit the relevant API Docs and provide the required permissions needed in your application for that action to run without issues.

### Additional Information about Capabilities

The Microsoft Defender Advanced Threat Protection API allows the user to run queries against their enrolled systems. You can find information about the Advanced Hunting API [here](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/run-advanced-query-api).

Additionally, Microsoft has provided example queries [here](https://github.com/microsoft/WindowsDefenderATP-Hunting-Queries).

## Installation Considerations

To utilize this Connector, you must have access to an E5 license of Microsoft Defender ATP. Additionally, you must create a new application in Azure Active Directory:

+ Start a new [trial](https://www.microsoft.com/en-us/microsoft-365/windows/microsoft-defender-atp) of Microsoft Defender ATP or use your existing license to access the API.
    + If you have not done so already, please follow the initial setup instructions [here](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/licensing).
+ Once you have a Microsoft Defender ATP installed on a machine, then you will create a new application in Azure Active Directory.

## Application Permissions
* Ti.ReadWrite.All required for Import Indicators Action