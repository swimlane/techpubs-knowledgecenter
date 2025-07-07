# Create Event

**Description**: Creates a new calendar event in the specified user's calendar using their email address through the Microsoft Graph API.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/events`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required
- **json_body** (object) – Required
  - **subject** (string): The text of the event's subject line.
  - **body** (object): The body of the message associated with the event. It can be in HTML or text format.
    - **contentType** (string): The content of the item.
    - **content** (string): The type of the content.
  - **start** (object): The start date, time, and time zone of the event. By default, the start time is in UTC.
    - **dateTime** (string): A single point of time in a combined date and time representation ({date}T{time}; for example, 2017-08-29T04:00:00.0000000).
    - **timeZone** (string): Represents a time zone, for example, "Pacific Standard Time".
  - **end** (object): The date, time, and time zone that the event ends. By default, the end time is in UTC.
    - **dateTime** (string): A single point of time in a combined date and time representation ({date}T{time}; for example, 2017-08-29T04:00:00.0000000).
    - **timeZone** (string): Represents a time zone, for example, "Pacific Standard Time".
  - **location** (object): The location of the event.
    - **displayName** (string): The name associated with the location.
  - **locations** (array): The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection would be removed and replaced by the new location value.
    - **displayName** (string): The name associated with the location.
    - **locationType** (string): The type of location.
    - **uniqueIdType** (string): For internal use only.
    - **locationEmailAddress** (): Optional email address of the location.
    - **locationUri** (string): Optional URI representing the location.
    - **uniqueId** (): For internal use only.
    - **address** (object): The street address of the location.
      - **city** (string): The city.
      - **countryOrRegion** (string): The country or region. It's a free-format string value, for example, "United States".
      - **postalCode** (string): The postal code.
      - **state** (string): The state.
      - **street** (string): The street.
    - **coordinates** (object): The geographic coordinates and elevation of the location.
      - **accuracy** (number): The accuracy of the latitude and longitude. As an example, the accuracy can be measured in meters, such as the latitude and longitude are accurate to within 50 meters.
      - **altitude** (number): The altitude of the location.
      - **altitudeAccuracy** (number): The accuracy of the altitude.
      - **latitude** (number): The latitude of the location.
      - **longitude** (number): The longitude of the location.
  - **recurrence** (object): The recurrence pattern for the event.
  - **attendees** (array): The collection of attendees for the event.
    - **emailAddress** (object): Includes the name and SMTP address of the attendee.
      - **address** (string): The email address of the person or entity.
      - **name** (string): The display name of the person or entity.
    - **status** (object): The attendee's response (none, accepted, declined, etc.) for the event and date-time that the response was sent.
      - **response** (string): The response type.
      - **time** (string): The date and time when the response was returned. It uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    - **proposedNewTime** (object): An alternate date/time proposed by the attendee for a meeting request to start and end. If the attendee hasn't proposed another time, then this property isn't included in a response of a GET event.
      - **start** (object): The start date, time, and time zone of the event. By default, the start time is in UTC.
        - **dateTime** (string): A single point of time in a combined date and time representation ({date}T{time}; for example, 2017-08-29T04:00:00.0000000).
        - **timeZone** (string): Represents a time zone, for example, "Pacific Standard Time".
      - **end** (object): The date, time, and time zone that the event ends. By default, the end time is in UTC.
        - **dateTime** (string): A single point of time in a combined date and time representation ({date}T{time}; for example, 2017-08-29T04:00:00.0000000).
        - **timeZone** (string): Represents a time zone, for example, "Pacific Standard Time".
    - **type** (string): The attendee type.
  - **allowNewTimeProposals** (boolean): True if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. Default is true.
  - **isOnlineMeeting** (boolean): True if this event has online meeting information (that is, onlineMeeting points to an onlineMeetingInfo resource), false otherwise. Default is false (onlineMeeting is null).
- **headers** (object)
  - **Prefer** (string): Specify the time zone for the start and end times in the response.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **@odata.etag** (string)
  - **id** (string)
  - **createdDateTime** (string)
  - **lastModifiedDateTime** (string)
  - **changeKey** (string)
  - **categories** (array)
  - **transactionId** (object)
  - **originalStartTimeZone** (string)
  - **originalEndTimeZone** (string)
  - **iCalUId** (string)
  - **uid** (string)
  - **reminderMinutesBeforeStart** (number)
  - **isReminderOn** (boolean)
  - **hasAttachments** (boolean)
  - **subject** (string)
  - **bodyPreview** (string)
  - **importance** (string)
  - **sensitivity** (string)
  - **isAllDay** (boolean)
  - **isCancelled** (boolean)
  - **isOrganizer** (boolean)
  - **responseRequested** (boolean)
  - **seriesMasterId** (object)
  - **showAs** (string)
  - **type** (string)
  - **webLink** (string)
  - **onlineMeetingUrl** (object)
  - **isOnlineMeeting** (boolean)
  - **onlineMeetingProvider** (string)
  - **allowNewTimeProposals** (boolean)
  - **occurrenceId** (object)
  - **isDraft** (boolean)
  - **hideAttendees** (boolean)
  - **responseStatus** (object)
    - **response** (string)
    - **time** (string)
  - **body** (object)
    - **contentType** (string)
    - **content** (string)
  - **start** (object)
    - **dateTime** (string)
    - **timeZone** (string)
  - **end** (object)
    - **dateTime** (string)
    - **timeZone** (string)
  - **location** (object)
    - **displayName** (string)
    - **locationType** (string)
    - **uniqueId** (string)
    - **uniqueIdType** (string)
  - **locations** (array)
    - **displayName** (string)
    - **locationType** (string)
    - **uniqueId** (string)
    - **uniqueIdType** (string)
  - **recurrence** (object)
  - **attendees** (array)
    - **type** (string)
    - **status** (object)
      - **response** (string)
      - **time** (string)
    - **emailAddress** (object)
      - **name** (string)
      - **address** (string)
  - **organizer** (object)
    - **emailAddress** (object)
      - **name** (string)
      - **address** (string)
  - **onlineMeeting** (object)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Location | string |
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| Date | string |