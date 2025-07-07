# Search Logs

**Description**: Initiates a task to search logs in Forti Analyzer with specified parameters, requiring a 'params' JSON body input.

## Endpoint

- **URL:** `/logview/logsearch`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: Auto-generated description for `json_body`. Please update manually if needed.
  - **id** (string): An identifier established by the client.
  - **jsonrpc** (string): A string specifying the JSON-RPC protocol version.
  - **method** (string): A string containing the method name to be invoked.
  - **params** (array) – Required: A structure that holds the parameter values.
    - **apiver** (number) – Required: Current API version.
    - **case-sensitive** (boolean): Case sensitivity in filter.
    - **device** (array) – Required: Device filter. For all devices in some type please use the All-Device ID.
      - **csfname** (string): Name of security fabric. Format - csfname. e.g. 'Corp_SF'
      - **devid** (string): Format - devid[vdom]. e.g. 'FGT60C0000000001[root]'.
      - **devname** (string): Format - devname[vdom]. e.g. 'FGT-vancouver[traffic]'.
    - **filter** (string): Filter expression.
    - **logtype** (string) – Required: The name of the logtype.
    - **time-order** (string): Sort result in descending or ascending order by time.
    - **time-range** (object) – Required: Time range for log selection.
      - **end** (string) – Required: Ending date time. Consider it following the timezone parameter's, ADOM's or FortiAnalyzer's timezone if timezone info is not specified within time range. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' (RFC 3339) e.g. '2016-10-17T20:45:37-07:00 or 'yyyy-MM-dd HH:mm:ss' e.g. '2016-10-17 20:45:37'.
      - **start** (string) – Required: Starting date time. Consider it following the timezone parameter's, ADOM's or FortiAnalyzer's timezone if timezone info is not specified within time range. Format is 'yyyy-MM-dd'T'HH:mm:ssZ' (RFC 3339) e.g. '2016-10-17T20:45:37-07:00 or 'yyyy-MM-dd HH:mm:ss' e.g. '2016-10-17 20:45:37'.
    - **timezone** (string): The timezone index or name. Time range in request and date/time if any in response will follow this timezone.
    - **url** (string) – Required: The resource path to log Search.
  - **session** (string): The cookie of an active session in FortiAnalyzer.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "id": "string",
      "jsonrpc": "2.0",
      "result": {
        "tid": 0
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number): Auto-generated description for `status_code`. Please update manually if needed.
- **reason** (string): Auto-generated description for `reason`. Please update manually if needed.
- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.
  - **id** (string): Auto-generated description for `id`. Please update manually if needed.
  - **jsonrpc** (string): Auto-generated description for `jsonrpc`. Please update manually if needed.
  - **result** (object): Auto-generated description for `result`. Please update manually if needed.
    - **tid** (number): Auto-generated description for `tid`. Please update manually if needed.