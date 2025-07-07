# Get Search Results

**Description**: Obtain the results of a specified search in Cisco Splunk using the provided search ID and output mode.

## Inputs

- **output_mode** (string) – Required
- **search_id** (string) – Required
- **count** (number): The maximum number of results to return.
- **offset** (number): The first result from which to begin returning data.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **messages** (array)
    - **type** (string)
    - **text** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Expires | string |
| Cache-Control | string |
| Content-Type | string |
| X-Content-Type-Options | string |
| Content-Length | string |
| Vary | string |
| Connection | string |
| X-Frame-Options | string |
| Server | string |