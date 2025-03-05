List Incidents
==============
Retrieve a list of incidents.


Inputs
~~~~~~


*Parameters*                    (*object*)  

  *ID*                    (*array*)

    :Description: One or more incident identifiers to resolve. Must provide between 1 and 100 items.

    ..

    :Example: [952573, 952574]

    ..  

  *Offset*                    (*number*)

    :Description: The (zero-based) offset of the first item in the collection to return. Must be any value between 0 and 100.

    ..

    :Example: 0

    ..  

  *Limit*                    (*number*)

    :Description: The maximum number of items to return. Will default to 10 unless using ID which will default to the number of IDs provided. Must provide between 1 and 100 items.

    ..

    :Example: 10

    ..
Outputs
~~~~~~~


*Status Code*                    (*number*)

  :Example: 200

  ..

*Response Headers*                    (*object*)  

  *Date*                    (*string*)

    :Example: Fri, 12 Jul 2024 08:39:14 GMT

    ..  

  *Content-Type*                    (*string*)

    :Example: application/json

    ..  

  *Transfer-Encoding*                    (*string*)

    :Example: chunked

    ..  

  *Connection*                    (*string*)

    :Example: keep-alive

    ..  

  *X-Correlation-Id*                    (*string*)

    :Example: ARA0QC4VQ686K

    ..  

  *Vary*                    (*string*)

    :Example: Origin, Access-Control-Request-Method, Access-Control-Request-Headers

    ..  

  *Ratelimit Limit*                    (*string*)

    :Example: 100

    ..  

  *Ratelimit Remaining*                    (*string*)

    :Example: 99

    ..  

  *Ratelimit Reset*                    (*string*)

    :Example: 45

    ..  

  *Retry After*                    (*string*)

    :Example: 45

    ..  

  *X-Content-Type-Options*                    (*string*)

    :Example: nosniff

    ..  

  *X-XSS-Protection*                    (*string*)

    :Example: 1; mode=block

    ..  

  *Cache-Control*                    (*string*)

    :Example: no-cache, no-store, max-age=0, must-revalidate

    ..  

  *Pragma*                    (*string*)

    :Example: no-cache

    ..  

  *Expires*                    (*string*)

    :Example: 0

    ..  

  *X-Frame-Options*                    (*string*)

    :Example: DENY

    ..

*Reason*                    (*string*)

  :Example: 

  ..

*JSON Body*                    (*array*)

  :Example: [{'id': 952573, 'risk-type': 'weak-certificate', 'classification': 'domain-certificate-issue-incident', 'risk-level': 'medium', 'risk-factors': ['Example risk factor'], 'title': 'A type specific title', 'description': 'Each incident type will have a templated description intended for display, or ingest by a freetext indexing system.\n\nThis template can change at any time, so the description must NOT be parsed based on the assumption that the format cannot change.', 'impact-description': 'A description of the impact this incident may have on your organization', 'mitigation': 'Suggested actions that can be taken to mitigate the incident', 'assets': [{'id': 'a41ca518-9241-4bae-bbf4-ac1e3a339676'}, {'id': '40888aa0-2e4e-4503-ba53-c216d032bcbc'}, {'id': 'fd88ff6d-ee9b-4e79-b466-1e8946b97003'}, {'id': '440f1382-0abc-4086-9b1c-6bebc7805dbf'}], 'raised': '2024-06-17T10:59:40.943508223Z', 'updated': '2024-06-17T10:59:40.943508223Z', 'mitre-attack-mapping': None}, {'id': 952635, 'risk-type': 'weak-certificate', 'classification': 'domain-certificate-issue-incident', 'risk-level': 'very-high', 'risk-factors': ['Example risk factor'], 'title': 'A type specific title', 'description': 'Each incident type will have a templated description intended for display, or ingest by a freetext indexing system.\n\nThis template can change at any time, so the description must NOT be parsed based on the assumption that the format cannot change.', 'impact-description': 'A description of the impact this incident may have on your organization', 'mitigation': 'Suggested actions that can be taken to mitigate the incident', 'assets': [{'id': '1c65ea87-fcd3-46aa-808b-df5a4718171d'}, {'id': '5685880d-4524-43af-84c1-ecf7c908f566'}, {'id': '36b5ad09-e98e-47d1-92e6-a124177eb8f7'}, {'id': '3dfb97a2-4c3c-4ed2-a24c-53657194a480'}], 'raised': '2024-06-17T11:59:40.156831606Z', 'updated': '2024-06-17T11:59:40.156831606Z', 'mitre-attack-mapping': None}]

  ..