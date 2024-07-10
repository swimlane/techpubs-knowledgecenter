Directory Services Synchronization: Field Attribute Mappings
============================================================

When configuring Swimlane's Directory Services (DS), the default values
usually work fine. However, there are times when the defaults do not
provide the expected results. This is typically due to the environment's
DS customizations and requires an investigation into their DS tree
structure to determine the correct field attributes to be selected
rather than using specific defaults.

For example, one domain may use the value within *displayName* as the
primary means of identifying a person, while another may use
*userPrincipalName*, or *sAMAccountname*. Without querying the domain's
DS schema field configurations, you might have to determine the LDAP
attributes through trial and error. Instead of that time consuming
activity, consider the help provided in this topic to troubleshoot this
issue.

See the table below to view some of the available Active Directory
fields for a user. This table also shows the associated LDAP Attribute
for the corresponding AD schema field.

Common AD to LDAP Mappings for Users
------------------------------------

+----------------------+----------------------+----------------------+
|                      | **Active Directory   | **LDAP Attribute**   |
|                      | Field**              |                      |
+======================+======================+======================+
| **General Tab**      | First name           | givenName            |
+----------------------+----------------------+----------------------+
|                      | Initials             | initials             |
+----------------------+----------------------+----------------------+
|                      | Last name            | sn                   |
+----------------------+----------------------+----------------------+
|                      | Display name         | displayName          |
+----------------------+----------------------+----------------------+
|                      | Description          | description          |
+----------------------+----------------------+----------------------+
|                      | Office               | physic               |
|                      |                      | alDeliveryOfficeName |
+----------------------+----------------------+----------------------+
|                      | Telephone number     | telephoneNumber      |
+----------------------+----------------------+----------------------+
|                      | Telephone number     | otherTelephone       |
|                      | (Other... button)    |                      |
+----------------------+----------------------+----------------------+
|                      | E-mail               | mail                 |
+----------------------+----------------------+----------------------+
|                      | Web page             | wWWHomePage          |
+----------------------+----------------------+----------------------+
|                      | Web page (Other...   | url                  |
|                      | button)              |                      |
+----------------------+----------------------+----------------------+
| **Account Tab**      | User logon name      | userPrincipalName    |
+----------------------+----------------------+----------------------+
|                      | User logon name      | sAMAccountname       |
|                      | (pre-Windows 2000)   |                      |
+----------------------+----------------------+----------------------+
| **Organization Tab** | Title                | title                |
+----------------------+----------------------+----------------------+
|                      | Department           | department           |
+----------------------+----------------------+----------------------+
|                      | Company              | Company              |
+----------------------+----------------------+----------------------+
|                      | Manager              | Manager              |
+----------------------+----------------------+----------------------+
|                      | Direct reports       | directReports        |
+----------------------+----------------------+----------------------+

Determine Field Attribute Mappings
----------------------------------

Use a utility such as Microsoft's Active Directory Service Interface
Editor, or ADSI Edit, to get a view into the objects and attributes in
Active Directory. Other similar utilities include LDAPsoft's AD Browser,
Sysinternal's AD Explorer, etc. Swimlane recommends ASDSI Edit as it,
like Active Directory is a Microsoft product and is readily available.
The ADSI Edit utility can be added via Server Manager if its not already
available/installed. If these utilities are not available, you can try
the DSQUERY or LDAPSEARCH command-line tools.

Installing and Using ADSI Edit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install and use ADSI Edit:

#. Install/Add this utility.

#. Open and connect to the domain controller or DS server.

#. Navigate to the object you wish to analyze, or view any User or Group
   object to view the attributes that have the appropriate value to be
   synced.

#. Observe the results and identify the AD schema field's LDAP attribute
   that is not synchronizing.

#. Modify the Swimlane configuration to specify the new field attribute
   and see if the sync results are now as expected. If not, repeat steps
   3 - 5.
