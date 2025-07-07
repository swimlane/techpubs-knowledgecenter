# Get Count of Attributes by Category

**Description**: Retrieve the count of MISP attributes by category, using context and percentage as path parameters.

## Endpoint

- **URL:** `attributes/attributeStatistics/{{context}}/{{percentage}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **context** (string) – Required
  - **percentage** (number) – Required
- **headers** (object) – Required
  - **Accept** (string) – Required
  - **Content-Type** (string) – Required
## Output

### Example

```json
[
  [
    {
      "Antivirus detection": "10"
    },
    {
      "Artifacts dropped": "20"
    }
  ]
]
```