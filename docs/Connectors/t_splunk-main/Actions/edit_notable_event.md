# Edit Notable Event

**Description**: Update details of existing Notable Events in Cisco Splunk using the provided data body.

## Endpoint

- **URL:** `services/notable_update`
- **Method:** `POST`
## Inputs

- **data_body** (object) – Required
  - **ruleUIDs** (array) – Required
  - **searchID** (string)
  - **newOwner** (string)
  - **urgency** (string)
  - **status** (string)
  - **comment** (string)
  - **disposition** (string): An ID for a disposition that matches a disposition in the reviewstatuses.conf configuration file. Required only if you are changing the disposition of the event.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Mon, 17 Jul 2023 20:53:02 GMT",
      "Expires": "Thu, 26 Oct 1978 00:00:00 GMT",
      "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
      "Content-Type": "application/json; charset=UTF-8",
      "X-Content-Type-Options": "nosniff",
      "Transfer-Encoding": "chunked",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding, Cookie, Authorization",
      "Connection": "Keep-Alive",
      "X-Frame-Options": "SAMEORIGIN",
      "Server": "Splunkd"
    },
    "reason": "OK",
    "json_body": {
      "message": "",
      "failure_count": 0,
      "success": true,
      "success_count": 2
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **message** (string)
  - **failure_count** (number)
  - **success** (boolean)
  - **success_count** (number)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Expires | string |
| Cache-Control | string |
| Content-Type | string |
| X-Content-Type-Options | string |
| Transfer-Encoding | string |
| Content-Encoding | string |
| Vary | string |
| Connection | string |
| X-Frame-Options | string |
| Server | string |