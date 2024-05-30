Script Test Use Case
====================

Scenario: Test Script Action
----------------------------

Rowan is an orchestrator who wants to map static and playbook property
data to the Script native action inputs, so that he can reference this
data in the Python script and test the inputs to see the results before
continuing the build the playbook. He also want to see if there are any
discovered outputs in addition to the original outputs.

First, Rowan adds his webhook trigger, so the webhook property data is
available downstream in the playbook. Let's see how he sets up Script
native action to see if there are `discovered outputs and
testing <../../playbooks/actions/discovered-outputs-and-testing.rst>`__.

#. Click the Action drop-down menu, select **Script**, and enter a
   title.

#. Click **Configure**.

   The Script configuration window shows three tabs: Script, Outputs,
   and Test. This is great news for Rowan, because he wants to find if
   there are outputs besides the original outputs from the webhook
   trigger. First, he must enter inputs before testing results. Rowan
   uses two strings inputs and an object input.

#. From the Script tab, click **Add property** and select **String**.

   Rowan enters a simple string with **hello**. Next, he wants to add
   the Object property. Rowan repeats step 3, but selects **Object**
   this time. He renames the property types to **string_test** and
   **object_test1** so that he can identify these specified inputs after
   testing. Depending on the property type, Rowan could have clicked
   **select a property** and chosen a playbook property from the current
   action or webhook event, or he could have written an expression using
   dot notation.

#. Under the Object property type, click **Add property** and select
   **String**.

   Rowan names the string property **string_2**. Now he is ready to
   enter the script.

#. In the Script pane, enter ``action_outputs = action_inputs``.

   Now it's time to test! Rowan navigates to the Test tab. On the left,
   he sees the inputs that he added and the script command.

#. Above the Test Script pane, he clicks **Test** and view the Result
   pane at the bottom of the window for results.

   The results display, but Rowan wants to know what outputs were
   discovered that were not part of the original event outputs. Since
   Rowan already reviewed and understands what `discovered outputs and
   testing <../../playbooks/actions/discovered-outputs-and-testing.rst>`__
   are, he is ready to add the discovered outputs.

#. Click the check mark next to any discovered outputs to add them to
   the action's outputs.

   These are now available for him to use downstream and he is ready to
   continue building his playbook.

Conclusion
----------

Rowan successfully tested his script, and he was able to see discovered
outputs to use downstream as he builds the playbook.
