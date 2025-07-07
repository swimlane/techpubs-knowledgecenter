# Get Alert

**Description**: Retrieve a specific security alert from the Microsoft Graph Security API using the mandatory alert_id.

## Endpoint

- **URL:** `/v1.0/security/alerts_v2/{{alert_id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **alert_id** (string) – Required: ID of the Alert.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **id** (string)
  - **providerAlertId** (string)
  - **incidentId** (string)
  - **status** (string)
  - **severity** (string)
  - **classification** (string)
  - **determination** (string)
  - **serviceSource** (string)
  - **detectionSource** (string)
  - **productName** (string)
  - **detectorId** (string)
  - **tenantId** (string)
  - **title** (string)
  - **description** (string)
  - **recommendedActions** (string)
  - **category** (string)
  - **assignedTo** (string)
  - **alertWebUrl** (string)
  - **incidentWebUrl** (string)
  - **actorDisplayName** (object)
  - **threatDisplayName** (object)
  - **threatFamilyName** (object)
  - **mitreTechniques** (array)
  - **createdDateTime** (string)
  - **lastUpdateDateTime** (string)
  - **resolvedDateTime** (object)
  - **firstActivityDateTime** (string)
  - **lastActivityDateTime** (string)
  - **systemTags** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **alertPolicyId** (object)
  - **additionalData** (object)
  - **comments** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **evidence** (array)
    - **@odata.type** (string)
    - **createdDateTime** (string)
    - **verdict** (string)
    - **remediationStatus** (string)
    - **remediationStatusDetails** (object)
    - **roles** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **detailedRoles** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **tags** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **primaryAddress** (string)
    - **displayName** (string)
    - **userAccount** (object)
      - **accountName** (string)
      - **domainName** (string)
      - **userSid** (string)
      - **azureAdUserId** (string)
      - **userPrincipalName** (string)
      - **displayName** (string)
    - **networkMessageId** (string)
    - **internetMessageId** (string)
    - **subject** (string)
    - **language** (string)
    - **senderIp** (string)
    - **recipientEmailAddress** (string)
    - **antiSpamDirection** (object)
    - **deliveryAction** (string)
    - **deliveryLocation** (string)
    - **urn** (string)
    - **threats** (array)
    - **threatDetectionMethods** (array)
    - **urls** (array)
    - **urlCount** (number)
    - **attachmentsCount** (number)
    - **receivedDateTime** (string)
    - **p1Sender** (object)
      - **emailAddress** (string)
      - **displayName** (object)
      - **domainName** (string)
    - **p2Sender** (object)
      - **emailAddress** (string)
      - **displayName** (string)
      - **domainName** (string)
    - **stream** (object)
    - **detectionStatus** (object)
    - **mdeDeviceId** (object)
    - **fileDetails** (object)
      - **sha1** (object)
      - **sha256** (string)
      - **fileName** (string)
      - **filePath** (object)
      - **fileSize** (object)
      - **filePublisher** (object)
      - **signer** (object)
      - **issuer** (object)
    - **url** (string)
    - **clusterBy** (string)
    - **clusterByValue** (string)
    - **query** (string)
    - **emailCount** (number)
    - **networkMessageIds** (array)
## Response Headers

| Header | Type |
|--------|------|
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