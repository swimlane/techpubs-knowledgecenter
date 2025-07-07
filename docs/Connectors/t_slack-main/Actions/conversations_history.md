# Conversations History

**Description**: Retrieves message and event history for a specified Slack channel using its unique identifier.

## Endpoint

- **URL:** `api/conversations.history`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required
  - **channel** (string) – Required
  - **include_all_metadata** (boolean)
  - **inclusive** (boolean)
  - **limit** (number)
  - **cursor** (string)
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **ok** (boolean)
  - **messages** (array)
    - **type** (string)
    - **user** (string)
    - **text** (string)
    - **ts** (string)
    - **attachments** (array)
      - **service_name** (string)
      - **text** (string)
      - **fallback** (string)
      - **thumb_url** (string)
      - **thumb_width** (number)
      - **thumb_height** (number)
      - **id** (number)
  - **has_more** (boolean)
  - **pin_count** (number)
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