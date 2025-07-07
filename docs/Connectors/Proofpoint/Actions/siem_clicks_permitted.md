# Siem Clicks Permitted

**Description**: Fetch events for clicks to malicious URLs that were permitted within a specified time period in ProofPoint.

## Endpoint

- **URL:** `/v2/siem/clicks/permitted`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required: One of the following three query parameters describing the desired time range for the data must be supplied with each request interval, sinceSeconds, sinceTime.
  - **interval** (string): TODO: Add description
  - **sinceSeconds** (number): TODO: Add description
  - **sinceTime** (string): TODO: Add description
  - **format** (string): TODO: Add description
  - **threatType** (string): TODO: Add description
  - **threatStatus** (string): TODO: Add description
## Output

### Example

```json
[
  {
    "status_code": 204,
    "response_headers": {
      "Date": "Mon, 16 Oct 2023 09:27:36 GMT",
      "Connection": "keep-alive",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "No Content",
    "response_text": ""
  }
]
```
### Output Parameters

- **status_code** (number): TODO: Add description
- **reason** (string): TODO: Add description
- **response_text** (string): TODO: Add description
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string | TODO: Add description |
| Connection | string | TODO: Add description |
| Strict-Transport-Security | string | TODO: Add description |