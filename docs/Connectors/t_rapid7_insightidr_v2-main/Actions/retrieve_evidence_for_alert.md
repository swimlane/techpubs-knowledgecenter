# Retrieve Evidence for Alert

**Description**: Retrieve associated evidence for a specific alert in Rapid7 InsightIDR using the alert's unique resource name (RRN).

## Endpoint

- **URL:** `/idr/at/alerts/{{alert_rrn}}/evidences`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **alert_rrn** (string) – Required: The unique identifier of the alert.
- **parameters** (object)
  - **index** (number): The index of the page to retrieve (zero-indexed).
  - **size** (number): The size of the page to retrieve.
- **headers** (object) – Required
  - **Accept-Version** (string) – Required: Acknowledges the API preview status.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 21 Jun 2024 08:01:46 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "r7-correlation-id": "04bad1e4-ac8d-4645-adc2-9d4d3588cb80",
      "vary": "accept-encoding, Origin",
      "content-encoding": "gzip",
      "x-envoy-upstream-service-time": "261",
      "server": "istio-envoy",
      "x-envoy-decorator-operation": "protonclass1apigatewayapp.default.svc.cluster.local:9873/*",
      "Access-Control-Allow-Credentials": "true",
      "Access-Control-Expose-Headers": "R7-Correlation-Id",
      "RateLimit-Limit": "250",
      "RateLimit-Reset": "19",
      "RateLimit-Remaining": "249"
    },
    "reason": "OK",
    "json_body": {
      "evidences": [
        {
          "rrn": "string",
          "version": 0,
          "created_at": "2019-08-24T14:15:22Z",
          "updated_at": "2019-08-24T14:15:22Z",
          "evented_at": "2019-08-24T14:15:22Z",
          "external_source": "string",
          "event_type": "string",
          "data": "string"
        }
      ],
      "metadata": {
        "index": 0,
        "size": 0,
        "items_in_index": 0,
        "total_items": 0,
        "is_last_index": true
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **evidences** (array)
    - **rrn** (string)
    - **version** (number)
    - **created_at** (string)
    - **updated_at** (string)
    - **evented_at** (string)
    - **external_source** (string)
    - **event_type** (string)
    - **data** (string)
  - **metadata** (object)
    - **index** (number)
    - **size** (number)
    - **items_in_index** (number)
    - **total_items** (number)
    - **is_last_index** (boolean)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| r7-correlation-id | string |
| vary | string |
| content-encoding | string |
| x-envoy-upstream-service-time | string |
| server | string |
| x-envoy-decorator-operation | string |
| Access-Control-Allow-Credentials | string |
| Access-Control-Expose-Headers | string |
| RateLimit-Limit | string |
| RateLimit-Reset | string |
| RateLimit-Remaining | string |