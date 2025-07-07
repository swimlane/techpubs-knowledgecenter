# Bulk Close Investigations

**Description**: Closes multiple investigations in Rapid7 InsightIDR within a specified date range, requiring 'from', 'source', and 'to' parameters.

## Endpoint

- **URL:** `idr/v2/investigations/bulk_close`
- **Method:** `POST`
## Inputs

- **headers** (object) – Required
  - **Accept-version** (string) – Required
- **json_body** (object) – Required
  - **alert_type** (string)
  - **detection_rule_rrn** (string)
  - **disposition** (string)
  - **from** (string) – Required
  - **max_investigations_to_close** (number)
  - **source** (string) – Required
  - **to** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "",
    "json_body": {
      "ids": [
        "581134c9-2510-4010-865c-7ae81761315b",
        "114c706d-e64a-4731-997b-9115beef3026"
      ],
      "num_closed": 2
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **ids** (array)
  - **num_closed** (number)