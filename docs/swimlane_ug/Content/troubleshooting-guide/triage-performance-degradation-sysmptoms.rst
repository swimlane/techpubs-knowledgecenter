Triage Performance Degradation Symptoms
=======================================

Swimlane performance degradation symptoms can arise for a variety of
causes including:

-  Platform limitations

-  Client code limitations

-  Client job/data load upon the Platform

-  Large record sets

-  Suboptimal backup configuration

-  Hardware limitations

-  Any combination of these

Examples include:

-  `Text data entry
   lag <report-a-data-entry-lag-in-swimlane-records.htm>`__

-  UI navigation and/or page-load speed slowdowns

   These sometimes manifest as HTTP 502 and 504 errors reported in
   Chrome Developer Tools.

-  Poor performance when searching records or exporting records

-  Timing out of Python script tasks that interact with the RESTful API

   These also sometimes manifest as HTTP 502 and 504 errors.

-  Background job queue congestion

To triage performance degradation symptoms:

#. Take a screen capture video of the symptom while it is manifesting.

   Use video, screenshots, log file entries, etc, to help Swimlane
   support to get into context and see the symptom through your eyes.

   Your Swimlane support representative will join via Zoom to witness
   the symptom and can record the Zoom meeting screen sharing display.

#. For UI slowness, `collect a HAR
   file <https://toolbox.googleapps.com/apps/har_analyzer/>`__ from
   Chrome Developer Tools.

#. Use the watershed script to export a copy of all of your
   apps/workflows, integration tasks, and other related artifacts. You
   can request a copy of this script from your Swimlane Professional
   Services Engineer.

#. Capture the MongoDB query profiler data. Work with your support
   representative on this.

#. If requested by the your support representative, assist them to
   harvest MongoDB diagnostic and log data.

   These data can sometimes be large and require special arrangements
   for the file transfers.

#. See the instructions below for background job queue congestion
   symptoms.

#. Provide all of the artifacts above in the pertinent support portal
   ticket.

Tuning Scripts
--------------

Whenever possible, you should attempt to refactor your automations
targeting the RESTful API to:

-  Minimize the number of round trips to the RESTful API and remove
   superfluous calls to record.save() / record.patch().

-  Minimize the load imposed on the RESTful API (and, by extension, the
   MongoDB database) in each round trip.

   Where possible, control the number of records against which searches
   are performed.

   -  Make smart use of search APIs.

   -  See `this
      resource <https://swimlane-python-driver.readthedocs.io/en/stable/examples/resources.html#search-records>`__
      to:

      -  use the limit parameter appropriately with the Swimlane
         Driver’s app.records.search()

      -  use app.reports.build() against large record sets

   -  Constrain the sorting order of results. This may work best in
      cases where only the first few results in a sorted set are really
      needed.

   The Driver does not support the RESTful API’s sorting interface
   formally. See below for a workaround. Note line 3:

   report = soc_records_app.reports.build('source_ip_report', limit=0)
   report.filter('First Created', GTE, dt.subtract(days=2))
   report._raw['sorts']['Threat Score'] = 'ascending' for record in
   report: # consume each resultant record

Background Job Queue Congestion
-------------------------------

The queue is congested whenever its
`dashboard <https://swimlane.com/knowledge-center/docs/administrator-guide/system-settings/background-jobs>`__
shows that new jobs are being enqueued faster than previously enqueued
jobs can finish processing.

This symptom can be either the result of underlying performance problems
or the cause of other performance degradation symptoms.

When this symptom is severe (thousands or tens of thousands of enqueued
jobs), it can prevent newly enqueued jobs from executing for hours or
days.

To understand this symptom and its remedies, it’s important to
understand the queue itself. Each job is an instance of either:

-  A built-in integration task (one example is the nightly Directory
   Services sync).

-  A customer-created integration task

As shown in the queue’s dashboard, each job passes through the following
states:

#. Enqueued

#. Processing

#. Succeeded / Deleted (The Failed state is not used by Swimlane. Failed
   jobs are grouped in the Deleted state.)

There are other states such as Scheduled, Awaiting, or Aborted, but
these are not used often.

The quick fix to temporarily eliminate congestion is to work with your
Swimlane support representative to purge the Background job queue to
allow newer jobs to process. This works for a short time.

!> **Important!** Before purging the job queue consider the
ramifications. The recommended purge method will delete all job
execution data from the queue.

Be aware that:

-  No Swimlane records will be altered by the purge (but they may suffer
   indirect harm as described below).

-  Loss of knowledge of success/fail outcomes for completed jobs is
   often negligible because:

   -  Information about Succeeded and Deleted jobs are purged
      automatically every night at midnight server time. Swimlane only
      retains this data for 24-48 hours.

   -  This same information can often be reconstructed from the Swimlane
      log stream (the Swimlane.Logs collection in MongoDB).

However, the loss whose cost must be carefully considered is the
elimination of the jobs in the Enqueued state. When thousands or tens of
thousands of jobs are congested the following questions must be
addressed:

-  Is it more harmful to leave these jobs enqueued knowing that recent
   Swimlane alarm records will go under-enriched for hours or days?

-  Or, is it more harmful to eliminate all enqueued jobs so that
   subsequent jobs can start and finish more promptly?

   -  To answer this question, consider the consequences of either:

      -  Leaving the recently ingested records under-enriched or

      -  Putting forth special effort to back-fill the under-enriched
         records

         -  Consult with your Professional Services Engineer for
            assistance using the Bulk Edit feature and/or special
            purpose scripts to catalyze enrichment on all records
            neglected during queue congestion.

Diagnosing the Queue
~~~~~~~~~~~~~~~~~~~~

#. After stopping the Tasks service(s) and purging the queue, disable
   all Integration tasks.

#. Decide on one small suit of tasks to enable.

   These tasks should all pertain to one use case (one security alarm
   type and its automation processing flow), but they may only be a
   subset of the tasks belonging to that use case.

#. Enable only those chosen tasks.

#. Monitor the job queue for 1-3 hours.

   Does Swimlane keep up with this reduced load of tasks?

#. If Swimlane keeps up with the reduced load by never falling
   permanently behind, then add a few more tasks (completing the first
   use case’s portfolio or adding a small second use case), and continue
   monitoring.

#. As soon as Swimlane falls behind permanently, then you know precisely
   how to increase load incrementally until the ability of the Swimlane
   deployment to keep up has been surpassed.

The information about which tasks were enabled, in what order, during
what span of time, is the information you need to pass along (along with
the other artifacts requested above) to provide a solution.
