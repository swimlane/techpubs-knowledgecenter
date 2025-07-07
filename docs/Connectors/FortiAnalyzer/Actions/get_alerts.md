# Get Alerts

**Description**: Fetches alert events from Forti Analyzer, allowing for monitoring and analysis of security alerts.

## Endpoint

- **URL:** `/eventmgmt/alerts`
- **Method:** `GET`
## Inputs

- **json_body** (object) – Required
  - **id** (string): An identifier established by the client.
  - **jsonrpc** (string): A string specifying the JSON-RPC protocol version.
  - **method** (string): A string containing the method name to be invoked.
  - **params** (array)
    - **apiver** (number) – Required: Current API version.
    - **filter** (string): Filter expression. 'event_value', 'severity', 'trigger_name', 'count', 'comment' and 'flags' are supported. i.e. trigger_name='Local Device Event' and severity >= 3.
    - **limit** (number): The max number of records to get (min - 1, max - 2000).
    - **offset** (number): offset of records to get.
    - **time-range** (object): Time range for data selection.
      - **end** (string) – Required: Ending date time. Consider it following the timezone parameter's, ADOM's or FortiAnalyzer's timezone if timezone info is not specified within time range. Format 'yyyy-MM-dd'T'HH:mm:ssZ' (RFC 3339) e.g. '2016-10-17T20:45:37-07:00 or 'yyyy-MM-dd HH:mm:ss' e.g. '2016-10-17 20:45:37'.
      - **start** (string) – Required: Starting date time. Consider it following the timezone parameter's, ADOM's or FortiAnalyzer's timezone if timezone info is not specified within time range. Format 'yyyy-MM-dd'T'HH:mm:ssZ' (RFC 3339) e.g. '2016-10-17T20:45:37-07:00 or 'yyyy-MM-dd HH:mm:ss' e.g. '2016-10-17 20:45:37'.
    - **timezone** (string): The timezone index or name. Time range in request and date/time if any in response will follow this timezone.
    - **url** (string) – Required: The resource path to Alert Events. Example /eventmgmt/adom/<adom-name>/alerts.
  - **session** (string): The cookie of an active session in FortiAnalyzer.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "content-length": "140",
      "content-type": "application/json",
      "Date": "Thu, 2 May 2024 20:37:23 GMT"
    },
    "reason": "OK",
    "json_body": {}
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
## Response Headers

- **content-length** (string)
- **content-type** (string)
- **Date** (string)