# Get Blocklist Items

**Description**: Retrieves all items in the SentinelOne Blocklist that meet specified filter criteria, such as hash values or threat IDs.

## Endpoint

- **URL:** `/web/api/v2.1/restrictions`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **accountids** (string): List of Account IDs to filter by.
  - **countonly** (boolean): If true, only total number of items will be returned, without any of the actual objects.
  - **createdat__between** (string): Date range for creation time (format - <from_timestamp> - <to_timestamp>, inclusive)
  - **createdat__gt** (string): Created after this timestamp.
  - **createdat__gte** (string): Created after or at this timestamp.
  - **createdat__lt** (string): Created before this timestamp.
  - **createdat__lte** (string): Created before or at this timestamp.
  - **cursor** (string): Cursor position returned by the last request. Use to iterate over more than 1000 items.
  - **description__contains** (string): Free-text filter by description.
  - **groupids** (string): List of Group IDs to filter by.
  - **ids** (string): List of IDs to filter by.
  - **imported** (boolean): Indication whether the hash was imported by a bulk operation or not.
  - **includechildren** (boolean): Return filters from children scope levels.
  - **includeparents** (boolean): Return filters from parent scope levels.
  - **limit** (string): Limit number of returned items (1-1000).
  - **modes** (string): List of modes to filter by (Path exclusions only).
  - **ostypes** (string): List of OS types to filter by.
  - **query** (string): A free-text search term, will match applicable attributes
  - **recommendations** (string): List of recommendations to filter by.
  - **siteids** (string): List of Site IDs to filter by.
  - **skip** (string): Skip first number of items (0-1000). To iterate over more than 1000 items, use "cursor".
  - **skipcount** (boolean): If true, total number of items will not be calculated, which speeds up execution time.
  - **sortby** (string): The column to sort the results by.
  - **sortorder** (string): Sort direction.
  - **source** (string): List sources to filter by.
  - **tenant** (string): Indicates a tenant scope request.
  - **type** (string): Type.
  - **types** (string): Type in.
  - **unified** (string): Unified.
  - **updatedat__between** (string): Date range for update time (format - <from_timestamp> - <to_timestamp>, inclusive).
  - **updatedat__gt** (string): Updated after this timestamp.
  - **updatedat__gte** (string): Updated after or at this timestamp.
  - **updatedat__lt** (string): Updated before this timestamp.
  - **updatedat__lte** (string): Updated before or at this timestamp.
  - **user__contains** (string): Free-text filter by user name.
  - **userids** (string): List of user IDs to filter by.
  - **value** (string): Value.
  - **value__contains** (string): Free-text filter by value
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (array)
    - **createdAt** (string)
    - **description** (string)
    - **id** (string)
    - **imported** (boolean)
    - **includeChildren** (boolean)
    - **includeParents** (boolean)
    - **notRecommended** (string)
    - **osType** (string)
    - **scope** (object)
      - **accountIds** (array)
      - **groupIds** (array)
      - **siteIds** (array)
      - **tenant** (boolean)
    - **scopeName** (string)
    - **scopePath** (string)
    - **source** (string)
    - **type** (string)
    - **updatedAt** (string)
    - **userId** (string)
    - **userName** (string)
    - **value** (string)
  - **errors** (array)
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