# Get Domain Indicators

**Description**: Get Domain Indicators

## Endpoint

- **URL:** `api/v1/indicators/domain/{{domain}}/{{section}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **domain** (string) – Required
  - **section** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Content-Type": "application/json",
      "Content-Length": "268",
      "Connection": "keep-alive",
      "Date": "Fri, 06 Jan 2023 00:27:24 GMT",
      "Server": "gunicorn",
      "Cache-Control": "max-age=0",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Remote-User-Name": "swimlane_dev",
      "X-OTX-ACTIVE": "1",
      "Content-Encoding": "gzip",
      "Access-Control-Allow-Origin": "*",
      "Vary": "Accept-Encoding",
      "X-Cache": "Miss from cloudfront",
      "Via": "1.1 e074760d97af50b62db843a4057448cc.cloudfront.net (CloudFront)",
      "X-Amz-Cf-Pop": "FOR50-P3",
      "X-Amz-Cf-Id": "r-BhM_yW66-BJWE4d7S-_c83xVUysFlrm9cDpXmZHf2mo0weHWeE1A=="
    },
    "reason": "OK",
    "json_body": {
      "sections": [
        "general",
        "geo",
        "url_list",
        "passive_dns",
        "malware",
        "whois",
        "http_scans"
      ],
      "whois": "http://whois.domaintools.com/swimlane.com",
      "alexa": "http://www.alexa.com/siteinfo/swimlane.com",
      "indicator": "swimlane.com",
      "type": "domain",
      "type_title": "Domain",
      "validation": [],
      "base_indicator": {},
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
  - **whois** (string)
  - **alexa** (string)
  - **indicator** (string)
  - **type** (string)
  - **type_title** (string)
  - **validation** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **base_indicator** (object)
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