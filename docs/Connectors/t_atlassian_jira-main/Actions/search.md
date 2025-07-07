# Search

**Description**: Executes a search for Jira issues using JQL based on criteria specified in the request body.

## Endpoint

- **URL:** `/rest/api/3/search`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **expand** (array)
  - **jql** (string)
  - **maxResults** (number)
  - **fieldsByKeys** (boolean)
  - **fields** (array)
  - **startAt** (number)
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **expand** (string)
  - **startAt** (number)
  - **maxResults** (number)
  - **total** (number)
  - **issues** (array)
    - **expand** (string)
    - **id** (string)
    - **self** (string)
    - **key** (string)
    - **fields** (object)
      - **resolution** (object)
      - **lastViewed** (object)
      - **labels** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **aggregatetimeoriginalestimate** (object)
      - **issuelinks** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **assignee** (object)
      - **components** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **subtasks** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **reporter** (object)
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
      - **progress** (object)
        - **progress** (number)
        - **total** (number)
      - **votes** (object)
        - **self** (string)
        - **votes** (number)
        - **hasVoted** (boolean)
      - **issuetype** (object)
        - **self** (string)
        - **id** (string)
        - **description** (string)
        - **iconUrl** (string)
        - **name** (string)
        - **subtask** (boolean)
        - **avatarId** (number)
        - **hierarchyLevel** (number)
      - **project** (object)
        - **self** (string)
        - **id** (string)
        - **key** (string)
        - **name** (string)
        - **projectTypeKey** (string)
        - **simplified** (boolean)
        - **avatarUrls** (object)
          - **48x48** (string)
          - **24x24** (string)
          - **16x16** (string)
          - **32x32** (string)
      - **resolutiondate** (object)
      - **watches** (object)
        - **self** (string)
        - **watchCount** (number)
        - **isWatching** (boolean)
      - **updated** (string)
      - **timeoriginalestimate** (object)
      - **description** (object)
        - **version** (number)
        - **type** (string)
        - **content** (array)
          - **type** (string)
          - **content** (array)
            - **type** (string)
            - **text** (string)
      - **summary** (string)
      - **duedate** (object)
      - **statuscategorychangedate** (string)
      - **fixVersions** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **priority** (object)
        - **self** (string)
        - **iconUrl** (string)
        - **name** (string)
        - **id** (string)
      - **timeestimate** (object)
      - **versions** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **status** (object)
        - **self** (string)
        - **description** (string)
        - **iconUrl** (string)
        - **name** (string)
        - **id** (string)
        - **statusCategory** (object)
          - **self** (string)
          - **id** (number)
          - **key** (string)
          - **colorName** (string)
          - **name** (string)
      - **aggregatetimeestimate** (object)
      - **creator** (object)
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
      - **timespent** (object)
      - **aggregatetimespent** (object)
      - **workratio** (number)
      - **created** (string)
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