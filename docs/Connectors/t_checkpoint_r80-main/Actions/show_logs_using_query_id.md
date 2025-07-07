# Show Logs using Query ID

**Description**: Retrieves logs from Check Point R80 using a specified 'query-id' included in the JSON body of the request.

## Endpoint

- **URL:** `/web_api/show-logs`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **query-id** (string) – Required: Get the next page of last run query with specified limit.
  - **ignore-warnings** (boolean): Ignore warnings if exist.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "content-length": "140",
      "content-type": "application/json",
      "Date": "Wed, 13 Dec 2023 20:37:23 GMT"
    },
    "reason": "OK",
    "json_body": {
      "incidents": [
        {
          "isCHKPObject": "false",
          "resolved": "labs-proxy-old.ad.checkpoint.com"
        }
      ],
      "logs": [
        {
          "analyzed_on": "Check Point Threat Cloud",
          "i_f_dir": "inbound",
          "proto_attr": [
            {
              "isCHKPObject": "false",
              "resolved": "TCP (6)"
            }
          ]
        }
      ],
      "logs-count": 2,
      "query-id": "aa_be383957-9167-4ca3-b101-a25bc0fbec1c",
      "tops": [
        {
          "Firewall": "717"
        },
        {
          "System Monitor": "132"
        }
      ],
      "tops-count": 935
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **incidents** (array)
    - **isCHKPObject** (string)
    - **resolved** (string)
  - **logs** (array)
    - **analyzed_on** (string)
    - **i_f_dir** (string)
    - **proto_attr** (array)
      - **isCHKPObject** (string)
      - **resolved** (string)
  - **logs-count** (number)
  - **query-id** (string)
  - **tops** (array)
    - **Firewall** (string)
    - **System Monitor** (string)
  - **tops-count** (number)
## Response Headers

| Header | Type |
|--------|------|
| content-length | string |
| content-type | string |
| Date | string |