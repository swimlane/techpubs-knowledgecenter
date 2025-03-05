List Impersonating Domain Alerts
================================
Retrieve a list of impersonating domain alerts.


Inputs
~~~~~~


*Parameters*                    (*object*)  

  *Offset*                    (*number*)

    :Description: The (zero-based) offset of the first item in the collection to return. Must be any value between 0 and 100.

    ..

    :Example: 0

    ..  

  *Limit*                    (*number*)

    :Description: The maximum number of items to return. Will default to 10 unless using id which will default to the number of ids provided. Must be any value between 0 and 100.

    ..

    :Example: 10

    ..  

  *ID*                    (*array*)

    :Description: One or more alert identifiers to resolve. Must provide between 1 and 100 items.

    ..

    :Example: ['799098e1-d380-4f64-a8d1-2de0b265a0b8']

    ..
Outputs
~~~~~~~


*Status Code*                    (*number*)

  :Example: 200

  ..

*Response Headers*                    (*object*)  

  *Date*                    (*string*)

    :Example: Mon, 15 Jul 2024 05:58:09 GMT

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

    :Example: 4CPH9JPBRKNBK

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

    :Example: 51

    ..  

  *Retry After*                    (*string*)

    :Example: 51

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

  :Example: [{'id': 'e9d84d52-818e-442d-8e1a-578677ddec27', 'portal-id': 'BBCBBQ', 'risk-type': 'impersonating-domain', 'classification': 'impersonating-domain-alert', 'risk-assessment': {'risk-level': 'medium'}, 'risk-factors': ['Has assets in content', 'Has logos in content', 'Domain in threat feed', 'Referencing website content', 'Has a DNS record', 'Newly registered when raised'], 'title': 'Impersonating Domain - idomain241.com', 'description': 'Each alert risk type will have a templated description intended for display, or ingest by a freetext indexing system.\n\nThis template can change at any time, so the description must NOT be parsed based on the assumption that the format cannot change.', 'assets': [{'id': '16be54a5-2b6c-4363-baea-c6f6da534546'}, {'id': '18367ce9-24a0-4631-aa64-13be5eadf0be'}], 'raised': '2024-06-17T16:59:39.633875225Z', 'updated': '2024-06-17T16:59:39.633875225Z', 'mitre-attack-mapping': None, 'domain': 'idomain241.com'}]

  ..