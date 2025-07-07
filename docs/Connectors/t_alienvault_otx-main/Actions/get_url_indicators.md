# Get URL Indicators

**Description**: Get URL Indicators

## Endpoint

- **URL:** `api/v1/indicators/url/{{url}}/{{section}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **url** (string) – Required
  - **section** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Content-Type": "application/json",
      "Content-Length": "375",
      "Connection": "keep-alive",
      "Date": "Fri, 06 Jan 2023 00:25:46 GMT",
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
      "X-Amz-Cf-Id": "o2bTd9T92pm-fkjL4EgSQ0tosuiDIe6_4Z1pfJi_GkVzOiJaiYBGIw=="
    },
    "reason": "OK",
    "json_body": {
      "sections": [
        "general",
        "url_list",
        "http_scans",
        "screenshot"
      ],
      "indicator": "http://www.fotoidea.com/sport/4x4_san_ponso/slides/IMG_0068.html",
      "type": "url",
      "type_title": "URL",
      "validation": [],
      "base_indicator": {
        "id": 314386135,
        "indicator": "http://www.fotoidea.com/sport/4x4_san_ponso/slides/IMG_0068.html",
        "type": "URL",
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
            "industries": [],
            "unique_indicators": 0
          },
          "other": {
            "adversary": [],
            "malware_families": [],
            "industries": [],
            "unique_indicators": 0
          }
        }
      },
      "false_positive": [],
      "alexa": "http://www.alexa.com/siteinfo/fotoidea.com",
      "whois": "http://whois.domaintools.com/fotoidea.com",
      "domain": "fotoidea.com",
      "hostname": "www.fotoidea.com"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **sections** (array)
  - **indicator** (string)
  - **type** (string)
  - **type_title** (string)
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
        - **unique_indicators** (number)
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
        - **unique_indicators** (number)
  - **false_positive** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **alexa** (string)
  - **whois** (string)
  - **domain** (string)
  - **hostname** (string)
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