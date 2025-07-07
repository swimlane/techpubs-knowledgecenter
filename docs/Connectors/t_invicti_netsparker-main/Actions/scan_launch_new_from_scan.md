# Launch New Scan from Scan

**Description**: Launches a new scan with same configuration from the scan specified with scan ID.

## Endpoint

- **URL:** `/api/1.0/scans/newfromscan`
- **Method:** `POST`
## Inputs

- **data_body** (object) – Required
  - **id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 201,
    "response_headers": {
      "Date": "Thu, 28 Mar 2024 10:02:30 GMT",
      "Content-Type": "application/json; charset=utf-8",
      "Content-Length": "54",
      "Connection": "keep-alive",
      "Cache-Control": "no-cache",
      "Pragma": "no-cache",
      "Expires": "-1",
      "X-Content-Type-Options": "nosniff",
      "X-Frame-Options": "DENY",
      "Referrer-Policy": "no-referrer",
      "X-XSS-Protection": "1; mode=block",
      "Origin-Trial": "Au1hLO38HdoU0c5ahko3BUGr8p9Kt881bvrcCP4vESne1HV+B1XX/MZhfZNP/TWW4+BPBlKO9h3fokvWCxZdsQAAAABieyJvcmlnaW4iOiJodHRwczovL3d3dy5uZXRzcGFya2VyY2xvdWQuY29tOjQ0MyIsImZlYXR1cmUiOiJVMkZTZWN1cml0eUtleUFQSSIsImV4cGlyeSI6MTY1ODg3OTk5OX0=",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
      "Expect-CT": "max-age=30,report-uri=\"https://www.netsparkercloud.com/report-ct/\""
    },
    "reason": "OK",
    "json_body": {
      "AdditionalWebsites": [
        {
          "Canonical": true,
          "TargetUrl": "string"
        }
      ],
      "AgentId": "00000000-0000-0000-0000-000000000000",
      "AgentName": "string",
      "Cookies": "string",
      "CrawlAndAttack": true,
      "DeletedOn": "2024-03-28T06:07:58.141Z",
      "EnableHeuristicChecksInCustomUrlRewrite": true,
      "ExcludedLinks": "string",
      "ExcludeLinks": true,
      "DisallowedHttpMethods": "string",
      "FindAndFollowNewLinks": true,
      "ImportedLinks": "string",
      "AllImportedLinks": "string",
      "DesktopScanId": "00000000-0000-0000-0000-000000000000",
      "InitiatedTime": "string",
      "InitiatedDate": "string",
      "InitiatedAt": "2024-03-28T06:07:58.141Z",
      "MaxDynamicSignatures": 0,
      "MaxScanDuration": 0,
      "Duration": "string",
      "PolicyDescription": "string",
      "PolicyId": "00000000-0000-0000-0000-000000000000",
      "PolicyUserId": "00000000-0000-0000-0000-000000000000",
      "PolicyIsDefault": true,
      "PolicyIsShared": true,
      "PolicyName": "string",
      "AuthenticationProfileId": "00000000-0000-0000-0000-000000000000",
      "AuthenticationProfileOption": "DontUse",
      "ReportPolicyDescription": "string",
      "ReportPolicyId": "00000000-0000-0000-0000-000000000000",
      "ReportPolicyUserId": "00000000-0000-0000-0000-000000000000",
      "ReportPolicyIsDefault": true,
      "ReportPolicyIsShared": true,
      "ReportPolicyName": "string",
      "Scope": "EnteredPathAndBelow",
      "SubPathMaxDynamicSignatures": 0,
      "TargetPath": "string",
      "TargetUrl": "string",
      "TargetUrlRoot": "string",
      "TimeWindow": {
        "Items": [
          {
            "Day": "Sunday",
            "From": "string",
            "ScanningAllowed": true,
            "To": "string"
          }
        ]
      },
      "TotalVulnerabilityCount": 0,
      "UrlRewriteAnalyzableExtensions": "string",
      "UrlRewriteBlockSeparators": "string",
      "UrlRewriteMode": "None",
      "UrlRewriteRules": [
        {
          "PlaceholderPattern": "string",
          "RegexPattern": "string"
        }
      ],
      "UrlRewriteExcludedLinks": [
        {
          "ExcludedPath": "string",
          "IsRegex": true
        }
      ],
      "UserId": "00000000-0000-0000-0000-000000000000",
      "VcsCommitInfo": {
        "CiBuildConfigurationName": "string",
        "CiBuildHasChange": true,
        "CiBuildId": "string",
        "CiBuildServerName": "string",
        "CiBuildServerVersion": "string",
        "CiBuildUrl": "string",
        "CiNcPluginVersion": "string",
        "CiTimestamp": "2024-03-28T06:07:58.142Z",
        "ComitterId": "00000000-0000-0000-0000-000000000000",
        "Committer": "string",
        "CommitterName": "string",
        "CommitterOverride": "string",
        "IntegrationSystem": "Teamcity",
        "IsCommiterExistAndAuthorizedInNc": true,
        "VcsName": "string",
        "VcsVersion": "string"
      },
      "WebsiteName": "string",
      "WebsiteUrl": "string",
      "WebsiteDescription": "string",
      "WebsiteProtocol": "Http",
      "WebsiteIsDeleted": true,
      "IsWebsiteLatestCompletedFullScanTask": true,
      "EnablePciScanTask": true,
      "PciScanTask": {
        "Name": "string",
        "Progress": 0,
        "ScanState": "New",
        "ComplianceStatus": "Scanning",
        "EndDate": "2024-03-28T06:07:58.142Z"
      },
      "UserName": "string",
      "QueuedScanTaskExist": true,
      "ScanTaskProfileId": "00000000-0000-0000-0000-000000000000",
      "ScanTaskProfile": {
        "Id": "00000000-0000-0000-0000-000000000000",
        "IsMine": true,
        "IsPrimary": true,
        "IsShared": true,
        "Name": "string",
        "TargetUrl": "string",
        "ScanPolicyName": "string",
        "Tags": [
          "string"
        ]
      },
      "WebsiteGroupIds": [
        "00000000-0000-0000-0000-000000000000"
      ],
      "Comments": "string",
      "BusinessLogicRecorderSetting": {
        "SequenceModelList": [
          {
            "Name": "string",
            "BusinessLogicRecorderSettings": "string"
          }
        ]
      },
      "ScanProfileChanged": true,
      "CompletedSteps": 0,
      "EstimatedLaunchTime": 0,
      "EstimatedSteps": 0,
      "FailureReason": "None",
      "FailureReasonDescription": "string",
      "FailureReasonString": "string",
      "GlobalThreatLevel": "Unknown",
      "GlobalVulnerabilityCriticalCount": 0,
      "GlobalVulnerabilityHighCount": 0,
      "GlobalVulnerabilityInfoCount": 0,
      "GlobalVulnerabilityBestPracticeCount": 0,
      "GlobalVulnerabilityLowCount": 0,
      "GlobalVulnerabilityMediumCount": 0,
      "Id": "00000000-0000-0000-0000-000000000000",
      "IsCompleted": true,
      "Percentage": 0,
      "Phase": "Pending",
      "ScanTaskGroupId": "00000000-0000-0000-0000-000000000000",
      "ScanType": "Full",
      "ScheduledScanId": "00000000-0000-0000-0000-000000000000",
      "State": "Queued",
      "StateChanged": "2024-03-28T06:07:58.142Z",
      "ThreatLevel": "Unknown",
      "VulnerabilityCriticalCount": 0,
      "VulnerabilityHighCount": 0,
      "VulnerabilityInfoCount": 0,
      "VulnerabilityBestPracticeCount": 0,
      "VulnerabilityLowCount": 0,
      "VulnerabilityMediumCount": 0,
      "WebsiteId": "00000000-0000-0000-0000-000000000000",
      "Initiated": "2024-03-28T06:07:58.142Z",
      "Tags": [
        "string"
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **AdditionalWebsites** (array)
    - **Canonical** (boolean)
    - **TargetUrl** (string)
  - **AgentId** (string)
  - **AgentName** (string)
  - **Cookies** (string)
  - **CrawlAndAttack** (boolean)
  - **DeletedOn** (string)
  - **EnableHeuristicChecksInCustomUrlRewrite** (boolean)
  - **ExcludedLinks** (string)
  - **ExcludeLinks** (boolean)
  - **DisallowedHttpMethods** (string)
  - **FindAndFollowNewLinks** (boolean)
  - **ImportedLinks** (string)
  - **AllImportedLinks** (string)
  - **DesktopScanId** (string)
  - **InitiatedTime** (string)
  - **InitiatedDate** (string)
  - **InitiatedAt** (string)
  - **MaxDynamicSignatures** (number)
  - **MaxScanDuration** (number)
  - **Duration** (string)
  - **PolicyDescription** (string)
  - **PolicyId** (string)
  - **PolicyUserId** (string)
  - **PolicyIsDefault** (boolean)
  - **PolicyIsShared** (boolean)
  - **PolicyName** (string)
  - **AuthenticationProfileId** (string)
  - **AuthenticationProfileOption** (string)
  - **ReportPolicyDescription** (string)
  - **ReportPolicyId** (string)
  - **ReportPolicyUserId** (string)
  - **ReportPolicyIsDefault** (boolean)
  - **ReportPolicyIsShared** (boolean)
  - **ReportPolicyName** (string)
  - **Scope** (string)
  - **SubPathMaxDynamicSignatures** (number)
  - **TargetPath** (string)
  - **TargetUrl** (string)
  - **TargetUrlRoot** (string)
  - **TimeWindow** (object)
    - **Items** (array)
      - **Day** (string)
      - **From** (string)
      - **ScanningAllowed** (boolean)
      - **To** (string)
  - **TotalVulnerabilityCount** (number)
  - **UrlRewriteAnalyzableExtensions** (string)
  - **UrlRewriteBlockSeparators** (string)
  - **UrlRewriteMode** (string)
  - **UrlRewriteRules** (array)
    - **PlaceholderPattern** (string)
    - **RegexPattern** (string)
  - **UrlRewriteExcludedLinks** (array)
    - **ExcludedPath** (string)
    - **IsRegex** (boolean)
  - **UserId** (string)
  - **VcsCommitInfo** (object)
    - **CiBuildConfigurationName** (string)
    - **CiBuildHasChange** (boolean)
    - **CiBuildId** (string)
    - **CiBuildServerName** (string)
    - **CiBuildServerVersion** (string)
    - **CiBuildUrl** (string)
    - **CiNcPluginVersion** (string)
    - **CiTimestamp** (string)
    - **ComitterId** (string)
    - **Committer** (string)
    - **CommitterName** (string)
    - **CommitterOverride** (string)
    - **IntegrationSystem** (string)
    - **IsCommiterExistAndAuthorizedInNc** (boolean)
    - **VcsName** (string)
    - **VcsVersion** (string)
  - **WebsiteName** (string)
  - **WebsiteUrl** (string)
  - **WebsiteDescription** (string)
  - **WebsiteProtocol** (string)
  - **WebsiteIsDeleted** (boolean)
  - **IsWebsiteLatestCompletedFullScanTask** (boolean)
  - **EnablePciScanTask** (boolean)
  - **PciScanTask** (object)
    - **Name** (string)
    - **Progress** (number)
    - **ScanState** (string)
    - **ComplianceStatus** (string)
    - **EndDate** (string)
  - **UserName** (string)
  - **QueuedScanTaskExist** (boolean)
  - **ScanTaskProfileId** (string)
  - **ScanTaskProfile** (object)
    - **Id** (string)
    - **IsMine** (boolean)
    - **IsPrimary** (boolean)
    - **IsShared** (boolean)
    - **Name** (string)
    - **TargetUrl** (string)
    - **ScanPolicyName** (string)
    - **Tags** (array)
  - **WebsiteGroupIds** (array)
  - **Comments** (string)
  - **BusinessLogicRecorderSetting** (object)
    - **SequenceModelList** (array)
      - **Name** (string)
      - **BusinessLogicRecorderSettings** (string)
  - **ScanProfileChanged** (boolean)
  - **CompletedSteps** (number)
  - **EstimatedLaunchTime** (number)
  - **EstimatedSteps** (number)
  - **FailureReason** (string)
  - **FailureReasonDescription** (string)
  - **FailureReasonString** (string)
  - **GlobalThreatLevel** (string)
  - **GlobalVulnerabilityCriticalCount** (number)
  - **GlobalVulnerabilityHighCount** (number)
  - **GlobalVulnerabilityInfoCount** (number)
  - **GlobalVulnerabilityBestPracticeCount** (number)
  - **GlobalVulnerabilityLowCount** (number)
  - **GlobalVulnerabilityMediumCount** (number)
  - **Id** (string)
  - **IsCompleted** (boolean)
  - **Percentage** (number)
  - **Phase** (string)
  - **ScanTaskGroupId** (string)
  - **ScanType** (string)
  - **ScheduledScanId** (string)
  - **State** (string)
  - **StateChanged** (string)
  - **ThreatLevel** (string)
  - **VulnerabilityCriticalCount** (number)
  - **VulnerabilityHighCount** (number)
  - **VulnerabilityInfoCount** (number)
  - **VulnerabilityBestPracticeCount** (number)
  - **VulnerabilityLowCount** (number)
  - **VulnerabilityMediumCount** (number)
  - **WebsiteId** (string)
  - **Initiated** (string)
  - **Tags** (array)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Content-Length | string |
| Connection | string |
| Cache-Control | string |
| Pragma | string |
| Expires | string |
| X-Content-Type-Options | string |
| X-Frame-Options | string |
| Referrer-Policy | string |
| X-XSS-Protection | string |
| Origin-Trial | string |
| Strict-Transport-Security | string |
| Expect-CT | string |