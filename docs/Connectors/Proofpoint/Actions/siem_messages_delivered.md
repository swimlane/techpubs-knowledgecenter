# Siem Messages Delivered

**Description**: Fetch events for messages delivered within a specified time frame that contained a known threat, requiring specific parameters.

## Endpoint

- **URL:** `/v2/siem/messages/delivered`
- **Method:** `GET`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| parameters | object | One of the following three query parameters describing the desired time range for the data must be supplied with each request interval, sinceSeconds, sinceTime. | Yes |
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

| Name | Type | Description |
|------|------|-------------|
| status_code | number |  |
| reason | string |  |
| response_text | string |  |
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string |  |
| Content-Type | string |  |
| Transfer-Encoding | string |  |
| Connection | string |  |
| Vary | string |  |
| Content-Encoding | string |  |
| Strict-Transport-Security | string |  |