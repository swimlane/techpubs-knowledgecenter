.. _multiple-applications-workflow-and-reference-fields-a-swimlane-use-case:

Multiple Applications, Workflow, and Reference Fields - A Swimlane Use Case
===========================================================================

   .. rubric:: Scenario
      :name: scenario

   Mike works in a Security Operations Center (SOC). He is responsible
   for discovering and reporting malicious URLs. He has a list of URLs
   that are reported to him each morning. He looks up each of the URLs
   in the list with VirusTotal. He then uses the resulting VirusTotal
   scans to report which URLs are most severe. This takes up most of
   Mike's morning each work day.

   Mike would like to use Swimlane to simplify and automate this
   process. He has already ensured that his version of Swimlane has a
   VirusTotal integration. He has also reviewed the VirusTotal report to
   determine which data he will want to use to feed his Swimlane
   application(s) and workflow.

Solution
--------

Mike can resolve the scenario above with the following solution:

#. Build an application in Swimlane that includes a Reference field. The
   application should also include a Selection field that can handle
   multiple values.

2. With the reference field selected, create a new application to
   reference.

3. Create the application to reference from the *Incidents* application.
   Include the fields you will use as targets when setting up task
   output mapping.

4. Back in the original *Incidents* application, notice how the
   secondary application, *VirusTotal Results* is now selected in the
   Reference Application field. Next, select the fields to reference.

5. Next, you'll create a VirusTotal task, and map to the *VirusTotal
   Results* fields.

6. Now that the integration task and the applications are set up, create
   the workflow that will automate the URL lookup and reporting
   processes.

7. The VirusTotal integration task returns a value to the Positives
   field. Create a new workflow condition that points to the target
   field in order to process the action.

8. Finish the workflow by setting up additional stages and actions for
   each value for the **Severity** field, then click **OK.**

Conclusion
----------

Mike can now start his day knowing that he has automated the process of
searching for and reporting malicious URLs.
