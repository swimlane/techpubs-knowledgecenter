# Get Ticket by ID

**Description**: Retrieve a specific ticket from HaloPSA using the unique identifier (ID) provided.

## Endpoint

- **URL:** `/api/Tickets/{{id}}`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **includedetails** (boolean): Whether to include extra objects in the response.
  - **includelastaction** (boolean): Whether to include the last action in the response.
  - **ticketidonly** (boolean): Returns only the ID fields (Ticket ID, SLA ID, Status ID, Client ID and Name and Lastincomingemail date) of the Tickets (Not compatible with Pagination).
- **path_parameters** (object) – Required
  - **id** (number) – Required: The Ticket's ID.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Content-Type": "text/html; charset=utf-8",
      "x-hsci-cache-time": "2024-10-21T12:01:22.328Z",
      "Content-Encoding": "gzip",
      "Expires": "Mon, 21 Oct 2024 12:08:57 GMT",
      "Cache-Control": "max-age=0, no-cache, no-store",
      "Pragma": "no-cache",
      "Date": "Mon, 21 Oct 2024 12:08:57 GMT",
      "Content-Length": "106931",
      "Connection": "keep-alive"
    },
    "reason": "OK",
    "json_body": {
      "actioncode": 0,
      "id": 0,
      "dateoccurred": "2019-08-02T14:35:55.618Z",
      "status_id": 0,
      "tickettype_id": 0,
      "sla_id": 0,
      "priority_id": 0,
      "client_id": 0,
      "timetaken": 0,
      "respondbydate": "2019-08-02T14:35:55.618Z",
      "responsedate": "2019-08-02T14:35:55.618Z",
      "responsestartdate": "2019-08-02T14:35:55.618Z",
      "slaresponsestate": "string",
      "fixbydate": "2019-08-02T14:35:55.618Z",
      "dateclosed": "2019-08-02T14:35:55.618Z",
      "excludefromsla": true,
      "slaholdtime": 0,
      "slaactiondate": "2019-08-02T14:35:55.618Z",
      "slapercused": 0,
      "slatimeleft": 0,
      "lastactiondate": "2019-08-02T14:35:55.618Z",
      "organisation_id": 0,
      "department_id": 0
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **actioncode** (number)
  - **id** (number)
  - **dateoccurred** (string)
  - **status_id** (number)
  - **tickettype_id** (number)
  - **sla_id** (number)
  - **priority_id** (number)
  - **client_id** (number)
  - **timetaken** (number)
  - **respondbydate** (string)
  - **responsedate** (string)
  - **responsestartdate** (string)
  - **slaresponsestate** (string)
  - **fixbydate** (string)
  - **dateclosed** (string)
  - **excludefromsla** (boolean)
  - **slaholdtime** (number)
  - **slaactiondate** (string)
  - **slapercused** (number)
  - **slatimeleft** (number)
  - **lastactiondate** (string)
  - **organisation_id** (number)
  - **department_id** (number)
## Response Headers

| Header | Type |
|--------|------|
| Content-Type | string |
| x-hsci-cache-time | string |
| Content-Encoding | string |
| Expires | string |
| Cache-Control | string |
| Pragma | string |
| Date | string |
| Content-Length | string |
| Connection | string |