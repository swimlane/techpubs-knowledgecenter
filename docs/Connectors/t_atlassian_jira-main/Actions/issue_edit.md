# Edit Issue

**Description**: Modify an existing issue in Atlassian Jira using the specified issue ID or key.

## Endpoint

- **URL:** `/rest/api/3/issue/{{issueIdOrKey}}`
- **Method:** `PUT`
## Inputs

- **path_parameters** (object) – Required
  - **issueIdOrKey** (string) – Required
- **json_body** (object) – Required
  - **historyMetadata** (object)
    - **actor** (object)
      - **avatarUrl** (string)
      - **displayName** (string)
      - **id** (string)
      - **type** (string)
      - **url** (string)
    - **extraData** (object)
      - **Iteration** (string)
      - **Step** (string)
    - **description** (string)
    - **generator** (object)
      - **id** (string)
      - **type** (string)
    - **cause** (object)
      - **id** (string)
      - **type** (string)
    - **activityDescription** (string)
    - **type** (string)
  - **update** (object)
    - **summary** (array)
      - **set** (string)
    - **components** (array)
      - **set** (string)
    - **timetracking** (array)
      - **edit** (object)
        - **remainingEstimate** (string)
        - **originalEstimate** (string)
    - **labels** (array)
      - **add** (string)
      - **remove** (string)
  - **fields** (object)
    - **summary** (string)
    - **customfield_10010** (number)
    - **customfield_10000** (object)
      - **type** (string)
      - **version** (number)
      - **content** (array)
        - **type** (string)
        - **content** (array)
          - **text** (string)
          - **type** (string)
  - **properties** (array)
    - **value** (string)
    - **key** (string)
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