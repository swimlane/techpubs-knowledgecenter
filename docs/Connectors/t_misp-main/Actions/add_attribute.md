# Add Attribute

**Description**: Adds a new attribute to an existing event in MISP using the provided event ID.

## Endpoint

- **URL:** `attributes/add/{{eventId}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **eventId** (string) – Required
- **json_body** (object)
  - **event_id** (string)
  - **object_id** (string)
  - **object_relation** (string)
  - **category** (string)
  - **type** (string)
  - **value** (string)
  - **to_ids** (boolean)
  - **uuid** (string)
  - **timestamp** (string)
  - **distribution** (string)
  - **sharing_group_id** (string)
  - **comment** (string)
  - **deleted** (boolean)
  - **disable_correlation** (boolean)
  - **first_seen** (string)
  - **last_seen** (string)
- **headers** (object) – Required
  - **Accept** (string) – Required
  - **Content-Type** (string) – Required
## Output

### Example

```json
[
  {
    "Attribute": {
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
  }
]
```
### Output Parameters

- **Attribute** (object)
  - **id** (string)
  - **event_id** (string)
  - **object_id** (string)
  - **object_relation** (string)
  - **category** (string)
  - **type** (string)
  - **value** (string)
  - **to_ids** (boolean)
  - **uuid** (string)
  - **timestamp** (string)
  - **distribution** (string)
  - **sharing_group_id** (string)
  - **comment** (string)
  - **deleted** (boolean)
  - **disable_correlation** (boolean)
  - **first_seen** (string)
  - **last_seen** (string)