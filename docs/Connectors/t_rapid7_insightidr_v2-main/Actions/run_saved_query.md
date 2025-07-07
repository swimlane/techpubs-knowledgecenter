# Run Saved Query

**Description**: Executes a predefined saved query within Rapid7 InsightIDR using the provided 'saved_query_id'.

## Endpoint

- **URL:** `/log_search/query/saved_query/{{saved_query_id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **saved_query_id** (string) – Required: The ID of the saved query.
- **parameters** (object) – Required
  - **time_range** (string): An alternative to the from and to query parameters. Possible values are "yesterday", "today" and "last x timeunits" where x is the number of time unit back from the current server time. Supported time units (case insensitive) are min(s) or minute(s), hr(s) or hour(s), day(s), week(s), month(s) and year(s). If "time_range" is used, then the "from" and "to" query parameters must not be used.
  - **from** (number): The start of the time range for the query, as a UNIX timestamp in milliseconds.
  - **to** (number): The end of the time range for the query, as a UNIX timestamp in milliseconds.
  - **per_page** (number): Number of log entries to return per page, up to 500(the maximum allowed).
  - **kvp_info** (boolean): When set to true, the events object that is returned will additionally contain information about all the key-value pairs in each returned log entry.
  - **most_recent_first** (boolean): When set to true, the query returns the most recent events first. When set to false, it returns the oldest events first.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "logs": [
        "565c1b7b-c08b-4c87-a42a-ab08bad56071"
      ],
      "leql": {
        "statement": "where(931dde6c60>=800)",
        "during": {
          "from": 1609629856000,
          "to": 1609629992000
        }
      },
      "events": [
        {
          "labels": [
            {
              "links": [
                {
                  "rel": "Self",
                  "href": "https://ap.rest.logs.insight.rapid7.com/management/labels/00000000-0000-0000-0000-000000000001"
                }
              ],
              "id": "00000000-0000-0000-0000-000000000001"
            }
          ],
          "timestamp": 1609629969390,
          "sequence_number": 2234733321019952000,
          "log_id": "565c1b7b-c08b-4c87-a42a-ab08bad56071",
          "message": "{\"931dde6c60\":899}",
          "links": [
            {
              "rel": "Context",
              "href": "https://ap.rest.logs.insight.rapid7.com/query/context/2234733321019952220?per_page=50&timestamp=1609629969390&log_keys=565c1b7b-c08b-4c87-a42a-ab08bad56071&context_type=SURROUND&kvp_info=true"
            }
          ],
          "sequence_number_str": 2234733321019952000,
          "kvp_info": [
            {
              "key": {
                "text": "json.931dde6c60",
                "start": 2,
                "end": 12
              },
              "value": {
                "text": 899,
                "start": 14,
                "end": 17
              }
            }
          ]
        },
        {
          "labels": [
            {
              "links": [
                {
                  "rel": "Self",
                  "href": "https://ap.rest.logs.insight.rapid7.com/management/labels/00000000-0000-0000-0000-000000000001"
                }
              ],
              "id": "00000000-0000-0000-0000-000000000001"
            }
          ],
          "timestamp": 1609629978988,
          "sequence_number": 2234733321345612300,
          "log_id": "565c1b7b-c08b-4c87-a42a-ab08bad56071",
          "message": "{\"931dde6c60\":931}",
          "links": [
            {
              "rel": "Context",
              "href": "https://ap.rest.logs.insight.rapid7.com/query/context/2234733321345612345?per_page=1&timestamp=1609629978988&log_keys=565c1b7b-c08b-4c87-a42a-ab08bad56071&context_type=SURROUND&kvp_info=true"
            }
          ],
          "sequence_number_str": 2234733321345612300,
          "kvp_info": [
            {
              "key": {
                "text": "json.931dde6c60",
                "start": 2,
                "end": 12,
                "value": {
                  "text": 931,
                  "start": 14,
                  "end": 17
                }
              }
            }
          ]
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **logs** (array)
  - **leql** (object)
    - **statement** (string)
    - **during** (object)
      - **from** (number)
      - **to** (number)
  - **events** (array)
    - **labels** (array)
      - **links** (array)
        - **rel** (string)
        - **href** (string)
      - **id** (string)
    - **timestamp** (number)
    - **sequence_number** (number)
    - **log_id** (string)
    - **message** (string)
    - **links** (array)
      - **rel** (string)
      - **href** (string)
    - **sequence_number_str** (number)
    - **kvp_info** (array)
      - **key** (object)
        - **text** (string)
        - **start** (number)
        - **end** (number)
        - **value** (object)
          - **text** (number)
          - **start** (number)
          - **end** (number)