# Create Threat Intel Indicator Azure Sentinel

**Description**: Creates a Threat Intelligence Indicator in Azure Sentinel, including threat type, target product, and TLP level.

## Endpoint

- **URL:** `/beta/security/tiIndicators`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **action** (string) – Required: The action to apply if the indicator is matched from within the targetProduct security tool. Possible values are `unknown`, `allow`, `block` or `alert`
  - **activityGroupNames** (array): The cyber threat intelligence name(s) for the parties responsible for the malicious activity covered by the threat indicator
  - **additionalInformation** (string): A catchall area into which extra data from the indicator not covered by the other tiIndicator properties may be placed. Data placed into additionalInformation will typically not be utilized by the targetProduct security tool
  - **azureTenantId** (string) – Required: Stamped by the system when the indicator is ingested. The Azure Active Directory tenant id of submitting client
  - **confidence** (number): An integer representing the confidence the data within the indicator accurately identifies malicious behavior. Acceptable values are 0-100 with 100 being the highest.
  - **description** (string) – Required: Brief description (100 characters or less) of the threat represented by the indicator
  - **diamondModel** (string): The area of the Diamond Model in which this indicator exists. Possible values are `unknown`, `adversary`, `capability`, `infrastructure` and `victim`
  - **domainName** (string): Domain name associated with this indicator. Should be of the format subdomain.domain.topleveldomain (For example, baddomain.domain.net)
  - **emailEncoding** (string): The type of text encoding used in the email
  - **emailLanguage** (string): The Language of the email
  - **emailRecipient** (string): Email Recipient Address
  - **emailSenderAddress** (string): Email Sender Address
  - **emailSenderName** (string): Email Sender Name
  - **emailSourceDomain** (string)
  - **emailSourceIpAddress** (string)
  - **emailSubject** (string)
  - **emailXMailer** (string): X-Mailer value used in the email
  - **expirationDateTime** (string) – Required: The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time
  - **externalId** (string)
  - **fileCompileDateTime** (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time
  - **fileCreatedDateTime** (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time
  - **fileHashType** (string): The type of hash stored in fileHashValue. Possible values are `unknown`, `sha1`, `sha256`, `md5`, `authenticodeHash256`, `lsHash`, `ctph`
  - **fileHashValue** (string)
  - **fileMutexName** (string)
  - **fileName** (string)
  - **filePacker** (string)
  - **filePath** (string): Path of file indicating compromise. May be a Windows or *nix style path
  - **fileSize** (number): Size of the file in bytes
  - **fileType** (string): Text description of the type of file. For example `Word Document` or `Binary`
  - **isActive** (string): Used to deactivate indicators within system. By default, any indicator submitted is set as active. However, providers may submit existing indicators with this set to `false` to deactivate indicators in the system.
  - **killChain** (array): A JSON array of strings that describes which point or points on the Kill Chain this indicator targets. Possible values are `Actions`, `C2`, `Delivery`, `Exploitation`, `Installation`, `Reconnaissance`, `Weaponization`
  - **knownFalsePositives** (string): Scenarios in which the indicator may cause false positives. This should be human-readable text
  - **lastReportedDateTime** (string): The last time the indicator was seen. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time
  - **malwareFamilyNames** (string): The malware family name associated with an indicator if it exists. Microsoft prefers the Microsoft malware family name if at all possible which can be found via the Windows Defender Security Intelligence threat encyclopedia
  - **networkCidrBlock** (string): CIDR Block notation representation of the network referenced in this indicator. Use only if the Source and Destination cannot be identified
  - **networkDestinationAsn** (number): The destination autonomous system identifier of the network referenced in the indicator
  - **networkDestinationCidrBlock** (string): CIDR Block notation representation of the destination network in this indicator
  - **networkDestinationIPv4** (string)
  - **networkDestinationIPv6** (string)
  - **networkDestinationPort** (number)
  - **networkIPv4** (string): IPv4 IP address. Use only if the Source and Destination cannot be identified
  - **networkIPv6** (string): IPv6 IP address. Use only if the Source and Destination cannot be identified
  - **networkPort** (number): TCP port. Use only if the Source and Destination cannot be identified
  - **networkProtocol** (number): Decimal representation of the protocol field in the IPv4 header
  - **networkSourceAsn** (number): The source autonomous system identifier of the network referenced in the indicator
  - **networkSourceCidrBlock** (string): CIDR Block notation representation of the source network in this indicator
  - **networkSourceIPv4** (string)
  - **networkSourceIPv6** (string)
  - **networkSourcePort** (number)
  - **passiveOnly** (string): Determines if the indicator should trigger an event that is visible to an end-user. When set to `true` security tools will not notify the end user that a hit has occurred. This is most often treated as audit or silent mode by security products where they will simply log that a match occurred but will not perform the action. Default value is `false`
  - **severity** (number): An integer representing the severity of the malicious behavior identified by the data within the indicator. Acceptable values are 0–5 where 5 is the most severe and 0 is not severe at all. Default value is 3
  - **tags** (array): A JSON array of strings that stores arbitrary tags/keywords
  - **targetProduct** (string) – Required: A string value representing a single security product to which the indicator should be applied. Acceptable values are `Azure Sentinel`, ``
  - **threatType** (string) – Required: Each indicator must have a valid Indicator Threat Type. Possible values are `Botnet`, `C2`, `CryptoMining`, `Darknet`, `DDoS`, `MaliciousUrl`, `Malware`, `Phishing`, `Proxy`, `PUA`, `WatchList`
  - **tlpLevel** (string) – Required: Traffic Light Protocol value for the indicator. Possible values are `unknown`, `white`, `green`, `amber`, `red`
  - **url** (string): Uniform Resource Locator. This URL must comply with RFC 1738
  - **userAgent** (string): User-Agent string from a web request that could indicate compromise
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **id** (string)
  - **azureTenantId** (string)
  - **action** (string)
  - **additionalInformation** (object)
  - **activityGroupNames** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **confidence** (object)
  - **description** (string)
  - **diamondModel** (object)
  - **emailEncoding** (object)
  - **emailLanguage** (object)
  - **emailRecipient** (object)
  - **emailSenderAddress** (object)
  - **emailSenderName** (object)
  - **emailSourceDomain** (object)
  - **emailSourceIpAddress** (object)
  - **emailSubject** (object)
  - **emailXMailer** (object)
  - **expirationDateTime** (string)
  - **externalId** (object)
  - **fileCompileDateTime** (object)
  - **fileCreatedDateTime** (object)
  - **fileHashType** (object)
  - **fileHashValue** (object)
  - **fileMutexName** (object)
  - **fileName** (object)
  - **filePacker** (object)
  - **filePath** (object)
  - **fileSize** (object)
  - **fileType** (object)
  - **domainName** (object)
  - **ingestedDateTime** (string)
  - **isActive** (boolean)
  - **killChain** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **knownFalsePositives** (object)
  - **lastReportedDateTime** (object)
  - **malwareFamilyNames** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **networkCidrBlock** (object)
  - **networkDestinationAsn** (object)
  - **networkDestinationCidrBlock** (object)
  - **networkDestinationIPv4** (string)
  - **networkDestinationIPv6** (object)
  - **networkDestinationPort** (object)
  - **networkIPv4** (object)
  - **networkIPv6** (object)
  - **networkPort** (object)
  - **networkProtocol** (object)
  - **networkSourceAsn** (object)
  - **networkSourceCidrBlock** (object)
  - **networkSourceIPv4** (object)
  - **networkSourceIPv6** (object)
  - **networkSourcePort** (object)
  - **passiveOnly** (object)
  - **severity** (object)
  - **tags** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **targetProduct** (string)
  - **threatType** (string)
  - **tlpLevel** (string)
  - **url** (object)
  - **userAgent** (object)
  - **vendorInformation** (object)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Location | string |
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| OData-Version | string |
| Date | string |