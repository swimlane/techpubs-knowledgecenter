List Triage Item Comments
========================
Retrieve a list of comments for a given triage item.


Inputs
~~~~~~


*Path Parameters**                    (*object*)  

  *Triage ID**                    (*string*)

    :Example: 77d21124-c5e6-4386-be23-072eddc319f9

    ..

*Parameters*                    (*object*)  

  *Offset*                    (*number*)

    :Description: The (zero-based) offset of the first item in the collection to return. Must be any value between 0 and 250.

    ..

    :Example: 0

    ..  

  *Limit*                    (*number*)

    :Description: The maximum number of items to return. If unset, the default value will be 10. Must be any value between 0 and 250.

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

    :Example: Mon, 15 Jul 2024 05:52:43 GMT

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

    :Example: BQQ049UQVFF91

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

    :Example: 17

    ..  

  *Retry After*                    (*string*)

    :Example: 17

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

  :Example: [{'id': '6ff2e3ad-92d7-40a0-b4cd-74b3a5a4ec68', 'triage-item-id': '77d21124-c5e6-4386-be23-072eddc319f9', 'content': 'A custom comment has been created!', 'user': {'id': '29f01f82-76c7-4cb9-89b9-3103a531de94', 'name': '[HIB2TO:199023892748]'}, 'created': '2024-07-15T05:44:31.351068063Z', 'updated': '2024-07-15T05:44:31.351068063Z'}, {'id': 'efeb75d8-4102-4ec6-bb2b-54e70d1f72ea', 'triage-item-id': '77d21124-c5e6-4386-be23-072eddc319f9', 'content': 'this is a comment', 'user': {'id': 'ede62927-3276-40d9-a31d-0b37009eabea', 'name': 'TEST2'}, 'created': '2024-06-17T10:59:40.882542018Z', 'updated': '2024-06-17T10:59:40.882542018Z'}]

  ..