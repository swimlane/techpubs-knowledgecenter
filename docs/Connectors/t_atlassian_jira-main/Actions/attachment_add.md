# Add Attachment

**Description**: Adds an attachment to a specified Jira issue using the issueIdOrKey, including necessary path parameters and headers.

## Endpoint

- **URL:** `/rest/api/3/issue/{{issueIdOrKey}}/attachments`
- **Method:** `POST`
## Inputs

- **attachments** (array) – Required: Attachment to add
  - **file** (string)
  - **file_name** (string)
- **path_parameters** (object) – Required
  - **issueIdOrKey** (string) – Required
- **headers** (object) – Required
  - **X-Atlassian-Token** (string) – Required
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (array)
  - **self** (string)
  - **id** (string)
  - **filename** (string)
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
  - **created** (string)
  - **size** (number)
  - **content** (string)
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
| Expect-Ct | string |
| Strict-Transport-Security | string |
| X-Content-Type-Options | string |
| X-Xss-Protection | string |
| Atl-Traceid | string |
| Report-To | string |
| Nel | string |
| Transfer-Encoding | string |