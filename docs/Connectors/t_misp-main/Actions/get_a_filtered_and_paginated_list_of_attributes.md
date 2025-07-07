# Get a Filtered and Paginated List of Attributes

**Description**: Retrieve a filtered and paginated list of attributes from MISP, including specified request headers.

## Endpoint

- **URL:** `attributes/restSearch`
- **Method:** `POST`
## Inputs

- **json_body** (object)
  - **page** (number)
  - **limit** (number)
  - **value** (string)
  - **value1** (string)
  - **value2** (string)
  - **type** (string)
  - **category** (string)
  - **org** (string)
  - **tags** (array)
  - **from** (string)
  - **to** (string)
  - **last** (number)
  - **eventid** (string)
  - **withAttachments** (boolean)
  - **uuid** (string)
  - **publish_timestamp** (string)
  - **published** (boolean)
  - **timestamp** (string)
  - **attribute_timestamp** (string)
  - **enforceWarninglist** (boolean)
  - **to_ids** (boolean)
  - **deleted** (boolean)
  - **event_timestamp** (string)
  - **threat_level_id** (string)
  - **eventinfo** (string)
  - **sharinggroup** (array)
  - **decayingModel** (string)
  - **score** (string)
  - **first_seen** (string)
  - **last_seen** (string)
  - **includeEventUuid** (boolean)
  - **includeEventTags** (boolean)
  - **includeProposals** (boolean)
  - **requested_attributes** (array)
  - **includeContext** (boolean)
  - **headerless** (boolean)
  - **includeWarninglistHits** (boolean)
  - **attackGalaxy** (string)
  - **object_relation** (string)
  - **includeSightings** (boolean)
  - **includeCorrelations** (boolean)
  - **modelOverrides** (object)
    - **lifetime** (number)
    - **decay_speed** (number)
    - **threshold** (number)
    - **default_base_score** (number)
    - **base_score_config** (object)
      - **estimative-language:confidence-in-analytic-judgment** (number)
      - **estimative-language:likelihood-probability** (number)
      - **phishing:psychological-acceptability** (number)
      - **phishing:state** (number)
  - **includeDecayScore** (boolean)
  - **includeFullModel** (boolean)
  - **excludeDecayed** (boolean)
  - **returnFormat** (string)
- **headers** (object) – Required
  - **Accept** (string) – Required
  - **Content-Type** (string) – Required
## Output

### Example

```json
[
  {
    "response": {
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
          "last_seen": "1581984000000000",
          "data": "string",
          "event_uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b1b",
          "decay_score": [
            {
              "score": 10.5,
              "base_score": 80,
              "decayed": true,
              "DecayingModel": {
                "id": "12345",
                "name": "Phishing model"
              }
            }
          ],
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
            "event_creator_email": "user@example.com"
          },
          "Object": {
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
          },
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
      ]
    }
  }
]
```
### Output Parameters

- **response** (object)
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
    - **data** (string)
    - **event_uuid** (string)
    - **decay_score** (array)
      - **score** (number)
      - **base_score** (number)
      - **decayed** (boolean)
      - **DecayingModel** (object)
        - **id** (string)
        - **name** (string)
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
    - **Object** (object)
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