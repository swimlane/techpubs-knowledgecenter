# Forensics Campaign

**Description**: Retrieve aggregate forensics data for a specified campaign in ProofPoint using the campaignId parameter.

## Endpoint

- **URL:** `/v2/forensics`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required: Structured object with nested properties.
  - **campaignId** (string) – Required: Unique identifier.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Wed, 18 Oct 2023 13:42:53 GMT",
      "Content-Type": "application/json",
      "Content-Length": "188",
      "Connection": "keep-alive",
      "X-Content-Type-Options": "nosniff",
      "Vary": "Accept-Encoding, User-Agent",
      "Content-Encoding": "gzip",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "generated": "2023-10-18T13:42:53.056Z",
      "reports": [
        {
          "scope": "CAMPAIGN",
          "id": "e144426d-7bcd-4695-98a7-c9f6551f3d48",
          "name": "Ursnif \"2000\" | US Targeting | URLs | 3 July 2019",
          "forensics": []
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number): Status value or code.
- **reason** (string): Text string.
- **json_body** (object): Structured object with nested properties.
  - **generated** (string): Text string.
  - **reports** (array): List of items.
    - **scope** (string): Text string.
    - **id** (string): Unique identifier.
    - **name** (string): Name or label.
    - **forensics** (array): List of items.
      - **file_name** (string) – Required: Name or label.
      - **file** (string) – Required: Text string.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string | Timestamp in ISO 8601 format. |
| Content-Type | string | Type of the resource or value. |
| Content-Length | string | Text string. |
| Connection | string | Text string. |
| X-Content-Type-Options | string | Type of the resource or value. |
| Vary | string | Text string. |
| Content-Encoding | string | Text string. |
| Strict-Transport-Security | string | Text string. |