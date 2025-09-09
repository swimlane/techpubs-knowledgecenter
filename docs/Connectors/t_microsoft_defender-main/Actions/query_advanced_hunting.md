# Query Advanced Hunting

**Description**: Executes an advanced hunting query in Microsoft Defender to identify threats, with a required 'Query' parameter.

## Endpoint

- **URL:** `/api/advancedhunting/run`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **Query** (string) – Required: The query to run.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 05 Sep 2024 07:29:53 GMT",
      "Content-Type": "application/json; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "Stats": {
        "ExecutionTime": 0.171881,
        "resource_usage": {
          "cache": {
            "memory": null,
            "disk": null
          },
          "cpu": {
            "user": "00:00:00",
            "kernel": "00:00:00",
            "total cpu": "00:00:00"
          },
          "memory": {
            "peak_per_node": 3146640
          }
        },
        "dataset_statistics": [
          {
            "table_row_count": 0,
            "table_size": 0
          }
        ]
      },
      "Schema": [
        {
          "Name": "Timestamp",
          "Type": "DateTime"
        },
        {
          "Name": "FileName",
          "Type": "String"
        },
        {
          "Name": "InitiatingProcessFileName",
          "Type": "String"
        }
      ],
      "Results": []
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **Stats** (object)
    - **ExecutionTime** (number)
    - **resource_usage** (object)
      - **cache** (object)
        - **memory** (object)
        - **disk** (object)
      - **cpu** (object)
        - **user** (string)
        - **kernel** (string)
        - **total cpu** (string)
      - **memory** (object)
        - **peak_per_node** (number)
    - **dataset_statistics** (array)
      - **table_row_count** (number)
      - **table_size** (number)
  - **Schema** (array)
    - **Name** (string)
    - **Type** (string)
  - **Results** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Content-Encoding | string |
| Vary | string |
| Strict-Transport-Security | string |