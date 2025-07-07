# Dispatch Name Saved Search

**Description**: Executes a predefined saved search in Cisco Splunk using the 'name' parameter provided in the path.

## Endpoint

- **URL:** `/services/saved/searches/{{name}}/dispatch`
- **Method:** `POST`
## Inputs

- **data_body** (object) – Required
  - **args.index_name** (string): Arg values to create a saved search is the saved search if a template search.
  - **dispatchAs** (string): Indicate the user context, quota, and access rights for the saved search. The saved search runs according to the context indicated.
  - **dispatch.now** (boolean): Dispatch the search as if the specified time for this parameter was the current time.
  - **dispatch.adhoc_search_level** (string): The level of adhoc search to run. The default is smart, which runs the search at the level specified in the saved search.
  - **force_dispatch** (boolean): Indicates whether to start a new search even if another instance of this search is already running.
  - **trigger_actions** (string): Indicates whether to trigger alert actions.
  - **replay_speed** (number): Indicate a real-time search replay speed factor. For example, 1 indicates normal speed. 0.5 indicates half of normal speed, and 2 indicates twice as fast as normal. earliest_time and latest_time arguments must indicate a real-time time range to use replay options.
  - **replay_et** (string): Relative "wall clock" start time for the replay.
  - **replay_lt** (string): Relative end time for the replay clock. The replay stops when clock time reaches this time.
- **path_parameters** (object) – Required
  - **name** (string) – Required: The name of the saved search to dispatch.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {}
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)