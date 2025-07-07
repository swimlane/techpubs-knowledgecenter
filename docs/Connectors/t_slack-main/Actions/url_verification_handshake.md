# URL Verification Handshake

**Description**: Confirms the integrity of a Slack webhook setup by verifying the challenge present in the provided data body content.

## Endpoint

- **Method:** `POST`
## Inputs

- **data_body** (object) – Required
  - **challenge** (string) – Required
## Output

### Example

```json
[
  {
    "headers": null,
    "reason": "OK",
    "status_code": 200
  }
]
```
### Output Parameters

- **headers** (object)
- **reason** (string)
- **status_code** (number)