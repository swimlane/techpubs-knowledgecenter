# Get Activities

**Description**: Retrieve activity data from SentinelOne, applying specified filters to ensure relevant and manageable outcomes.

## Endpoint

- **URL:** `/web/api/v2.1/activities`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **accountIds** (string): List of Account IDs to filter by.
  - **activityTypes** (string): Return only these activity codes (comma-separated list). Select a code from the dropdown, or see the id field from the Get activity types command.
  - **activityUuids** (string): Return activities by specific activity UUIDs.
  - **agentIds** (string): Return activities related to specified agents.
  - **alertIds** (string): Return activities related to specified alerts.
  - **countOnly** (boolean): If true, only total number of items will be returned, without any of the actual objects.
  - **createdAt__between** (string): Get activities created in this range (inclusive) of a start timestamp and an end timestamp.
  - **createdAt__gt** (string): Get activities created after this timestamp.
  - **createdAt__gte** (string): Get activities created after or at this timestamp.
  - **createdAt__lt** (string): Get activities created before this timestamp.
  - **createdAt__lte** (string): Get activities created before or at this timestamp.
  - **cursor** (string): Cursor position returned by the last request. Use to iterate over more than 1000 items.
  - **groupIds** (string): List of Group IDs to filter by.
  - **ids** (string): Filter activities by specific activity IDs.
  - **includeHidden** (boolean): Include internal activities hidden from display.
  - **limit** (number): Limit number of returned items (1-1000).
  - **ruleIds** (string): Return activities related to specified rules.
  - **siteIds** (string): List of Site IDs to filter by.
  - **skip** (number): Skip first number of items (0-1000). To iterate over more than 1000 items, use "cursor".
  - **skipCount** (boolean): If true, total number of items will not be calculated, which speeds up execution time.
  - **sortBy** (string): The column to sort the results by.
  - **sortOrder** (string): Sort direction.
  - **threatIds** (string): Return activities related to specified threats.
  - **userEmails** (string): Email of the user who invoked the activity (If applicable).
  - **userIds** (string): The user who invoked the activity (If applicable).
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (array)
    - **accountId** (string)
    - **accountName** (string)
    - **activityType** (number)
    - **activityUuid** (string)
    - **agentId** (object)
    - **agentUpdatedVersion** (object)
    - **comments** (object)
    - **createdAt** (string)
    - **data** (object)
      - **accountName** (string)
      - **fileName** (string)
      - **fullScopeDetails** (string)
      - **fullScopeDetailsPath** (string)
      - **groupName** (object)
      - **ipAddress** (string)
      - **majorVersion** (string)
      - **minorVersion** (string)
      - **osArch** (string)
      - **packageId** (number)
      - **platformType** (string)
      - **realUser** (object)
      - **scopeLevel** (string)
      - **scopeName** (string)
      - **siteName** (object)
      - **sourceType** (string)
      - **status** (string)
      - **username** (string)
      - **version** (string)
    - **description** (object)
    - **groupId** (object)
    - **groupName** (object)
    - **hash** (object)
    - **id** (string)
    - **osFamily** (object)
    - **primaryDescription** (string)
    - **secondaryDescription** (string)
    - **siteId** (object)
    - **siteName** (object)
    - **threatId** (object)
    - **updatedAt** (string)
    - **userId** (string)
  - **pagination** (object)
    - **nextCursor** (string)
    - **totalItems** (number)
## Response Headers

| Header | Type |
|--------|------|
| Server | string |
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| X-RQID | string |
| Access-Control-Allow-Origin | string |
| Access-Control-Allow-Credentials | string |
| Vary | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| X-Content-Type-Options | string |
| Content-Security-Policy | string |
| Cache-Control | string |
| Pragma | string |
| Expires | string |
| Content-Encoding | string |