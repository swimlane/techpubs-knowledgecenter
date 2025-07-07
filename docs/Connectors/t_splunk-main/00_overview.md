# Cisco Splunk Connector
## Overview
The Cisco Splunk connector enables streamlined interactions with Splunk's data analytics and search functionalities, allowing users to perform and manage searches, create and edit events, and retrieve search results.

Cisco Splunk is a powerful platform for searching, monitoring, and analyzing machine-generated big data. This connector allows Swimlane Turbine users to automate the creation of events, execution of searches, and management of notable events within Splunk. By integrating with Cisco Splunk, Swimlane Turbine users can streamline incident logging, enhance search capabilities, and manage notable events efficiently, leading to faster threat detection and response. The connector's actions are designed to support complex security operations without the need for manual coding, enabling a more agile and responsive security posture.

### Limitations

None to date.

### Supported Versions

* Splunk Enterprise
* Splunk Cloud

V1 or V2 endpoints will be called based on the version in the asset configuration. Defaults to 9.0.1

### Additional Docs

* Splunk's [REST API Reference](https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTprolog)

## Configuration

### Prerequisites


To effectively utilize the Cisco Splunk connector for Swimlane Turbine, ensure you have the following prerequisites:
- HTTP Basic Authentication with these parameters:
  * URL: Endpoint URL for the Cisco Splunk instance
  * Username: Your Cisco Splunk account username
  * Password: Your Cisco Splunk account password
- HTTP Bearer Token Authentication with these parameters:
  * URL: Endpoint URL for the Cisco Splunk instance
  * Token: A valid bearer token for authentication


## Authentication Methods

To effectively utilize the Cisco Splunk connector with Swimlane Turbine, ensure you have the following prerequisites:
#### HTTP Basic Authentication with the following parameters:
  * URL: Endpoint for the Splunk API.
  * Username: Your Splunk account username.
  * Password: Your Splunk account password.

#### HTTP Bearer [Token Authentication](https://docs.splunk.com/Documentation/Splunk/9.1.1/Security/UseAuthTokens) with the following parameters:
  * URL: Endpoint for the Splunk API.
  * Token: A valid bearer token such as a JWT for authenticating API requests.

Generally, the port must be set to **8089** when connecting to Splunk.


## Capabilities

The Cisco Splunk connector has the following capabilities:

* Create Event
* Create Search
* Dispatch Name Saved Search
* Edit Notable Events
* Get Saved Search
* Get Search
* Get Search Results
* One-Shot Search
* Run Search with Polling

### Generic

Actions that contain the output_mode parameter allow for:

* `json` - JSON output (default)
* `csv` - CSV output.
* `xml` - XML output.
* `raw` - Raw output.

### Create Event
Create events from the contents contained in the HTTP body.

The edit_tcp capability is additionally required for this endpoint.

### Create Search

This action will not return the search results. This action will return the search id.
It is important that the search might take some time in Splunk and might not be immediately available for fetching the results.

data_body examples:

Search for notable events in the last 5 minutes
```yaml
  search: 'search index=notable earliest=-5m'
```
Count HTTP 200 responses grouped by URI path:
```yaml
  search: 'search sourcetype=access_combined status=200 | stats count by uri_path'
```
Lookup data from a CSV file
```yaml
  search: '| inputlookup mylookup'
```
Splunk's documentation for this endpoint can be found [here](https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTsearch#search.2Fjobs)
### Edit Notable Events

Splunk's documentation for this endpoint can be found [here](https://docs.splunk.com/Documentation/ES/7.3.2/API/NotableEventAPIreference)
### Get Saved Search
Access the named saved search.

Splunk's documentation for this endpoint can be found [here](https://docs.splunk.com/Documentation/Splunk/9.3.1/RESTREF/RESTsearch#saved.2Fsearches.2F.7Bname.7D)
### Get Search
The user ID is implied by the authentication to the call.

The dispatchState field can be one of the following values:
* QUEUED
* PARSING
* RUNNING
* FINALIZING
* DONE
* PAUSE
* INTERNAL_CANCEL 
* USER_CANCEL
* BAD_INPUT_CANCEL
* QUIT
* FAILED

Splunk's documentation for this endpoint can be found [here](https://docs.splunk.com/Documentation/Splunk/9.3.1/RESTREF/RESTsearch#search.2Fjobs.2F.7Bsearch_id.7D)
### Get Search Results

The output_mode parameter for this action allows for:
* `json` - JSON output (default)
* `csv` - CSV output.
* `xml` - XML output.
* `raw` - Raw output.
* `json_cols` - JSON output with columns.
* `json_rows` - JSON output with rows.
* `row` - Row output.
* `atom` - Atom output.

Splunks documentation for this endpoint can be found [here](https://docs.splunk.com/Documentation/Splunk/9.3.1/RESTREF/RESTsearch#search.2Fjobs.2F.7Bsearch_id.7D.2Fresults)
### One-Shot Search

This action will run a search and return the results in a single call. 

#### Inputs

* **Search**:

Retrieve the first 10 events from the _internal index:
```yaml
  search_string: 'index=_internal | head 10
```
Find and count 404 errors by URI path:
```yaml
  search_string: 'search sourcetype=access_combined status=404 | stats count by uri_path'
```
Use tstats to count events by host:
```yaml
  search_string: '| tstats count where index=* by host'
```

* **add_search**:

If set to true, the keyword search will be prepended to your search_string unless it already starts with a pipe (|) or another generating command.
```yaml
add_search: true
search_string: 'index=main error'
# The executed search will be: 'search index=main error'
```
```yaml
add_search: false
search_string: '| inputlookup my_lookup_table'
# The executed search will be: '| inputlookup my_lookup_table'
```

* **earliest_time and latest_time**:

```yaml
earliest_time: '-1h'
```
```yaml
earliest_time: '2023-07-01T00:00:00Z'
```

* **app**:

Run search in the default Search app:
```yaml
app: 'search'
```
Run search in the Search & Reporting app:
```yaml
app: 'SplunkEnterpriseSecuritySuite'
```

* **parse_json**:

Due to a known Splunk issue with malformed JSON outputs, setting this to true will attempt to correct and parse the JSON response