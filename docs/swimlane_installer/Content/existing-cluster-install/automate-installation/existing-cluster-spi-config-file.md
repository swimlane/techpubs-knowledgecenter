Existing Cluster SPI Config File
########

Below is a reference of the available configurable options for an
existing cluster Swimlane deployment. Refer to `Configure the Swimlane
Platform for an Existing Cluster
Install <../configure-the-swimlane-platform-for-an-existing-cluster-install.htm>`__
for an explanation of these options.

Required Configuration Options
#####################~~

An SPI config file requires certain MongoDB options to be set in order
to be valid for deployment. These options will change depending on your
MongoDB setup. Refer to the `MongoDB Settings <#MongoDB>`__ section to
determine which settings you need to create a valid SPI config file.

All other options are optional, but some options are dependent on other
options being enabled or set to valid values. Refer to the
`Requirements` column in each of the sections below, where applicable:

Configuration Options
###############~

Ingress Settings
################

To access the Swimlane UI, either `expose_web_service_externally` or
`swimlane_enable_ingress` config options must be enabled.

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| expose_     | Expose the  |             | boolean     | "0" is      |
| web_service | Swimlane    |             | integer     | false, "1"  |
| _externally | web service |             |             | is true     |
|             | directly    |             |             |             |
|             | from each   |             |             |             |
|             | node in the |             |             |             |
|             | cluster on  |             |             |             |
|             | TCP.        |             |             |             |
+######-+######-+######-+######-+######-+
| e           | Specify the |             | integer     |             |
| xpose_web_s | port that   |             |             |             |
| ervice_exte | the         |             |             |             |
| rnally_port | Swimlane    |             |             |             |
|             | web service |             |             |             |
|             | will use    |             |             |             |
|             | when        |             |             |             |
|             | exposed     |             |             |             |
|             | with        |             |             |             |
|             | `           |             |             |             |
|             | `expose_web |             |             |             |
|             | _service_ex |             |             |             |
|             | ternally`. |             |             |             |
|             | A random    |             |             |             |
|             | port will   |             |             |             |
|             | be selected |             |             |             |
|             | if this is  |             |             |             |
|             | left unset. |             |             |             |
+######-+######-+######-+######-+######-+
| s           | Enable      |             | boolean     | "0" is      |
| wimlane_ena | ingress     |             | integer     | false, "1"  |
| ble_ingress | options for |             |             | is true     |
|             | Swimlane    |             |             |             |
|             | web pods    |             |             |             |
+######-+######-+######-+######-+######-+
| swimla      | Set any     | Requires    | string      |             |
| ne_ingress_ | ingress     | `swi       |             |             |
| annotations | annotations | mlane_enabl |             |             |
|             | for the     | e_ingress` |             |             |
|             | Swimlane    | to be       |             |             |
|             | web         | enabled.    |             |             |
|             | ingress.    |             |             |             |
+######-+######-+######-+######-+######-+
| swimlane_in | Set a       | Requires    | string      | Similar to  |
| gress_hosts | hostname to | `swi       |             | YAML        |
|             | be used     | mlane_enabl |             | format: '-  |
|             | with the    | e_ingress` |             | ""'         |
|             | Swimlane    | to be       |             |             |
|             | web         | enabled.    |             |             |
|             | ingress.    |             |             |             |
+######-+######-+######-+######-+######-+
| swimlane_   | Set any tls | Requires    | string      | Styled as a |
| ingress_tls | settings    | `swi       |             | YAML tls    |
|             | for the     | mlane_enabl |             | block       |
|             | Swimlane    | e_ingress` |             |             |
|             | web         | to be       |             |             |
|             | ingress.    | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| swi         | Enable any  |             | boolean     | "0" is      |
| mlane_set_w | ingress     |             | integer     | false, "1"  |
| eb_service_ | annotations |             |             | is true     |
| annotations | set with    |             |             |             |
|             | `sw        |             |             |             |
|             | imlane_web_ |             |             |             |
|             | service_ann |             |             |             |
|             | otations`. |             |             |             |
+######-+######-+######-+######-+######-+
| swimlane_w  | Set any web | Requires    | string      |             |
| eb_service_ | service     | `swiml     |             |             |
| annotations | annotations | ane_set_web |             |             |
|             | required by | _service_an |             |             |
|             | your        | notations` |             |             |
|             | ingress.    | and         |             |             |
|             |             | `expose_we |             |             |
|             |             | b_service_e |             |             |
|             |             | xternally` |             |             |
|             |             | to be       |             |             |
|             |             | enabled.    |             |             |
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
| onment_type | e           |             |             | vironment_d |
|             | nvironment, |             |             | evelopment" |
|             | either      |             |             | or          |
|             | Development |             |             | "a          |
|             | or          |             |             | spnetcore_e |
|             | Production. |             |             | nvironment_ |
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
| swimlane_st | Set the     |             | string      |             |
| orage_class | name of the |             |             |             |
|             | storage     |             |             |             |
|             | class that  |             |             |             |
|             | Swimlane    |             |             |             |
|             | will use    |             |             |             |
|             | for MongoDB |             |             |             |
|             | PVCs        |             |             |             |
+######-+######-+######-+######-+######-+
| mongo_      | The size of |             | integer     |             |
| volume_size | the PVC     |             |             |             |
|             | that        |             |             |             |
|             | MongoDB     |             |             |             |
|             | will        |             |             |             |
|             | attempt to  |             |             |             |
|             | claim       |             |             |             |
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

Affinity Settings
################^

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| simp        | Set         |             | boolean     | "0" is      |
| le_affinity | an          |             | integer     | false, "1"  |
|             | ti-affinity |             |             | is true     |
|             | for API,    |             |             |             |
|             | Chrome,     |             |             |             |
|             | Reports,    |             |             |             |
|             | Syslog,     |             |             |             |
|             | Tasks,      |             |             |             |
|             | Tools, and  |             |             |             |
|             | Web pods to |             |             |             |
|             | "soft" and  |             |             |             |
|             | MongoDB     |             |             |             |
|             | pods to     |             |             |             |
|             | "hard".     |             |             |             |
+######-+######-+######-+######-+######-+
| mongo_an    | An          | Requires    | string      | "hard",     |
| ti_affinity | ti-affinity | `simple    |             | "soft", or  |
|             | setting for | _affinity` |             | "none"      |
|             | the MongoDB | to be       |             |             |
|             | replicaset. | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| pod_an      | An          | Requires    | string      | "hard",     |
| ti_affinity | ti-affinity | `simple    |             | "soft", or  |
|             | setting for | _affinity` |             | "none"      |
|             | the MongoDB | to be       |             |             |
|             | replicaset. | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| pod_a       | Set         | Requires    | string      | "hard",     |
| ffinity_api | an          | `simple    |             | "soft", or  |
|             | ti-affinity | _affinity` |             | "none"      |
|             | setting for | to be       |             |             |
|             | the         | disabled.   |             |             |
|             | Swimlane    |             |             |             |
|             | API pods.   |             |             |             |
+######-+######-+######-+######-+######-+
| pod_affi    | Set         | Requires    | string      | "hard",     |
| nity_chrome | an          | `simple    |             | "soft", or  |
|             | ti-affinity | _affinity` |             | "none"      |
|             | setting for | to be       |             |             |
|             | the         | disabled.   |             |             |
|             | Swimlane    |             |             |             |
|             | Chrome      |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_affin   | Set         | Requires    | string      | "hard",     |
| ity_mongodb | an          | `simple    |             | "soft", or  |
|             | ti-affinity | _affinity` |             | "none"      |
|             | setting for | to be       |             |             |
|             | the MongoDB | disabled.   |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_affin   | Set         | Requires    | string      | "hard",     |
| ity_reports | an          | `simple    |             | "soft", or  |
|             | ti-affinity | _affinity` |             | "none"      |
|             | setting for | to be       |             |             |
|             | the         | disabled.   |             |             |
|             | Swimlane    |             |             |             |
|             | Reports     |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_affi    | Set         | Requires    | string      | "hard",     |
| nity_syslog | an          | `simple    |             | "soft", or  |
|             | ti-affinity | _affinity` |             | "none"      |
|             | setting for | to be       |             |             |
|             | the         | disabled.   |             |             |
|             | Swimlane    |             |             |             |
|             | Syslog      |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_aff     | Set         | Requires    | string      | "hard",     |
| inity_tasks | an          | `simple    |             | "soft", or  |
|             | ti-affinity | _affinity` |             | "none"      |
|             | setting for | to be       |             |             |
|             | the         | disabled.   |             |             |
|             | Swimlane    |             |             |             |
|             | Tasks pods. |             |             |             |
+######-+######-+######-+######-+######-+
| pod_aff     | Set         | Requires    | string      | "hard",     |
| inity_tools | an          | `simple    |             | "soft", or  |
|             | ti-affinity | _affinity` |             | "none"      |
|             | setting for | to be       |             |             |
|             | the         | disabled.   |             |             |
|             | Swimlane    |             |             |             |
|             | Tools pods. |             |             |             |
+######-+######-+######-+######-+######-+
| pod_a       | Set         | Requires    | string      | "hard",     |
| ffinity_web | an          | `simple    |             | "soft", or  |
|             | ti-affinity | _affinity` |             | "none"      |
|             | setting for | to be       |             |             |
|             | the         | disabled.   |             |             |
|             | Swimlane    |             |             |             |
|             | Web pods.   |             |             |             |
+######-+######-+######-+######-+######-+

Service Account Settings
########################

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| create      | Ensure the  |             | string      | "c          |
| _tools_serv | creation of |             |             | reate_tools |
| ice_account | a service   |             |             | _service_ac |
|             | account for |             |             | count_true" |
|             | Swimlane    |             |             | or          |
|             | Tools.      |             |             | "cr         |
|             |             |             |             | eate_tools_ |
|             |             |             |             | service_acc |
|             |             |             |             | ount_false" |
+######-+######-+######-+######-+######-+
| set_servi   | Enable any  |             | boolean     | "0" is      |
| ce_accounts | pod service |             | integer     | false, "1"  |
|             | account     |             |             | is true     |
|             | names that  |             |             |             |
|             | were set    |             |             |             |
|             | with the    |             |             |             |
|             | `s         |             |             |             |
|             | ervice_acco |             |             |             |
|             | unt_name__< |             |             |             |
|             | pod_name>` |             |             |             |
|             | config      |             |             |             |
|             | option.     |             |             |             |
+######-+######-+######-+######-+######-+
| se          | Set the     | Requires    | string      |             |
| rvice_accou | name of the | `          |             |             |
| nt_name_api | service     | set_service |             |             |
|             | account     | _accounts` |             |             |
|             | that the    | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | API pods    |             |             |             |
|             | will use.   |             |             |             |
+######-+######-+######-+######-+######-+
| servi       | Set the     | Requires    | string      |             |
| ce_account_ | name of the | `          |             |             |
| name_chrome | service     | set_service |             |             |
|             | account     | _accounts` |             |             |
|             | that the    | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Chrome pods |             |             |             |
|             | will use.   |             |             |             |
+######-+######-+######-+######-+######-+
| servic      | Set the     | Requires    | string      |             |
| e_account_n | name of the | `          |             |             |
| ame_mongodb | service     | set_service |             |             |
|             | account     | _accounts` |             |             |
|             | that the    | to be       |             |             |
|             | MongoDB     | enabled.    |             |             |
|             | pods will   |             |             |             |
|             | use.        |             |             |             |
+######-+######-+######-+######-+######-+
| servic      | Set the     | Requires    | string      |             |
| e_account_n | name of the | `          |             |             |
| ame_reports | service     | set_service |             |             |
|             | account     | _accounts` |             |             |
|             | that the    | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Reports     |             |             |             |
|             | pods will   |             |             |             |
|             | use.        |             |             |             |
+######-+######-+######-+######-+######-+
| servi       | Set the     | Requires    | string      |             |
| ce_account_ | name of the | `          |             |             |
| name_syslog | service     | set_service |             |             |
|             | account     | _accounts` |             |             |
|             | that the    | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Syslog pods |             |             |             |
|             | will use.   |             |             |             |
+######-+######-+######-+######-+######-+
| serv        | Set the     | Requires    | string      |             |
| ice_account | name of the | `          |             |             |
| _name_tasks | service     | set_service |             |             |
|             | account     | _accounts` |             |             |
|             | that the    | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Tasks pods  |             |             |             |
|             | will use.   |             |             |             |
+######-+######-+######-+######-+######-+
| serv        | Set the     | Requires    | string      |             |
| ice_account | name of the | `          |             |             |
| _name_tools | service     | set_service |             |             |
|             | account     | _accounts` |             |             |
|             | that the    | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Tools pods  |             |             |             |
|             | will use.   |             |             |             |
+######-+######-+######-+######-+######-+
| se          | Set the     | Requires    | string      |             |
| rvice_accou | name of the | `          |             |             |
| nt_name_web | service     | set_service |             |             |
|             | account     | _accounts` |             |             |
|             | that the    | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Web pods    |             |             |             |
|             | will use.   |             |             |             |
+######-+######-+######-+######-+######-+

Annotation Settings
################^^^

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| set_pod_    | Enable any  |             | boolean     | "0" is      |
| annotations | pod         |             | integer     | false, "1"  |
|             | annotations |             |             | is true     |
|             | that were   |             |             |             |
|             | set with    |             |             |             |
|             | the         |             |             |             |
|             | `pod_an    |             |             |             |
|             | notations_< |             |             |             |
|             | pod_name>` |             |             |             |
|             | config      |             |             |             |
|             | option.     |             |             |             |
+######-+######-+######-+######-+######-+
| pod_anno    | Set         | Requires    | string      |             |
| tations_api | additional  | `           |             |             |
|             | pod         | `set_pod_an |             |             |
|             | annotations | notations` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | API pods.   |             |             |             |
+######-+######-+######-+######-+######-+
| pod_annotat | Set         | Requires    | string      |             |
| ions_chrome | additional  | `           |             |             |
|             | pod         | `set_pod_an |             |             |
|             | annotations | notations` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Chrome      |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| p           | Set         | Requires    | string      |             |
| od_annotati | additional  | `           |             |             |
| ons_mongodb | pod         | `set_pod_an |             |             |
|             | annotations | notations` |             |             |
|             | for the     | to be       |             |             |
|             | MongoDB     | enabled.    |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| p           | Set         | Requires    | string      |             |
| od_annotati | additional  | `           |             |             |
| ons_reports | pod         | `set_pod_an |             |             |
|             | annotations | notations` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Reports     |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_annotat | Set         | Requires    | string      |             |
| ions_syslog | additional  | `           |             |             |
|             | pod         | `set_pod_an |             |             |
|             | annotations | notations` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Syslog      |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_annota  | Set         | Requires    | string      |             |
| tions_tasks | additional  | `           |             |             |
|             | pod         | `set_pod_an |             |             |
|             | annotations | notations` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Tasks pods. |             |             |             |
+######-+######-+######-+######-+######-+
| pod_annota  | Set         | Requires    | string      |             |
| tions_tools | additional  | `           |             |             |
|             | pod         | `set_pod_an |             |             |
|             | annotations | notations` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Tools pods. |             |             |             |
+######-+######-+######-+######-+######-+
| pod_anno    | Set         | Requires    | string      |             |
| tations_web | additional  | `           |             |             |
|             | pod         | `set_pod_an |             |             |
|             | annotations | notations` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Web pods.   |             |             |             |
+######-+######-+######-+######-+######-+

Label Settings
############^^

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| set         | Enable any  |             | boolean     | "0" is      |
| _pod_labels | pod labels  |             | integer     | false, "1"  |
|             | that were   |             |             | is true     |
|             | set with    |             |             |             |
|             | the         |             |             |             |
|             | `p         |             |             |             |
|             | od_labels_< |             |             |             |
|             | pod_name>` |             |             |             |
|             | config      |             |             |             |
|             | option.     |             |             |             |
+######-+######-+######-+######-+######-+
| pod         | Set         | Requires    | string      |             |
| _labels_api | additional  | `set_p     |             |             |
|             | pod labels  | od_labels` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | API pods.   |             |             |             |
+######-+######-+######-+######-+######-+
| pod_la      | Set         | Requires    | string      |             |
| bels_chrome | additional  | `set_p     |             |             |
|             | pod labels  | od_labels` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Chrome      |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_lab     | Set         | Requires    | string      |             |
| els_mongodb | additional  | `set_p     |             |             |
|             | pod labels  | od_labels` |             |             |
|             | for the     | to be       |             |             |
|             | MongoDB     | enabled.    |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_lab     | Set         | Requires    | string      |             |
| els_reports | additional  | `set_p     |             |             |
|             | pod labels  | od_labels` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Reports     |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_la      | Set         | Requires    | string      |             |
| bels_syslog | additional  | `set_p     |             |             |
|             | pod labels  | od_labels` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Syslog      |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_l       | Set         | Requires    | string      |             |
| abels_tasks | additional  | `set_p     |             |             |
|             | pod labels  | od_labels` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Tasks pods. |             |             |             |
+######-+######-+######-+######-+######-+
| pod_l       | Set         | Requires    | string      |             |
| abels_tools | additional  | `set_p     |             |             |
|             | pod labels  | od_labels` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Tools pods. |             |             |             |
+######-+######-+######-+######-+######-+
| pod         | Set         | Requires    | string      |             |
| _labels_web | additional  | `set_p     |             |             |
|             | pod labels  | od_labels` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Web pods.   |             |             |             |
+######-+######-+######-+######-+######-+

Resource Settings
################^

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| set_po      | Enable any  |             | boolean     | "0" is      |
| d_resources | pod         |             | integer     | false, "1"  |
|             | resource    |             |             | is true     |
|             | limits that |             |             |             |
|             | were set    |             |             |             |
|             | with the    |             |             |             |
|             | `pod_      |             |             |             |
|             | resources_< |             |             |             |
|             | pod_name>` |             |             |             |
|             | config      |             |             |             |
|             | option.     |             |             |             |
+######-+######-+######-+######-+######-+
| pod_re      | Set pod     | Requires    | string      |             |
| sources_api | resource    | `set_pod_  |             |             |
|             | limits for  | resources` |             |             |
|             | the         | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | API pods.   |             |             |             |
+######-+######-+######-+######-+######-+
| pod_resou   | Set pod     | Requires    | string      |             |
| rces_chrome | resource    | `set_pod_  |             |             |
|             | limits for  | resources` |             |             |
|             | the         | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Chrome      |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_resour  | Set pod     | Requires    | string      |             |
| ces_mongodb | resource    | `set_pod_  |             |             |
|             | limits for  | resources` |             |             |
|             | the Main    | to be       |             |             |
|             | MongoDB     | enabled.    |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_        | Set pod     | Requires    | string      |             |
| resources_m | resource    | `set_pod_  |             |             |
| ongodb_init | limits for  | resources` |             |             |
|             | the Initial | to be       |             |             |
|             | MongoDB     | enabled.    |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_resour  | Set pod     | Requires    | string      |             |
| ces_reports | resource    | `set_pod_  |             |             |
|             | limits for  | resources` |             |             |
|             | the         | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Reports     |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_resou   | Set pod     | Requires    | string      |             |
| rces_syslog | resource    | `set_pod_  |             |             |
|             | limits for  | resources` |             |             |
|             | the         | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Syslog      |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| pod_reso    | Set pod     | Requires    | string      |             |
| urces_tasks | resource    | `set_pod_  |             |             |
|             | limits for  | resources` |             |             |
|             | the         | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Tasks pods. |             |             |             |
+######-+######-+######-+######-+######-+
| pod_reso    | Set pod     | Requires    | string      |             |
| urces_tools | resource    | `set_pod_  |             |             |
|             | limits for  | resources` |             |             |
|             | the         | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Tools pods. |             |             |             |
+######-+######-+######-+######-+######-+
| pod_re      | Set pod     | Requires    | string      |             |
| sources_web | resource    | `set_pod_  |             |             |
|             | limits for  | resources` |             |             |
|             | the         | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Web pods.   |             |             |             |
+######-+######-+######-+######-+######-+

Node Selector Settings
####################^^

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| set_pod_nod | Enable any  |             | boolean     | "0" is      |
| e_selectors | node        |             | integer     | false, "1"  |
|             | selecters   |             |             | is true     |
|             | that were   |             |             |             |
|             | set with    |             |             |             |
|             | the         |             |             |             |
|             | `node_     |             |             |             |
|             | selectors_< |             |             |             |
|             | pod_name>` |             |             |             |
|             | config      |             |             |             |
|             | option.     |             |             |             |
+######-+######-+######-+######-+######-+
| node_se     | Set         | Requires    | string      |             |
| lectors_api | additional  | `se        |             |             |
|             | node        | t_pod_node_ |             |             |
|             | selectors   | selectors` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | API pods.   |             |             |             |
+######-+######-+######-+######-+######-+
| node_selec  | Set         | Requires    | string      |             |
| tors_chrome | additional  | `se        |             |             |
|             | node        | t_pod_node_ |             |             |
|             | selectors   | selectors` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Chrome      |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| node_select | Set         | Requires    | string      |             |
| ors_mongodb | additional  | `se        |             |             |
|             | node        | t_pod_node_ |             |             |
|             | selectors   | selectors` |             |             |
|             | for the     | to be       |             |             |
|             | MongoDB     | enabled.    |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| node_select | Set         | Requires    | string      |             |
| ors_reports | additional  | `se        |             |             |
|             | node        | t_pod_node_ |             |             |
|             | selectors   | selectors` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Reports     |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| node_selec  | Set         | Requires    | string      |             |
| tors_syslog | additional  | `se        |             |             |
|             | node        | t_pod_node_ |             |             |
|             | selectors   | selectors` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Syslog      |             |             |             |
|             | pods.       |             |             |             |
+######-+######-+######-+######-+######-+
| node_sele   | Set         | Requires    | string      |             |
| ctors_tasks | additional  | `se        |             |             |
|             | node        | t_pod_node_ |             |             |
|             | selectors   | selectors` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Tasks pods. |             |             |             |
+######-+######-+######-+######-+######-+
| node_sele   | Set         | Requires    | string      |             |
| ctors_tools | additional  | `se        |             |             |
|             | node        | t_pod_node_ |             |             |
|             | selectors   | selectors` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Tools pods. |             |             |             |
+######-+######-+######-+######-+######-+
| node_se     | Set         | Requires    | string      |             |
| lectors_web | additional  | `se        |             |             |
|             | node        | t_pod_node_ |             |             |
|             | selectors   | selectors` |             |             |
|             | for the     | to be       |             |             |
|             | Swimlane    | enabled.    |             |             |
|             | Web pods.   |             |             |             |
+######-+######-+######-+######-+######-+

Tolerations Settings
####################

+######-+######-+######-+######-+######-+
| Key         | Description | R           | Type        | Accepted    |
|             |             | equirements |             | value       |
|             |             |             |             | (where      |
|             |             |             |             | applicable) |
+###=+###=+###=+###=+###=+
| set_pod_    | Enable any  |             | boolean     | "0" is      |
| tolerations | pod         |             | integer     | false, "1"  |
|             | tolerations |             |             | is true     |
|             | that were   |             |             |             |
|             | set with    |             |             |             |
|             | the         |             |             |             |
|             | `pod_to    |             |             |             |
|             | lerations_< |             |             |             |
|             | pod_name>` |             |             |             |
|             | config      |             |             |             |
|             | option.     |             |             |             |
+######-+######-+######-+######-+######-+
| pod_tole    | Set pod     | Requires    | string      |             |
| rations_api | tolerations | `           |             |             |
|             | for the     | `set_pod_to |             |             |
|             | Swimlane    | lerations` |             |             |
|             | API pods.   | to be       |             |             |
|             |             | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| pod_tolerat | Set pod     | Requires    | string      |             |
| ions_chrome | tolerations | `           |             |             |
|             | for the     | `set_pod_to |             |             |
|             | Swimlane    | lerations` |             |             |
|             | Chrome      | to be       |             |             |
|             | pods.       | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| p           | Set pod     | Requires    | string      |             |
| od_tolerati | tolerations | `           |             |             |
| ons_mongodb | for the     | `set_pod_to |             |             |
|             | MongoDB     | lerations` |             |             |
|             | pods.       | to be       |             |             |
|             |             | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| p           | Set pod     | Requires    | string      |             |
| od_tolerati | tolerations | `           |             |             |
| ons_reports | for the     | `set_pod_to |             |             |
|             | Swimlane    | lerations` |             |             |
|             | Reports     | to be       |             |             |
|             | pods.       | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| pod_tolerat | Set pod     | Requires    | string      |             |
| ions_syslog | tolerations | `           |             |             |
|             | for the     | `set_pod_to |             |             |
|             | Swimlane    | lerations` |             |             |
|             | Syslog      | to be       |             |             |
|             | pods.       | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| pod_tolera  | Set pod     | Requires    | string      |             |
| tions_tasks | tolerations | `           |             |             |
|             | for the     | `set_pod_to |             |             |
|             | Swimlane    | lerations` |             |             |
|             | Tasks pods. | to be       |             |             |
|             |             | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| pod_tolera  | Set pod     | Requires    | string      |             |
| tions_tools | tolerations | `           |             |             |
|             | for the     | `set_pod_to |             |             |
|             | Swimlane    | lerations` |             |             |
|             | Tools pods. | to be       |             |             |
|             |             | enabled.    |             |             |
+######-+######-+######-+######-+######-+
| pod_tole    | Set pod     | Requires    | string      |             |
| rations_web | tolerations | `           |             |             |
|             | for the     | `set_pod_to |             |             |
|             | Swimlane    | lerations` |             |             |
|             | Web pods.   | to be       |             |             |
|             |             | enabled.    |             |             |
+######-+######-+######-+######-+######-+
