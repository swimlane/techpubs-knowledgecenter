Resolve SSDEEP Tasks in Hangfire
================================

When your SSDEEP tasks are taking longer to process (up to over 24
hours), and you receive errors like this one from the Hangfire page:

ProxyError:
HTTPSConnectionPool(host='swimlane.corpzone.internalzone.com',
port=443): Max retries exceeded with url: /api/user/authorize (Caused by
ProxyError('Cannot connect to proxy.',
NewConnectionError('<urllib3.connection.HTTPSConnection object at
0x0000000003232C88>: Failed to establish a new connection: [Errno 11001]
getaddrinfo failed

You may have also attempted to drop the Hangfire JobGraph collection
``db.hangfire.jobGraph.drop()`` but that still does not resolve the
issue.

Then you will need to modify the loopback time in the Python integration
script.

The loopback time is used to create a record filter. Then a “for loop”
will run through the filter and process the data. If there are thousands
of records that come up in the search filter, this may cause the task to
be stuck in a loop for hours, causing a huge queue.

The loopback time variable is set to 24 hours (1 day) by default. Set
this to fewer hours, like between 1 and 12 hours.

Then, comment out the lines for Deduped Email and Tracking Id lines in
the fuzzymatch.

At times, depending on what you get from the logs, you may need to
comment out the lines for NOT_EQ for Deduped Email and Tracking Id:

records.filter('Deduped Email', NOT_EQ, 'Yes') records.filter('Tracking
Id', NOT_EQ, trackingId)

Mongo profiler logs indicate that using the NOT_EQ boolean was causing
the indexing to fail and was slowing mongo lookup in the records in
Hangfire, causing a huge processing queue. Comment the lines out and
replace both lines with the “for loop” statements below:

for record in records: if record.tacking_Id == trackingId: continue if
record['deduped Alert'] == 'YES': continue

Limiting the sleep times in the code should help the overall
performance, as well.

Update all sleep timer in the code to sleep for less than 3 seconds. The
default may be (0, 3) which will indicate sleep between 0 and 3 seconds.
Reduce all to (0.5, 1)
