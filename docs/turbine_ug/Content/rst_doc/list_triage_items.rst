List Triage Items
=================
Retrieve triage items from given triage event IDs.


Inputs
~~~~~~


*Parameters*                    (*object*)  

  *ID*                    (*array*)

    :Description: One or more triage item identifiers to resolve. Must provide between 1 and 100 items.

    ..

    :Example: ['c10407f2-1aec-4b35-b6c3-086b396eb824', 'f40be971-ecea-4f25-ab33-f4f2566b12ab']

    ..  

  *Offset*                    (*number*)

    :Description: The (zero-based) offset of the first item in the collection to return. Must be any value between 0 and 1000.

    ..

    :Example: 0

    ..  

  *Limit*                    (*number*)

    :Description: The maximum number of items to return. Will default to 10 unless using id which will default to the number of ids provided. Must be any value between 0 and 1000.

    ..

    :Example: 10

    ..  

  *Portal Shortcode*                    (*array*)

    :Description: One or more triage item portal-shortcode to resolve. Must provide between 1 and 100 items.

    ..
Outputs
~~~~~~~


*Status Code*                    (*number*)

  :Example: 200

  ..

*Response Headers*                    (*object*)  

  *Date*                    (*string*)

    :Example: Fri, 12 Jul 2024 07:34:57 GMT

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

    :Example: EHOF7VR5NLJJN

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

    :Example: 2

    ..  

  *Retry After*                    (*string*)

    :Example: 2

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

  :Example: [{'id': '77d21124-c5e6-4386-be23-072eddc319f9', 'risk-type': 'unauthorized-code-commit', 'classification': 'unauthorized-code-commit-alert', 'state': 'unread', 'portal-shortcode': 'BBCBBB', 'portal-id': 'BBCBBB', 'title': 'Unauthorized Code Commit - https://github.com/topuserBBJjdoqF/examplerepoEStiAuRF', 'risk-level': 'medium', 'raised': '2024-06-17T10:59:40.845840534Z', 'updated': '2024-06-17T10:59:40.845840534Z', 'source-updated': '2024-06-17T10:59:40.845840534Z', 'source': {'alert-id': '7f0a23d0-fd8e-43ce-b267-e6386af876cf', 'incident-id': None}, 'assignee': None}, {'id': '4b4286b3-f11b-427e-98ff-3b5a50bab47e', 'risk-type': 'weak-certificate', 'classification': 'domain-certificate-issue-incident', 'state': 'unread', 'portal-shortcode': 'BBCBBC', 'portal-id': '952573', 'title': 'A type specific title', 'risk-level': 'medium', 'raised': '2024-06-17T10:59:40.943508223Z', 'updated': '2024-06-17T10:59:40.943508223Z', 'source-updated': '2024-06-17T10:59:40.943508223Z', 'source': {'alert-id': None, 'incident-id': 952573}, 'assignee': None}]

  ..