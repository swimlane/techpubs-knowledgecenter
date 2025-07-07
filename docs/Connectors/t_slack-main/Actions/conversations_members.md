# Conversations Members

**Description**: Retrieves a list of all members within a specified Slack channel, requiring the 'channel' parameter for execution.

## Endpoint

- **URL:** `api/conversations.members`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required
  - **channel** (string) – Required
  - **limit** (number)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "date": "Fri, 16 Dec 2022 14:07:50 GMT",
      "server": "Apache",
      "x-powered-by": "HHVM/4.153.1",
      "access-control-allow-origin": "*",
      "referrer-policy": "no-referrer",
      "x-slack-backend": "r",
      "x-slack-unique-id": "Y5x7tuDJgIq_ncq0sDiaPQAAECw",
      "strict-transport-security": "max-age=31536000; includeSubDomains; preload",
      "access-control-allow-headers": "slack-route, x-slack-version-ts, x-b3-traceid, x-b3-spanid, x-b3-parentspanid, x-b3-sampled, x-b3-flags",
      "access-control-expose-headers": "x-slack-req-id, retry-after",
      "x-oauth-scopes": "app_mentions:read,channels:history,channels:join,channels:manage,channels:read,chat:write.customize,chat:write.public,chat:write,files:read,files:write,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,links:write,mpim:history,mpim:read,mpim:write,pins:read,pins:write,reactions:read,reactions:write,reminders:read,reminders:write,team:read,usergroups:read,usergroups:write,users:read,users:write,users.profile:read",
      "x-accepted-oauth-scopes": "channels:read,groups:read,mpim:read,im:read,read",
      "expires": "Mon, 26 Jul 1997 05:00:00 GMT",
      "cache-control": "private, no-cache, no-store, must-revalidate",
      "pragma": "no-cache",
      "x-xss-protection": "0",
      "x-content-type-options": "nosniff",
      "x-slack-req-id": "4eb734cd833fa4dd77d346955ffb9fbd",
      "vary": "Accept-Encoding",
      "content-encoding": "gzip",
      "content-length": "130",
      "content-type": "application/json; charset=utf-8",
      "x-envoy-upstream-service-time": "142",
      "x-backend": "main_normal main_bedrock_normal_with_overflow main_canary_with_overflow main_bedrock_canary_with_overflow main_control_with_overflow main_bedrock_control_with_overflow",
      "x-server": "slack-www-hhvm-main-iad-ngow",
      "x-slack-shared-secret-outcome": "no-match",
      "via": "envoy-www-iad-r9kw, envoy-edge-gru-46m1",
      "x-edge-backend": "envoy-www",
      "x-slack-edge-shared-secret-outcome": "no-match"
    },
    "reason": "OK",
    "json_body": {
      "ok": true,
      "members": [
        "U0E7MM1MK",
        "U0E7RF35G"
      ],
      "response_metadata": {
        "next_cursor": "dXNlcl9pZDoxNDI2MzUxMzE4Ng=="
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **ok** (boolean)
  - **members** (array)
  - **response_metadata** (object)
    - **next_cursor** (string)
## Response Headers

| Header | Type |
|--------|------|
| date | string |
| server | string |
| x-powered-by | string |
| access-control-allow-origin | string |
| referrer-policy | string |
| x-slack-backend | string |
| x-slack-unique-id | string |
| strict-transport-security | string |
| access-control-allow-headers | string |
| access-control-expose-headers | string |
| x-oauth-scopes | string |
| x-accepted-oauth-scopes | string |
| expires | string |
| cache-control | string |
| pragma | string |
| x-xss-protection | string |
| x-content-type-options | string |
| x-slack-req-id | string |
| vary | string |
| content-encoding | string |
| content-length | string |
| content-type | string |
| x-envoy-upstream-service-time | string |
| x-backend | string |
| x-server | string |
| x-slack-shared-secret-outcome | string |
| via | string |
| x-edge-backend | string |
| x-slack-edge-shared-secret-outcome | string |