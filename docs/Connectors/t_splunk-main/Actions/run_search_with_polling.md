# Run Search with Polling

**Description**: Executes a long-running search in Cisco Splunk and continuously polls for results until completion or timeout, using the provided 'search_string'.

## Endpoint

- **URL:** `/services/search/jobs`
- **Method:** `POST`
## Inputs

- **search_string** (string) – Required: The Splunk search query string to run. Example- index=_internal | head 10.
- **output_mode** (string)
- **add_search** (boolean): If true, prepends 'search' to the search string automatically. Default is true.
- **timeout** (integer): Maximum number of seconds to wait for the search to complete before timing out. Default is 600 seconds (10 minutes).
- **poll_interval** (integer): Interval in seconds between each status check. Default is 10 seconds.
- **count** (number): The maximum number of results to return.
- **offset** (number): The first result from which to begin returning data.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Wed, 04 Jun 2025 08:50:29 GMT",
      "Expires": "Thu, 26 Oct 1978 00:00:00 GMT",
      "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
      "Content-Type": "application/json; charset=UTF-8",
      "X-Content-Type-Options": "nosniff",
      "Link": "<../1749027018.39126>; rel=info",
      "Content-Length": "166",
      "Vary": "Cookie, Authorization",
      "Connection": "Keep-Alive",
      "X-Frame-Options": "SAMEORIGIN",
      "Server": "Splunkd"
    },
    "reason": "OK",
    "json_body": {
      "preview": false,
      "init_offset": 0,
      "post_process_count": 0,
      "messages": [
        {
          "type": "INFO",
          "text": "Your timerange was substituted based on your search string"
        }
      ],
      "results": []
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **preview** (boolean)
  - **init_offset** (number)
  - **post_process_count** (number)
  - **messages** (array)
    - **type** (string)
    - **text** (string)
  - **results** (array)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Expires | string |
| Cache-Control | string |
| Content-Type | string |
| X-Content-Type-Options | string |
| Link | string |
| Content-Length | string |
| Vary | string |
| Connection | string |
| X-Frame-Options | string |
| Server | string |