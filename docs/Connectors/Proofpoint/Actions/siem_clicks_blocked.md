# Siem Clicks Blocked

**Description**: Fetch events for clicks to malicious URLs that were blocked by ProofPoint within a specified time period.

## Endpoint

- **URL:** `/v2/siem/clicks/blocked`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required: One of the following three query parameters describing the desired time range for the data must be supplied with each request interval, sinceSeconds, sinceTime.
  - **interval** (string)
  - **sinceSeconds** (number)
  - **sinceTime** (string)
  - **format** (string)
  - **threatType** (string)
  - **threatStatus** (string)
## Output

### Example

```json
[
  {
    "status_code": 204,
    "response_headers": {
      "Date": "Mon, 16 Oct 2023 09:02:15 GMT",
      "Connection": "keep-alive",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "No Content",
    "response_text": ""
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (string)
## Response Headers

- **Date** (string)
- **Connection** (string)
- **Strict-Transport-Security** (string)