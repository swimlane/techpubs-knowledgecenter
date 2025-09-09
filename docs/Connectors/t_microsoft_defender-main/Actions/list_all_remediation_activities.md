# List All Remediation Activities

**Description**: Retrieve comprehensive details on all remediation activities, including statuses and identifiers, within Microsoft Defender.

## Endpoint

- **URL:** `/api/remediationtasks`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **$skip** (number): Indexes into a result set. Also used by some APIs to implement paging and can be used together with $top to manually page results.
  - **$top** (number): Sets the page size of results. Top with max value of 10,000.
  - **$filter** (string): Filter on createdon and status properties.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Mon, 10 Feb 2025 05:20:10 GMT",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "mise-correlation-id": "245dc196-fb84-44dd-adc4-d91b3abec8da",
      "OData-Version": "4.0",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#RemediationTasks",
      "value": [
        {
          "id": "03942ef5-aewb-4w6e-b555-d6a97013844w",
          "title": "Update Microsoft Silverlight",
          "createdOn": "2021-02-10T13:20:36.4718166Z",
          "requesterId": "65548a1d-ef00-4a7a-8d19-1b967b5c36f4",
          "requesterEmail": "user1@contoso.com",
          "status": "Active",
          "statusLastModifiedOn": "2021-02-10T13:20:36.4719698Z",
          "description": "Update Silverlight to a later version  to mitigate 55 known vulnerabilities affecting your devices. Doing so can help lessen the security risk to your organization due to versions which have reached their end-of-support.",
          "relatedComponent": "Microsoft Silverlight",
          "targetDevices": 18511,
          "rbacGroupNames": [
            "UnassignedGroup",
            "hhh"
          ],
          "fixedDevices": 2866,
          "requesterNotes": "test",
          "dueOn": "2021-02-11T00:00:00Z",
          "category": "Software",
          "productivityImpactRemediationType": "AllExposedAssets",
          "priority": "Medium",
          "completionMethod": "Automatic",
          "completerId": "",
          "completerEmail": "",
          "scid": "",
          "type": "Update",
          "productId": "microsoft-_-silverlight",
          "vendorId": "microsoft",
          "nameId": "silverlight",
          "recommendedVersion": "",
          "recommendedVendor": "",
          "recommendedProgram": ""
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
    - **title** (string)
    - **createdOn** (string)
    - **requesterId** (string)
    - **requesterEmail** (string)
    - **status** (string)
    - **statusLastModifiedOn** (string)
    - **description** (string)
    - **relatedComponent** (string)
    - **targetDevices** (number)
    - **rbacGroupNames** (array)
    - **fixedDevices** (number)
    - **requesterNotes** (string)
    - **dueOn** (string)
    - **category** (string)
    - **productivityImpactRemediationType** (string)
    - **priority** (string)
    - **completionMethod** (string)
    - **completerId** (string)
    - **completerEmail** (string)
    - **scid** (string)
    - **type** (string)
    - **productId** (string)
    - **vendorId** (string)
    - **nameId** (string)
    - **recommendedVersion** (string)
    - **recommendedVendor** (string)
    - **recommendedProgram** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Content-Encoding | string |
| Vary | string |
| mise-correlation-id | string |
| OData-Version | string |
| Strict-Transport-Security | string |