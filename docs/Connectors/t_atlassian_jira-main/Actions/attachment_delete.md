# Delete Attachment

**Description**: Removes a specified attachment from a Jira issue using the unique attachment ID provided in path parameters.

## Endpoint

- **URL:** `/rest/api/3/attachment/{{id}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
- **headers** (object) – Required
  - **X-Atlassian-Token** (string) – Required
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (string)
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
| Expect-Ct | string |
| Strict-Transport-Security | string |
| X-Content-Type-Options | string |
| X-Xss-Protection | string |
| Atl-Traceid | string |
| Report-To | string |
| Nel | string |