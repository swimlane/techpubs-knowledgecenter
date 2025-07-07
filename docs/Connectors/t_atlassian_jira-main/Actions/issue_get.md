# Get Issue

**Description**: Retrieve detailed information for a specific issue in Atlassian Jira using the provided issue ID or key.

## Endpoint

- **URL:** `/rest/api/3/issue/{{issueIdOrKey}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **issueIdOrKey** (string) – Required
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **expand** (string)
  - **id** (string)
  - **self** (string)
  - **key** (string)
  - **fields** (object)
    - **parent** (object)
      - **id** (string)
      - **key** (string)
      - **self** (string)
      - **fields** (object)
        - **summary** (string)
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
        - **priority** (object)
          - **self** (string)
          - **iconUrl** (string)
          - **name** (string)
          - **id** (string)
        - **issuetype** (object)
          - **self** (string)
          - **id** (string)
          - **description** (string)
          - **iconUrl** (string)
          - **name** (string)
          - **subtask** (boolean)
          - **avatarId** (number)
          - **hierarchyLevel** (number)
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
    - **worklog** (object)
      - **startAt** (number)
      - **maxResults** (number)
      - **total** (number)
      - **worklogs** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
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
    - **timetracking** (object)
    - **summary** (string)
    - **duedate** (object)
    - **comment** (object)
      - **comments** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **self** (string)
      - **maxResults** (number)
      - **total** (number)
      - **startAt** (number)
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
    - **issuerestriction** (object)
      - **issuerestrictions** (object)
      - **shouldDisplay** (boolean)
    - **created** (string)
    - **attachment** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
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