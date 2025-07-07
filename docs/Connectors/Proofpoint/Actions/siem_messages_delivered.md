# Siem Messages Delivered

**Description**: Fetch events for messages delivered within a specified time frame that contained a known threat, requiring specific parameters.

## Endpoint

- **URL:** `/v2/siem/messages/delivered`
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
    "status_code": 200,
    "response_headers": {
      "Date": "Mon, 16 Oct 2023 09:34:21 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Vary": "Accept-Encoding, User-Agent",
      "Content-Encoding": "gzip",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "OK",
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
| Content-Type | string | Type of the resource or value. |
| Transfer-Encoding | string | Text string. |
| Connection | string | Text string. |
| Vary | string | Text string. |
| Content-Encoding | string | Text string. |
| Strict-Transport-Security | string | Text string. |