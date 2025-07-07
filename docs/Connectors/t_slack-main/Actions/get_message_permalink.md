# Get Message Permalink

**Description**: Retrieve a permalink URL for a Slack message using the channel ID and message timestamp.

## Endpoint

- **URL:** `api/chat.getPermalink`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required
  - **channel** (string) – Required: The ID of the conversation or channel containing the message.
  - **message_ts** (string) – Required: A Message's TS value, uniquely identifying it within a channel.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "date": "Wed, 16 Oct 2024 10:52:06 GMT",
      "server": "Apache",
      "vary": "Accept-Encoding",
      "x-slack-req-id": "13dabbfa12beeaefe788b03b2f6ace65",
      "x-content-type-options": "nosniff",
      "x-xss-protection": "0",
      "pragma": "no-cache",
      "cache-control": "private, no-cache, no-store, must-revalidate",
      "expires": "Sat, 26 Jul 1997 05:00:00 GMT",
      "content-type": "application/json; charset=utf-8",
      "x-oauth-scopes": "chat:write,channels:history,channels:join,channels:manage,channels:read,chat:write.customize,groups:write,groups:history,groups:read,groups:write.invites,im:history,mpim:history,im:read,mpim:read,users:read,users:read.email,im:write,mpim:write,channels:write.invites",
      "access-control-expose-headers": "x-slack-req-id, retry-after",
      "access-control-allow-headers": "slack-route, x-slack-version-ts, x-b3-traceid, x-b3-spanid, x-b3-parentspanid, x-b3-sampled, x-b3-flags",
      "strict-transport-security": "max-age=31536000; includeSubDomains; preload",
      "referrer-policy": "no-referrer",
      "x-slack-unique-id": "Zw-a1qlgB2l9h_MWjXCEgQAAEDQ",
      "x-slack-backend": "r",
      "access-control-allow-origin": "*",
      "via": "1.1 slack-prod.tinyspeck.com, envoy-www-iad-ytlcjyak,envoy-edge-bom-fhhusbjo",
      "content-encoding": "gzip",
      "content-length": "127",
      "x-envoy-attempt-count": "1",
      "x-envoy-upstream-service-time": "205",
      "x-backend": "main_normal main_canary_with_overflow main_control_with_overflow",
      "x-server": "slack-www-hhvm-main-iad-hsyo",
      "x-slack-shared-secret-outcome": "no-match",
      "x-edge-backend": "envoy-www",
      "x-slack-edge-shared-secret-outcome": "no-match"
    },
    "reason": "OK",
    "json_body": {
      "ok": true,
      "permalink": "https://swimlane.slack.com/archives/C1234567890/p1729074892900389",
      "channel": "C1234567890"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **ok** (boolean)
  - **permalink** (string)
  - **channel** (string)
## Response Headers

| Header | Type |
|--------|------|
| date | string |
| server | string |
| vary | string |
| x-slack-req-id | string |
| x-content-type-options | string |
| x-xss-protection | string |
| pragma | string |
| cache-control | string |
| expires | string |
| content-type | string |
| x-oauth-scopes | string |
| access-control-expose-headers | string |
| access-control-allow-headers | string |
| strict-transport-security | string |
| referrer-policy | string |
| x-slack-unique-id | string |
| x-slack-backend | string |
| access-control-allow-origin | string |
| via | string |
| content-encoding | string |
| content-length | string |
| x-envoy-attempt-count | string |
| x-envoy-upstream-service-time | string |
| x-backend | string |
| x-server | string |
| x-slack-shared-secret-outcome | string |
| x-edge-backend | string |
| x-slack-edge-shared-secret-outcome | string |