# Add Analysis

**Description**: Processes a query for analysis

## Endpoint

- **URL:** `rest/analysis`
- **Method:** `POST`
## Inputs

- **json_body** (object)
  - **type** (string)
  - **query** (object)
    - **id** (number)
  - **sortDir** (string)
  - **sortField** (string)
  - **sourceType** (string)
  - **startOffset** (number)
  - **endOffset** (number)
  - **scanID** (number)
  - **view** (string)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "type": "regular",
      "response": {
        "totalRecords": "1",
        "returnedRecords": 1,
        "startOffset": "0",
        "endOffset": "50",
        "matchingDataElementCount": "-1",
        "results": [
          {
            "pluginID": "119500",
            "severity": {
              "id": "4",
              "name": "Critical",
              "description": "Critical Severity"
            },
            "vprScore": "6.7",
            "vprContext": [
              {
                "id": "age_of_vuln",
                "name": "Vulnerability Age",
                "value": "60 - 180 days",
                "type": "string"
              },
              {
                "id": "cvssV3_impactScore",
                "name": "CvssV3 Impact Score",
                "value": 5.9,
                "type": "number"
              },
              {
                "id": "exploit_code_maturity",
                "name": "Exploit Code Maturity",
                "value": "Unproven",
                "type": "string"
              },
              {
                "id": "predicted_impactScore",
                "name": "Predicted Impact Score",
                "value": false,
                "type": "boolean"
              },
              {
                "id": "product_coverage",
                "name": "Product Coverage",
                "value": "Low",
                "type": "string"
              },
              {
                "id": "threat_intensity_last_28",
                "name ": "Threat Intensity",
                "value": "Low",
                "type": "string"
              },
              {
                "id": "threat_recency",
                "name": "Threat Recency",
                "value": "7 to 30 days",
                "type": "string"
              },
              {
                "id": "threat_sources_last_28",
                "name": "Threat Sources",
                "value": "Security Research",
                "type": "string"
              }
            ],
            "ip": "172.26.48.75",
            "uuid": "",
            "port": "8080",
            "protocol": "TCP",
            "name": "Jenkins < 2.138.4 LTS / 2.150.1 LTS / 2.154 MultipleVulnerabilities",
            "dnsName": "",
            "macAddress": "00:50:56:be:27:da",
            "netbiosName": "TARGET\\WINDOW7X64",
            "uniqueness": "repositoryID,ip,dnsName",
            "hostUniqueness": "repositoryID,ip,dnsName",
            "family": {
              "id": "6",
              "name": "CGI abuses",
              "type": "active"
            },
            "repository": {
              "id": "516",
              "name": "repo1",
              "description": "",
              "dataFormat": "IPv4"
            },
            "pluginInfo": "119500 (8080/6) Jenkins < 2.138.4 LTS / 2.150.1 LTS / 2.154 Multiple Vulnerabilities"
          }
        ]
      },
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1553525692
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **type** (string)
  - **response** (object)
    - **totalRecords** (string)
    - **returnedRecords** (number)
    - **startOffset** (string)
    - **endOffset** (string)
    - **matchingDataElementCount** (string)
    - **results** (array)
      - **pluginID** (string)
      - **severity** (object)
        - **id** (string)
        - **name** (string)
        - **description** (string)
      - **vprScore** (string)
      - **vprContext** (array)
        - **id** (string)
        - **name** (string)
        - **value** (string)
        - **type** (string)
        - **name ** (string)
      - **ip** (string)
      - **uuid** (string)
      - **port** (string)
      - **protocol** (string)
      - **name** (string)
      - **dnsName** (string)
      - **macAddress** (string)
      - **netbiosName** (string)
      - **uniqueness** (string)
      - **hostUniqueness** (string)
      - **family** (object)
        - **id** (string)
        - **name** (string)
        - **type** (string)
      - **repository** (object)
        - **id** (string)
        - **name** (string)
        - **description** (string)
        - **dataFormat** (string)
      - **pluginInfo** (string)
  - **error_code** (number)
  - **error_msg** (string)
  - **warnings** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **timestamp** (number)