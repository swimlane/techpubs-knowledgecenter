# Add Comment

**Description**: Adds a comment to a Jira issue identified by issueIdOrKey with the specified text content in the body.

## Endpoint

- **URL:** `/rest/api/3/issue/{{issueIdOrKey}}/comment`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **issueIdOrKey** (string) – Required
- **json_body** (object) – Required
  - **visibility** (object)
    - **identifier** (string)
    - **type** (string)
    - **value** (string)
  - **body** (object) – Required
    - **type** (string)
    - **version** (number)
    - **content** (array) – Required
      - **type** (string)
      - **content** (array)
        - **type** (string)
        - **text** (string)
        - **marks** (array)
          - **type** (string)
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **self** (string)
  - **id** (string)
  - **author** (object)
    - **self** (string)
    - **accountId** (string)
    - **emailAddress** (string)
    - **avatarUrls** (object)
      - **48x48** (string)
      - **24x24** (string)
      - **16x16** (string)
      - **32x32** (string)
    - **displayName** (string)
    - **active** (boolean)
    - **timeZone** (string)
    - **accountType** (string)
  - **body** (object)
    - **type** (string)
    - **version** (number)
    - **content** (array)
      - **type** (string)
      - **content** (array)
        - **type** (string)
        - **text** (string)
  - **updateAuthor** (object)
    - **self** (string)
    - **accountId** (string)
    - **emailAddress** (string)
    - **avatarUrls** (object)
      - **48x48** (string)
      - **24x24** (string)
      - **16x16** (string)
      - **32x32** (string)
    - **displayName** (string)
    - **active** (boolean)
    - **timeZone** (string)
    - **accountType** (string)
  - **created** (string)
  - **updated** (string)
  - **jsdPublic** (boolean)
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
| Location | string |
| Cache-Control | string |
| Vary | string |
| Expect-Ct | string |
| Strict-Transport-Security | string |
| X-Content-Type-Options | string |
| X-Xss-Protection | string |
| Atl-Traceid | string |
| Report-To | string |
| Nel | string |
| Transfer-Encoding | string |