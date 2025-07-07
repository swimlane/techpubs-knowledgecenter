# Get Scan Report

**Description**: Get the report of a scan in the specified format.

## Endpoint

- **URL:** `/api/1.0/scans/report/`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required
  - **contentFormat** (string): Gets or sets the content format. This parameter can only be used for vulnerabilities XML and JSON report.
  - **excludeResponseData** (boolean): If set to true, HTTP response data will be excluded from the vulnerability detail. This parameter can only be used for vulnerabilities XML report. Default: false
  - **format** (string) – Required: Gets or sets the report format. Crawled URLs, scanned URLs and vulnerabilities can be exported as XML, CSV or JSON. Scan detail, SANS Top 25, Owasp Top Ten 2013, WASC Threat Classification, PCI Compliance, HIPAA Compliance, Executive Summary and Knowledge Base reports can be exported as HTML or PDF. ModSecurity WAF Rules report can be exported as TXT.
  - **id** (string) – Required: Gets or sets the scan identifier.
  - **type** (string) – Required: Gets or sets the report type. FullScanDetail option corresponds to "Detailed Scan Report (Including addressed issues)". ScanDetail option corresponds to "Detailed Scan Report (Excluding addressed issues)".
  - **onlyConfirmedIssues** (boolean)
  - **onlyUnconfirmedIssues** (boolean)
  - **excludeAddressedIssues** (boolean)
  - **excludeHistoryOfIssues** (boolean)
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **file** (object): Attachments
  - **file** (string)
  - **file_name** (string)