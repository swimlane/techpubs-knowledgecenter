Webhook Discovered Outputs
==========================

Scenario
--------

Eli is an orchestrator who wants to test and preview outputs from a
webhook event before configuring and saving the rest of his playbook.
Luckily, as an orchestrator, Eli knows that testing a webhook event is
like testing `discovered outputs and
testing <../../playbooks/actions/discovered-outputs-and-testing.htm>`__.
Let's watch how he tests his webhook event!

Eli has already created his playbook and added a Webhook trigger. After
giving the webhook a name and generating the URL, he's ready to
configure.

#. Click **Configure**.

   The Webhook Events, Outputs, and Map to Playbook Inputs tabs are
   available. Eli checks the Output tabs to see the original outputs for
   the webhook. But he wants to test for any additional outputs that
   might not be being pulled. To do this, he needs to test the webhook.

#. Click **Test** next to the URL and view the Result pane at the bottom
   of the window.

The results display, but Eli wants to know which outputs were discovered
that were not part of the original event outputs. Since Eli already
reviewed and understands what `discovered outputs and
testing <../../playbooks/actions/discovered-outputs-and-testing.htm>`__
are, he is ready to add the discovered outputs.

#. Click the check mark next to any discovered outputs to add them to
   the action's outputs.

Conclusion
----------

These are now available for Eli to apply downstream and as he builds the
playbook.
