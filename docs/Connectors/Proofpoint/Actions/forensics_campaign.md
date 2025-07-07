# Forensics Campaign

**Description**: Retrieve aggregate forensics data for a specified campaign in ProofPoint using the campaignId parameter.

## Endpoint

- **URL:** `/v2/forensics`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required: TODO: Add description
  - **campaignId** (string) – Required: TODO: Add description
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

- **status_code** (number): TODO: Add description
- **reason** (string): TODO: Add description
- **json_body** (object): TODO: Add description
  - **generated** (string): TODO: Add description
  - **reports** (array): TODO: Add description
    - **scope** (string): TODO: Add description
    - **id** (string): TODO: Add description
    - **name** (string): TODO: Add description
    - **forensics** (array): TODO: Add description
      - **file_name** (string) – Required: TODO: Add description
      - **file** (string) – Required: TODO: Add description
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string | TODO: Add description |
| Content-Type | string | TODO: Add description |
| Content-Length | string | TODO: Add description |
| Connection | string | TODO: Add description |
| X-Content-Type-Options | string | TODO: Add description |
| Vary | string | TODO: Add description |
| Content-Encoding | string | TODO: Add description |
| Strict-Transport-Security | string | TODO: Add description |