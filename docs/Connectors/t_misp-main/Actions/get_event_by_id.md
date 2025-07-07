# Get Event by Id

**Description**: Retrieve detailed information for a specific event in MISP by providing the unique event ID.

## Endpoint

- **URL:** `events/view/{{eventId}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **eventId** (string) – Required
- **headers** (object) – Required
  - **Accept** (string) – Required
  - **Content-Type** (string) – Required
## Output

### Example

```json
[
  {
    "Event": {
      "id": "12345",
      "org_id": "12345",
      "distribution": "0",
      "info": "logged source ip",
      "orgc_id": "12345",
      "uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b1b",
      "date": "1991-01-15",
      "published": false,
      "analysis": "0",
      "attribute_count": "321",
      "timestamp": "1617875568",
      "sharing_group_id": "1",
      "proposal_email_lock": true,
      "locked": true,
      "threat_level_id": "1",
      "publish_timestamp": "1617875568",
      "sighting_timestamp": "1617875568",
      "disable_correlation": false,
      "extends_uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b1b",
      "event_creator_email": "user@example.com",
      "Feed": {
        "id": "3",
        "name": "CIRCL OSINT Feed",
        "provider": "CIRCL",
        "url": "https://www.circl.lu/doc/misp/feed-osint",
        "rules": "{\"tags\":{\"OR\":[],\"NOT\":[]},\"orgs\":{\"OR\":[],\"NOT\":[]},\"url_params\":\"\"}",
        "enabled": true,
        "distribution": "0",
        "sharing_group_id": "1",
        "tag_id": "12345",
        "default": true,
        "source_format": "1",
        "fixed_event": true,
        "delta_merge": true,
        "event_id": "12345",
        "publish": false,
        "override_ids": true,
        "settings": "{\"csv\":{\"value\":\"\",\"delimiter\":\"\"},\"common\":{\"excluderegex\":\"\"},\"disable_correlation\":\"1\"}",
        "input_source": "local",
        "delete_local_file": true,
        "lookup_visible": true,
        "headers": "X-Custom-Header-A: Foo\nX-Custom-Header-B: Bar\n",
        "caching_enabled": true,
        "force_to_ids": true,
        "orgc_id": "12345",
        "cache_timestamp": "1617875568"
      },
      "Org": {
        "id": "12345",
        "name": "ORGNAME",
        "uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b1b"
      },
      "Orgc": {
        "id": "12345",
        "name": "ORGNAME",
        "uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b1b"
      },
      "Attribute": [
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
      ],
      "ShadowAttribute": [
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
      ],
      "RelatedEvent": [
        {}
      ],
      "Galaxy": [
        {
          "id": "12345",
          "uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b1b",
          "name": "Ransomware",
          "type": "ransomware",
          "description": "Ransomware galaxy based on ...",
          "version": "1",
          "icon": "globe",
          "namespace": "misp",
          "kill_chain_order": {
            "fraud-tactics": [
              "Initiation",
              "Target Compromise",
              "Perform Fraud",
              "Obtain Fraudulent Assets",
              "Assets Transfer",
              "Monetisation"
            ]
          }
        }
      ],
      "Object": [
        {
          "id": "12345",
          "name": "ail-leak",
          "meta-category": "string",
          "description": "string",
          "template_uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b1b",
          "template_version": "1",
          "event_id": "12345",
          "uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b1b",
          "timestamp": "1617875568",
          "distribution": "0",
          "sharing_group_id": "1",
          "comment": "string",
          "deleted": true,
          "first_seen": "1581984000000000",
          "last_seen": "1581984000000000",
          "Attribute": [
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
        }
      ],
      "EventReport": [
        {}
      ],
      "Tag": [
        {
          "id": "12345",
          "name": "tlp:white",
          "colour": "#ffffff",
          "exportable": true,
          "org_id": "12345",
          "user_id": "12345",
          "hide_tag": false,
          "numerical_value": "12345",
          "is_galaxy": true,
          "is_custom_galaxy": true,
          "inherited": 1
        }
      ]
    }
  }
]
```
### Output Parameters

- **Event** (object)
  - **id** (string)
  - **org_id** (string)
  - **distribution** (string)
  - **info** (string)
  - **orgc_id** (string)
  - **uuid** (string)
  - **date** (string)
  - **published** (boolean)
  - **analysis** (string)
  - **attribute_count** (string)
  - **timestamp** (string)
  - **sharing_group_id** (string)
  - **proposal_email_lock** (boolean)
  - **locked** (boolean)
  - **threat_level_id** (string)
  - **publish_timestamp** (string)
  - **sighting_timestamp** (string)
  - **disable_correlation** (boolean)
  - **extends_uuid** (string)
  - **event_creator_email** (string)
  - **Feed** (object)
    - **id** (string)
    - **name** (string)
    - **provider** (string)
    - **url** (string)
    - **rules** (string)
    - **enabled** (boolean)
    - **distribution** (string)
    - **sharing_group_id** (string)
    - **tag_id** (string)
    - **default** (boolean)
    - **source_format** (string)
    - **fixed_event** (boolean)
    - **delta_merge** (boolean)
    - **event_id** (string)
    - **publish** (boolean)
    - **override_ids** (boolean)
    - **settings** (string)
    - **input_source** (string)
    - **delete_local_file** (boolean)
    - **lookup_visible** (boolean)
    - **headers** (string)
    - **caching_enabled** (boolean)
    - **force_to_ids** (boolean)
    - **orgc_id** (string)
    - **cache_timestamp** (string)
  - **Org** (object)
    - **id** (string)
    - **name** (string)
    - **uuid** (string)
  - **Orgc** (object)
    - **id** (string)
    - **name** (string)
    - **uuid** (string)
  - **Attribute** (array)
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
  - **ShadowAttribute** (array)
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
  - **RelatedEvent** (array)
  - **Galaxy** (array)
    - **id** (string)
    - **uuid** (string)
    - **name** (string)
    - **type** (string)
    - **description** (string)
    - **version** (string)
    - **icon** (string)
    - **namespace** (string)
    - **kill_chain_order** (object)
      - **fraud-tactics** (array)
  - **Object** (array)
    - **id** (string)
    - **name** (string)
    - **meta-category** (string)
    - **description** (string)
    - **template_uuid** (string)
    - **template_version** (string)
    - **event_id** (string)
    - **uuid** (string)
    - **timestamp** (string)
    - **distribution** (string)
    - **sharing_group_id** (string)
    - **comment** (string)
    - **deleted** (boolean)
    - **first_seen** (string)
    - **last_seen** (string)
    - **Attribute** (array)
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
  - **EventReport** (array)
  - **Tag** (array)
    - **id** (string)
    - **name** (string)
    - **colour** (string)
    - **exportable** (boolean)
    - **org_id** (string)
    - **user_id** (string)
    - **hide_tag** (boolean)
    - **numerical_value** (string)
    - **is_galaxy** (boolean)
    - **is_custom_galaxy** (boolean)
    - **inherited** (number)