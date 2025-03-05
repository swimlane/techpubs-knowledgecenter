Create Triage Item Comment
==========================

Create a new comment for a given triage item.

Inputs
------

**Path Parameters** (*object*)

  **Triage ID** (*string**)

  .. list-table::
     :class: custom-table

     * - Description
       - Identifier of the triage item to which the comments belong.
     * - Example
       - 77d21124-c5e6-4386-be23-072eddc319f9

**JSON Body** (*object*)

  **Content** (*string**)

  .. list-table::
     :class: custom-table

     * - Description
       - The comment text content. Must not include the null character.
     * - Example
       - A custom comment has been created!

Outputs
-------

**Status Code** (*number**)

  .. list-table::
     :class: custom-table

     * - Example
       - 200

**Response Headers** (*object**)

  **Date** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - Mon, 15 Jul 2024 05:44:34 GMT

  **Content-Type** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - application/json

  **Transfer-Encoding** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - chunked

  **Connection** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - keep-alive

  **X-Correlation-Id** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - AQTI3K9F413A

  **Vary** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - Origin, Access-Control-Request-Method, Access-Control-Request-Headers

  **Ratelimit Limit** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - 100

  **Ratelimit Remaining** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - 99

  **Ratelimit Reset** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - 28

  **Retry After** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - 28

  **X-Content-Type-Options** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - nosniff

  **X-XSS-Protection** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - 1; mode=block

  **Cache-Control** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - no-cache, no-store, max-age=0, must-revalidate

  **Pragma** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - no-cache

  **Expires** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - 0

  **X-Frame-Options** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - DENY

**Reason** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - 

**JSON Body** (*object**)

  **ID** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - 6ff2e3ad-92d7-40a0-b4cd-74b3a5a4ec68

  **Triage Item ID** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - 77d21124-c5e6-4386-be23-072eddc319f9

  **Content** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - A custom comment has been created!

  **User** (*object**)

    **ID** (*string**)

    .. list-table::
       :class: custom-table

       * - Example
         - 29f01f82-76c7-4cb9-89b9-3103a531de94

    **Name** (*string**)

    .. list-table::
       :class: custom-table

       * - Example
         - [HIB2TO:199023892748]

  **Created** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - 2024-07-15T05:44:31.351068063Z

  **Updated** (*string**)

  .. list-table::
     :class: custom-table

     * - Example
       - 2024-07-15T05:44:31.351068063Z
