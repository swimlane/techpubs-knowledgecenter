# Users List

**Description**: Retrieves a comprehensive list of users within a Slack team, providing insights into current team membership.

## Endpoint

- **URL:** `api/users.list`
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
  - **offset** (string)
  - **members** (array)
    - **id** (string)
    - **team_id** (string)
    - **name** (string)
    - **deleted** (boolean)
    - **color** (string)
    - **real_name** (string)
    - **tz** (string)
    - **tz_label** (string)
    - **tz_offset** (number)
    - **profile** (object)
      - **title** (string)
      - **phone** (string)
      - **skype** (string)
      - **real_name** (string)
      - **real_name_normalized** (string)
      - **display_name** (string)
      - **display_name_normalized** (string)
      - **fields** (object)
      - **status_text** (string)
      - **status_emoji** (string)
      - **status_emoji_display_info** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **status_expiration** (number)
      - **avatar_hash** (string)
      - **image_original** (string)
      - **is_custom_image** (boolean)
      - **first_name** (string)
      - **last_name** (string)
      - **image_24** (string)
      - **image_32** (string)
      - **image_48** (string)
      - **image_72** (string)
      - **image_192** (string)
      - **image_512** (string)
      - **image_1024** (string)
      - **status_text_canonical** (string)
      - **team** (string)
    - **is_admin** (boolean)
    - **is_owner** (boolean)
    - **is_primary_owner** (boolean)
    - **is_restricted** (boolean)
    - **is_ultra_restricted** (boolean)
    - **is_bot** (boolean)
    - **is_app_user** (boolean)
    - **updated** (number)
    - **is_email_confirmed** (boolean)
    - **who_can_share_contact_card** (string)
  - **cache_ts** (number)
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