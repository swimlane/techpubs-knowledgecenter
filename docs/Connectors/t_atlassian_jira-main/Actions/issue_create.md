# Create Issue

**Description**: Creates a new issue or subtask in Atlassian Jira with details specified in the 'fields' parameter of the JSON body.

## Endpoint

- **URL:** `/rest/api/3/issue`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **fields** (object) – Required
    - **summary** (string) – Required
    - **parent** (object)
      - **key** (string)
    - **issuetype** (object) – Required
      - **id** (string) – Required
    - **components** (array)
      - **id** (string)
    - **project** (object) – Required
      - **id** (string)
      - **key** (string)
    - **description** (object)
      - **type** (string)
      - **version** (number)
      - **content** (array)
        - **type** (string)
        - **content** (array)
          - **text** (string)
          - **type** (string)
    - **reporter** (object)
      - **id** (string)
    - **fixVersions** (array)
      - **id** (string)
    - **priority** (object)
      - **id** (string)
    - **labels** (array)
    - **timetracking** (object)
      - **remainingEstimate** (string)
      - **originalEstimate** (string)
    - **security** (object)
      - **id** (string)
    - **environment** (object)
      - **type** (string)
      - **version** (number)
      - **content** (array)
        - **type** (string)
        - **content** (array)
          - **text** (string)
          - **type** (string)
    - **versions** (array)
      - **id** (string)
    - **duedate** (string)
    - **assignee** (object)
      - **id** (string)
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **id** (string)
  - **key** (string)
  - **self** (string)
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
| Transfer-Encoding | string |