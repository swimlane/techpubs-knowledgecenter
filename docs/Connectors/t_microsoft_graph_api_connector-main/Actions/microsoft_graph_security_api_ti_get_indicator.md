# Get Threat Intelligence Indicator

**Description**: Retrieves a specific Threat Intelligence Indicator from Microsoft Graph Security API using the provided unique ID.

## Endpoint

- **URL:** `/beta/security/tiIndicators/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Threat Intelligence Indicator ID
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
  - **fileHashType** (string)
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
  - **networkDestinationIPv4** (object)
  - **networkDestinationIPv6** (object)
  - **networkDestinationPort** (object)
  - **networkIPv4** (string)
  - **networkIPv6** (object)
  - **networkPort** (object)
  - **networkProtocol** (object)
  - **networkSourceAsn** (object)
  - **networkSourceCidrBlock** (object)
  - **networkSourceIPv4** (object)
  - **networkSourceIPv6** (object)
  - **networkSourcePort** (object)
  - **passiveOnly** (object)
  - **severity** (number)
  - **tags** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **targetProduct** (string)
  - **threatType** (object)
  - **tlpLevel** (object)
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
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| OData-Version | string |
| Date | string |