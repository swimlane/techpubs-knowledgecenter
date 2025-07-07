# Get Incident Correlations

**Description**: Retrieve correlations for a specified incident in Symantec DLP using the unique identifier provided.

## Endpoint

- **URL:** `/ProtectManager/webservices/v2/incidents/{{id}}/correlations`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (number) – Required: The incident ID.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": [
      {
        "variable": "incident.sender",
        "label": "Sender",
        "correlationValues": [
          {
            "value": "janedoe@gmail.com",
            "countSevenDays": 0,
            "countThirtyDays": 0,
            "countAllDays": 24
          }
        ]
      },
      {
        "variable": "incident.recipient",
        "label": "Recipient",
        "correlationValues": [
          {
            "value": "bobdoe@gmail.com",
            "countSevenDays": 0,
            "countThirtyDays": 0,
            "countAllDays": 24
          }
        ]
      },
      {
        "variable": "incident.message.subject",
        "label": "Subject",
        "correlationValues": [
          {
            "value": "secret",
            "countSevenDays": 0,
            "countThirtyDays": 0,
            "countAllDays": 24
          }
        ]
      },
      {
        "variable": "incident.policy.id",
        "label": "Policy",
        "correlationValues": [
          {
            "value": "1",
            "label": "secret policy",
            "countSevenDays": 0,
            "countThirtyDays": 0,
            "countAllDays": 24
          }
        ]
      }
    ]
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (array)
  - **variable** (string)
  - **label** (string)
  - **correlationValues** (array)
    - **value** (string)
    - **label** (string)
    - **countSevenDays** (number)
    - **countThirtyDays** (number)
    - **countAllDays** (number)