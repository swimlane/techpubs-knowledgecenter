# List Analyzed Emails

**Description**: Retrieve a comprehensive list of analyzed email objects with their properties from the Microsoft Graph API.

## Endpoint

- **URL:** `/beta/security/collaboration/analyzedEmails`
- **Method:** `GET`
## Inputs

- **parameters** (object): OData query parameters to help customize the response. This action supports the following parameters  $count, $filter, $skiptoken and $top.
  - **$count** (boolean): Retrieves the total count of matching resources.
  - **$filter** (string): Use the `filter` query parameter to retrieve just a subset of a collection. For guidance on using `filter`, see https://learn.microsoft.com/en-us/graph/filter-query-parameter.
  - **$top** (number): Sets the page size of results.
  - **$skiptoken** (string): Retrieves the next page of results from result sets that span multiple pages. (Some APIs use $skip instead.)
  - **startTime** (string): The start time of the email search.
  - **endTime** (string): The end time of the email search.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **value** (array)
    - **@odata.type** (string)
    - **id** (string)
    - **loggedDateTime** (string)
    - **networkMessageId** (string)
    - **internetMessageId** (string)
    - **senderDetail** (object)
      - **@odata.type** (string)
    - **recipientEmailAddress** (string)
    - **distributionList** (string)
    - **subject** (string)
    - **returnPath** (string)
    - **directionality** (string)
    - **originalDelivery** (object)
      - **@odata.type** (string)
    - **latestDelivery** (object)
      - **@odata.type** (string)
    - **attachmentsCount** (string)
    - **urlsCount** (string)
    - **language** (string)
    - **sizeInBytes** (string)
    - **alertIds** (array)
    - **exchangeTransportRules** (array)
      - **@odata.type** (string)
    - **overrideSources** (array)
    - **threatTypes** (array)
    - **detectionMethods** (array)
    - **contexts** (array)
    - **authenticationDetails** (object)
      - **@odata.type** (string)
    - **phishConfidenceLevel** (string)
    - **spamConfidenceLevel** (string)
    - **bulkComplaintLevel** (string)
    - **emailClusterId** (string)
    - **policyAction** (string)
    - **policy** (string)