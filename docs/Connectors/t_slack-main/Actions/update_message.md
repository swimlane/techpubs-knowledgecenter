# Update Message

**Description**: Updates an existing message in a specified Slack channel using the channel ID and message timestamp.

## Endpoint

- **Method:** `POST`
## Inputs

- **channel** (string) – Required
- **message_timestamp** (string) – Required
- **title** (string)
- **reply_broadcast** (string)
- **username** (string)
- **parse** (string)
- **link_names** (string)
- **text** (string)
- **unfurl_links** (string)
- **unfurl_media** (string)
- **icon_url** (string)
- **icon_emoji** (string)
- **blocks** (array)
  - **type** (string)
  - **text** (object)
    - **type** (string)
    - **text** (string)
  - **fields** (array)
    - **type** (string)
    - **text** (string)
## Output

### Output Parameters

- **headers** (object)
- **reason** (string)
- **status_code** (number)
- **channel** (string)
- **ts** (string)
- **message** (object)
  - **bot_id** (string)
  - **type** (string)
  - **text** (string)
  - **user** (string)
  - **app_id** (string)
  - **blocks** (array)
    - **type** (string)
    - **block_id** (string)
    - **text** (object)
      - **type** (string)
      - **text** (string)
      - **verbatim** (boolean)
    - **fields** (array)
      - **type** (string)
      - **text** (string)
      - **verbatim** (boolean)
  - **team** (string)
  - **bot_profile** (object)
    - **id** (string)
    - **app_id** (string)
    - **name** (string)
    - **icons** (object)
      - **image_36** (string)
      - **image_48** (string)
      - **image_72** (string)
    - **deleted** (boolean)
    - **updated** (number)
    - **team_id** (string)
  - **edited** (object)
    - **user** (string)
    - **ts** (string)