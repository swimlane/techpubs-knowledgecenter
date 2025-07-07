# Get All Users Default

**Description**: Retrieves a comprehensive list of all users within Atlassian Jira, encompassing active, inactive, and deleted accounts.

## Endpoint

- **URL:** `/rest/api/3/users`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **startAt** (number): The index of the first item to return.
  - **maxResults** (number): The maximum number of items to return.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 09 Jan 2025 10:07:44 GMT",
      "Content-Type": "application/json;charset=UTF-8",
      "Server": "AtlassianEdge",
      "Timing-Allow-Origin": "*",
      "X-Arequestid": "45c9fb52879c4b3eb540cd8c9fb94205",
      "Set-Cookie": "atlassian.xsrf.token=5b8d9da0169a025c9f394f0e4434c12aa4e646d5_lin; Path=/; SameSite=None; Secure",
      "X-Aaccountid": "5d07f57ceec00a0bcb5eca63",
      "Cache-Control": "no-cache, no-store, no-transform",
      "Vary": "Accept-Encoding",
      "Content-Encoding": "gzip",
      "X-Content-Type-Options": "nosniff",
      "X-Xss-Protection": "1; mode=block",
      "Atl-Traceid": "d99ae7c156c84ec3be9436847ece934f",
      "Atl-Request-Id": "d99ae7c1-56c8-4ec3-be94-36847ece934f",
      "Strict-Transport-Security": "max-age=63072000; includeSubDomains; preload",
      "Report-To": "{\"endpoints\": [{\"url\": \"https://dz8aopenkvv6s.cloudfront.net\"}], \"group\": \"endpoint-1\", \"include_subdomains\": true, \"max_age\": 600}",
      "Nel": "{\"failure_fraction\": 0.001, \"include_subdomains\": true, \"max_age\": 600, \"report_to\": \"endpoint-1\"}",
      "Server-Timing": "atl-edge;dur=340,atl-edge-internal;dur=14,atl-edge-upstream;dur=328,atl-edge-pop;desc=\"aws-ap-south-1\"",
      "Transfer-Encoding": "chunked"
    },
    "reason": "OK",
    "json_body": [
      {
        "self": "https://swimlane.atlassian.net/rest/api/3/user?accountId=557058:545e539f-d725-4df9-623b3176d634",
        "accountId": "557058:545e539f-d725-4df9-623b3176d634",
        "accountType": "atlassian",
        "avatarUrls": {
          "48x48": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/default-avatar.png",
          "24x24": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/default-avatar.png",
          "16x16": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/default-avatar.png",
          "32x32": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/default-avatar.png"
        },
        "displayName": "Former user",
        "active": false
      },
      {
        "self": "https://swimlane.atlassian.net/rest/api/3/user?accountId=557058:9564a115-86ee-a8ce-9d3a14b125d1",
        "accountId": "557058:9564a115-86ee-a8ce-9d3a14b125d1",
        "accountType": "atlassian",
        "avatarUrls": {
          "48x48": "https://secure.gravatar.com/avatar/60e126c66b33d270979329ff9efb27e8?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FAK-3.png",
          "24x24": "https://secure.gravatar.com/avatar/60e126c66b33d270979329ff9efb27e8?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FAK-3.png",
          "16x16": "https://secure.gravatar.com/avatar/60e126c66b33d270979329ff9efb27e8?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FAK-3.png",
          "32x32": "https://secure.gravatar.com/avatar/60e126c66b33d270979329ff9efb27e8?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FAK-3.png"
        },
        "displayName": "Test User",
        "active": false
      }
    ]
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (array)
  - **self** (string)
  - **accountId** (string)
  - **accountType** (string)
  - **avatarUrls** (object)
    - **48x48** (string)
    - **24x24** (string)
    - **16x16** (string)
    - **32x32** (string)
  - **displayName** (string)
  - **active** (boolean)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Server | string |
| Timing-Allow-Origin | string |
| X-Arequestid | string |
| Set-Cookie | string |
| X-Aaccountid | string |
| Cache-Control | string |
| Vary | string |
| Content-Encoding | string |
| X-Content-Type-Options | string |
| X-Xss-Protection | string |
| Atl-Traceid | string |
| Atl-Request-Id | string |
| Strict-Transport-Security | string |
| Report-To | string |
| Nel | string |
| Server-Timing | string |
| Transfer-Encoding | string |