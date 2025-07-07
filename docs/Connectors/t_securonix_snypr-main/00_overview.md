## Overview

SNYPR is a big data security analytics platform built on Hadoop that utilizes Securonix machine-learning-based anomaly detection techniques and threat models to detect sophisticated cyber and insider attacks.

## Capabilities

This connector provides the following capabilities:

* Run Activity Query
* Get Top Threats
* Get Top Violations
* Get Top Violators
* List All Policies
* List All Users
* Retrieve List of Incidents

Note: To get "All Violations by Policy Name", use "Run Activity Query" action with the query:

`index=violation AND policyname = <policyname> AND <additional conditions>`


## Asset Setup

This connector asset requires an URL, Username and a Password to authenticate.

## Notes

* [API Documentation](https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/rest-api-categories.htm)

## Additional Notes

* __BASE_URL__ or __HOST_URL__ must be in the format: __HOSTNAME_or_IPADDRESS/Snypr__

* While using the __Retrieve List of Incidents__ action, please note that the parameter __tenantname__ is optional for non-MSSP and is required to pass for MSSP and if needed, check here for documentation [Retrieve List of Incidents API Documentation](https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/rest-api-categories.htm#retrieve_list_of_incidents)
