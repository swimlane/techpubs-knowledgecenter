# Update Alert

**Description**: Updates an existing alert in the Microsoft Graph Security API using a specified alert_id and provided information.

## Endpoint

- **URL:** `/v1.0/security/alerts_v2/{{alert_id}}`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **alert_id** (string) – Required: ID of the Alert
- **json_body** (object) – Required: JSON Body
  - **assignedTo** (string): Owner of the incident, or null if no owner is assigned.
  - **determination** (string): Specifies the determination of the alert.
  - **classification** (string): Specifies the classification of the alert.
  - **customDetails** (string): User defined custom fields with string values.
  - **status** (string): Alert lifecycle status (stage).
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false;charset=utf-8",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "3763884a-1de2-4f55-a7cd-53a5fda6a36d",
      "client-request-id": "3763884a-1de2-4f55-a7cd-53a5fda6a36d",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Central India\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"002\",\"RoleInstance\":\"PN2PEPF000005BA\"}}",
      "OData-Version": "4.0",
      "Date": "Fri, 23 May 2025 10:42:13 GMT"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#security/alerts_v2/$entity",
      "id": "maf25f0fa0-126a-4297-aff6-ae579cb984a3",
      "providerAlertId": "f25f0fa0-126a-4297-aff6-ae579cb984a3",
      "incidentId": "563",
      "status": "new",
      "severity": "medium",
      "classification": "truePositive",
      "determination": null,
      "serviceSource": "microsoftAppGovernance",
      "detectionSource": "appGovernanceDetection",
      "productName": "App Governance",
      "detectorId": "b62ae531-7aa6-4bc8-91b9-49a9be960145",
      "tenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
      "title": "Dormant OAuth App with no recent MS Graph activity",
      "description": "The OAuth application (WindowsDefenderATPSiemConnector) was created in your tenant with high MS Graph privileges and was dormant for extended period of time in the given tenant. The activity is indicative of a dormant app with high scopes which maybe not in active use but has high MS Graph scopes that be misused if compromised. An attacker might be using this app with potential active credentials to start accessing or creating Azure resources for persistence or/and further move laterally in the tenant.\r\n<a href=\"https://security.microsoft.com//app?oauthAppId=29c9ea20-6466-4ddd-8f23-bcd0b9e74bbd\">WindowsDefenderATPSiemConnector</a>",
      "recommendedActions": "1. Contact the users or admins who have created or have granted permissions to the app. Verify if the any changes were intentional and if any excessive privileges are normal.\r\n2. Search the CloudAppEvents table in advanced hunting to understand app activity and identify data accessed by the app. Check affected Azure resources and monitor for any unexpected Azure resource creation , updating or deleteion\r\n3. Verify whether the app is critical to your organization before considering any containment actions. Deactivate the app using app governance or Entra ID to prevent it from accessing resources.\r\n4. Verify whether the deployed resources are critical to the organization as the dormant app may be reused or its functionality extended as the underlying API activity is showing dormancy\r\n5. Check affected accounts for suspicious activity. Suspend and reset passwords for all affected accounts and implement credential and account recycling for non-active apps",
      "category": "SuspiciousActivity",
      "assignedTo": "XSOAR",
      "alertWebUrl": "https://security.microsoft.com/alerts/maf25f0fa0-126a-4297-aff6-ae579cb984a3?tid=f5d73c4c-bb3d-421b-8bee-424916a4acca",
      "incidentWebUrl": "https://security.microsoft.com/incident2/563/overview?tid=f5d73c4c-bb3d-421b-8bee-424916a4acca",
      "actorDisplayName": null,
      "threatDisplayName": null,
      "threatFamilyName": null,
      "mitreTechniques": [
        "T1078",
        "T1078.004"
      ],
      "createdDateTime": "2024-11-25T18:22:38.2566667Z",
      "lastUpdateDateTime": "2025-05-23T10:41:12.25Z",
      "resolvedDateTime": null,
      "firstActivityDateTime": "2024-10-25T02:53:43.273Z",
      "lastActivityDateTime": "2024-10-25T02:56:20.776Z",
      "systemTags": [],
      "alertPolicyId": null,
      "comments": [],
      "customDetails": {},
      "evidence": [
        {
          "@odata.type": "#microsoft.graph.security.oauthApplicationEvidence",
          "createdDateTime": "2024-11-25T18:22:38.35Z",
          "verdict": "unknown",
          "remediationStatus": "none",
          "remediationStatusDetails": null,
          "roles": [],
          "detailedRoles": [],
          "tags": [],
          "appId": "29c9ea20-6466-4ddd-8f23-bcd0b9e74bbd",
          "displayName": "WindowsDefenderATPSiemConnector",
          "objectId": null,
          "publisher": null
        }
      ],
      "additionalData": {}
    }
  }
]
```
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
  - **determination** (object)
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
  - **alertPolicyId** (object)
  - **comments** (array)
  - **customDetails** (object)
  - **evidence** (array)
    - **@odata.type** (string)
    - **createdDateTime** (string)
    - **verdict** (string)
    - **remediationStatus** (string)
    - **remediationStatusDetails** (object)
    - **roles** (array)
    - **detailedRoles** (array)
    - **tags** (array)
    - **appId** (string)
    - **displayName** (string)
    - **objectId** (object)
    - **publisher** (object)
  - **additionalData** (object)
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