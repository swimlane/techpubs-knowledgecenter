# List Vulnerabilities by Machine and Software

**Description**: Retrieve a categorized list of vulnerabilities by machine and software from Microsoft Defender.

## Endpoint

- **URL:** `/api/vulnerabilities/machinesVulnerabilities`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **$filter** (string): Filter the vulnerabilities using id, cveId, machineId, fixingKbId, productName, productVersion, severity, and productVendor properties.
  - **$stop** (number)
  - **$skip** (number): The number of items in the queried collection that are to be skipped and not included in the response.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Tue, 30 Jul 2024 05:42:20 GMT",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "OData-Version": "4.0",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Collection(microsoft.windowsDefenderATP.api.PublicAssetVulnerabilityDto)",
      "@odata.count": 0,
      "value": [
        {
          "id": "5afa3afc92a7c63d4b70129e0a6f33f63a427e21-_-CVE-2020-6494-_-microsoft-_-edge_chromium-based-_-81.0.416.77-_-",
          "cveId": "CVE-2020-6494",
          "machineId": "5afa3afc92a7c63d4b70129e0a6f33f63a427e21",
          "fixingKbId": null,
          "productName": "edge_chromium-based",
          "productVendor": "microsoft",
          "productVersion": "81.0.416.77",
          "severity": "Low"
        },
        {
          "id": "7a704e17d1c2977c0e7b665fb18ae6e1fe7f3283-_-CVE-2016-3348-_-microsoft-_-windows_server_2012_r2-_-6.3.9600.19728-_-3185911",
          "cveId": "CVE-2016-3348",
          "machineId": "7a704e17d1c2977c0e7b665fb18ae6e1fe7f3283",
          "fixingKbId": "3185911",
          "productName": "windows_server_2012_r2",
          "productVendor": "microsoft",
          "productVersion": "6.3.9600.19728",
          "severity": "Low"
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
  - **@odata.count** (number)
  - **value** (array)
    - **id** (string)
    - **cveId** (string)
    - **machineId** (string)
    - **fixingKbId** (string)
    - **productName** (string)
    - **productVendor** (string)
    - **productVersion** (string)
    - **severity** (string)
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