# Search Logs

**Description**: Initiates a task to search logs in Forti Analyzer with specified parameters, requiring a 'params' JSON body input.

## Endpoint

- **URL:** `/logview/logsearch`
- **Method:** `POST`
## Inputs

| Name | Type | Required |
|------|------|----------|
| json_body | object | Yes |
## Output

### Output Parameters

| Name | Type |
|------|------|
| status_code | number |
| reason | string |
| json_body | object |