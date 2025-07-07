# Create Exclusion

**Description**: Establish exclusions within SentinelOne to suppress alerts and mitigate benign items, with required 'data' and 'filter' inputs.

## Endpoint

- **URL:** `/web/api/v2.1/exclusions`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **data** (object) – Required
    - **osType** (string) – Required: OS type.
    - **type** (string) – Required: Exclusion item type.
    - **value** (string) – Required: Value for the item type.
    - **actions** (array): Actions to perform.
    - **description** (string): Description.
    - **mode** (string): Exclusion mode (path exclusion only).
    - **pathExclusionType** (string): Excluded path for a path exclusion list.
    - **source** (string): Source.
  - **filter** (object) – Required
    - **accountIds** (array): List of Account IDs to filter by.
    - **groupIds** (array): List of Group IDs to filter by.
    - **siteIds** (array): List of Site IDs to filter by.
    - **tenant** (boolean): Indicates a tenant scope request.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (object)
    - **scope** (object)
      - **accountIds** (array)
      - **groupIds** (array)
      - **siteIds** (array)
      - **tenant** (boolean)
    - **actions** (array)
    - **createdAt** (string)
    - **description** (string)
    - **id** (string)
    - **mode** (string)
    - **notRecommended** (string)
    - **osType** (string)
    - **pathExclusionType** (string)
    - **scopeName** (string)
    - **source** (string)
    - **type** (string)
    - **updatedAt** (string)
    - **userId** (string)
    - **userName** (string)
    - **value** (string)
  - **errors** (array)