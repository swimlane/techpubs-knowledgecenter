# Generic Task

**Description**: Execute a generic task in Okta Identity Management, offering complete control over the request parameters.

## Inputs

- **endpoint** (string): Path to the endpoint after url in asset. Use double brackets with path parameters for dynamic URLs.
- **method** (string): Method of the request such as: POST, GET, PUT, PATCH, DELETE. (Note, others are available to use)
- **path_parameters** (object): Path Parameters to mustache into the endpoint input.
- **parameters** (object): URL query parameters that get appended and url encoded.
- **json_body** (object): Body to send as a JSON payload, this automatically sets Content-Type: application/json in the headers.
- **data_body** (object): Body to send as data, this allows you to set the content-type in the headers manually.
- **headers** (object): Request headers to send with the individual request.
## Output

### Output Parameters

- **status_code** (number): The HTTP response status code
- **data** (object): The JSON response body
- **response_text** (string)
- **reason** (string): The HTTP reason, often times an error message can be here. OK means success.