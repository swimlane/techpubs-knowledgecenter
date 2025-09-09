# Get User Related Alerts

**Description**: Retrieve alerts linked to a specific user in Microsoft Defender by using the unique 'user' identifier.

## Endpoint

- **URL:** `/api/users/{{id}}/alerts`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required: The ID is not the full UPN, but only the user name. (for example, to retrieve alerts for user1@contoso.com use /api/users/user1/alerts).
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **value** (array)
    - **id** (string)
    - **incidentId** (number)
    - **investigationId** (object)
    - **assignedTo** (object)
    - **severity** (string)
    - **status** (string)
    - **classification** (object)
    - **determination** (object)
    - **investigationState** (string)
    - **detectionSource** (string)
    - **detectorId** (string)
    - **category** (string)
    - **threatFamilyName** (object)
    - **title** (string)
    - **description** (string)
    - **alertCreationTime** (string)
    - **firstEventTime** (string)
    - **lastEventTime** (string)
    - **lastUpdateTime** (string)
    - **resolvedTime** (object)
    - **machineId** (string)
    - **computerDnsName** (string)
    - **rbacGroupName** (object)
    - **aadTenantId** (string)
    - **threatName** (object)
    - **mitreTechniques** (array)
    - **relatedUser** (object)
      - **userName** (string)
      - **domainName** (string)
    - **loggedOnUsers** (array)
      - **accountName** (string)
      - **domainName** (string)
    - **comments** (array)
    - **evidence** (array)
      - **entityType** (string)
      - **evidenceCreationTime** (string)
      - **sha1** (object)
      - **sha256** (object)
      - **fileName** (object)
      - **filePath** (object)
      - **processId** (object)
      - **processCommandLine** (object)
      - **processCreationTime** (object)
      - **parentProcessId** (object)
      - **parentProcessCreationTime** (object)
      - **parentProcessFileName** (object)
      - **parentProcessFilePath** (object)
      - **ipAddress** (object)
      - **url** (string)
      - **registryKey** (object)
      - **registryHive** (object)
      - **registryValueType** (object)
      - **registryValue** (object)
      - **registryValueName** (object)
      - **accountName** (object)
      - **domainName** (object)
      - **userSid** (object)
      - **aadUserId** (object)
      - **userPrincipalName** (object)
      - **detectionStatus** (object)
    - **domains** (array)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Content-Encoding | string |
| Vary | string |
| OData-Version | string |
| Strict-Transport-Security | string |