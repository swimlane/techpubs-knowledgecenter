Save Phishing Attachment
========================

This page provides steps to set up saving phishing email attachments in
the SOC Solution. The saved file also displays in the TI record. Use the
following steps to configure saving the attachment. If you do not enable
this feature, the TI record is still written and enriched, but the
attachment won't be saved.

 

**Configuration**

If you want to ensure that an email attachment is saved to a TI record,
you can configure the **Bulk Ingest Phishing Emails** playbook.

#. Navigate to Turbine.

#. Navigate to ORCHESTRATION and click **Playbooks**.

#. Search and open **Bulk Ingest Phishing Emails**.

The last action is **Map to Case**, which is a nested playbook. From
here, you can configure the nested playbook inputs.

#. Click on the nested playbook and from the ACTION panel, click
   **Configure**.

#. Toggle the **save attachments?** Boolean value to **TRUE**.

#. Click **Save** the changes, and then save your playbook.

Now anytime that playbook runs, the attachment on the phishing email
will be saved to the TI record.
