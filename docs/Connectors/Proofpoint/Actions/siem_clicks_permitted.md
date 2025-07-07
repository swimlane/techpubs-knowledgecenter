# Siem Clicks Permitted

**Description**: Fetch events for clicks to malicious URLs that were permitted within a specified time period in ProofPoint.

## Endpoint

- **URL:** `/v2/siem/clicks/permitted`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required: One of the following three query parameters describing the desired time range for the data must be supplied with each request interval, sinceSeconds, sinceTime.
  - **interval** (string): Text string.
  - **sinceSeconds** (number): Numerical value.
  - **sinceTime** (string): Timestamp in ISO 8601 format.
  - **format** (string): Text string.
  - **threatType** (string): Type of the resource or value.
  - **threatStatus** (string): Status value or code.
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

- **status_code** (number): Status value or code.
- **reason** (string): Text string.
- **response_text** (string): Text string.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string | Timestamp in ISO 8601 format. |
| Connection | string | Text string. |
| Strict-Transport-Security | string | Text string. |