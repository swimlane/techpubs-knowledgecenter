# Get Rogues Settings

**Description**: Retrieve the current configuration settings for rogue devices from SentinelOne.

## Endpoint

- **URL:** `/web/api/v2.1/rogues/settings`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **accountIds** (array)
  - **siteIds** (array)
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (object)
    - **minAgentsInNetworkToScan** (number)
    - **accountId** (string)
    - **enabled** (boolean)
    - **useSpecificPorts** (boolean)
    - **restrictions** (array)
      - **annotation** (string)
      - **values** (array)
      - **type** (string)
    - **specificPorts** (array)
      - **values** (array)
      - **type** (string)
  - **errors** (array)
    - **code** (number)
    - **detail** (object)
    - **title** (string)
## Response Headers

| Header | Type |
|--------|------|
| Server | string |
| Date | string |
| Content-Type | string |
| Content-Length | string |
| Connection | string |
| Set-Cookie | string |
| X-RQID | string |
| Access-Control-Allow-Origin | string |
| Access-Control-Allow-Credentials | string |
| Vary | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| X-Content-Type-Options | string |
| Content-Security-Policy | string |