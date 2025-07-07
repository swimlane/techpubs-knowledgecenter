# Get IPV6 Indicators

**Description**: Get IPV6 Indicators

## Endpoint

- **URL:** `api/v1/indicators/IPv6/{{ip}}/{{section}}`
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
      "Content-Length": "458",
      "Connection": "keep-alive",
      "Date": "Mon, 09 Jan 2023 23:42:33 GMT",
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
      "X-Amz-Cf-Id": "KuULqZtZ3XtykEW6x6Qf3POR6jmWufCkoj4ygOF2Ri-yY2565v0-Dw=="
    },
    "reason": "OK",
    "json_body": {
      "whois": "http://whois.domaintools.com/0:0:0:0:0:ffff:808:808",
      "reputation": 0,
      "indicator": "0:0:0:0:0:ffff:808:808",
      "type": "IPv6",
      "type_title": "IPv6",
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
      "false_positive": [],
      "validation": [],
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
  - **validation** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
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