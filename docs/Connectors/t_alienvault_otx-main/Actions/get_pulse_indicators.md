# Get Pulse Indicators

**Description**: Get Pulse Indicators

## Endpoint

- **URL:** `api/v1/pulses/{{pulse_id}}/indicators`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **pulse_id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Content-Type": "application/json",
      "Content-Length": "633",
      "Connection": "keep-alive",
      "Date": "Fri, 06 Jan 2023 00:23:30 GMT",
      "Server": "gunicorn",
      "Content-Encoding": "gzip",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Remote-User-Name": "swimlane_dev",
      "X-OTX-ACTIVE": "1",
      "Access-Control-Allow-Origin": "*",
      "Vary": "Accept-Encoding",
      "X-Cache": "Miss from cloudfront",
      "Via": "1.1 3cf6fe633fae664d54600fda39cf3e78.cloudfront.net (CloudFront)",
      "X-Amz-Cf-Pop": "FOR50-P3",
      "X-Amz-Cf-Id": "89Jvx2EYjrRVhrjds1c1AtbtrmWAZduXZLnLekiCQcQ3-uCy8Zeybw=="
    },
    "reason": "OK",
    "json_body": {
      "results": [
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 361850,
          "indicator": "webserver.servehttp.com",
          "type": "hostname",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "hostname"
        },
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 361851,
          "indicator": "web.microsoftdefence.com",
          "type": "hostname",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "hostname"
        },
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 175207,
          "indicator": "jackhex.md5c.net",
          "type": "hostname",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "hostname"
        },
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 361852,
          "indicator": "admin.nslookupdns.com",
          "type": "hostname",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "hostname"
        },
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 175151,
          "indicator": "news.tibetgroupworks.com",
          "type": "hostname",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "hostname"
        },
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 361853,
          "indicator": "cbbfc3b5ff08de14fdb2316f3b14886dfe5504ef",
          "type": "FileHash-SHA1",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "file"
        },
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 361854,
          "indicator": "63e00dbf45961ad11bd1eb55dff9c2771c2916a6",
          "type": "FileHash-SHA1",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "file"
        },
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 361855,
          "indicator": "a7d206791b1cdec616e9b18ae6fa1548ca96a321",
          "type": "FileHash-SHA1",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "file"
        },
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 361856,
          "indicator": "49e36de6d757ca44c43d5670d497bd8738c1d2a4",
          "type": "FileHash-SHA1",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "file"
        },
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 361857,
          "indicator": "ec646c57f9ac5e56230a17aeca6523a4532ff472",
          "type": "FileHash-SHA1",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "file"
        },
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 361858,
          "indicator": "f389e1c970b2ca28112a30a8cfef1f3973fa82ea",
          "type": "FileHash-SHA1",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "file"
        },
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 361859,
          "indicator": "ef2618d58bd50fa232a19f9bcf3983d1e2dff266",
          "type": "FileHash-SHA1",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "file"
        },
        {
          "pulse_key": "57204e9b3c4c3e015d93cb12",
          "id": 361860,
          "indicator": "675a3247f4c0e1105a41c685f4c2fb606e5b1eac",
          "type": "FileHash-SHA1",
          "created": "2016-04-27T05:31:07",
          "content": "",
          "title": "",
          "description": "",
          "expiration": null,
          "is_active": 1,
          "false_positive": {
            "assessment": null,
            "assessment_date": null,
            "report_date": null
          },
          "slug": "file"
        }
      ],
      "count": 13,
      "previous": null,
      "next": null
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **results** (array)
    - **pulse_key** (string)
    - **id** (number)
    - **indicator** (string)
    - **type** (string)
    - **created** (string)
    - **content** (string)
    - **title** (string)
    - **description** (string)
    - **expiration** (object)
    - **is_active** (number)
    - **false_positive** (object)
      - **assessment** (object)
      - **assessment_date** (object)
      - **report_date** (object)
    - **slug** (string)
  - **count** (number)
  - **previous** (object)
  - **next** (object)
## Response Headers

| Header | Type |
|--------|------|
| Content-Type | string |
| Content-Length | string |
| Connection | string |
| Date | string |
| Server | string |
| Content-Encoding | string |
| X-Frame-Options | string |
| X-Remote-User-Name | string |
| X-OTX-ACTIVE | string |
| Access-Control-Allow-Origin | string |
| Vary | string |
| X-Cache | string |
| Via | string |
| X-Amz-Cf-Pop | string |
| X-Amz-Cf-Id | string |