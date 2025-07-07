# Get Tickets

**Description**: Retrieve an array of ticket objects from HaloPSA, offering a summary of existing tickets.

## Endpoint

- **URL:** `/api/Tickets`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **pageinate** (boolean): Whether to use Pagination in the response.
  - **page_size** (number): When using Pagination, the size of the page. Maximum size is 100.
  - **page_no** (number): When using Pagination, the page number to return.
  - **order** (string): The name of the field to order by.
  - **orderdesc** (boolean): Whether to order ascending or descending.
  - **ticketidonly** (boolean): Returns only the ID fields (Ticket ID, SLA ID, Status ID, Client ID and Name and Lastincomingemail date) of the Tickets (Not compatible with Pagination).
  - **view_id** (number): The ID of the filter profile to filter by.
  - **columns_id** (number): The column profile ID.
  - **includecolumns** (boolean): Include column details in the response.
  - **includeslaactiondate** (boolean): Include the SLA action date in the response.
  - **includeslatimer** (boolean): Include SLA timer in the response.
  - **includetimetaken** (boolean): Include time taken in the response.
  - **includesupplier** (boolean): Include supplier details in the response.
  - **includerelease1** (boolean): Include release 1 details in the response.
  - **includerelease2** (boolean): Include release 2 details in the response.
  - **includerelease3** (boolean): Include release 3 details in the response.
  - **includechildids** (boolean): Include child ticket IDs in the response.
  - **includenextactivitydate** (boolean): Include nextactivitydate in the response.
  - **includefirstresponse** (boolean): Include First Response data in the response.
  - **list_id** (number): Filters by the specified list.
  - **agent_id** (number): Filters by the specified agent.
  - **status_id** (number): Filters by the specified status.
  - **requesttype_id** (number): Filters by the specified request type.
  - **supplier_id** (number): Filters by the specified supplier.
  - **client_id** (number): Filters by the specified client.
  - **site** (number): Filters by the specified site.
  - **username** (string): Filters by the specified user.
  - **user_id** (number): Filters by the specified user.
  - **release_id** (number): Filters by the specified release.
  - **asset_id** (number): Filters by the specified asset.
  - **itil_requesttype_id** (number): Filters by the specified ITIL request type.
  - **open_only** (boolean): Returns only open tickets in the response.
  - **closed_only** (boolean): Returns only closed tickets in the response.
  - **unlinked_only** (boolean): Returns only unlinked tickets in the response.
  - **contract_id** (number): Filters by the specified contract.
  - **withattachments** (boolean): Returns only tickets with 1 or more attachment.
  - **team** (array): Returns tickets based on Team ID's in the array.
  - **agent** (array): Returns tickets based on Agent ID's in the array.
  - **status** (array): Returns tickets based on status ID's in the array.
  - **requesttype** (array): Returns tickets based on request type ID's in the array.
  - **itil_requesttype** (array): Returns tickets based on ITIL request type ID's in the array.
  - **category_1** (array): Returns tickets based on category 1 ID's in the array.
  - **category_2** (array): Returns tickets based on category 2 ID's in the array.
  - **category_3** (array): Returns tickets based on category 3 ID's in the array.
  - **category_4** (array): Returns tickets based on category 4 ID's in the array.
  - **sla** (array): Returns tickets based on SLA ID's in the array.
  - **priority** (array): Returns tickets based on priority ID's in the array.
  - **products** (array): Returns tickets based on product ID's in the array.
  - **flagged** (array): Returns tickets based on flagged ticket ID's in the array.
  - **excludethese** (array): Excludes these tickets from the response.
  - **search** (string): Filters response based on the search string.
  - **searchactions** (boolean): Whether to search actions when using search.
  - **datesearch** (string): The date field to search against. Examples are Date Opened - 'dateoccured', Date Closed - 'datecleared'.
  - **startdate** (string): For use with the datesearch parameter.
  - **enddate** (string): For use with the datesearch parameter.
  - **search_user_name** (string): Returns tickets based on users matching the search.
  - **search_summary** (string): Returns tickets based on the summary matching the search.
  - **search_details** (string): Returns tickets based on the details matching the search.
  - **search_reportedby** (string): Returns tickets based on the reportedby field matching the search.
  - **search_version** (string): Returns tickets based on the software version matching the search.
  - **search_release1** (string): Returns tickets based on release 1 matching the search.
  - **search_release2** (string): Returns tickets based on release 2 matching the search
  - **search_release3** (string): Returns tickets based on release 3 matching the search
  - **search_releasenote** (string): Returns tickets based on the release note matching the search.
  - **search_inventory_number** (string): Returns tickets based on an asset tag matching the search.
  - **search_oppcontactname** (string): Returns tickets based on the opportunity contact name matching the search.
  - **search_oppcompanyname** (string): Returns tickets based on the opportunity company name matching the search.
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
      "page_no": 0,
      "page_size": 0,
      "record_count": 0,
      "tickets": [
        {
          "id": 0,
          "dateoccurred": "2017-11-01T16:03:32.714Z",
          "summary": "",
          "status_id": 0,
          "tickettype_id": 0,
          "sla_id": 0,
          "priority_id": 0,
          "client_id": 0,
          "client_name": "",
          "site_id": 0,
          "site_name": "",
          "user_name": "",
          "team": "",
          "agent_id": 0,
          "agent_name": "",
          "category_1": "",
          "category_2": "",
          "category_3": "",
          "category_4": "",
          "estimate": 0,
          "timetaken": 0,
          "parent_id": 0,
          "flagged": true,
          "read": true,
          "enduserstatus": 0,
          "onhold": true,
          "respondbydate": "2017-11-01T16:03:32.714Z",
          "slaresponsestate": "",
          "fixbydate": "2017-11-01T16:03:32.714Z",
          "dateclosed": "2017-11-01T16:03:32.714Z",
          "excludefromsla": true,
          "slaholdtime": 0,
          "site_timezone": "",
          "slaactiondate": "2017-11-01T16:03:32.714Z",
          "slapercused": 0,
          "slatimeleft": 0,
          "responsedate": "2017-11-01T16:03:32.714Z"
        }
      ],
      "columns_id": 0,
      "columns": [
        {
          "id": 0,
          "columns_id": 0,
          "column_seq": 0,
          "column_name": "",
          "width": 0,
          "order_seq": 0,
          "order_desc": true
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **page_no** (number)
  - **page_size** (number)
  - **record_count** (number)
  - **tickets** (array)
    - **id** (number)
    - **dateoccurred** (string)
    - **summary** (string)
    - **status_id** (number)
    - **tickettype_id** (number)
    - **sla_id** (number)
    - **priority_id** (number)
    - **client_id** (number)
    - **client_name** (string)
    - **site_id** (number)
    - **site_name** (string)
    - **user_name** (string)
    - **team** (string)
    - **agent_id** (number)
    - **agent_name** (string)
    - **category_1** (string)
    - **category_2** (string)
    - **category_3** (string)
    - **category_4** (string)
    - **estimate** (number)
    - **timetaken** (number)
    - **parent_id** (number)
    - **flagged** (boolean)
    - **read** (boolean)
    - **enduserstatus** (number)
    - **onhold** (boolean)
    - **respondbydate** (string)
    - **slaresponsestate** (string)
    - **fixbydate** (string)
    - **dateclosed** (string)
    - **excludefromsla** (boolean)
    - **slaholdtime** (number)
    - **site_timezone** (string)
    - **slaactiondate** (string)
    - **slapercused** (number)
    - **slatimeleft** (number)
    - **responsedate** (string)
  - **columns_id** (number)
  - **columns** (array)
    - **id** (number)
    - **columns_id** (number)
    - **column_seq** (number)
    - **column_name** (string)
    - **width** (number)
    - **order_seq** (number)
    - **order_desc** (boolean)
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