# Get User

**Description**: Retrieves a specific user's details from Atlassian Jira using the accountId, respecting user privacy settings.

## Endpoint

- **URL:** `/rest/api/3/user`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required
  - **accountId** (string) – Required: The account ID of the user, which uniquely identifies the user across all Atlassian products. Max length is 128.
  - **expand** (string): Use expand to include additional information about users in the response.  This parameter accepts a comma-separated list. Expand options include: groups includes all groups and nested groups to which the user belongs. applicationRoles includes details of all the applications to which the user has access.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 09 Jan 2025 09:22:15 GMT",
      "Content-Type": "application/json;charset=UTF-8",
      "Server": "AtlassianEdge",
      "Timing-Allow-Origin": "*",
      "X-Arequestid": "3755c266a371a3de6f4ac4e217c9c2cf",
      "Set-Cookie": "atlassian.xsrf.token=180eb947a40a03f89fc1aa377d3d0be76190e334_lin; Path=/; SameSite=None; Secure",
      "X-Aaccountid": "5d07f57ceec00a0bcb5eca63",
      "Cache-Control": "no-cache, no-store, no-transform",
      "Vary": "Accept-Encoding",
      "Content-Encoding": "gzip",
      "X-Content-Type-Options": "nosniff",
      "X-Xss-Protection": "1; mode=block",
      "Atl-Traceid": "13d28234934c4319902f54f1c38e5fff",
      "Atl-Request-Id": "13d28234-934c-4319-902f-54f1c38e5fff",
      "Strict-Transport-Security": "max-age=63072000; includeSubDomains; preload",
      "Report-To": "{\"endpoints\": [{\"url\": \"https://dz8aopenkvv6s.cloudfront.net\"}], \"group\": \"endpoint-1\", \"include_subdomains\": true, \"max_age\": 600}",
      "Nel": "{\"failure_fraction\": 0.001, \"include_subdomains\": true, \"max_age\": 600, \"report_to\": \"endpoint-1\"}",
      "Server-Timing": "atl-edge;dur=348,atl-edge-internal;dur=15,atl-edge-upstream;dur=335,atl-edge-pop;desc=\"aws-ap-south-1\"",
      "Transfer-Encoding": "chunked"
    },
    "reason": "OK",
    "json_body": {
      "self": "https://swimlane.atlassian.net/rest/api/3/user?accountId=5d07f57ceec00a0bcb5eca63",
      "accountId": "5d07f57ceec00a0bcb5eca63",
      "accountType": "atlassian",
      "emailAddress": "integrations@swimlane.com",
      "avatarUrls": {
        "48x48": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5d07f57ceec00a0bcb5eca63/b2f62753-cd5f-4178-a52f-25e838a67035/48",
        "24x24": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5d07f57ceec00a0bcb5eca63/b2f62753-cd5f-4178-a52f-25e838a67035/24",
        "16x16": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5d07f57ceec00a0bcb5eca63/b2f62753-cd5f-4178-a52f-25e838a67035/16",
        "32x32": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5d07f57ceec00a0bcb5eca63/b2f62753-cd5f-4178-a52f-25e838a67035/32"
      },
      "displayName": "Swimlane Integrations",
      "active": true,
      "timeZone": "America/Denver",
      "locale": "en_US",
      "groups": {
        "size": 4,
        "items": []
      },
      "applicationRoles": {
        "size": 1,
        "items": []
      },
      "expand": "groups,applicationRoles"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **self** (string)
  - **accountId** (string)
  - **accountType** (string)
  - **emailAddress** (string)
  - **avatarUrls** (object)
    - **48x48** (string)
    - **24x24** (string)
    - **16x16** (string)
    - **32x32** (string)
  - **displayName** (string)
  - **active** (boolean)
  - **timeZone** (string)
  - **locale** (string)
  - **groups** (object)
    - **size** (number)
    - **items** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
  - **applicationRoles** (object)
    - **size** (number)
    - **items** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
  - **expand** (string)
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