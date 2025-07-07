# Audit Logs Get SignIn

**Description**: Retrieve details for a specific sign-in event in Microsoft Entra using the provided tenant's unique ID.

## Endpoint

- **URL:** `/v1.0/auditLogs/signIns/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
- **parameters** (object): OData query parameters to help customize the response.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#auditLogs/signIns",
      "value": [
        {
          "id": "66ea54eb-6301-4ee5-be62-ff5a759b0100",
          "createdDateTime": "2023-12-01T16:03:24Z",
          "userDisplayName": "Test Contoso",
          "userPrincipalName": "testaccount1@contoso.com",
          "userId": "26be570a-ae82-4189-b4e2-a37c6808512d",
          "appId": "de8bc8b5-d9f9-48b1-a8ad-b748da725064",
          "appDisplayName": "Graph explorer",
          "ipAddress": "131.107.159.37",
          "clientAppUsed": "Browser",
          "correlationId": "d79f5bee-5860-4832-928f-3133e22ae912",
          "conditionalAccessStatus": "notApplied",
          "isInteractive": true,
          "riskDetail": "none",
          "riskLevelAggregated": "none",
          "riskLevelDuringSignIn": "none",
          "riskState": "none",
          "riskEventTypes": [],
          "resourceDisplayName": "Microsoft Graph",
          "resourceId": "00000003-0000-0000-c000-000000000000",
          "status": {
            "errorCode": 0,
            "failureReason": null,
            "additionalDetails": null
          },
          "deviceDetail": {
            "deviceId": "",
            "displayName": null,
            "operatingSystem": "Windows 10",
            "browser": "Edge 80.0.361",
            "isCompliant": null,
            "isManaged": null,
            "trustType": null
          },
          "location": {
            "city": "Redmond",
            "state": "Washington",
            "countryOrRegion": "US",
            "geoCoordinates": {
              "altitude": null,
              "latitude": 47.68050003051758,
              "longitude": -122.12094116210938
            }
          },
          "appliedConditionalAccessPolicies": [
            {
              "id": "de7e60eb-ed89-4d73-8205-2227def6b7c9",
              "displayName": "SharePoint limited access for guest workers",
              "enforcedGrantControls": [],
              "enforcedSessionControls": [],
              "result": "notEnabled"
            },
            {
              "id": "6701123a-b4c6-48af-8565-565c8bf7cabc",
              "displayName": "Medium signin risk block",
              "enforcedGrantControls": [],
              "enforcedSessionControls": [],
              "result": "notEnabled"
            }
          ]
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **value** (array)
    - **id** (string)
    - **createdDateTime** (string)
    - **userDisplayName** (string)
    - **userPrincipalName** (string)
    - **userId** (string)
    - **appId** (string)
    - **appDisplayName** (string)
    - **ipAddress** (string)
    - **clientAppUsed** (string)
    - **correlationId** (string)
    - **conditionalAccessStatus** (string)
    - **isInteractive** (boolean)
    - **riskDetail** (string)
    - **riskLevelAggregated** (string)
    - **riskLevelDuringSignIn** (string)
    - **riskState** (string)
    - **riskEventTypes** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **resourceDisplayName** (string)
    - **resourceId** (string)
    - **status** (object)
      - **errorCode** (number)
      - **failureReason** (object)
      - **additionalDetails** (object)
    - **deviceDetail** (object)
      - **deviceId** (string)
      - **displayName** (object)
      - **operatingSystem** (string)
      - **browser** (string)
      - **isCompliant** (object)
      - **isManaged** (object)
      - **trustType** (object)
    - **location** (object)
      - **city** (string)
      - **state** (string)
      - **countryOrRegion** (string)
      - **geoCoordinates** (object)
        - **altitude** (object)
        - **latitude** (number)
        - **longitude** (number)
    - **appliedConditionalAccessPolicies** (array)
      - **id** (string)
      - **displayName** (string)
      - **enforcedGrantControls** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **enforcedSessionControls** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **result** (string)