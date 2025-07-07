# Get Scan Custom Report

**Description**: Returns the custom report of a scan in the specified format.

## Endpoint

- **URL:** `/api/1.0/scans/custom-report/`
- **Method:** `get`
## Inputs

- **parameters** (object) – Required
  - **excludeIgnoreds** (boolean)
  - **id** (string) – Required
  - **onlyConfirmedVulnerabilities** (boolean)
  - **onlyUnconfirmedVulnerabilities** (boolean)
  - **reportName** (string) – Required: Gets or sets report name. Report name also keeps report type in it.
  - **reportFormat** (string)
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **file** (object): Attachments
  - **file** (string)
  - **file_name** (string)