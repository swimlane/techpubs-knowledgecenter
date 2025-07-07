# Forensics Campaign

**Description**: Retrieve aggregate forensics data for a specified campaign in ProofPoint using the campaignId parameter.

## Endpoint

- **URL:** `/v2/forensics`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required: Auto-generated description for `parameters`. Please update manually if needed.
  - **campaignId** (string) – Required: Auto-generated description for `campaignId`. Please update manually if needed.
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

- **status_code** (number): Auto-generated description for `status_code`. Please update manually if needed.
- **reason** (string): Auto-generated description for `reason`. Please update manually if needed.
- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.
  - **generated** (string): Auto-generated description for `generated`. Please update manually if needed.
  - **reports** (array): Auto-generated description for `reports`. Please update manually if needed.
    - **scope** (string): Auto-generated description for `scope`. Please update manually if needed.
    - **id** (string): Auto-generated description for `id`. Please update manually if needed.
    - **name** (string): Auto-generated description for `name`. Please update manually if needed.
    - **forensics** (array): Auto-generated description for `forensics`. Please update manually if needed.
      - **file_name** (string) – Required: Auto-generated description for `file_name`. Please update manually if needed.
      - **file** (string) – Required: Auto-generated description for `file`. Please update manually if needed.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string | Auto-generated description for `Date`. Please update manually if needed. |
| Content-Type | string | Auto-generated description for `Content-Type`. Please update manually if needed. |
| Content-Length | string | Auto-generated description for `Content-Length`. Please update manually if needed. |
| Connection | string | Auto-generated description for `Connection`. Please update manually if needed. |
| X-Content-Type-Options | string | Auto-generated description for `X-Content-Type-Options`. Please update manually if needed. |
| Vary | string | Auto-generated description for `Vary`. Please update manually if needed. |
| Content-Encoding | string | Auto-generated description for `Content-Encoding`. Please update manually if needed. |
| Strict-Transport-Security | string | Auto-generated description for `Strict-Transport-Security`. Please update manually if needed. |