Run Swimlane on AWS
===================

To run Swimlane on AWS:

#. In your AWS EC2 console, find the Swimlane instance and locate the
   ``IP Address``
#. In your browser, navigate to ``https://<IP Address>``
#. Complete the post-install wizard.

A ``centos`` user is available on the instance with sudo privileges that
utilizes the public SSH key chosen when the instance was launched.

A ``swimlane-host`` user is available via the ``su`` command and should
be used for all operations on the Swimlane Docker containers.
