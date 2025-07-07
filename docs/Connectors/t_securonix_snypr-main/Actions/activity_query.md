# Run Activity Query

**Description**: Run simple searches from the Unified Defense SIEM interface on the activity collection. "|" pipe or operator searches are not currently supported.

## Endpoint

- **URL:** `Snypr/ws/spotter/index/search`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required
  - **query** (string) – Required
  - **eventtime_from** (string) – Required
  - **eventtime_to** (string) – Required
  - **tz** (string)
  - **prettyJson** (boolean)
  - **max** (number): This parameter is only available for version 6.2 CU4 SP4 and above.
  - **queryId** (string): This parameter is only available for version 6.2 CU4 SP4 and above.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 25 Jan 2024 00:34:27 GMT",
      "Content-Type": "text/plain",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Strict-Transport-Security": "max-age=31536000 ; includeSubDomains",
      "Cache-Control": "private, no-store, no-cache, must-revalidate",
      "X-FRAME-OPTIONS": "DENY",
      "Pragma": "no-cache",
      "X-XSS-Protection": "1 ;mode=block",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "frame-ancestors 'self' *.securonix.net; default-src 'self' *.securonix.net; object-src 'self' *.securonix.net data: blob:; script-src 'unsafe-inline' 'unsafe-eval' 'self' *.securonix.net https://edge.fullstory.com https://rs.fullstory.com http://iph.zoominsoftware.io/widget.js data: blob:; style-src 'self' *.securonix.net https://fonts.googleapis.com 'unsafe-inline'; font-src 'self' *.securonix.net https://fonts.gstatic.com 'unsafe-inline'; connect-src 'self' *.securonix.net https://edge.fullstory.com https://rs.fullstory.com https://securonix-be-prod.zoominsoftware.io http://documentation-be.securonix.com wss://saaspoc5t16expo.securonix.net:443 data: blob:; img-src 'self' *.securonix.net https://rs.fullstory.com data: https:; child-src 'self' *.securonix.net blob:;"
    },
    "reason": "",
    "json_body": {
      "totalDocuments": 69490,
      "events": [
        {
          "timeline_by_month": "1588309200000",
          "rg_timezoneoffset": "Asia/Kolkata",
          "resourcegroupname": "carbonblackalert_19mayRIn",
          "eventid": "bcb2c382-a14f-4673-ae8e-af64901d2d94",
          "ipaddress": "192.168.1.14",
          "week": "21",
          "year": "2020",
          "accountresourcekey": "ROOT~carbonblackalert_19mayRIn~carbonblackalert_19mayRIn~815~-1",
          "resourcehostname": "lm11197",
          "sourceprocessname": "bash",
          "rg_functionality": "umesh",
          "userid": "-1",
          "customfield2": "1589916440853",
          "dayofmonth": "20",
          "jobid": "-5",
          "resourcegroupid": "815",
          "datetime": "1589916504386",
          "timeline_by_hour": "1589914800000",
          "collectiontimestamp": "1589915105445",
          "hour": "0",
          "accountname": "ROOT",
          "tenantid": "54",
          "id": "-1",
          "rg_resourcetypeid": "449",
          "_indexed_at_tdt": "Tue May 19 15:28:30 EDT 2020",
          "timeline_by_minute": "1589916300000",
          "routekey": "54-202005190003",
          "collectionmethod": "carbonblackalerts",
          "receivedtime": "1589916504387",
          "publishedtime": "1589916440853",
          "categorizedtime": "Night",
          "jobstarttime": "1589915105445",
          "dayofyear": "141",
          "minute": "58",
          "categoryseverity": "0",
          "rg_vendor": "umesh",
          "month": "4",
          "_version_": "1667148295203454980",
          "timeline": "1589864400000",
          "dayofweek": "4",
          "timeline_by_week": "1589691600000",
          "tenantname": "CORDALA",
          "resourcename": "carbonblackalert_19mayRIn",
          "ingestionnodeid": "umesh_du-10-0-0-81.securonix.com"
        }
      ],
      "error": false,
      "available": false,
      "queryId": "spotterwebservicee8904c76-b230-4ad7-990f-eefd220a22b8",
      "applicationTz": "CST6CDT",
      "inputParams": {
        "eventtime_from": " \"05/19/2020 00:00:00\"",
        "max": "1",
        "query": "index=activity AND resourcegroupname = \"carbonblackalert_19mayRIn\"",
        "eventtime_to": " \"05/19/2020 23:59:59\""
      },
      "index": "activity"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **totalDocuments** (number)
  - **events** (array)
    - **timeline_by_month** (string)
    - **rg_timezoneoffset** (string)
    - **resourcegroupname** (string)
    - **eventid** (string)
    - **ipaddress** (string)
    - **week** (string)
    - **year** (string)
    - **accountresourcekey** (string)
    - **resourcehostname** (string)
    - **sourceprocessname** (string)
    - **rg_functionality** (string)
    - **userid** (string)
    - **customfield2** (string)
    - **dayofmonth** (string)
    - **jobid** (string)
    - **resourcegroupid** (string)
    - **datetime** (string)
    - **timeline_by_hour** (string)
    - **collectiontimestamp** (string)
    - **hour** (string)
    - **accountname** (string)
    - **tenantid** (string)
    - **id** (string)
    - **rg_resourcetypeid** (string)
    - **_indexed_at_tdt** (string)
    - **timeline_by_minute** (string)
    - **routekey** (string)
    - **collectionmethod** (string)
    - **receivedtime** (string)
    - **publishedtime** (string)
    - **categorizedtime** (string)
    - **jobstarttime** (string)
    - **dayofyear** (string)
    - **minute** (string)
    - **categoryseverity** (string)
    - **rg_vendor** (string)
    - **month** (string)
    - **_version_** (string)
    - **timeline** (string)
    - **dayofweek** (string)
    - **timeline_by_week** (string)
    - **tenantname** (string)
    - **resourcename** (string)
    - **ingestionnodeid** (string)
  - **error** (boolean)
  - **available** (boolean)
  - **queryId** (string)
  - **applicationTz** (string)
  - **inputParams** (object)
    - **eventtime_from** (string)
    - **max** (string)
    - **query** (string)
    - **eventtime_to** (string)
  - **index** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Strict-Transport-Security | string |
| Cache-Control | string |
| X-FRAME-OPTIONS | string |
| Pragma | string |
| X-XSS-Protection | string |
| X-Content-Type-Options | string |
| Content-Security-Policy | string |