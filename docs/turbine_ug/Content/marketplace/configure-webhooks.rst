Configure Webhooks
==================

Configure Slack Webhook
-----------------------

**Note**: This configuration does not require Slack Admin permissions.

To generate the Slack webhook URL that you need for your Collaboration
Extension asset configuration, first make changes in incoming webhook
settings in Slack.

#. Click `Legacy: Incoming
   Webhooks <https://api.slack.com/legacy/custom-integrations/messaging/webhooks>`__
   to open the Slack API docs for configuring incoming webhooks.

#. Click the **Slack app** hyperlink.

#. Navigate to and click **Add apps**.

#. Click **Incoming Webhooks**.

You are redirected to the Slack App Directory in your browser.

#. Click **Add to Slack**.

Select a channel to be the default channel that messages will be posted
to when no input is specified.

#. Click **Add Incoming WebHooks integration**.

#. Copy the generated webhook URL and navigate back to the
   **Collaboration Extension Configuration** asset.

#. In the Slack_Webhook_URL field, paste the generated URL.

Configure MS Teams Webhook
--------------------------

**Note**: This configuration does not require Teams Admin permissions.

To add an Incoming Webhook to a Teams channel, follow these steps:

#. In MS Teams, open the channel in which you want to add the webhook.

#. Click the **ellipsis** icon in upper-right corner.

#. From the drop-down menu, select **Connectors**.

#. Search for **Incoming Webhook** and select **Add**.

#. Select **Configure**, provide a name, and upload an image for your
   webhook, if desired.

#. Copy and save the unique webhook URL present in the dialog.

The URL maps to the channel and you can use it to send information to
Teams.

#. Click **Done**.
