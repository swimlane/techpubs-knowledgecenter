# Create Triage Item Comment

## Description
Create a new comment on a specific triage item in Digital Shadows Search Light using the 'triage-id' and 'content' provided.

## Inputs
### Path_parameters
**Triage ID**: Identifier of the triage item which comments belongs.
  - Examples: ['77d21124-c5e6-4386-be23-072eddc319f9']
  - Type: string

### Json_body
**Content**: The comment text content. Must not include the null character.
  - Examples: ['A custom comment has been created!']
  - Type: string

## Outputs
### Example
**Status_code**: 200
**Response_headers**: {'Date': 'Mon, 15 Jul 2024 05:44:34 GMT', 'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'X-Correlation-Id': 'AQTI3K9F413A', 'Vary': 'Origin, Access-Control-Request-Method, Access-Control-Request-Headers', 'ratelimit-limit': '100', 'ratelimit-remaining': '99', 'ratelimit-reset': '28', 'retry-after': '28', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1; mode=block', 'Cache-Control': 'no-cache, no-store, max-age=0, must-revalidate', 'Pragma': 'no-cache', 'Expires': '0', 'X-Frame-Options': 'DENY'}
**Reason**: 
**Json_body**: {'id': '6ff2e3ad-92d7-40a0-b4cd-74b3a5a4ec68', 'triage-item-id': '77d21124-c5e6-4386-be23-072eddc319f9', 'content': 'A custom comment has been created!', 'user': {'id': '29f01f82-76c7-4cb9-89b9-3103a531de94', 'name': '[HIB2TO:199023892748]'}, 'created': '2024-07-15T05:44:31.351068063Z', 'updated': '2024-07-15T05:44:31.351068063Z'}

## Meta
**Endpoint**: /v1/triage-items/{{triage-id}}/comments
**Method**: POST
