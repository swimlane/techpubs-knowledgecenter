# List Alerts Investigation

**Description**: Retrieve all alerts associated with a given investigation in Rapid7 InsightIDR V2, utilizing the unique identifier.

## Endpoint

- **URL:** `idr/v2/investigations/{{identifier}}/alerts`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **identifier** (string) – Required
- **parameters** (object)
  - **index** (number)
  - **multi-customer** (boolean)
  - **size** (number)
- **headers** (object) – Required
  - **Accept-version** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Tue, 25 Jul 2023 05:00:27 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Cache-Control": "no-cache, no-store, max-age=0, must-revalidate",
      "Expires": "0",
      "Pragma": "no-cache",
      "X-Content-Type-Options": "nosniff",
      "X-Frame-Options": "DENY",
      "X-XSS-Protection": "1; mode=block",
      "vary": "Origin",
      "Access-Control-Allow-Credentials": "true"
    },
    "reason": "OK",
    "json_body": {
      "data": [
        {
          "alert_source": "User Behavior Analytics",
          "alert_type": "Account Created",
          "alert_type_description": "A new account has been created.",
          "created_time": "2018-06-06T16:56:42Z",
          "detection_rule_rrn": {
            "rule_name": "Attacker Technique - Accessibility Tool Launching Process",
            "rule_rrn": "rrn:cba:::detection-rule:FX11KBBSCK20"
          },
          "first_event_time": "2018-06-06T16:56:42Z",
          "id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
          "latest_event_time": "2018-06-06T16:56:42Z",
          "title": "Account jdoe had INBOUND firewall traffic from 1.2.3.4 (tracked in MyThreat) to 10.1.2.3"
        }
      ]
    },
    "metadata": {
      "index": 10,
      "size": 20,
      "total_pages": 1,
      "total_data": 1
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (array)
    - **alert_source** (string)
    - **alert_type** (string)
    - **alert_type_description** (string)
    - **created_time** (string)
    - **detection_rule_rrn** (object)
      - **rule_name** (string)
      - **rule_rrn** (string)
    - **first_event_time** (string)
    - **id** (string)
    - **latest_event_time** (string)
    - **title** (string)
- **metadata** (object)
  - **index** (number)
  - **size** (number)
  - **total_pages** (number)
  - **total_data** (number)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Cache-Control | string |
| Expires | string |
| Pragma | string |
| X-Content-Type-Options | string |
| X-Frame-Options | string |
| X-XSS-Protection | string |
| vary | string |
| Access-Control-Allow-Credentials | string |