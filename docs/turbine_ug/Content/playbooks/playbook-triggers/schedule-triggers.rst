Schedule Triggers
=================

A schedule trigger initiates a playbook at the configured schedule.

**Note:** You do not need to select a trigger before adding and
configuring actions and conditions.

.. _schedule-triggers-1:

Schedule Triggers
-----------------

Create a new playbook or upload an existing playbook, then follow the
steps below:

#. On the playbook, click **Add a trigger**.

#. Click **Schedule**.

**Example**

The schedule trigger example has a yearly cron job occurring at 12:00AM
on January 1st each year.

#. Once the trigger options display, select **Schedule**.

To the right, the TRIGGER window displays with the **Trigger Type** as
*Schedule* and **Schedule Type** as *cron*.

#. Select the desired list of schedule times from: **Minutely**,
   **Hourly**, **Daily**, **Weekly**, **Monthly**, **Yearly**,
   **Custom**.

#. Depending on the selected schedule, a field displays below for you to
   configure the schedule.

   **Minutely:** Every **\_\_** minute.

   **Hourly:** At **\_\_** minutes past the hour.

   **Daily:** At **HH:MM AM/PM**

   **Weekly:** At **HH:MM AM/PM**, only on **day of the week** values
   list

   **Monthly:** At **HH:MM AM/PM**, only on **date of month** values
   list

   **Yearly:** At **HH:MM AM/PM**, only on **date of month** values
   list, only in **month**

   **Custom:** Enter the desired date/time in cron format

**Tip:** You can also use the up/down arrow icons to select the
numerical date of the month.

**Note:** Coordinated Universal Time (UTC) is used for all schedules.

| 
| |image1|

5. When you are finished, click **Save**.

You have successfully created a playbook!

.. |image1| image:: ../../Resources/Images/cron-job-trigger-example.png
