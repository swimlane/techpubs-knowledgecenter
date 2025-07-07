# Download Scan Results

**Description**: Downloads the Scan Result associated with id

## Endpoint

- **URL:** `rest/scanResult/{{id}}/download`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **downloadType** (string) – Required
## Output

### Output Parameters

- **file** (object): File
  - **file_name** (string)
  - **file** (string)