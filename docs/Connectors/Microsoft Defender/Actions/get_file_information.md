# Get File Information

**Description**: Retrieve detailed information for a specific file in Microsoft Defender using the unique file identifier.

## Endpoint

- **URL:** `/api/files/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 04 May 2023 17:37:52 GMT",
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
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Files/$entity",
      "sha1": "6532ec91d513acc05f43ee0aa3002599729fd3e1",
      "sha256": "d4447dffdbb2889b4b4e746b0bc882df1b854101614b0aa83953ef3cb66904cf",
      "md5": "7f05a371d2beffb3784fd2199f81d730",
      "globalPrevalence": 10,
      "globalFirstObserved": "2018-05-07T14:05:18.4401316Z",
      "globalLastObserved": "2022-11-15T03:37:49.4593231Z",
      "size": 391680,
      "fileType": null,
      "isPeFile": true,
      "filePublisher": null,
      "fileProductName": null,
      "signer": null,
      "issuer": null,
      "signerHash": null,
      "isValidCertificate": null,
      "determinationType": "Unknown",
      "determinationValue": null
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **sha1** (string)
  - **sha256** (string)
  - **md5** (string)
  - **globalPrevalence** (number)
  - **globalFirstObserved** (string)
  - **globalLastObserved** (string)
  - **size** (number)
  - **fileType** (object)
  - **isPeFile** (boolean)
  - **filePublisher** (object)
  - **fileProductName** (object)
  - **signer** (object)
  - **issuer** (object)
  - **signerHash** (object)
  - **isValidCertificate** (object)
  - **determinationType** (string)
  - **determinationValue** (object)
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