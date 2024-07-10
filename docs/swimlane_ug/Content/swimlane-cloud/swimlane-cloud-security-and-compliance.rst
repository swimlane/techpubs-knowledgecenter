Swimlane Cloud Security and Compliance
======================================

Swimlane is designed to enable you to securely access and manage your
content. Technical and physical controls within Swimlane prevent the
disclosure of content as well as the unauthorized access to content. The
infrastructure is continuously monitored, and vulnerability testing is
conducted regularly by internal and external security staff.

Swimlane extensively leverages security automation and response to alert
suspicious activity across customer and corporate environments.
Internally, confidentiality requirements are communicated to employees
through training and policies. Employees are required to attend security
awareness training, which includes information, policies, and procedures
related to protecting our customers’ data.

Security
--------

Swimlane provides a number of security features within Swimlane Cloud
which helps ensure the confidentiality, integrity and availability of
customer information.

Data at Rest
~~~~~~~~~~~~

Here is how Swimlane Cloud protects your data at rest:

-  All customer data and application snapshots are encrypted using the
   AES256 encryption algorithm before being stored on disk.

-  Swimlane allows full-instance snapshots that support disaster
   recovery and the rollback of known good application state(s).

-  Entries in the Swimlane credentials library, as well as user and
   asset passwords, are encrypted at rest before they are stored in the
   Swimlane database. using the AES encryption algorithm with a 256-bit
   key and a 256-bit salt.

Data in Motion
~~~~~~~~~~~~~~

Swimlane protects your data in motion by using Transport Layer Security,
or TLS, (versions 1.2 and 1.3) to encrypt data between the Swimlane
application servers and client browsers, as well as the Swimlane
database.

SAML/SSO
~~~~~~~~

Swimlane supports local user account provisioning, Open LDAP, Microsoft
Active Directory, and SAML 2.0.

For more information on how Swimlane utilizes SAML, see `Enable SAML for
SSO <../administrator-guide/settings/sessions-and-security/enable-saml-for-sso.htm>`__.

Two-Factor Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~

Two-Factor Authentication, or 2FA, is enforced globally. All users are
required to set up their individual 2FA prior to being able to access
Swimlane Cloud.

For more information on 2FA and Swimlane, see `Enable Two-Factor
Authentication <../administrator-guide/settings/sessions-and-security/enable-two-factor-authentication.htm>`__.

Role-Based Access Control
~~~~~~~~~~~~~~~~~~~~~~~~~

Swimlane limits access to information by using Role-Based Access
Control, or RBAC. RBAC can be applied at every level of objects within
Swimlane: workspaces, dashboards, reports, applications, records and
individual records. Granular controls can be applied down to the
individual field level, and all components support the ability to
restrict access via user, group or role.

Swimlane can dynamically adjust permissions on a per-record basis based
on user/group field values, as well. For example, if a record is
assigned to Group A, only Group A and administrators will have access to
that record. If the assignment of the record changes to Group B, then
only Group B and administrators will have access to the records.

For more information about RBAC, see `Role
Permissions <../administrator-guide/permissions/role-permissions.htm>`__
and the other permissions topics within the Administrator Guide.

Access to Swimlane Cloud
~~~~~~~~~~~~~~~~~~~~~~~~

Swimlane restricts access to production systems to a handful of
employees. No contractors or third parties have access to any customer
production data. The list of employees with access to production is
audited regularly.

Reporting Security Vulnerabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Swimlane welcomes reports from security researchers and experts about
possible security vulnerabilities in our product. To report a security
vulnerability in Swimlane, please send details to security@swimlane.com.
Swimlane does not have a bug bounty program.

Compliance
----------

Data centers hosting Swimlane Cloud have achieved compliance with
ISO/IEC 27001:2013, 27017:2015, 27018:2019, 27701:2019, 9001:2015, and
CSA STAR CCM v3.0.1.

Additionally, all data centers have completed the following
examinations:

-  SSAE 16

-  SOC 1 Type II

-  SOC 2 Type II
