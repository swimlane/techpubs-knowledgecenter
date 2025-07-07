# One-shot Search

**Description**: Performs a one-time search in Cisco Splunk with a specified string and imports results into Swimlane records. Requires 'search_string'.

## Inputs

- **search_string** (string) – Required: Splunk Search Query. Eg index=_internal | head 10
- **add_search** (boolean): If True 'search' will be added to the start of the search string.  false will leave the 'search' prefix. Defaults to 'True'.
- **earliest_time** (string): This can be any standard datetime format supported by pendulum or a relative datetime. Format example is 2020-01-18T18:34:04Z or -1h
- **latest_time** (string): This can be any standard datetime format supported by pendulum or a relative datetime. Format example is 2020-01-18T18:34:04Z -1h
- **owner** (string): The owner's Splunk username. Eg admin
- **app** (string): The app to run the search in. Eg search
- **parse_json** (boolean): Splunk has a know bug that causes the JSON to be malformed. This will attempt to fix the JSON before parsing it. Defaults to true.
- **latest_result_head** (boolean): Returns the first result of response.
- **latest_result_tail** (boolean): Returns the last result of response.
## Output

### Example

```json
[
  {
    "json_body": [
      {
        "_bkt": "main~347~8A6B8C24-39C2-41D1-A0DE-53A1E4936F43",
        "_cd": "347:962465689",
        "_indextime": "1688236453",
        "_raw": "{\"attributes\":{\"logging.googleapis.com/timestamp\":\"2023-07-01T18:34:03.14Z\"},\"publish_time\":1593195281.507,\"data\":{\"insertId\":\"bnn247d1uuw\",\"protoPayload\":{\"resourceName\":\"projects/344444931094/zones/<#token_region#>/instances/<#token_instance_name#>\",\"authenticationInfo\":{\"principalEmail\":\"gsa_labs2@splunk.com\"},\"serviceName\":\"compute.googleapis.com\",\"request\":{\"@type\":\"type.googleapis.com/compute.instances.insert\"},\"@type\":\"type.googleapis.com/google.cloud.audit.AuditLog\",\"requestMetadata\":{\"callerSuppliedUserAgent\":\"GCE Managed Instance Group\"},\"methodName\":\"v1.compute.instances.insert\"},\"operation\":{\"last\":true,\"id\":\"operation-1593195275250-5a900ae706aac-9dd8bd24-20ca32d0\",\"producer\":\"compute.googleapis.com\"},\"timestamp\":\"2023-07-01T18:34:03\",\"receiveTimestamp\":\"2023-07-01T18:34:03.000000305578Z\",\"resource\":{\"labels\":{\"instance_id\":\"1129295029103986148\",\"project_id\":\"refined-copilot-275702\",\"zone\":\"<#token_region#>\"},\"type\":\"gce_instance\"},\"logName\":\"projects/refined-copilot-275702/logs/cloudaudit.googleapis.com%2Factivity\",\"severity\":\"NOTICE\"}}\n",
        "_serial": "0",
        "_si": [
          "splunk813",
          "main"
        ],
        "_sourcetype": "google:gcp:pubsub:audit",
        "_subsecond": ".14",
        "_time": "2023-07-01 18:34:03.140 UTC",
        "host": "127.0.0.1",
        "index": "main",
        "linecount": "2",
        "source": "google_gcp_pubsub_audit_instances_eventgen",
        "sourcetype": "google:gcp:pubsub:audit",
        "splunk_server": "splunk813"
      },
      {
        "_bkt": "main~347~8A6B8C24-39C2-41D1-A0DE-53A1E4936F43",
        "_cd": "347:962471023",
        "_indextime": "1688236457",
        "_raw": "{\"name\":\"475462518164251999999999_ebabb804-6b04-47546-b8ff-a27742ca3fb7\",\"type\":\"Microsoft.Security/Locations/alerts\",\"id\":\"/subscriptions/475461213b189-13ff-42fe-b370-df6da421bce1/resourceGroups/bots/providers/Microsoft.Security/locations/uksouth/alerts/475462518164251999999999_ebabb804-6b04-47546-b8ff-a27742ca3fb7\",\"properties\":{\"alertName\":\"Network_TrafficFromUnrecommendedIP\",\"confidenceReasons\":[],\"subscriptionId\":\"475461213b189-13ff-42fe-b370-df6da421bce1\",\"entities\":[{\"type\":\"azure-resource\",\"resourceId\":\"/subscriptions/475461213b189-13ff-42fe-b370-df6da421bce1/resourcegroups/bots/providers/microsoft.compute/virtualmachines/splunkhf047546\",\"$id\":\"uksouth_1\"},{\"type\":\"host\",\"$id\":\"uksouth_2\",\"azureID\":\"/subscriptions/475461213b189-13ff-42fe-b370-df6da421bce1/resourcegroups/bots/providers/microsoft.compute/virtualmachines/splunkhf047546\"},{\"address\":\"216.223.104.50\",\"type\":\"ip\",\"location\":{\"latitude\":32.04583,\"state\":\"Jiangsu\",\"countryCode\":\"CN\",\"countryName\":\"China\",\"longitude\":118.78417,\"city\":\"Nanjing\",\"asn\":23650},\"$id\":\"uksouth_3\"},{\"address\":\"92.88.112.115\",\"type\":\"ip\",\"location\":{\"latitude\":31.17389,\"state\":\"ShanghaiShi\",\"countryCode\":\"CN\",\"countryName\":\"China\",\"longitude\":121.41498,\"city\":\"XuhuiQu\",\"asn\":4134},\"$id\":\"uksouth_4\"}],\"workspaceArmId\":\"/subscriptions/475461213b189-13ff-42fe-b370-df6da421bce1/resourcegroups/defaultresourcegroup-cus/providers/microsoft.operationalinsights/workspaces/defaultworkspace-475461213b189-13ff-42fe-b370-df6da421bce1-cus\",\"canBeInvestigated\":true,\"associatedResource\":\"/subscriptions/475461213b189-13ff-42fe-b370-df6da421bce1/resourcegroups/bots/providers/microsoft.compute/virtualmachines/splunkhf047546\",\"reportedTimeUtc\":\"2023-07-01T18:34:03\",\"extendedProperties\":{\"protocol\":\"TCP\",\"resourceType\":\"VirtualMachine\",\"destinationPort\":\"22\",\"investigationSteps\":\"1.ReviewtheIPaddressesanddetermineiftheyshouldbecommunicatingwiththevirtualmachine\\r\\n2.EnforcethehardeningrulerecommendedbySecurityCenterwhichwillallowaccessonlytorecommendedIPaddresses.Youcanedittherule'spropertiesandchangetheIPaddressestobeallowed,oralternativelyedittheNetworkSecurityGroup'srulesdirectly\",\"sourceIP(s)[#attempts]\":\"IP:216.223.104.50[1]\\r\\nIP:92.88.112.115[1]\"},\"reportedSeverity\":\"Low\",\"state\":\"Active\",\"instanceId\":\"ebabb804-6b04-47546-b8ff-a27742ca3fb7\",\"alertDisplayName\":\"TrafficdetectedfromIPaddressesrecommendedforblocking\",\"isIncident\":false,\"actionTaken\":\"Undefined\",\"description\":\"AzureSecurityCenterdetectedinboundtrafficfromIPaddressesthatarerecommendedtobeblocked.ThistypicallyoccurswhenthisIPaddressdoesn'tcommunicateregularlywiththisresource.\\r\\nAlternatively,theIPaddresshasbeenflaggedasmaliciousbySecurityCenter'sthreatintelligencesources.\",\"remediationSteps\":\"{\\\"kind\\\":\\\"openBlade\\\",\\\"displayValue\\\":\\\"Enforcerule\\\",\\\"extension\\\":\\\"Microsoft_Azure_Security_R3\\\",\\\"detailBlade\\\":\\\"AdaptiveNetworkControlsResourceBlade\\\",\\\"detailBladeInputs\\\":\\\"protectedResourceId=/subscriptions/475461213b189-13ff-42fe-b370-df6da421bce1/resourcegroups/bots/providers/microsoft.compute/virtualmachines/splunkhf047546\\\"}\",\"compromisedEntity\":\"splunkhf047546\",\"vendorName\":\"Microsoft\",\"detectedTimeUtc\":\"2023-07-01T18:34:03\"}}\n",
        "_serial": "1",
        "_si": [
          "splunk813",
          "main"
        ],
        "_sourcetype": "azure:securityCenter:alert",
        "_time": "2023-07-01 18:34:03.000 UTC",
        "host": "127.0.0.1",
        "index": "main",
        "linecount": "2",
        "source": "azure_securityCenter_alert_eventgen",
        "sourcetype": "azure:securityCenter:alert",
        "splunk_server": "splunk813"
      },
      {
        "_bkt": "main~347~8A6B8C24-39C2-41D1-A0DE-53A1E4936F43",
        "_cd": "347:962469982",
        "_indextime": "1688236457",
        "_raw": "{\"name\":\"420352518164251999999999_ebabb804-6b04-42035-b8ff-a27742ca3fb7\",\"type\":\"Microsoft.Security/Locations/alerts\",\"id\":\"/subscriptions/420351213b189-13ff-42fe-b370-df6da421bce1/resourceGroups/bots/providers/Microsoft.Security/locations/westus/alerts/420352518164251999999999_ebabb804-6b04-42035-b8ff-a27742ca3fb7\",\"properties\":{\"alertName\":\"Network_TrafficFromUnrecommendedIP\",\"confidenceReasons\":[],\"subscriptionId\":\"420351213b189-13ff-42fe-b370-df6da421bce1\",\"entities\":[{\"type\":\"azure-resource\",\"resourceId\":\"/subscriptions/420351213b189-13ff-42fe-b370-df6da421bce1/resourcegroups/bots/providers/microsoft.compute/virtualmachines/splunkhf042035\",\"$id\":\"westus_1\"},{\"type\":\"host\",\"$id\":\"westus_2\",\"azureID\":\"/subscriptions/420351213b189-13ff-42fe-b370-df6da421bce1/resourcegroups/bots/providers/microsoft.compute/virtualmachines/splunkhf042035\"},{\"address\":\"107.184.36.92\",\"type\":\"ip\",\"location\":{\"latitude\":32.04583,\"state\":\"Jiangsu\",\"countryCode\":\"CN\",\"countryName\":\"China\",\"longitude\":118.78417,\"city\":\"Nanjing\",\"asn\":23650},\"$id\":\"westus_3\"},{\"address\":\"92.88.112.115\",\"type\":\"ip\",\"location\":{\"latitude\":31.17389,\"state\":\"ShanghaiShi\",\"countryCode\":\"CN\",\"countryName\":\"China\",\"longitude\":121.41498,\"city\":\"XuhuiQu\",\"asn\":4134},\"$id\":\"westus_4\"}],\"workspaceArmId\":\"/subscriptions/420351213b189-13ff-42fe-b370-df6da421bce1/resourcegroups/defaultresourcegroup-cus/providers/microsoft.operationalinsights/workspaces/defaultworkspace-420351213b189-13ff-42fe-b370-df6da421bce1-cus\",\"canBeInvestigated\":true,\"associatedResource\":\"/subscriptions/420351213b189-13ff-42fe-b370-df6da421bce1/resourcegroups/bots/providers/microsoft.compute/virtualmachines/splunkhf042035\",\"reportedTimeUtc\":\"2023-07-01T18:34:03\",\"extendedProperties\":{\"protocol\":\"TCP\",\"resourceType\":\"VirtualMachine\",\"destinationPort\":\"22\",\"investigationSteps\":\"1.ReviewtheIPaddressesanddetermineiftheyshouldbecommunicatingwiththevirtualmachine\\r\\n2.EnforcethehardeningrulerecommendedbySecurityCenterwhichwillallowaccessonlytorecommendedIPaddresses.Youcanedittherule'spropertiesandchangetheIPaddressestobeallowed,oralternativelyedittheNetworkSecurityGroup'srulesdirectly\",\"sourceIP(s)[#attempts]\":\"IP:107.184.36.92[1]\\r\\nIP:92.88.112.115[1]\"},\"reportedSeverity\":\"Low\",\"state\":\"Active\",\"instanceId\":\"ebabb804-6b04-42035-b8ff-a27742ca3fb7\",\"alertDisplayName\":\"TrafficdetectedfromIPaddressesrecommendedforblocking\",\"isIncident\":false,\"actionTaken\":\"Undefined\",\"description\":\"AzureSecurityCenterdetectedinboundtrafficfromIPaddressesthatarerecommendedtobeblocked.ThistypicallyoccurswhenthisIPaddressdoesn'tcommunicateregularlywiththisresource.\\r\\nAlternatively,theIPaddresshasbeenflaggedasmaliciousbySecurityCenter'sthreatintelligencesources.\",\"remediationSteps\":\"{\\\"kind\\\":\\\"openBlade\\\",\\\"displayValue\\\":\\\"Enforcerule\\\",\\\"extension\\\":\\\"Microsoft_Azure_Security_R3\\\",\\\"detailBlade\\\":\\\"AdaptiveNetworkControlsResourceBlade\\\",\\\"detailBladeInputs\\\":\\\"protectedResourceId=/subscriptions/420351213b189-13ff-42fe-b370-df6da421bce1/resourcegroups/bots/providers/microsoft.compute/virtualmachines/splunkhf042035\\\"}\",\"compromisedEntity\":\"splunkhf042035\",\"vendorName\":\"Microsoft\",\"detectedTimeUtc\":\"2023-07-01T18:34:03\"}}\n",
        "_serial": "2",
        "_si": [
          "splunk813",
          "main"
        ],
        "_sourcetype": "azure:securityCenter:alert",
        "_time": "2023-07-01 18:34:03.000 UTC",
        "host": "127.0.0.1",
        "index": "main",
        "linecount": "2",
        "source": "azure_securityCenter_alert_eventgen",
        "sourcetype": "azure:securityCenter:alert",
        "splunk_server": "splunk813"
      },
      {
        "_bkt": "main~347~8A6B8C24-39C2-41D1-A0DE-53A1E4936F43",
        "_cd": "347:962468403",
        "_indextime": "1688236454",
        "_raw": "{\"insertId\":\"-vw4eqbddh3o\",\"logName\":\"projects/gsa-project-1510183/logs/cloudaudit.googleapis.com%2Factivity\",\"operation\":{\"id\":\"operation-1594833414679-5aa7e17286b93-080f8d1e-e47a162e\",\"last\":true,\"producer\":\"compute.googleapis.com\"},\"protoPayload\":{\"@type\":\"type.googleapis.com/google.cloud.audit.AuditLog\",\"authenticationInfo\":{\"principalEmail\":\"gsa_labs2@splunk.com\"},\"methodName\":\"beta.compute.disks.insert\",\"request\":{\"@type\":\"type.googleapis.com/compute.disks.insert\"},\"requestMetadata\":{\"callerIp\":\"2601:204:c481:85d0:8d7a:8599:34b7:5736\",\"callerSuppliedUserAgent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36,gzip(gfe)\"},\"resourceName\":\"projects/gsa-project-1510183/zones/<#token_region#>/disks/disk4\",\"serviceName\":\"compute.googleapis.com\"},\"receiveTimestamp\":\"2023-07-01T18:34:03.000000235199Z\",\"resource\":{\"labels\":{\"disk_id\":\"6175893735208027369\",\"project_id\":\"gsa-project-1510183\",\"zone\":\"<#token_region#>\"},\"type\":\"gce_disk\"},\"severity\":\"NOTICE\",\"timestamp\":\"2023-07-01T18:34:03\"}\n",
        "_serial": "3",
        "_si": [
          "splunk813",
          "main"
        ],
        "_sourcetype": "google:gcp:pubsub:audit",
        "_time": "2023-07-01 18:34:03.000 UTC",
        "host": "127.0.0.1",
        "index": "main",
        "linecount": "2",
        "source": "google_gcp_pubsub_audit_disks_eventgen",
        "sourcetype": "google:gcp:pubsub:audit",
        "splunk_server": "splunk813"
      },
      {
        "_bkt": "main~347~8A6B8C24-39C2-41D1-A0DE-53A1E4936F43",
        "_cd": "347:962465356",
        "_indextime": "1688236453",
        "_raw": "{\"insertId\":\"-d16si2dees0\",\"logName\":\"projects/gsa-project-151018/logs/cloudaudit.googleapis.com%2Factivity\",\"operation\":{\"id\":\"operation-1594833240214-5aa7e0cc24c27-6bd67487-52539e26\",\"last\":true,\"producer\":\"compute.googleapis.com\"},\"protoPayload\":{\"@type\":\"type.googleapis.com/google.cloud.audit.AuditLog\",\"authenticationInfo\":{\"principalEmail\":\"gsa_labs2@splunk.com\"},\"methodName\":\"v1.compute.instances.start\",\"request\":{\"@type\":\"type.googleapis.com/compute.instances.start\"},\"requestMetadata\":{\"callerIp\":\"2601:204:c481:85d0:8d7a:8599:34b7:5736\",\"callerSuppliedUserAgent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36,gzip(gfe),gzip(gfe)\"},\"resourceName\":\"projects/gsa-project-1510183/zones/<#token_region#>/instances/instance4\",\"serviceName\":\"compute.googleapis.com\"},\"receiveTimestamp\":\"2023-07-01T18:34:03.000000483036Z\",\"resource\":{\"labels\":{\"instance_id\":\"<#token__instanceId#>\",\"project_id\":\"gsa-project-1510183\",\"zone\":\"<#token_region#>\"},\"type\":\"gce_instance\"},\"severity\":\"NOTICE\",\"timestamp\":\"2023-07-01T18:34:03\"} \n",
        "_serial": "4",
        "_si": [
          "splunk813",
          "main"
        ],
        "_sourcetype": "google:gcp:pubsub:audit",
        "_time": "2023-07-01 18:34:03.000 UTC",
        "host": "127.0.0.1",
        "index": "main",
        "linecount": "2",
        "source": "google_gcp_pubsub_audit_instances_eventgen",
        "sourcetype": "google:gcp:pubsub:audit",
        "splunk_server": "splunk813"
      }
    ],
    "status_code": 200,
    "response_headers": {
      "Date": "Mon, 17 Jul 2023 20:53:02 GMT",
      "Expires": "Thu, 26 Oct 1978 00:00:00 GMT",
      "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
      "Content-Type": "application/json; charset=UTF-8",
      "X-Content-Type-Options": "nosniff",
      "Transfer-Encoding": "chunked",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding, Cookie, Authorization",
      "Connection": "Keep-Alive",
      "X-Frame-Options": "SAMEORIGIN",
      "Server": "Splunkd"
    },
    "reason": "OK"
  }
]
```
### Output Parameters

- **json_body** (array)
  - **_bkt** (string)
  - **_cd** (string)
  - **_indextime** (string)
  - **_raw** (string)
  - **_serial** (string)
  - **_si** (array)
  - **_sourcetype** (string)
  - **_subsecond** (string)
  - **_time** (string)
  - **host** (string)
  - **index** (string)
  - **linecount** (string)
  - **source** (string)
  - **sourcetype** (string)
  - **splunk_server** (string)
- **status_code** (number)
- **reason** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Expires | string |
| Cache-Control | string |
| Content-Type | string |
| X-Content-Type-Options | string |
| Transfer-Encoding | string |
| Content-Encoding | string |
| Vary | string |
| Connection | string |
| X-Frame-Options | string |
| Server | string |