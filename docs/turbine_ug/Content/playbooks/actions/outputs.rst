.. _promote-action-outputs:

Outputs
=======

An action output is the response and/or result(s) from a connector
technology, which can be applied as an input for other actions within
your playbook, or promoted for use outside of the current playbook.

.. _promote-action-outputs-1:

Promote Action Outputs
----------------------

Once you have created and configured your action and action inputs, you
can promote action output(s) to the playbook output(s).

#. Click on an action.

#. Click **Configure**.

#. Click the **Outputs** tab.

The mapped action outputs display.

4. Click **+Promote**.

5. The output is **Promoted** and now displays in **Promoted Playbook
   Outputs**.

| You can promote as many outputs that are available.

6. To save, click **Apply**.

You have successfully promoted an action output!

Remove Promoted Action Outputs
------------------------------

Want to remove a promoted action output? No problem! From the Promoted
Playbook Outputs panel, click **x Remove**.

**Warning:** This will remove the promoted action output and break any
references outside of the playbook.

**Note:** It does *not* remove the output from the action itself, and
you can still apply it to other actions within that playbook.

**Tip:** You can also do this later from your Playbook Outputs
configuration.

Error Outputs
-------------

What happens to your action outputs if your action fails? See
`Discovered Outputs and Testing <discovered-outputs-and-testing.htm>`__
for more information. That section provides details about Discovered
Outputs, Action Testing, and Error Outputs.
