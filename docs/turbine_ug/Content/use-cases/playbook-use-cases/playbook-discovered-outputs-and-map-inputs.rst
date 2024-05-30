Playbook Discovered Outputs and Map Inputs
==========================================

What if you want to test your action to see the possible outputs? This
can be done at the action-level. Let's take a look at the how to test
the actions/connectors that Turbine supports.

Scenario
--------

Owen is an orchestrator who is trying to get data from Jira project.
Owen’s company has custom fields in their project. Owen can test the
action, view the result data and update the outputs with his tested
data.

Owen’s playbook receives a webhook event. However, the webhook body is
not available for easy mapping in the playbook. Owen sends a webhook to
his playbook and updates the output with the webhook event history.

Let's take a look at how Owen tests the Jira inputs and customizes the
outputs. First, Owen goes to the Swimlane Content and installs the
Atlassian Jira connector. This provides him with several Atlassian
actions. He creates his playbook and adds the desired Jira connector.

#. Click **Configure** and navigate to the **Test** tab.

Owen knows that all testing must occur from the Test tab. He cannot test
from the Inputs tab.

2. Enter the inputs and click **Test**.

   The Results pane below, provides the raw JSON data, but Turbine turns
   that into an easy-to-read format under the Discovered Outputs tab.
   Owen notices that the original inputs are not providing the exact
   data he is trying to get from Jira. So he goes to the Discovered
   Outputs.

3. Click **Discovered Outputs** to see the known outputs (shown with a
   check mark) and remaining outputs (shown without check marks).

   Since he wants to add the X output, he clicks the plus icon next to
   it. Now he wants to confirm his outputs.

4. Click the **Outputs** tab to view all of the outputs that were custom
   (that Owen just added).

Conclusion
----------

The custom outputs are now available and Owen can use them downstream as
he builds the playbook.
