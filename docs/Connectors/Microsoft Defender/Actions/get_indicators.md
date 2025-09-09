# Get Indicators

**Description**: Retrieves threat indicators from Microsoft Defender to pinpoint and analyze malicious activities.

## Endpoint

- **URL:** `/api/indicators`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **$filter** (string)
  - **$select** (string)
  - **$orderby** (string)
  - **$top** (number)
  - **$skip** (number)
  - **$count** (boolean)
  - **$expand** (string)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 04 May 2023 18:25:48 GMT",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "OData-Version": "4.0",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Indicators",
      "value": [
        {
          "id": "7",
          "indicatorValue": "bec1b52d350d721c7e22a6d4bb0a92909893a3ae",
          "indicatorType": "FileSha1",
          "action": "BlockAndRemediate",
          "createdBy": "pov@swimlaneintegrations.onmicrosoft.com",
          "severity": "Informational",
          "category": 1,
          "application": "demo-test",
          "educateUrl": null,
          "bypassDurationHours": null,
          "title": "test",
          "description": "test",
          "recommendedActions": "nothing",
          "creationTimeDateTimeUtc": "2023-04-25T17:37:28.8510566Z",
          "expirationTime": "2024-12-12T00:00:00Z",
          "lastUpdateTime": "2023-04-25T18:05:39.4204981Z",
          "lastUpdatedBy": "pov@swimlaneintegrations.onmicrosoft.com",
          "rbacGroupNames": [],
          "rbacGroupIds": [],
          "notificationId": null,
          "notificationBody": null,
          "version": null,
          "mitreTechniques": [],
          "historicalDetection": false,
          "lookBackPeriod": null,
          "generateAlert": false,
          "additionalInfo": null,
          "createdByDisplayName": "pov@swimlaneintegrations.onmicrosoft.com",
          "externalId": null,
          "createdBySource": "Portal",
          "certificateInfo": null
        },
        {
          "id": "8",
          "indicatorValue": "bec1b52d350d721c7e22a6d4bb0a92909893a3ae",
          "indicatorType": "FileSha1",
          "action": "Audit",
          "createdBy": "pov@swimlaneintegrations.onmicrosoft.com",
          "severity": "Informational",
          "category": 1,
          "application": "demo-test",
          "educateUrl": null,
          "bypassDurationHours": null,
          "title": "test",
          "description": "test",
          "recommendedActions": "nothing",
          "creationTimeDateTimeUtc": "2023-04-25T17:49:58.8706797Z",
          "expirationTime": "2024-12-12T00:00:00Z",
          "lastUpdateTime": "2023-04-25T18:29:47.7434049Z",
          "lastUpdatedBy": "pov@swimlaneintegrations.onmicrosoft.com",
          "rbacGroupNames": [],
          "rbacGroupIds": [],
          "notificationId": null,
          "notificationBody": null,
          "version": null,
          "mitreTechniques": [],
          "historicalDetection": false,
          "lookBackPeriod": null,
          "generateAlert": true,
          "additionalInfo": null,
          "createdByDisplayName": "pov@swimlaneintegrations.onmicrosoft.com",
          "externalId": null,
          "createdBySource": "Portal",
          "certificateInfo": null
        },
        {
          "id": "9",
          "indicatorValue": "bec1b52d350d721c7e22a6d4bb0a92909893a3ae",
          "indicatorType": "FileSha1",
          "action": "Allowed",
          "createdBy": "pov@swimlaneintegrations.onmicrosoft.com",
          "severity": "Informational",
          "category": 1,
          "application": "demo-test",
          "educateUrl": null,
          "bypassDurationHours": null,
          "title": "test",
          "description": "test",
          "recommendedActions": "nothing",
          "creationTimeDateTimeUtc": "2023-04-25T18:01:14.6910676Z",
          "expirationTime": "2024-12-12T00:00:00Z",
          "lastUpdateTime": "2023-04-25T18:01:14.6910676Z",
          "lastUpdatedBy": null,
          "rbacGroupNames": [],
          "rbacGroupIds": [],
          "notificationId": null,
          "notificationBody": null,
          "version": null,
          "mitreTechniques": [],
          "historicalDetection": false,
          "lookBackPeriod": null,
          "generateAlert": false,
          "additionalInfo": null,
          "createdByDisplayName": "pov@swimlaneintegrations.onmicrosoft.com",
          "externalId": null,
          "createdBySource": "Portal",
          "certificateInfo": null
        },
        {
          "id": "10",
          "indicatorValue": "bec1b52d350d721c7e22a6d4bb0a92909893a3ae",
          "indicatorType": "FileSha1",
          "action": "Warn",
          "createdBy": "pov@swimlaneintegrations.onmicrosoft.com",
          "severity": "Informational",
          "category": 1,
          "application": "demo-test",
          "educateUrl": null,
          "bypassDurationHours": null,
          "title": "test",
          "description": "test",
          "recommendedActions": "nothing",
          "creationTimeDateTimeUtc": "2023-04-25T18:02:06.322598Z",
          "expirationTime": "2024-12-12T00:00:00Z",
          "lastUpdateTime": "2023-04-25T18:02:06.322598Z",
          "lastUpdatedBy": null,
          "rbacGroupNames": [],
          "rbacGroupIds": [],
          "notificationId": null,
          "notificationBody": null,
          "version": null,
          "mitreTechniques": [],
          "historicalDetection": false,
          "lookBackPeriod": null,
          "generateAlert": false,
          "additionalInfo": null,
          "createdByDisplayName": "pov@swimlaneintegrations.onmicrosoft.com",
          "externalId": null,
          "createdBySource": "Portal",
          "certificateInfo": null
        },
        {
          "id": "11",
          "indicatorValue": "bec1b52d350d721c7e22a6d4bb0a92909893a3ae",
          "indicatorType": "FileSha1",
          "action": "Block",
          "createdBy": "pov@swimlaneintegrations.onmicrosoft.com",
          "severity": "Informational",
          "category": 1,
          "application": "demo-test",
          "educateUrl": null,
          "bypassDurationHours": null,
          "title": "test",
          "description": "test",
          "recommendedActions": "nothing",
          "creationTimeDateTimeUtc": "2023-04-25T18:02:53.8659665Z",
          "expirationTime": "2024-12-12T00:00:00Z",
          "lastUpdateTime": "2023-04-25T18:02:53.8659665Z",
          "lastUpdatedBy": null,
          "rbacGroupNames": [],
          "rbacGroupIds": [],
          "notificationId": null,
          "notificationBody": null,
          "version": null,
          "mitreTechniques": [],
          "historicalDetection": false,
          "lookBackPeriod": null,
          "generateAlert": false,
          "additionalInfo": null,
          "createdByDisplayName": "pov@swimlaneintegrations.onmicrosoft.com",
          "externalId": null,
          "createdBySource": "Portal",
          "certificateInfo": null
        },
        {
          "id": "12",
          "indicatorValue": "3395856ce81f2b7382dee72602f798b642f14140",
          "indicatorType": "FileSha1",
          "action": "BlockAndRemediate",
          "createdBy": "29c9ea20-6466-4ddd-8f23-bcd0b9e74bbd",
          "severity": "Informational",
          "category": 1,
          "application": null,
          "educateUrl": null,
          "bypassDurationHours": null,
          "title": "test2",
          "description": "test2",
          "recommendedActions": null,
          "creationTimeDateTimeUtc": "2023-04-25T19:14:16.864235Z",
          "expirationTime": null,
          "lastUpdateTime": "2023-04-29T03:38:37.9997514Z",
          "lastUpdatedBy": "29c9ea20-6466-4ddd-8f23-bcd0b9e74bbd",
          "rbacGroupNames": [],
          "rbacGroupIds": [],
          "notificationId": null,
          "notificationBody": null,
          "version": null,
          "mitreTechniques": [],
          "historicalDetection": false,
          "lookBackPeriod": null,
          "generateAlert": true,
          "additionalInfo": null,
          "createdByDisplayName": "WindowsDefenderATPSiemConnector",
          "externalId": null,
          "createdBySource": "PublicApi",
          "certificateInfo": null
        },
        {
          "id": "14",
          "indicatorValue": "https://www.google.com",
          "indicatorType": "Url",
          "action": "BlockAndRemediate",
          "createdBy": "29c9ea20-6466-4ddd-8f23-bcd0b9e74bbd",
          "severity": "Informational",
          "category": 1,
          "application": null,
          "educateUrl": null,
          "bypassDurationHours": null,
          "title": "Block Google",
          "description": "See above",
          "recommendedActions": null,
          "creationTimeDateTimeUtc": "2023-04-29T03:22:12.3386173Z",
          "expirationTime": null,
          "lastUpdateTime": "2023-04-29T06:19:02.652157Z",
          "lastUpdatedBy": "29c9ea20-6466-4ddd-8f23-bcd0b9e74bbd",
          "rbacGroupNames": [],
          "rbacGroupIds": [],
          "notificationId": null,
          "notificationBody": null,
          "version": null,
          "mitreTechniques": [],
          "historicalDetection": false,
          "lookBackPeriod": null,
          "generateAlert": true,
          "additionalInfo": null,
          "createdByDisplayName": "WindowsDefenderATPSiemConnector",
          "externalId": null,
          "createdBySource": "PublicApi",
          "certificateInfo": null
        },
        {
          "id": "15",
          "indicatorValue": "https://www.facebook.com",
          "indicatorType": "Url",
          "action": "BlockAndRemediate",
          "createdBy": "29c9ea20-6466-4ddd-8f23-bcd0b9e74bbd",
          "severity": "Informational",
          "category": 1,
          "application": null,
          "educateUrl": null,
          "bypassDurationHours": null,
          "title": "Block Facebook",
          "description": "Block Facebook",
          "recommendedActions": null,
          "creationTimeDateTimeUtc": "2023-04-29T03:27:48.914513Z",
          "expirationTime": null,
          "lastUpdateTime": "2023-04-29T06:18:37.4589084Z",
          "lastUpdatedBy": "29c9ea20-6466-4ddd-8f23-bcd0b9e74bbd",
          "rbacGroupNames": [],
          "rbacGroupIds": [],
          "notificationId": null,
          "notificationBody": null,
          "version": null,
          "mitreTechniques": [],
          "historicalDetection": false,
          "lookBackPeriod": null,
          "generateAlert": true,
          "additionalInfo": null,
          "createdByDisplayName": "WindowsDefenderATPSiemConnector",
          "externalId": null,
          "createdBySource": "PublicApi",
          "certificateInfo": null
        },
        {
          "id": "16",
          "indicatorValue": "https://www.google.com",
          "indicatorType": "Url",
          "action": "Allowed",
          "createdBy": "29c9ea20-6466-4ddd-8f23-bcd0b9e74bbd",
          "severity": "Informational",
          "category": 1,
          "application": null,
          "educateUrl": null,
          "bypassDurationHours": null,
          "title": "Block Google",
          "description": "See above",
          "recommendedActions": null,
          "creationTimeDateTimeUtc": "2023-05-01T20:36:56.7510696Z",
          "expirationTime": null,
          "lastUpdateTime": "2023-05-02T13:52:21.7065962Z",
          "lastUpdatedBy": "29c9ea20-6466-4ddd-8f23-bcd0b9e74bbd",
          "rbacGroupNames": [],
          "rbacGroupIds": [],
          "notificationId": null,
          "notificationBody": null,
          "version": null,
          "mitreTechniques": [],
          "historicalDetection": false,
          "lookBackPeriod": null,
          "generateAlert": true,
          "additionalInfo": null,
          "createdByDisplayName": "WindowsDefenderATPSiemConnector",
          "externalId": null,
          "createdBySource": "PublicApi",
          "certificateInfo": null
        },
        {
          "id": "17",
          "indicatorValue": "yahoo.com",
          "indicatorType": "DomainName",
          "action": "Block",
          "createdBy": "29c9ea20-6466-4ddd-8f23-bcd0b9e74bbd",
          "severity": "Informational",
          "category": 1,
          "application": null,
          "educateUrl": null,
          "bypassDurationHours": null,
          "title": "Block the yahoo.com Domain",
          "description": "Block the yahoo.com Domain, this will apply to all defender protected endpoints",
          "recommendedActions": null,
          "creationTimeDateTimeUtc": "2023-05-04T16:08:56.7716458Z",
          "expirationTime": null,
          "lastUpdateTime": "2023-05-04T16:21:24.6281036Z",
          "lastUpdatedBy": "29c9ea20-6466-4ddd-8f23-bcd0b9e74bbd",
          "rbacGroupNames": [],
          "rbacGroupIds": [],
          "notificationId": null,
          "notificationBody": null,
          "version": null,
          "mitreTechniques": [],
          "historicalDetection": false,
          "lookBackPeriod": null,
          "generateAlert": true,
          "additionalInfo": null,
          "createdByDisplayName": "WindowsDefenderATPSiemConnector",
          "externalId": null,
          "createdBySource": "PublicApi",
          "certificateInfo": null
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
    - **indicatorValue** (string)
    - **indicatorType** (string)
    - **action** (string)
    - **createdBy** (string)
    - **severity** (string)
    - **category** (number)
    - **application** (object)
    - **educateUrl** (object)
    - **bypassDurationHours** (object)
    - **title** (string)
    - **description** (string)
    - **recommendedActions** (object)
    - **creationTimeDateTimeUtc** (string)
    - **expirationTime** (object)
    - **lastUpdateTime** (string)
    - **lastUpdatedBy** (string)
    - **rbacGroupNames** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **rbacGroupIds** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **notificationId** (object)
    - **notificationBody** (object)
    - **version** (object)
    - **mitreTechniques** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **historicalDetection** (boolean)
    - **lookBackPeriod** (object)
    - **generateAlert** (boolean)
    - **additionalInfo** (object)
    - **createdByDisplayName** (string)
    - **externalId** (object)
    - **createdBySource** (string)
    - **certificateInfo** (object)
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