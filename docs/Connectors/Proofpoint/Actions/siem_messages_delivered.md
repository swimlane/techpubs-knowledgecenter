# Siem Messages Delivered

**Description**: Fetch events for messages delivered within a specified time frame that contained a known threat, requiring specific parameters.

## Endpoint

- **URL:** `/v2/siem/messages/delivered`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required: One of the following three query parameters describing the desired time range for the data must be supplied with each request interval, sinceSeconds, sinceTime.
  - **interval** (string): Auto-generated description for `interval`. Please update manually if needed.
  - **sinceSeconds** (number): Auto-generated description for `sinceSeconds`. Please update manually if needed.
  - **sinceTime** (string): Auto-generated description for `sinceTime`. Please update manually if needed.
  - **format** (string): Auto-generated description for `format`. Please update manually if needed.
  - **threatType** (string): Auto-generated description for `threatType`. Please update manually if needed.
  - **threatStatus** (string): Auto-generated description for `threatStatus`. Please update manually if needed.
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

- **status_code** (number): Auto-generated description for `status_code`. Please update manually if needed.
- **reason** (string): Auto-generated description for `reason`. Please update manually if needed.
- **response_text** (string): Auto-generated description for `response_text`. Please update manually if needed.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string | Auto-generated description for `Date`. Please update manually if needed. |
| Content-Type | string | Auto-generated description for `Content-Type`. Please update manually if needed. |
| Transfer-Encoding | string | Auto-generated description for `Transfer-Encoding`. Please update manually if needed. |
| Connection | string | Auto-generated description for `Connection`. Please update manually if needed. |
| Vary | string | Auto-generated description for `Vary`. Please update manually if needed. |
| Content-Encoding | string | Auto-generated description for `Content-Encoding`. Please update manually if needed. |
| Strict-Transport-Security | string | Auto-generated description for `Strict-Transport-Security`. Please update manually if needed. |