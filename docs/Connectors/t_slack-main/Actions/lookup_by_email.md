# Lookup by Email

**Description**: Retrieves Slack user details by email, using the 'email' parameter to identify the user.

## Endpoint

- **URL:** `/api/users.lookupByEmail`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required
  - **email** (string) – Required
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **ok** (boolean)
  - **user** (object)
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
      - **email** (string)
      - **huddle_state** (string)
      - **huddle_state_expiration_ts** (number)
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
| x-accepted-oauth-scopes | string |
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