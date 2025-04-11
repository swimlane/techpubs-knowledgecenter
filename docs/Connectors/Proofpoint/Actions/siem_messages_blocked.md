# Siem Messages Blocked

**Description**: Retrieve events for messages that were blocked within a specified time frame due to recognized threats in ProofPoint.

## Endpoint

- **URL:** `/v2/siem/messages/blocked`
- **Method:** `GET`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| parameters | object | One of the following three query parameters describing the desired time range for the data must be supplied with each request interval, sinceSeconds, sinceTime. | Yes |
## Output

### Output Parameters

| Name | Type |
|------|------|
| status_code | number |
| reason | string |
| response_text | string |
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string |  |
| Content-Type | string |  |
| Transfer-Encoding | string |  |
| Connection | string |  |
| Vary | string |  |
| Content-Encoding | string |  |
| Strict-Transport-Security | string |  |