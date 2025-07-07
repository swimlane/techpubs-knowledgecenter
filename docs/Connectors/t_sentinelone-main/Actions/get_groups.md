# Get Groups

**Description**: Retrieve details of SentinelOne groups based on specified filter criteria.

## Endpoint

- **URL:** `/web/api/v2.1/groups`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **accountids** (string): List of Account IDs to filter by.
  - **countonly** (boolean): If true, only total number of items will be returned, without any of the actual objects.
  - **cursor** (string): Cursor position returned by the last request. Use to iterate over more than 1000 items.
  - **description** (string): The description for the Group.
  - **groupids** (string): List of Group IDs to filter by.
  - **id** (string): ID.
  - **isdefault** (boolean): If true, default group is set.
  - **limit** (string): Limit number of returned items (1-300).
  - **name** (string): Name.
  - **query** (string): Free text search on fields name, description.
  - **rank** (string): The rank sets the priority of a dynamic group over others.
  - **registrationtoken** (string): Registration token.
  - **siteids** (string): List of Site IDs to filter by.
  - **skip** (string): Skip first number of items (0-1000). To iterate over more than 1000 items, use "cursor".
  - **skipcount** (boolean): If true, total number of items will not be calculated, which speeds up execution time.
  - **sortby** (string): The column to sort the results by.
  - **sortorder** (string): Sort direction.
  - **type** (string): Group type.
  - **types** (string): A list of Group types.
  - **updatedat__gt** (string): Updated at greater than.
  - **updatedat__gte** (string): Updated at greater or equal than.
  - **updatedat__lt** (string): Updated at lesser than.
  - **updatedat__lte** (string): Updated at lesser or equal than.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Tue, 11 Jun 2024 11:26:21 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "112653fa-4329-4f71-a7a6-5dc163b97fd2",
      "Access-Control-Allow-Origin": "https://cns.na1.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' *.sentinelone.net cdn.pendo.io app.pendo.io *.pendo.io data.pendo.io *.scalyr.com *.storage.googleapis.com sentry.io *.sentry.io *.google-analytics.com *.gstatic.com unpkg.com cdn.auth0.com wss://*.sentinelone.net https://www.googletagmanager.com https://cdnjs.cloudflare.com https://dm64t97qsxvuz.cloudfront.net data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' blob: *.sentinelone.net cdn.pendo.io app.pendo.io pendo-io-static.storage.googleapis.com *.storage.googleapis.com data.pendo.io https://www.google-analytics.com https://www.googletagmanager.com https://unpkg.com https://cdnjs.cloudflare.com https://dm64t97qsxvuz.cloudfront.net ; img-src 'self' blob: *.sentinelone.net *.sentinelone.com dm64t97qsxvuz.cloudfront.net data: https://www.google-analytics.com cdn.pendo.io app.pendo.io *.storage.googleapis.com data.pendo.io ; style-src 'self' 'unsafe-inline' *.sentinelone.net app.pendo.io cdn.pendo.io *.storage.googleapis.com https://cdnjs.cloudflare.com https://dm64t97qsxvuz.cloudfront.net ; font-src 'self' data: *.sentinelone.net https://cdn.auth0.com https://dm64t97qsxvuz.cloudfront.net ; manifest-src 'self' https://dm64t97qsxvuz.cloudfront.net ; frame-src 'self' blob: https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://*.youtube.com *.sentinelone.net *.scalyr.com; frame-ancestors 'self' app.pendo.io *.sentinelone.net; object-src 'none' ; worker-src 'self' blob: ;",
      "Cache-Control": "no-store",
      "Pragma": "no-cache",
      "Expires": "-1",
      "Content-Encoding": "gzip"
    },
    "reason": "OK",
    "json_body": {
      "data": [
        {
          "createdAt": "2021-11-10T21:37:36.554715Z",
          "creator": "Sandeep Minhas",
          "creatorId": "1170348439571106212",
          "filterId": null,
          "filterName": null,
          "id": "1286405255265411734",
          "inherits": true,
          "isDefault": true,
          "name": "Default Group",
          "rank": null,
          "registrationToken": "eyJ1cmwiOiAiaHR0cHM6Ly91c2VhMS1wYXJ0bmVycy5zZW50aW5lbG9uZS5uZXQiLCAic2l0ZV9rZXkiOiAiZ19hN2M1ODJlNTViMzE2NmE5In0=",
          "siteId": "1286405255257023125",
          "totalAgents": 2,
          "type": "static",
          "updatedAt": "2021-11-10T21:37:37.094755Z"
        },
        {
          "createdAt": "2023-08-24T21:24:49.806822Z",
          "creator": "Travis Riley",
          "creatorId": "1286405906565325677",
          "filterId": null,
          "filterName": null,
          "id": "1758952600065820586",
          "inherits": true,
          "isDefault": true,
          "name": "Default Group",
          "rank": null,
          "registrationToken": "eyJ1cmwiOiAiaHR0cHM6Ly91c2VhMS1wYXJ0bmVycy5zZW50aW5lbG9uZS5uZXQiLCAic2l0ZV9rZXkiOiAiZ18zMDY4NWRkZGNjOTlmZmY2In0=",
          "siteId": "1758952600032266153",
          "totalAgents": 0,
          "type": "static",
          "updatedAt": "2023-08-24T21:24:50.592583Z"
        },
        {
          "createdAt": "2023-08-24T21:26:37.251651Z",
          "creator": "Travis Riley",
          "creatorId": "1286405906565325677",
          "filterId": null,
          "filterName": null,
          "id": "1758953501371423302",
          "inherits": true,
          "isDefault": true,
          "name": "Default Group",
          "rank": null,
          "registrationToken": "eyJ1cmwiOiAiaHR0cHM6Ly91c2VhMS1wYXJ0bmVycy5zZW50aW5lbG9uZS5uZXQiLCAic2l0ZV9rZXkiOiAiZ18wMGM5MzNhZTNjNDFkNGIwIn0=",
          "siteId": "1758953501354646085",
          "totalAgents": 0,
          "type": "static",
          "updatedAt": "2023-08-24T21:26:37.992107Z"
        }
      ],
      "pagination": {
        "nextCursor": null,
        "totalItems": 3
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (array)
    - **createdAt** (string)
    - **creator** (string)
    - **creatorId** (string)
    - **filterId** (object)
    - **filterName** (object)
    - **id** (string)
    - **inherits** (boolean)
    - **isDefault** (boolean)
    - **name** (string)
    - **rank** (object)
    - **registrationToken** (string)
    - **siteId** (string)
    - **totalAgents** (number)
    - **type** (string)
    - **updatedAt** (string)
  - **pagination** (object)
    - **nextCursor** (object)
    - **totalItems** (number)
## Response Headers

| Header | Type |
|--------|------|
| Server | string |
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| X-RQID | string |
| Access-Control-Allow-Origin | string |
| Access-Control-Allow-Credentials | string |
| Vary | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| X-Content-Type-Options | string |
| Content-Security-Policy | string |
| Cache-Control | string |
| Pragma | string |
| Expires | string |
| Content-Encoding | string |