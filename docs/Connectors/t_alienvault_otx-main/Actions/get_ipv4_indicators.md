# Get IPV4 Indicators

**Description**: Get IPV4 Indicators

## Endpoint

- **URL:** `api/v1/indicators/IPv4/{{ip}}/{{section}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **ip** (string) – Required
  - **section** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Content-Type": "application/json",
      "Content-Length": "646",
      "Connection": "keep-alive",
      "Date": "Mon, 09 Jan 2023 23:41:34 GMT",
      "Server": "gunicorn",
      "Cache-Control": "max-age=0",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Remote-User-Name": "swimlane_dev",
      "X-OTX-ACTIVE": "1",
      "Content-Encoding": "gzip",
      "Access-Control-Allow-Origin": "*",
      "Vary": "Accept-Encoding",
      "X-Cache": "Miss from cloudfront",
      "Via": "1.1 804a8375579a9f838ab10ed130908180.cloudfront.net (CloudFront)",
      "X-Amz-Cf-Pop": "FOR50-P3",
      "X-Amz-Cf-Id": "SJmIw6Z8IrM-7BqEAjt3wyglF9zRT8bSYU_OH5IWZHa2QrRJ-fn1bA=="
    },
    "reason": "OK",
    "json_body": {
      "whois": "http://whois.domaintools.com/8.8.8.8",
      "reputation": 0,
      "indicator": "8.8.8.8",
      "type": "IPv4",
      "type_title": "IPv4",
      "base_indicator": {
        "id": 11911,
        "indicator": "8.8.8.8",
        "type": "IPv4",
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
      "false_positive": [
        {
          "assessment": "accepted",
          "assessment_date": "2021-05-19T15:36:44.966000",
          "report_date": "2021-03-16T14:46:19.003000"
        }
      ],
      "validation": [
        {
          "source": "false_positive",
          "message": "Known False Positive",
          "name": "Known False Positive"
        },
        {
          "source": "whitelist",
          "message": "contained in whitelisted prefix",
          "name": "Whitelisted IP"
        }
      ],
      "asn": "AS15169 google llc",
      "city_data": true,
      "city": null,
      "region": null,
      "continent_code": "NA",
      "country_code3": "USA",
      "country_code2": "US",
      "subdivision": null,
      "latitude": 37.751,
      "postal_code": null,
      "longitude": -97.822,
      "accuracy_radius": 1000,
      "country_code": "US",
      "country_name": "United States of America",
      "dma_code": 0,
      "charset": 0,
      "area_code": 0,
      "flag_url": "/assets/images/flags/us.png",
      "flag_title": "United States of America",
      "sections": [
        "general",
        "geo",
        "reputation",
        "url_list",
        "passive_dns",
        "malware",
        "nids_list",
        "http_scans"
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **whois** (string)
  - **reputation** (number)
  - **indicator** (string)
  - **type** (string)
  - **type_title** (string)
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
    - **assessment** (string)
    - **assessment_date** (string)
    - **report_date** (string)
  - **validation** (array)
    - **source** (string)
    - **message** (string)
    - **name** (string)
  - **asn** (string)
  - **city_data** (boolean)
  - **city** (object)
  - **region** (object)
  - **continent_code** (string)
  - **country_code3** (string)
  - **country_code2** (string)
  - **subdivision** (object)
  - **latitude** (number)
  - **postal_code** (object)
  - **longitude** (number)
  - **accuracy_radius** (number)
  - **country_code** (string)
  - **country_name** (string)
  - **dma_code** (number)
  - **charset** (number)
  - **area_code** (number)
  - **flag_url** (string)
  - **flag_title** (string)
  - **sections** (array)
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