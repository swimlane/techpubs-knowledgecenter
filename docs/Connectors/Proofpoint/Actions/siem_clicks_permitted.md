# Siem Clicks Permitted

**Description**: Fetch events for clicks to malicious URLs that were permitted within a specified time period in ProofPoint.

## Endpoint

- **URL:** `/v2/siem/clicks/permitted`
- **Method:** `GET`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| parameters | object | One of the following three query parameters describing the desired time range for the data must be supplied with each request interval, sinceSeconds, sinceTime. | Yes |
## Output

### Output Parameters

| Name | Type | Description |
|------|------|-------------|
| status_code | number |  |
| reason | string |  |
| response_text | string |  |
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string |  |
| Connection | string |  |
| Strict-Transport-Security | string |  |