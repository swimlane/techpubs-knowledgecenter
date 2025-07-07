# Get File Hash Indicators

**Description**: Get File Hash Indicators

## Endpoint

- **URL:** `api/v1/indicators/file/{{file_hash}}/{{section}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **file_hash** (string) – Required
  - **section** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Content-Type": "application/json",
      "Content-Length": "323",
      "Connection": "keep-alive",
      "Date": "Mon, 09 Jan 2023 23:40:19 GMT",
      "Server": "gunicorn",
      "Cache-Control": "max-age=0",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Remote-User-Name": "swimlane_dev",
      "X-OTX-ACTIVE": "1",
      "Content-Encoding": "gzip",
      "Access-Control-Allow-Origin": "*",
      "Vary": "Accept-Encoding",
      "X-Cache": "Miss from cloudfront",
      "Via": "1.1 021fce58f4d2d5cc960cb6a0e0c04fc0.cloudfront.net (CloudFront)",
      "X-Amz-Cf-Pop": "FOR50-P3",
      "X-Amz-Cf-Id": "3Cxg4RSv_u0G7TwfSLd9-gMSS_5vmvNXvza1ppHPFIS8PHdcbe_2rA=="
    },
    "reason": "OK",
    "json_body": {
      "sections": [
        "general",
        "analysis"
      ],
      "type": "sha1",
      "type_title": "FileHash-SHA1",
      "indicator": "6c5360d41bd2b14b1565f5b18e5c203cf512e493",
      "validation": [],
      "base_indicator": {
        "id": 2113706547,
        "indicator": "2eb14920c75d5e73264f77cfa273ad2c",
        "type": "FileHash-MD5",
        "title": "",
        "description": "",
        "content": "",
        "access_type": "public",
        "access_reason": ""
      },
      "pulse_info": {
        "count": 0,
        "pulses": [],
        "references": [],
        "related": {
          "alienvault": {
            "adversary": [],
            "malware_families": [],
            "industries": []
          },
          "other": {
            "adversary": [],
            "malware_families": [],
            "industries": []
          }
        }
      },
      "false_positive": []
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **sections** (array)
  - **type** (string)
  - **type_title** (string)
  - **indicator** (string)
  - **validation** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **base_indicator** (object)
    - **id** (number)
    - **indicator** (string)
    - **type** (string)
    - **title** (string)
    - **description** (string)
    - **content** (string)
    - **access_type** (string)
    - **access_reason** (string)
  - **pulse_info** (object)
    - **count** (number)
    - **pulses** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **references** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **related** (object)
      - **alienvault** (object)
        - **adversary** (array)
          - **file_name** (string) – Required
          - **file** (string) – Required
        - **malware_families** (array)
          - **file_name** (string) – Required
          - **file** (string) – Required
        - **industries** (array)
          - **file_name** (string) – Required
          - **file** (string) – Required
      - **other** (object)
        - **adversary** (array)
          - **file_name** (string) – Required
          - **file** (string) – Required
        - **malware_families** (array)
          - **file_name** (string) – Required
          - **file** (string) – Required
        - **industries** (array)
          - **file_name** (string) – Required
          - **file** (string) – Required
  - **false_positive** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
## Response Headers

| Header | Type |
|--------|------|
| Content-Type | string |
| Content-Length | string |
| Connection | string |
| Date | string |
| Server | string |
| Cache-Control | string |
| X-Frame-Options | string |
| X-Remote-User-Name | string |
| X-OTX-ACTIVE | string |
| Content-Encoding | string |
| Access-Control-Allow-Origin | string |
| Vary | string |
| X-Cache | string |
| Via | string |
| X-Amz-Cf-Pop | string |
| X-Amz-Cf-Id | string |