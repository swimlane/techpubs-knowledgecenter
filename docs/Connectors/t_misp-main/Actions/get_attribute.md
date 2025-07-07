# Get Attribute

**Description**: Fetches a specific attribute from MISP for threat analysis and intelligence, using provided headers.

## Endpoint

- **URL:** `attributes`
- **Method:** `GET`
## Inputs

- **headers** (object) – Required
  - **Accept** (string) – Required
  - **Content-Type** (string) – Required
## Output

### Example

```json
[
  [
    {
      "id": "12345",
      "event_id": "12345",
      "object_id": "12345",
      "object_relation": "sensor",
      "category": "Internal reference",
      "type": "md5",
      "value": "127.0.0.1",
      "to_ids": true,
      "uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b1b",
      "timestamp": "1617875568",
      "distribution": "0",
      "sharing_group_id": "1",
      "comment": "logged source ip",
      "deleted": false,
      "disable_correlation": false,
      "first_seen": "1581984000000000",
      "last_seen": "1581984000000000"
    }
  ]
]
```