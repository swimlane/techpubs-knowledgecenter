Set Triage Item State
=====================
Set the state for a triage item.


Inputs
~~~~~~


*Path Parameters**                    (*object*)  

  *Triage ID**                    (*string*)

    :Description: Identifier of the triage item to set the state for.

    ..

    :Example: 77d21124-c5e6-4386-be23-072eddc319f9
      * 77d21124-c5e6-4386-be23-072edfyrftrv

    ..

*JSON Body**                    (*object*)  

  *State**                    (*string*)

    :Description: The new state to set for the triage item.

    ..

    :Example: open

    ..

    :Possible Values: * open
      * closed
      * unread
      * rejected
      * resolved

    ..  

  *Previous State*                    (*string*)

    :Description: The previous state as last seen prior to requesting this change. Used to confirm that this change is not overwriting a change made by another user in the interim.

    ..

    :Example: closed

    ..

    :Possible Values: * open
      * closed
      * unread
      * rejected
      * resolved

    ..  

  *Comment*                    (*object*)

    :Description: An optional custom comment to include with the state change.

    ..    

    *Content**                    (*string*)

      :Description: The comment text content. Must not include the null character.

      ..

      :Example: A custom comment that is 1-500 characters in length

      ..
Outputs
~~~~~~~


*Status Code*                    (*number*)

  :Example: 204

  ..

*Response Headers*                    (*object*)  

  *Date*                    (*string*)

    :Example: Tue, 16 Jul 2024 05:46:59 GMT

    ..  

  *Connection*                    (*string*)

    :Example: keep-alive

    ..  

  *X-Correlation-Id*                    (*string*)

    :Example: 31LHVT1OLKG82

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

    :Example: 1

    ..  

  *Retry After*                    (*string*)

    :Example: 1

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

  :Example: OK

  ..

*Response Text*                    (*string*)

  :Example: SUCCESS

  ..