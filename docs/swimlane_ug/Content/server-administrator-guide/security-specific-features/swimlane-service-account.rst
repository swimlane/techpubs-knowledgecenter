Swimlane Service Account
========================

A single dedicated Swimlane service account is required for the Swimlane
Web Application and the Swimlane Task Service. This user account is used
for key management of the Swimlane encryption key chosen during Swimlane
installation. The same domain user account should be used across all
servers in a multi-server deployment. This user account should have
these permissions:

-  Read permissions to the Swimlane web application directory (Located
   by default in C:\\inetpub)

   -  Modify access to the App_Data folder within the Swimlane web
      application directory

-  Modify access to the Swimlane tasks directory (Located by default in
   C:\\Program Files\\Swimlane)

As the Swimlane task service executes integration jobs, it has the
potential to modify the system running Swimlane itself. It is
recommended that the Swimlane service account have no access or only
read access on other system directories to prevent an integration job
from causing harm to the server. Integrations that need to administer
the Swimlane server can use remote configuration tools such as WMI to
mange the Swimlane server as any other remote server.
