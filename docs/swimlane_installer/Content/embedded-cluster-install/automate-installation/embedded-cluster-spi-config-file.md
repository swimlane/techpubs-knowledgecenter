Embedded Cluster SPI Config File
########

Here is a reference of the available configurable options for an
embedded cluster Swimlane deployment. Refer to `Configure the Swimlane
Platform for an Embedded Cluster
Install <../configure-the-swimlane-platform-for-an-embedded-cluster-install.htm>`__
for more explanation of these options.

Required Configuration Options
##############--

An SPI config file requires certain MongoDB options to be set in order
to be valid for deployment. These options will change depending on your
MongoDB setup. Refer to the `MongoDB Settings <#MongoDB>`__ section to
determine which settings you need to create a valid SPI config file.

Some options are dependent on other options being enabled or set to
valid values, refer to the `Requirements` column in each of the
sections below:

Configuration Options
###############~

Ingress Settings
################

To access the Swimlane UI, either `expose_web_service_externally` or
`use_included_ingress` config options must be enabled.

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| expose_     | Enable this |             | boolean     | "0" is      |
| web_service | option when |             | integer     | false, "1"  |
| _externally | using a     |             |             | is true     |
|             | Layer 7     |             |             |             |
|             | load        |             |             |             |
|             | balancer.   |             |             |             |
|             | The         |             |             |             |
|             | Swimlane    |             |             |             |
|             | web service |             |             |             |
|             | will be     |             |             |             |
|             | directly    |             |             |             |
|             | exposed     |             |             |             |
|             | from each   |             |             |             |
|             | node in the |             |             |             |
|             | cluster on  |             |             |             |
|             | TCP port    |             |             |             |
|             | 4443.       |             |             |             |
+######-+######-+######-+######-+######-+
| swimla      | Set the     | Requires    | string      | FQDN        |
| ne_hostname | hostname    | `          |             | Hostname    |
|             | used to     | use_include |             |             |
|             | access      | d_ingress` |             |             |
|             | swimlane.   | to be       |             |             |
|             |             | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| use_inclu   | Enable the  | Requires    | boolean     | "0" is      |
| ded_ingress | included    | `swimlane  | integer     | false, "1"  |
|             | ingress to  | _hostname` |             | is true     |
|             | access the  | to be set.  |             |             |
|             | Swimlane    |             |             |             |
|             | web pod.    |             |             |             |
+######-+######-+######-+######-+######-+
| sw          | Enable the  | Requires    | boolean     | "0" is      |
| imlane_tls_ | upload of a | `          | integer     | false, "1"  |
| cert_upload | certificate | use_include |             | is true     |
|             | and key for | d_ingress` |             |             |
|             | Swimlane    | to be       |             |             |
|             | web         | enabled.    |             |             |
|             | traffic.    |             |             |             |
+######-+######-+######-+######-+######-+
| swimla      | Set the     | Requires    | Base64      |             |
| ne_tls_cert | certificate | `          | Encoded RSA |             |
|             | that you    | use_include | Formatted   |             |
|             | want        | d_ingress` | Certificate |             |
|             | Swimlane to | and         |             |             |
|             | use for web | `swim      |             |             |
|             | traffic.    | lane_tls_ce |             |             |
|             | Corresponds | rt_upload` |             |             |
|             | to          | to be       |             |             |
|             | `swimlan   | enabled.    |             |             |
|             | e_tls_key` |             |             |             |
|             | config      |             |             |             |
|             | option.     |             |             |             |
+######-+######-+######-+######-+######-+
| swiml       | Set the key | Requires    | Base64      |             |
| ane_tls_key | that you    | `          | Encoded RSA |             |
|             | want        | use_include | Formatted   |             |
|             | Swimlane to | d_ingress` | Key         |             |
|             | use for web | and         |             |             |
|             | traffic.    | `swim      |             |             |
|             |             | lane_tls_ce |             |             |
|             | Corresponds | rt_upload` |             |             |
|             | to          | to be       |             |             |
|             | `swimlane  | enabled.    |             |             |
|             | _tls_cert` |             |             |             |
|             | config      |             |             |             |
|             | option.     |             |             |             |
+######-+######-+######-+######-+######-+
| swimlane_t  | Enable the  |             | boolean     | "0" is      |
| ls_cert_upl | upload of a |             | integer     | false, "1"  |
| oad_backend | cerfificate |             |             | is true     |
|             | and key for |             |             |             |
|             | Swimlane    |             |             |             |
|             | backend     |             |             |             |
|             | traffic.    |             |             |             |
+######-+######-+######-+######-+######-+
| swi         | Set the     | Requires    | Base64      |             |
| mlane_tls_c | certificate | `s         | Encoded RSA |             |
| ert_backend | that you    | wimlane_tls | Formatted   |             |
|             | want        | _cert_uploa | Certificate |             |
|             | Swimlane to | d_backend` |             |             |
|             | use for     | to be       |             |             |
|             | backend     | enabled.    |             |             |
|             | traffic.    |             |             |             |
|             |             |             |             |             |
|             | Corresponds |             |             |             |
|             | to          |             |             |             |
|             | `swi       |             |             |             |
|             | mlane_tls_k |             |             |             |
|             | ey_backed` |             |             |             |
|             | config      |             |             |             |
|             | option.     |             |             |             |
+######-+######-+######-+######-+######-+
| sw          | Set the key | Requires    | Base64      |             |
| imlane_tls_ | that you    | `s         | Encoded RSA |             |
| key_backend | want        | wimlane_tls | Formatted   |             |
|             | Swimlane to | _cert_uploa | Key         |             |
|             | use for     | d_backend` |             |             |
|             | backend     | to be       |             |             |
|             | traffic.    | enabled.    |             |             |
|             |             |             |             |             |
|             | Corresponds |             |             |             |
|             | to          |             |             |             |
|             | `swiml     |             |             |             |
|             | ane_tls_cer |             |             |             |
|             | t_backend` |             |             |             |
|             | config      |             |             |             |
|             | option.     |             |             |             |
+######-+######-+######-+######-+######-+

Swimlane Settings
################^

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| aspne       | The type of |             | string      | "as         |
| tcore_envir | Swimlane    |             |             | pnetcore_en |
| onment_type | environment |             |             | vironment_d |
|             | - either    |             |             | evelopment" |
|             | Development |             |             | or          |
|             | or          |             |             | "a          |
|             | Production. |             |             | spnetcore_e |
|             |             |             |             | nvironment_ |
|             |             |             |             | production" |
+######-+######-+######-+######-+######-+
| swimlane_au | Turn Audit  |             | boolean     | "0" is      |
| dit_logging | Logging on  |             | integer     | false, "1"  |
|             | or off for  |             |             | is true     |
|             | Swimlane.   |             |             |             |
+######-+######-+######-+######-+######-+
| swimla      | The logging | Requires    | string      | "Debug",    |
| ne_audit_lo | level for   | `sw        |             | "Info",     |
| gging_level | the         | imlane_audi |             | "Warn", or  |
|             | Swimlane    | t_logging` |             | "Error"     |
|             | audit logs. | to be       |             |             |
|             |             | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| swimlan     | Set the     |             | string      | DEFAULT     |
| e_openssl_c | level of    |             |             | @SECLEVEL=2 |
| ipherstring | openssl     |             |             |             |
|             | cipher.     |             |             |             |
+######-+######-+######-+######-+######-+
| swimla      | Set the     |             | string      | TLSv1.2     |
| ne_openssl_ | minimum     |             |             |             |
| minprotocol | level of    |             |             |             |
|             | OpenSSL     |             |             |             |
|             | protocol.   |             |             |             |
+######-+######-+######-+######-+######-+
| mongo_exter | Expose      | Only        | boolean     | "0" is      |
| nal_service | MongoDB     | applicable  | integer     | false, "1"  |
|             | externally  | with        |             | is true     |
|             | on each     | embedded    |             |             |
|             | node        | MongoDB     |             |             |
+######-+######-+######-+######-+######-+
| pip_config  | The pip     | Requires    | Base64      |             |
|             | config file | `pip_conf  | Encoded pip |             |
|             | that will   | ig_upload` | config file |             |
|             | be uploaded | to be       |             |             |
|             | into the    | enabled.    |             |             |
|             | Swimlane    |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pip_co      | Enable the  |             | boolean     | "0" is      |
| nfig_upload | upload of   |             | integer     | false, "1"  |
|             | the pip     |             |             | is true     |
|             | config file |             |             |             |
|             | specified   |             |             |             |
|             | in          |             |             |             |
|             | `pi        |             |             |             |
|             | p_config`. |             |             |             |
+######-+######-+######-+######-+######-+
| swim        | Enable the  |             | boolean     | "0" is      |
| lane_chrome | Swimlane    |             | integer     | false, "1"  |
|             | chrome pod  |             |             | is true     |
|             | for         |             |             |             |
|             | deployment. |             |             |             |
+######-+######-+######-+######-+######-+
| sw          | Enable the  |             | boolean     | "0" is      |
| imlane_sysl | Swimlane    |             | integer     | false, "1"  |
| og_receiver | syslog      |             |             | is true     |
|             | receiver    |             |             |             |
|             | pod for     |             |             |             |
|             | deployment. |             |             |             |
+######-+######-+######-+######-+######-+
| swimlan     | Set the     | Requires    | integer     |             |
| e_syslog_re | port the    | `swim      |             |             |
| ceiver_port | Swimlane    | lane_syslog |             |             |
|             | syslog      | _receiver` |             |             |
|             | receiver    | to be       |             |             |
|             | will use.   | enabled     |             |             |
+######-+######-+######-+######-+######-+
| third_      | Set any     | Requires    | Base64      |             |
| party_certs | third party | `thir      | Encoded RSA |             |
|             | certs that  | d_party_cer | Formatted   |             |
|             | you want    | ts_upload` | CA          |             |
|             | Swimlane to | to be       | C           |             |
|             | be able to  | enabled.    | ertificate> |             |
|             | use.        |             |             |             |
+######-+######-+######-+######-+######-+
| th          | Enable the  |             | boolean     | "0" is      |
| ird_party_c | upload of   |             | integer     | false, "1"  |
| erts_upload | any third   |             |             | is true     |
|             | party       |             |             |             |
|             | certs.      |             |             |             |
+######-+######-+######-+######-+######-+

MongoDB Settings
################

MongoDB can either be deployed as part of the embedded cluster or
connected to externally. The config option
`mongo_use_external_deployment` controls this setting. By default,
this is set to `0`, meaning an embedded cluster will be deployed and
used. If set to `1`, no embedded MongoDB cluster will be deployed.
Refer to `Deploy with an External MongoDB
Cluster <../deploy-with-an-external-mongodb-cluster.htm>`__ for more
explanation on external cluster options.

Required Embedded MongoDB Settings
''''''''''''''''''''''''''''''''''

These settings are required to be set for any SPI Install with an
embedded MongoDB cluster.

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| swimlan     | Set the     | Has to be   | Base64      |             |
| e_database_ | database    | identical   | Encoded     |             |
| encrypt_key | encryption  | to          | String      |             |
|             | key for     | `swimla    |             |             |
|             | MongoDB     | ne_database |             |             |
|             |             | _encrypt_ke |             |             |
|             |             | y_confirm` |             |             |
+######-+######-+######-+######-+######-+
| swim        | Confirm the | Has to be   | Base64      |             |
| lane_databa | database    | identical   | Encoded     |             |
| se_encrypt_ | encryption  | to          | String      |             |
| key_confirm | key for     | `swimlane_ |             |             |
|             | MongoDB     | database_en |             |             |
|             |             | crypt_key` |             |             |
+######-+######-+######-+######-+######-+
| mon         | The MongoDB | Requires    | Base64      |             |
| go_admin_us | password    | `mo        | Encoded     |             |
| er_password | for the     | ngo_admin_u | String      |             |
|             | Admin user. | ser_passwor |             |             |
|             |             | d_confirm` |             |             |
|             |             | to be set   |             |             |
|             |             | and         |             |             |
|             |             | identical.  |             |             |
+######-+######-+######-+######-+######-+
| mongo_admin | C           | Requires    | Base64      |             |
| _user_passw | onfirmation | `mongo     | Encoded     |             |
| ord_confirm | for the     | _admin_user | String      |             |
|             | MongoDB     | _password` |             |             |
|             | password    | to be set   |             |             |
|             | for the     | and         |             |             |
|             | Admin user. | identical.  |             |             |
+######-+######-+######-+######-+######-+
| mongo_      | Set the     | Requires    | Base64      |             |
| swimlane_us | MongoDB     | `mongo     | Encoded     |             |
| er_password | password    | _swimlane_u | String      |             |
|             | for the     | ser_passwor |             |             |
|             | Swimlane    | d_confirm` |             |             |
|             | user.       | to be set   |             |             |
|             |             | and         |             |             |
|             |             | identical.  |             |             |
+######-+######-+######-+######-+######-+
| mon         | Confirm the | Requires    | Base64      |             |
| go_swimlane | MongoDB     | `mongo_sw  | Encoded     |             |
| _user_passw | password    | imlane_user | String      |             |
| ord_confirm | for the     | _password` |             |             |
|             | Swimlane    | to be set   |             |             |
|             | user.       | and         |             |             |
|             |             | identical.  |             |             |
+######-+######-+######-+######-+######-+

Required External MongoDB Settings
''''''''''''''''''''''''''''''''''

These settings are required to be set for any SPI Install that connects
to an external MongoDB cluster.

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| swimlan     | Set the     | Has to be   | Base64      |             |
| e_database_ | database    | identical   | Encoded     |             |
| encrypt_key | encryption  | to          | String      |             |
|             | key for     | `swimla    |             |             |
|             | MongoDB     | ne_database |             |             |
|             |             | _encrypt_ke |             |             |
|             |             | y_confirm` |             |             |
+######-+######-+######-+######-+######-+
| swim        | Confirm the | Has to be   | Base64      |             |
| lane_databa | database    | identical   | Encoded     |             |
| se_encrypt_ | encryption  | to          | String      |             |
| key_confirm | key for     | `swimlane_ |             |             |
|             | MongoDB     | database_en |             |             |
|             |             | crypt_key` |             |             |
+######-+######-+######-+######-+######-+
| mongo_u     | Enable the  | Requires    | boolean     | "0" is      |
| se_external | usage of an | `mongo_use | integer     | false, "1"  |
| _deployment | external    | _external_d |             | is true     |
|             | MongoDB     | eployment` |             |             |
|             | database    | to be       |             |             |
|             |             | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| mongo_      | Set the     | Requires    | string      |             |
| external_db | name of the | `mongo_use |             |             |
|             | Swimlane    | _external_d |             |             |
|             | database in | eployment` |             |             |
|             | your        | to be       |             |             |
|             | external    | enabled.    |             |             |
|             | MongoDB     |             |             |             |
+######-+######-+######-+######-+######-+
| mon         | Set the     | Requires    | string      |             |
| go_external | name of the | `mongo_use |             |             |
| _history_db | Swimlane    | _external_d |             |             |
|             | History     | eployment` |             |             |
|             | database in | to be       |             |             |
|             | your        | enabled.    |             |             |
|             | external    |             |             |             |
|             | MongoDB     |             |             |             |
+######-+######-+######-+######-+######-+
| mongo       | Set the     | Requires    | string      |             |
| _external_h | host name   | `mongo_use |             |             |
| istory_host | that will   | _external_d |             |             |
|             | be used in  | eployment` |             |             |
|             | the MongoDB | to be       |             |             |
|             | connection  | enabled.    |             |             |
|             | URI string  |             |             |             |
|             | for the     |             |             |             |
|             | Swimlane    |             |             |             |
|             | History     |             |             |             |
|             | database.   |             |             |             |
+######-+######-+######-+######-+######-+
| mongo_ex    | Set any     | Requires    | string      |             |
| ternal_hist | options     | `mongo_use |             |             |
| ory_options | that will   | _external_d |             |             |
|             | be used in  | eployment` |             |             |
|             | the MongoDB | to be       |             |             |
|             | connection  | enabled.    |             |             |
|             | URI string  |             |             |             |
|             | for the     |             |             |             |
|             | Swimlane    |             |             |             |
|             | History     |             |             |             |
|             | database.   |             |             |             |
+######-+######-+######-+######-+######-+
| mongo       | Set the     | Requires    | string      |             |
| _external_h | name of the | `mongo_use |             |             |
| istory_user | user that   | _external_d |             |             |
|             | will be     | eployment` |             |             |
|             | used in the | to be       |             |             |
|             | MongoDB     | enabled.    |             |             |
|             | connection  |             |             |             |
|             | URI string  |             |             |             |
|             | for the     |             |             |             |
|             | Swimlane    |             |             |             |
|             | History     |             |             |             |
|             | database.   |             |             |             |
+######-+######-+######-+######-+######-+
| mongo_ex    | Set the     | Requires    | string      |             |
| ternal_host | host name   | `mongo_use |             |             |
|             | that will   | _external_d |             |             |
|             | be used in  | eployment` |             |             |
|             | the MongoDB | to be       |             |             |
|             | connection  | enabled.    |             |             |
|             | URI string  |             |             |             |
|             | for the     |             |             |             |
|             | Swimlane    |             |             |             |
|             | database.   |             |             |             |
+######-+######-+######-+######-+######-+
| mongo_exter | Set any     | Requires    | string      |             |
| nal_options | options     | `mongo_use |             |             |
|             | that will   | _external_d |             |             |
|             | be used in  | eployment` |             |             |
|             | the MongoDB | to be       |             |             |
|             | connection  | enabled.    |             |             |
|             | URI string  |             |             |             |
|             | for the     |             |             |             |
|             | Swimlane    |             |             |             |
|             | database.   |             |             |             |
+######-+######-+######-+######-+######-+
| mongo_ex    | Set the     | Requires    | string      |             |
| ternal_user | name of the | `mongo_use |             |             |
|             | user that   | _external_d |             |             |
|             | will be     | eployment` |             |             |
|             | used in the | to be       |             |             |
|             | MongoDB     | enabled.    |             |             |
|             | connection  |             |             |             |
|             | URI string  |             |             |             |
|             | for the     |             |             |             |
|             | Swimlane    |             |             |             |
|             | database.   |             |             |             |
+######-+######-+######-+######-+######-+
| mon         | Set the     | Requires    | string      |             |
| go_external | password    | `mongo_use |             |             |
| _user_histo | that will   | _external_d |             |             |
| ry_password | be used in  | eployment` |             |             |
|             | the MongoDB | to be       |             |             |
|             | connection  | enabled and |             |             |
|             | URI string  | `mo        |             |             |
|             | for the     | ngo_externa |             |             |
|             | Swimlane    | l_user_hist |             |             |
|             | History     | ory_passwor |             |             |
|             | database.   | d_confirm` |             |             |
|             |             | to be set   |             |             |
|             |             | and         |             |             |
|             |             | identical.  |             |             |
+######-+######-+######-+######-+######-+
| mongo_exter | Confirm the | Requires    |             |             |
| nal_user_hi | password    | `mongo_use |             |             |
| story_passw | that will   | _external_d |             |             |
| ord_confirm | be used in  | eployment` |             |             |
|             | the MongoDB | to be       |             |             |
|             | connection  | enabled and |             |             |
|             | URI string  | `mongo     |             |             |
|             | for the     | _external_u |             |             |
|             | Swimlane    | ser_history |             |             |
|             | History     | _password` |             |             |
|             | database.   | to be set   |             |             |
|             |             | and         |             |             |
|             |             | identical.  |             |             |
+######-+######-+######-+######-+######-+
| mongo_      | Set the     | Requires    |             |             |
| external_us | password    | `mongo_use |             |             |
| er_password | that will   | _external_d |             |             |
|             | be used in  | eployment` |             |             |
|             | the MongoDB | to be       |             |             |
|             | connection  | enabled and |             |             |
|             | URI string  | `mongo     |             |             |
|             | for the     | _external_u |             |             |
|             | Swimlane    | ser_passwor |             |             |
|             | database.   | d_confirm` |             |             |
|             |             | to be set   |             |             |
|             |             | and         |             |             |
|             |             | identical.  |             |             |
+######-+######-+######-+######-+######-+
| mon         | Confirm the | Requires    |             |             |
| go_external | password    | `mongo_use |             |             |
| _user_passw | that will   | _external_d |             |             |
| ord_confirm | be used in  | eployment` |             |             |
|             | the MongoDB | to be       |             |             |
|             | connection  | enabled and |             |             |
|             | URI string  | `mongo_ex  |             |             |
|             | for the     | ternal_user |             |             |
|             | Swimlane    | _password` |             |             |
|             | database.   | to be set   |             |             |
|             |             | and         |             |             |
|             |             | identical.  |             |             |
+######-+######-+######-+######-+######-+

Optional External MongoDB Settings
''''''''''''''''''''''''''''''''''

These settings are optional for an SPI Install that connects to an
external MongoDB cluster:

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| mo          | Set the ca  | Requires    | Base64      |             |
| ngo_ca_cert | certificate | `mongo_use | Encoded RSA |             |
|             | if you need | _external_d | Formatted   |             |
|             | one to      | eployment` | Certificate |             |
|             | connect to  | to be       |             |             |
|             | the         | enabled and |             |             |
|             | Swimlane    | `mongo_e   |             |             |
|             | database in | xternal_upl |             |             |
|             | your        | oad_certs` |             |             |
|             | external    | to be       |             |             |
|             | MongoDB.    | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| mongo       | Enable      | Requires    | boolean     | "0" is      |
| _external_u | uploading   | `mongo_use | integer     | false, "1"  |
| pload_certs | of the ca   | _external_d |             | is true     |
|             | cert        | eployment` |             |             |
|             | specified   | to be       |             |             |
|             | with        | enabled     |             |             |
|             | `mongo     |             |             |             |
|             | _ca_cert`. |             |             |             |
+######-+######-+######-+######-+######-+
| mongo_ex    | Set any     | Requires    | string      |             |
| ternal_hist | options     | `mongo_use |             |             |
| ory_options | that will   | _external_d |             |             |
|             | be used in  | eployment` |             |             |
|             | the MongoDB | to be       |             |             |
|             | connection  | enabled     |             |             |
|             | URI string  |             |             |             |
|             | for the     |             |             |             |
|             | Swimlane    |             |             |             |
|             | History     |             |             |             |
|             | database.   |             |             |             |
+######-+######-+######-+######-+######-+
| mongo_e     | Set the     | Requires    | string      |             |
| xternal_his | prefix that | `mongo_use |             |             |
| tory_prefix | will be     | _external_d |             |             |
|             | used in the | eployment` |             |             |
|             | MongoDB     | to be       |             |             |
|             | connection  | enabled     |             |             |
|             | URI string  |             |             |             |
|             | for the     |             |             |             |
|             | Swimlane    |             |             |             |
|             | History     |             |             |             |
|             | database.   |             |             |             |
+######-+######-+######-+######-+######-+
| mongo_exter | Set any     | Requires    | string      |             |
| nal_options | options     | `mongo_use |             |             |
|             | that will   | _external_d |             |             |
|             | be used in  | eployment` |             |             |
|             | the MongoDB | to be       |             |             |
|             | connection  | enabled     |             |             |
|             | URI string  |             |             |             |
|             | for the     |             |             |             |
|             | Swimlane    |             |             |             |
|             | database.   |             |             |             |
+######-+######-+######-+######-+######-+
| mongo_exte  | Set the     | Requires    | string      |             |
| rnal_prefix | prefix that | `mongo_use |             |             |
|             | will be     | _external_d |             |             |
|             | used in the | eployment` |             |             |
|             | MongoDB     | to be       |             |             |
|             | connection  | enabled     |             |             |
|             | URI string  |             |             |             |
|             | for the     |             |             |             |
|             | Swimlane    |             |             |             |
|             | database.   |             |             |             |
+######-+######-+######-+######-+######-+
| mongo_hist  | Set the ca  | Requires    | Base64      |             |
| ory_ca_cert | certificate | `mongo_use | Encoded RSA |             |
|             | if you need | _external_d | Formatted   |             |
|             | one to      | eployment` | Certificate |             |
|             | connect to  | to be       |             |             |
|             | the         | enabled and |             |             |
|             | Swimlane    | `mong      |             |             |
|             | History     | o_external_ |             |             |
|             | database in | history_upl |             |             |
|             | your        | oad_certs` |             |             |
|             | external    | to be       |             |             |
|             | MongoDB.    | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| mo          | Enable      | Requires    | boolean     | "0" is      |
| ngo_externa | uploading   | `mongo_use | integer     | false, "1"  |
| l_history_u | of the ca   | _external_d |             | is true     |
| pload_certs | cert        | eployment` |             |             |
|             | specified   | to be       |             |             |
|             | with        | enabled     |             |             |
|             | `mo        |             |             |             |
|             | ngo_history |             |             |             |
|             | _ca_cert`. |             |             |             |
+######-+######-+######-+######-+######-+

High Availability Settings
########################^^

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| is_ha       | Enable this |             | boolean     | "0" is      |
|             | option to   |             | integer     | false, "1"  |
|             | deploy      |             |             | is true     |
|             | Swimlane    |             |             |             |
|             | with high   |             |             |             |
|             | a           |             |             |             |
|             | vailability |             |             |             |
|             | after       |             |             |             |
|             | joining     |             |             |             |
|             | multiple    |             |             |             |
|             | nodes.      |             |             |             |
+######-+######-+######-+######-+######-+
| a           | Set the     | Requires    | integer     | "1" if a    |
| pi_replicas | number of   | `is_ha`   |             | single node |
|             | Swimlane    | to be       |             | deployment  |
|             | API pods.   | enabled.    |             | or "3"+ if  |
|             |             |             |             | Swimlane is |
|             |             |             |             | deployed HA |
+######-+######-+######-+######-+######-+
| mon         | Set the     | Requires    | integer     | "1" if a    |
| go_replicas | number of   | `is_ha`   |             | single node |
|             | MongoDB     | to be       |             | deployment  |
|             | replica     | enabled.    |             | or "3"+ if  |
|             | pods.       |             |             | Swimlane is |
|             |             |             |             | deployed HA |
+######-+######-+######-+######-+######-+
| repo        | The number  | Requires    | integer     | "1" if a    |
| rt_replicas | of Swimlane | `is_ha`   |             | single node |
|             | Reports     | to be       |             | deployment  |
|             | pods.       | enabled.    |             | or "3"+ if  |
|             |             |             |             | Swimlane is |
|             |             |             |             | deployed HA |
+######-+######-+######-+######-+######-+
| ta          | The number  | Requires    | integer     | "1" if a    |
| sk_replicas | of Swimlane | `is_ha`   |             | single node |
|             | task pods.  | to be       |             | deployment  |
|             |             | enabled.    |             | or "3"+ if  |
|             |             |             |             | Swimlane is |
|             |             |             |             | deployed HA |
+######-+######-+######-+######-+######-+
| w           | The number  | Requires    | integer     | "1" if a    |
| eb_replicas | of Swimlane | `is_ha`   |             | single node |
|             | web pods.   | to be       |             | deployment  |
|             |             | enabled.    |             | or "3"+ if  |
|             |             |             |             | Swimlane is |
|             |             |             |             | deployed HA |
+######-+######-+######-+######-+######-+
| mongo_an    | An          | Requires    | string      | "hard",     |
| ti_affinity | ti-affinity | `is_ha`   |             | "soft", or  |
|             | setting for | to be       |             | "none"      |
|             | the MongoDB | enabled.    |             |             |
|             | replicaset. |             |             |             |
+######-+######-+######-+######-+######-+
| pod_an      | An          | Requires    | string      | "hard",     |
| ti_affinity | ti-affinity | `is_ha`   |             | "soft", or  |
|             | setting for | to be       |             | "none"      |
|             | the MongoDB | enabled.    |             |             |
|             | replicaset. |             |             |             |
+######-+######-+######-+######-+######-+
