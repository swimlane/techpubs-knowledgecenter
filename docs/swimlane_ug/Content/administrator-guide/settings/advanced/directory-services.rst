Directory Services
==================

Swimlane integrates with two Directory Service types, Microsoft's Active
Directory (AD) and OpenLDAP.

Many Swimlane administrators leverage Swimlane's Directory Services to:

-  Allow their SOC Engineers and Analysts to log in to Swimlane with
   previously-established directory credentials.
-  Increase the ease of administrative maintenance for groups of users.

**Note:** Users are synced upon each login. Automatic synchronization
occurs every night at midnight, server time.

If you have difficulty configuring Directory Services due to unknown or
incorrect fields or attributes, see `Directory Services Synchronization:
Field Attribute
Mappings <../../../server-administrator-guide/troubleshooting-and-error-notifications/directory-services-synchronization-field-attribute-mappings.htm>`__.

Setting Up Open LDAP Services
-----------------------------

**Important!** Before you begin, verify that your server settings are
correct!

To set up Open LDAP:

#. From the left navigation menu, select Settings, Advanced.

#. Click **>** to expand Directory Services and then select **Enable
   Directory Syncing.**

3. Click **>** to expand Server Settings. On **Server Type,** select
   Open LDAP.

4. Input your server settings.

   Keep in mind that the **Username** must be an LDAP Distinguished Name
   (such as cn=Manager,dc=maxcrc,dc=com).

   **Note:** If you want to test the connection to the server at this
   point in the process, enter placeholder text in all required fields,
   including those in other sections, and then click **Save**. Once your
   initial settings are saved, you can click **Test Connection**. If
   your test does not succeed, see `Testing Connections in Directory
   Services <../../../server-administrator-guide/troubleshooting-and-error-notifications/testing-connections-in-directory-services.htm>`__.

5. Click **>** to expand **User Settings** and review or update the
   values there.

6. Click **>** to expand **Field Mapping** and review or update the
   values there.

7. Click **>** to expand **Group Settings** and review or update the
   values there.

8. Click **>** to expand **Groups** and review or update the values
   there.

   This is a list of manually entered groups. To add a group, type the
   name in the field and then click **Add Value**. Keep in mind that you
   have to add each group individually, and that the values are case
   sensitive.

9. Under **Groups to sync**, click **Validate Groups**.

10. Click **>** to expand **Membership** and review or update the values
    there.

11. Click **Save** again and then click **Sync Now**.

Setting Up Active Directory
---------------------------

Enable single sign-on for your Swimlane users by setting up and syncing
Active Directory in Swimlane Settings. Users created through Active
Directory sync count towards the Swimlane user license limit.

**Important!** Before you begin, verify that your server settings are
correct!

To set up Active Directory:

#. From the left navigation menu, select Settings, Advanced.

#. Click **>** to expand Directory Services and then select **Enable
   Directory Syncing.**

3. Click **>** to expand Server Settings. On **Server Type,** select
   Active Directory.

4. Input or verify the Server settings.

   **Note:** If you want to test the connection to the server at this
   point in the process, enter placeholder text in all required fields,
   including those in other sections, and then click **Save**. Once your
   initial settings are saved, you can click **Test Connection**. If
   your test does not succeed, see `Testing Connections in Directory
   Services <../../../server-administrator-guide/troubleshooting-and-error-notifications/testing-connections-in-directory-services.htm>`__.

5. Click **>** to expand **User Settings** and review or update the
   values there.

5. Click **>** to expand **Field Mapping** and review or update the
   values there.

6. Click **>** to expand **Group Settings** and review or update the
   values there.

7. Click **>** to expand **Groups** and review or update the values
   there.

   This is a list of manually entered groups. To add a group, type the
   name in the field and then click **Add Value**. Keep in mind that you
   have to add each group individually, and that the values are case
   sensitive.

8. Under **Groups to sync**, click **Validate Groups**.

9. Click **>** to expand **Membership** and review or update the values
   there.

10. Click **Save** again and then click **Sync Now**.

Authentication: Basic and LDAP
------------------------------

Swimlane's basic authentication does not rely on host OS support. When
you create a normal, non-synced user, their username is stored in plain
text. Their password is stored in scrambled form by encryption.

In contrast, when you create a synced user, their password is not stored
in Swimlane's MongoDB. They are authenticated to Swimlane by the
Swimlane Platform code sending a real-time request to the LDAP server to
approve the synced user's Swimlane login attempt.
