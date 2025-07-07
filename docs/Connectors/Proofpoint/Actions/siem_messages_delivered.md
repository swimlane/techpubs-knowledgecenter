# Siem Messages Delivered

**Description**: Fetch events for messages delivered within a specified time frame that contained a known threat, requiring specific parameters.

## Endpoint

- **URL:** `/v2/siem/messages/delivered`
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

- **status_code** (number): TODO: Add description
- **reason** (string): TODO: Add description
- **response_text** (string): TODO: Add description
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string | TODO: Add description |
| Content-Type | string | TODO: Add description |
| Transfer-Encoding | string | TODO: Add description |
| Connection | string | TODO: Add description |
| Vary | string | TODO: Add description |
| Content-Encoding | string | TODO: Add description |
| Strict-Transport-Security | string | TODO: Add description |