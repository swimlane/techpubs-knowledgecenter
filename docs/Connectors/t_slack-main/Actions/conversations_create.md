# Conversations Create

**Description**: Initiates a new public or private channel-based conversation in Slack with the provided name.

## Endpoint

- **URL:** `api/conversations.create`
- **Method:** `POST`
## Inputs

- **parameters** (object) – Required
  - **name** (string) – Required
  - **is_private** (boolean)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "date": "Fri, 16 Dec 2022 14:33:36 GMT",
      "server": "Apache",
      "x-powered-by": "HHVM/4.153.1",
      "access-control-allow-origin": "*",
      "referrer-policy": "no-referrer",
      "x-slack-backend": "r",
      "x-slack-unique-id": "Y5yBwKgib4832auTRSYC9gAAAC4",
      "strict-transport-security": "max-age=31536000; includeSubDomains; preload",
      "access-control-allow-headers": "slack-route, x-slack-version-ts, x-b3-traceid, x-b3-spanid, x-b3-parentspanid, x-b3-sampled, x-b3-flags",
      "access-control-expose-headers": "x-slack-req-id, retry-after",
      "x-oauth-scopes": "app_mentions:read,channels:history,channels:join,channels:manage,channels:read,chat:write.customize,chat:write.public,chat:write,files:read,files:write,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,links:write,mpim:history,mpim:read,mpim:write,pins:read,pins:write,reactions:read,reactions:write,reminders:read,reminders:write,team:read,usergroups:read,usergroups:write,users:read,users:write,users.profile:read",
      "x-accepted-oauth-scopes": "channels:write,groups:write,mpim:write,im:write,post",
      "expires": "Mon, 26 Jul 1997 05:00:00 GMT",
      "cache-control": "private, no-cache, no-store, must-revalidate",
      "pragma": "no-cache",
      "x-xss-protection": "0",
      "x-content-type-options": "nosniff",
      "x-slack-req-id": "4b8e72501927109ea109f3d47d2dfee2",
      "vary": "Accept-Encoding",
      "content-encoding": "gzip",
      "content-length": "350",
      "content-type": "application/json; charset=utf-8",
      "x-envoy-upstream-service-time": "402",
      "x-backend": "main_normal main_bedrock_normal_with_overflow main_canary_with_overflow main_bedrock_canary_with_overflow main_control_with_overflow main_bedrock_control_with_overflow",
      "x-server": "slack-www-hhvm-main-iad-yioh",
      "x-slack-shared-secret-outcome": "no-match",
      "via": "envoy-www-iad-9hxq, envoy-edge-gru-mji1",
      "x-edge-backend": "envoy-www",
      "x-slack-edge-shared-secret-outcome": "no-match"
    },
    "reason": "OK",
    "json_body": {
      "ok": true,
      "channel": {
        "id": "C04FH1ESM8D",
        "name": "test_channel2",
        "is_channel": true,
        "is_group": false,
        "is_im": false,
        "is_mpim": false,
        "is_private": false,
        "created": 1671201216,
        "is_archived": false,
        "is_general": false,
        "unlinked": 0,
        "name_normalized": "test_channel2",
        "is_shared": false,
        "is_org_shared": false,
        "is_pending_ext_shared": false,
        "pending_shared": [],
        "context_team_id": "T0E7QGG8G",
        "updated": 1671201216878,
        "parent_conversation": null,
        "creator": "U04E7SA0XH8",
        "is_ext_shared": false,
        "shared_team_ids": [
          "T0E7QGG8G"
        ],
        "pending_connected_team_ids": [],
        "is_member": true,
        "last_read": "0000000000.000000",
        "topic": {
          "value": "",
          "creator": "",
          "last_set": 0
        },
        "purpose": {
          "value": "",
          "creator": "",
          "last_set": 0
        },
        "previous_names": [],
        "priority": 0
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
  - **channel** (object)
    - **id** (string)
    - **name** (string)
    - **is_channel** (boolean)
    - **is_group** (boolean)
    - **is_im** (boolean)
    - **is_mpim** (boolean)
    - **is_private** (boolean)
    - **created** (number)
    - **is_archived** (boolean)
    - **is_general** (boolean)
    - **unlinked** (number)
    - **name_normalized** (string)
    - **is_shared** (boolean)
    - **is_org_shared** (boolean)
    - **is_pending_ext_shared** (boolean)
    - **pending_shared** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **context_team_id** (string)
    - **updated** (number)
    - **parent_conversation** (object)
    - **creator** (string)
    - **is_ext_shared** (boolean)
    - **shared_team_ids** (array)
    - **pending_connected_team_ids** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **is_member** (boolean)
    - **last_read** (string)
    - **topic** (object)
      - **value** (string)
      - **creator** (string)
      - **last_set** (number)
    - **purpose** (object)
      - **value** (string)
      - **creator** (string)
      - **last_set** (number)
    - **previous_names** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **priority** (number)
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