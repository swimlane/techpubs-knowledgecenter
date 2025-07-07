# Conversations List

**Description**: Retrieves all channels within a Slack team to provide an overview of available conversation spaces.

## Endpoint

- **URL:** `api/conversations.list`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **limit** (number)
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **ok** (boolean)
  - **channels** (array)
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
    - **num_members** (number)
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