Context Variables
=================

Context variables are variables that hold a variety of contextual
information relating to the current playbook, its invocation parameters,
and executed actions.

Using context variables is especially helpful when creating `Playbook
Triggers <playbook-triggers/playbook-triggers.htm>`__ to help define
parameters and retrieve/store specific data.

This table lists some of the helpful context variables you can use.

+----------------------+----------------------+----------------------+
| Context Variables    | Description          | Example              |
+======================+======================+======================+
| $playbook            | The name of the      | find_iocs            |
|                      | playbook             |                      |
+----------------------+----------------------+----------------------+
| $inputs              | User-defined schema  | "$inputs": {         |
|                      | of inputs for a      |                      |
|                      | playbook             | "some_str            |
|                      |                      | ing_playbook_input": |
|                      |                      | "some_string_pas     |
|                      |                      | sed_to_the_playbook" |
|                      |                      |                      |
|                      |                      | }                    |
+----------------------+----------------------+----------------------+
| $event               | Data related to the  | **Webhook**          |
|                      | sensor event that    |                      |
|                      | triggered the        |                      |
|                      | playbook             |                      |
|                      |                      | "$event": {          |
|                      |                      |                      |
|                      |                      | "data": {            |
|                      |                      |                      |
|                      |                      | "headers": {         |
|                      |                      |                      |
|                      |                      | "x-account-id":      |
|                      |                      | "228edce1-be3e-4b45  |
|                      |                      | -99d5-b4a11ac41489", |
|                      |                      |                      |
|                      |                      | "x-tenant-id":       |
|                      |                      | "911b9bae-540e-4064  |
|                      |                      | -93dc-33c1364587dd", |
|                      |                      |                      |
|                      |                      | "host":              |
|                      |                      | "turbine_            |
|                      |                      | webhook_agent_pool", |
|                      |                      |                      |
|                      |                      | "connection":        |
|                      |                      | "close",             |
|                      |                      |                      |
|                      |                      | "authorization":     |
|                      |                      | "Basic               |
|                      |                      | U3dpbWxhbmU6YXNk",   |
|                      |                      |                      |
|                      |                      | "user-agent":        |
|                      |                      | "Pos                 |
|                      |                      | tmanRuntime/7.28.3", |
|                      |                      |                      |
|                      |                      | "accept": "\*/\*",   |
|                      |                      |                      |
|                      |                      | "cache-control":     |
|                      |                      | "no-cache",          |
|                      |                      |                      |
|                      |                      | "postman-token":     |
|                      |                      | "fc42206a-66a0-4649  |
|                      |                      | -9885-a16e00ab8e9d", |
|                      |                      |                      |
|                      |                      | "accept-encoding":   |
|                      |                      | "gzip, deflate, br"  |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "url": {             |
|                      |                      |                      |
|                      |                      | "hostname":          |
|                      |                      | "turbine_            |
|                      |                      | webhook_agent_pool", |
|                      |                      |                      |
|                      |                      | "href":              |
|                      |                      | "http:/              |
|                      |                      | /turbine_webhook_age |
|                      |                      | nt_pool/v1/webhook/5 |
|                      |                      | e60bc88-5780-42a9-80 |
|                      |                      | 26-329fd0060d55/trig |
|                      |                      | gers_webhook_am9pa", |
|                      |                      |                      |
|                      |                      | "ips": [],           |
|                      |                      |                      |
|                      |                      | "pathname":          |
|                      |                      | "/v1/webhook/5       |
|                      |                      | e60bc88-5780-42a9-80 |
|                      |                      | 26-329fd0060d55/trig |
|                      |                      | gers_webhook_am9pa", |
|                      |                      |                      |
|                      |                      | "port": 80,          |
|                      |                      |                      |
|                      |                      | "protocol": "http",  |
|                      |                      |                      |
|                      |                      | "query": {}          |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "method": "GET"      |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "post": {},          |
|                      |                      |                      |
|                      |                      | "type":              |
|                      |                      | "custom_webhook",    |
|                      |                      |                      |
|                      |                      | "action": "request", |
|                      |                      |                      |
|                      |                      | "fqn":               |
|                      |                      | "turbine.cust        |
|                      |                      | om_webhook.request", |
|                      |                      |                      |
|                      |                      | "timestamp":         |
|                      |                      | 1717444327944,       |
|                      |                      |                      |
|                      |                      | "sensor": {          |
|                      |                      |                      |
|                      |                      | "name":              |
|                      |                      | "trig                |
|                      |                      | gers_webhook_am9pa", |
|                      |                      |                      |
|                      |                      | "tags": {}           |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "agent": {           |
|                      |                      |                      |
|                      |                      | "name":              |
|                      |                      | "webho               |
|                      |                      | ok-agent-a966253ee5a |
|                      |                      | 4-f975040d-f3e5-4a96 |
|                      |                      | -beec-bd729605537e", |
|                      |                      |                      |
|                      |                      | "tags": {}           |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "tags": {}           |
|                      |                      |                      |
|                      |                      | },                   |
+----------------------+----------------------+----------------------+
| $event               | Data related to the  | **Record**           |
|                      | sensor event that    |                      |
|                      | triggered the        |                      |
|                      | playbook             |                      |
|                      |                      | "$event": {          |
|                      |                      |                      |
|                      |                      | "data": {            |
|                      |                      |                      |
|                      |                      | "application": {     |
|                      |                      |                      |
|                      |                      | "id":                |
|                      |                      | "aXRvgAk9ufrM86LOp", |
|                      |                      |                      |
|                      |                      | "uid":               |
|                      |                      | "rec                 |
|                      |                      | ords-testing-658c9", |
|                      |                      |                      |
|                      |                      | "name": "Records     |
|                      |                      | Testing"             |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "currentUser": {     |
|                      |                      |                      |
|                      |                      | "id":                |
|                      |                      | "a6d44865-ed5d-4b9a  |
|                      |                      | -a29d-d0d3302d5629", |
|                      |                      |                      |
|                      |                      | "username":          |
|                      |                      | "swimlane            |
|                      |                      | admin@swimlane.com", |
|                      |                      |                      |
|                      |                      | "isSystemUser":      |
|                      |                      | false                |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "record": {          |
|                      |                      |                      |
|                      |                      | "id":                |
|                      |                      | "aN1Kk0cot6maprd0C", |
|                      |                      |                      |
|                      |                      | "url":               |
|                      |                      | "https://localho     |
|                      |                      | st:443/account/228ed |
|                      |                      | ce1-be3e-4b45-99d5-b |
|                      |                      | 4a11ac41489/tenant/9 |
|                      |                      | 11b9bae-540e-4064-93 |
|                      |                      | dc-33c1364587dd/reco |
|                      |                      | rd/aXRvgAk9ufrM86LOp |
|                      |                      | /aN1Kk0cot6maprd0C", |
|                      |                      |                      |
|                      |                      | "values": {          |
|                      |                      |                      |
|                      |                      | "text": "Example",   |
|                      |                      |                      |
|                      |                      | "multiline-text":    |
|                      |                      | "Multi line          |
|                      |                      | example",            |
|                      |                      |                      |
|                      |                      | "radio-buttons":     |
|                      |                      | "option-2",          |
|                      |                      |                      |
|                      |                      | "numeric": 1,        |
|                      |                      |                      |
|                      |                      | "tracking-id":       |
|                      |                      | "ORT-9",             |
|                      |                      |                      |
|                      |                      | "first-created":     |
|                      |                      | "2024-06-03          |
|                      |                      | T19:56:10.0259161Z", |
|                      |                      |                      |
|                      |                      | "last-updated":      |
|                      |                      | "2024-06-0           |
|                      |                      | 3T19:56:10.0606078Z" |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "post": {},          |
|                      |                      |                      |
|                      |                      | "type": "record",    |
|                      |                      |                      |
|                      |                      | "action": "create",  |
|                      |                      |                      |
|                      |                      | "fqn":               |
|                      |                      | "tur                 |
|                      |                      | bine.record.create", |
|                      |                      |                      |
|                      |                      | "timestamp":         |
|                      |                      | 1717444570268,       |
|                      |                      |                      |
|                      |                      | "sensor": {          |
|                      |                      |                      |
|                      |                      | "name": "turbine",   |
|                      |                      |                      |
|                      |                      | "tags": {}           |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "agent": {           |
|                      |                      |                      |
|                      |                      | "name": "sw_api",    |
|                      |                      |                      |
|                      |                      | "tags": {}           |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "tags": {}           |
|                      |                      |                      |
|                      |                      | }                    |
+----------------------+----------------------+----------------------+
| $event               | Data related to the  | **Cron**             |
|                      | sensor event that    |                      |
|                      | triggered the        |                      |
|                      | playbook             |                      |
|                      |                      | "$event": {          |
|                      |                      |                      |
|                      |                      | "data": {            |
|                      |                      |                      |
|                      |                      | "cron": "\* \* \* \* |
|                      |                      | \*"                  |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "post": {},          |
|                      |                      |                      |
|                      |                      | "type": "schedule",  |
|                      |                      |                      |
|                      |                      | "action": "cron",    |
|                      |                      |                      |
|                      |                      | "fqn":               |
|                      |                      | "tur                 |
|                      |                      | bine.schedule.cron", |
|                      |                      |                      |
|                      |                      | "timestamp":         |
|                      |                      | 1717446660290,       |
|                      |                      |                      |
|                      |                      | "sensor": {          |
|                      |                      |                      |
|                      |                      | "name": "turbine",   |
|                      |                      |                      |
|                      |                      | "tags": {}           |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "agent": {           |
|                      |                      |                      |
|                      |                      | "name":              |
|                      |                      | "engine-local",      |
|                      |                      |                      |
|                      |                      | "tags": {}           |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "tags": {}           |
|                      |                      |                      |
|                      |                      | }                    |
+----------------------+----------------------+----------------------+
| $event               | Data related to the  | **Manual**           |
|                      | sensor event that    |                      |
|                      | triggered the        |                      |
|                      | playbook             |                      |
|                      |                      | "$event": {          |
|                      |                      |                      |
|                      |                      | "data": {},          |
|                      |                      |                      |
|                      |                      | "post": {},          |
|                      |                      |                      |
|                      |                      | "type": "playbook",  |
|                      |                      |                      |
|                      |                      | "action":            |
|                      |                      | "executeTest",       |
|                      |                      |                      |
|                      |                      | "fqn":               |
|                      |                      | "turbine.pl          |
|                      |                      | aybook.executeTest", |
|                      |                      |                      |
|                      |                      | "timestamp":         |
|                      |                      | 1717442522695,       |
|                      |                      |                      |
|                      |                      | "sensor": {          |
|                      |                      |                      |
|                      |                      | "name": "turbine",   |
|                      |                      |                      |
|                      |                      | "tags": {}           |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "agent": {           |
|                      |                      |                      |
|                      |                      | "name":              |
|                      |                      | "api-local-dev",     |
|                      |                      |                      |
|                      |                      | "tags": {}           |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "tags": {}           |
+----------------------+----------------------+----------------------+
| $event.data          | Data/inputs from the |                      |
|                      | event                |                      |
+----------------------+----------------------+----------------------+
| $event.post          | Any data             |                      |
|                      | post-processing from |                      |
|                      | the trigger          |                      |
+----------------------+----------------------+----------------------+
| $event.type          | Type of event        |                      |
|                      | (events, sensors,    |                      |
|                      | schedules)           |                      |
+----------------------+----------------------+----------------------+
| $event.action        | Action of the event  |                      |
|                      | type                 |                      |
+----------------------+----------------------+----------------------+
| $event.fqn           | Fully qualified      |                      |
|                      | event name           |                      |
+----------------------+----------------------+----------------------+
| $event.timestamp     | Integer timestamp of |                      |
|                      | the event in         |                      |
|                      | milliseconds         |                      |
+----------------------+----------------------+----------------------+
| $event.sensor.name   | Name of the sensor   |                      |
|                      | that received the    |                      |
|                      | event                |                      |
+----------------------+----------------------+----------------------+
| $event.sensor.tags   | Tags associated with |                      |
|                      | the sensor           |                      |
+----------------------+----------------------+----------------------+
| $event.agent.name    | Name of the agent    |                      |
|                      | that was running the |                      |
|                      | sensor               |                      |
+----------------------+----------------------+----------------------+
| $event.agent.tags    | Tags associated with |                      |
|                      | the agent            |                      |
+----------------------+----------------------+----------------------+
| $event.tags          | Tags associated with |                      |
|                      | the event            |                      |
+----------------------+----------------------+----------------------+
| $trigger.name        | The name of the      | **Cron**             |
|                      | trigger              |                      |
|                      |                      |                      |
|                      |                      |                      |
|                      |                      | "$trigger": {        |
|                      |                      |                      |
|                      |                      | "type": "schedules", |
|                      |                      |                      |
|                      |                      | "name": "cron"       |
|                      |                      |                      |
|                      |                      | }                    |
+----------------------+----------------------+----------------------+
| $trigger.name        | The name of the      | **Webhook**          |
|                      | trigger              |                      |
|                      |                      |                      |
|                      |                      |                      |
|                      |                      | "$trigger": {        |
|                      |                      |                      |
|                      |                      | "type": "sensors",   |
|                      |                      |                      |
|                      |                      | "name":              |
|                      |                      | "tri                 |
|                      |                      | ggers_webhook_acu1r" |
|                      |                      |                      |
|                      |                      | },                   |
+----------------------+----------------------+----------------------+
| $trigger.name        | The name of the      | **Records**          |
|                      | trigger              |                      |
|                      |                      |                      |
|                      |                      |                      |
|                      |                      | "$trigger": {        |
|                      |                      |                      |
|                      |                      | "type": "records",   |
|                      |                      |                      |
|                      |                      | "name":              |
|                      |                      | "a6tgj.create"       |
|                      |                      |                      |
|                      |                      | },                   |
+----------------------+----------------------+----------------------+
| $trigger.name        | The name of the      | **Manual**           |
|                      | trigger              |                      |
|                      |                      |                      |
|                      |                      |                      |
|                      |                      | "$trigger": {        |
|                      |                      |                      |
|                      |                      | "type": "events",    |
|                      |                      |                      |
|                      |                      | "name":              |
|                      |                      | "p                   |
|                      |                      | laybook.executeTest" |
|                      |                      |                      |
|                      |                      | }                    |
+----------------------+----------------------+----------------------+
| $trigger.type        | The type of trigger  |                      |
|                      | (events, sensors,    |                      |
|                      | schedules)           |                      |
+----------------------+----------------------+----------------------+
| $actions             | Object containing    | "$actions": {        |
|                      | all preceding        |                      |
|                      | actions that led to  | "some_create_variabl |
|                      | the current action   | es_action_key_name": |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "result": {          |
|                      |                      |                      |
|                      |                      | "string_at7xg":      |
|                      |                      | "test",              |
|                      |                      |                      |
|                      |                      | "number_ajpro": 1,   |
|                      |                      |                      |
|                      |                      | "boolean_a7qe9":     |
|                      |                      | true,                |
|                      |                      |                      |
|                      |                      | "object_a4k88": {    |
|                      |                      |                      |
|                      |                      | "string_amul7": ""   |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "array_afhe7": [     |
|                      |                      |                      |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "array_agz7a": [     |
|                      |                      |                      |
|                      |                      | ""                   |
|                      |                      |                      |
|                      |                      | ]                    |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | ],                   |
|                      |                      |                      |
|                      |                      | "attachment_ah5dr":  |
|                      |                      | null,                |
|                      |                      |                      |
|                      |                      | "iterable": [        |
|                      |                      |                      |
|                      |                      | 1,                   |
|                      |                      |                      |
|                      |                      | 2,                   |
|                      |                      |                      |
|                      |                      | 0                    |
|                      |                      |                      |
|                      |                      | ]                    |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "published": {},     |
|                      |                      |                      |
|                      |                      | "status": "success"  |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "some_ht             |
|                      |                      | tp_action_key_name": |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "result": {          |
|                      |                      |                      |
|                      |                      | "status_code": 200,  |
|                      |                      |                      |
|                      |                      | "headers": {         |
|                      |                      |                      |
|                      |                      | "date": "Mon, 03 Jun |
|                      |                      | 2024 20:08:02 GMT",  |
|                      |                      |                      |
|                      |                      | "content-type":      |
|                      |                      | "application/json;   |
|                      |                      | charset=utf-8",      |
|                      |                      |                      |
|                      |                      | "content-length":    |
|                      |                      | "2110",              |
|                      |                      |                      |
|                      |                      | "connection":        |
|                      |                      | "close",             |
|                      |                      |                      |
|                      |                      | "etag":              |
|                      |                      | "W                   |
|                      |                      | /\\"83e-HiAiudLaghvV |
|                      |                      | /6XO4efAJkfVWT0\\"", |
|                      |                      |                      |
|                      |                      | "set-cookie": [      |
|                      |                      |                      |
|                      |                      | "sails.sid=s%3       |
|                      |                      | A6NN48IK2HUVfuh99U38 |
|                      |                      | mgwQTe3kfa9ZB.ebTIFf |
|                      |                      | sxekw%2Fn8r1yME8yYz2 |
|                      |                      | VzJxsa7pOsv9hBFmaQk; |
|                      |                      | Path=/; HttpOnly"    |
|                      |                      |                      |
|                      |                      | ]                    |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "status_reason":     |
|                      |                      | "OK",                |
|                      |                      |                      |
|                      |                      | "body": {            |
|                      |                      |                      |
|                      |                      | "args": {            |
|                      |                      |                      |
|                      |                      | "test": "1",         |
|                      |                      |                      |
|                      |                      | "{\\"block_1\\"      |
|                      |                      | :{\\"text\\":\\"some |
|                      |                      | text\\",             |
|                      |                      | \\"text-2\\":\\"more |
|                      |                      | text\\               |
|                      |                      | ",\\"text-list\\":": |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "\\"text1\\",\\"te   |
|                      |                      | xt2\\",\\"text3\\"": |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "1,2.2,3.45,-4": {   |
|                      |                      |                      |
|                      |                      | "\\"                 |
|                      |                      | one\\",\\"three\\"": |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "\\"option-1         |
|                      |                      | \\",\\"option-3\\"": |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "\\"ORT-4\\"": {     |
|                      |                      |                      |
|                      |                      | "[\\"                |
|                      |                      | ORT-4\\",\\"ORT-5\\" |
|                      |                      | ],\\"reference-grid\ |
|                      |                      | \":[\\"ORT-4\\",\\"O |
|                      |                      | RT-5\\"]},\\"block_2 |
|                      |                      | \\":[\\"text1\\",\\" |
|                      |                      | text2\\",\\"text3\\" |
|                      |                      | ],\\"true\\":true}": |
|                      |                      | "[\\"text1\\",\\"te  |
|                      |                      | xt2\\",\\"text3\\"]" |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "headers": {         |
|                      |                      |                      |
|                      |                      | "x-forwarded-proto": |
|                      |                      | "https",             |
|                      |                      |                      |
|                      |                      | "x-forwarded-port":  |
|                      |                      | "443",               |
|                      |                      |                      |
|                      |                      | "host":              |
|                      |                      | "postman-echo.com",  |
|                      |                      |                      |
|                      |                      | "x-amzn-trace-id":   |
|                      |                      | "Ro                  |
|                      |                      | ot=1-665e22a1-454ed5 |
|                      |                      | 8d1b586c896b75161a", |
|                      |                      |                      |
|                      |                      | "accept-encoding":   |
|                      |                      | "gzip, deflate, br"  |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "url":               |
|                      |                      | "https://postma      |
|                      |                      | n-echo.com/get?xxxx" |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "published": {},     |
|                      |                      |                      |
|                      |                      | "status": "success"  |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "some_loop_action":  |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "result": [          |
|                      |                      |                      |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "script_ac4ft": {    |
|                      |                      |                      |
|                      |                      | "result": {          |
|                      |                      |                      |
|                      |                      | "string_ano7f":      |
|                      |                      | "text1"              |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "script_ac4ft": {    |
|                      |                      |                      |
|                      |                      | "result": {          |
|                      |                      |                      |
|                      |                      | "string_ano7f":      |
|                      |                      | "text2"              |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "script_ac4ft": {    |
|                      |                      |                      |
|                      |                      | "result": {          |
|                      |                      |                      |
|                      |                      | "string_ano7f":      |
|                      |                      | "text3"              |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | ],                   |
|                      |                      |                      |
|                      |                      | "published": {},     |
|                      |                      |                      |
|                      |                      | "status": "success"  |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "$parent": {         |
|                      |                      |                      |
|                      |                      | "published": {},     |
|                      |                      |                      |
|                      |                      | "status": "fail"     |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "$current": {        |
|                      |                      |                      |
|                      |                      | "result": {          |
|                      |                      |                      |
|                      |                      | "actions": {         |
|                      |                      |                      |
|                      |                      | "cre                 |
|                      |                      | ateVariables_atysx": |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "result": {          |
|                      |                      |                      |
|                      |                      | "string_awuwp":      |
|                      |                      | "asdf"               |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "published": {},     |
|                      |                      |                      |
|                      |                      | "status": "success"  |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "published": {}      |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "published": {},     |
|                      |                      |                      |
|                      |                      | "status": "success"  |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "                    |
|                      |                      | newComponent_az0s4": |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "result": {          |
|                      |                      |                      |
|                      |                      | "actions": {         |
|                      |                      |                      |
|                      |                      | "cre                 |
|                      |                      | ateVariables_atysx": |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "result": {          |
|                      |                      |                      |
|                      |                      | "string_awuwp":      |
|                      |                      | "asdf"               |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "published": {},     |
|                      |                      |                      |
|                      |                      | "status": "success"  |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "published": {}      |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "published": {},     |
|                      |                      |                      |
|                      |                      | "status": "success"  |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "7_Script": {        |
|                      |                      |                      |
|                      |                      | "result": {},        |
|                      |                      |                      |
|                      |                      | "published": {},     |
|                      |                      |                      |
|                      |                      | "status": "success"  |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "condition_aexis": { |
|                      |                      |                      |
|                      |                      | "result": "3",       |
|                      |                      |                      |
|                      |                      | "published": {},     |
|                      |                      |                      |
|                      |                      | "status": "success"  |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "tr                  |
|                      |                      | ansformation_alag3": |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "result": {          |
|                      |                      |                      |
|                      |                      | "block_1": {         |
|                      |                      |                      |
|                      |                      | "text": "some text", |
|                      |                      |                      |
|                      |                      | "text-2": "more      |
|                      |                      | text",               |
|                      |                      |                      |
|                      |                      | "text-list": [       |
|                      |                      |                      |
|                      |                      | "text1",             |
|                      |                      |                      |
|                      |                      | "text2",             |
|                      |                      |                      |
|                      |                      | "text3"              |
|                      |                      |                      |
|                      |                      | ],                   |
|                      |                      |                      |
|                      |                      | "email":             |
|                      |                      | "ian.sc              |
|                      |                      | hultz@swimlane.com", |
|                      |                      |                      |
|                      |                      | "url":               |
|                      |                      | "ht                  |
|                      |                      | tps://swimlane.com", |
|                      |                      |                      |
|                      |                      | "rich-text":         |
|                      |                      | "<h3>header</h3>",   |
|                      |                      |                      |
|                      |                      | "multiline-text":    |
|                      |                      | "multi               |
|                      |                      | line\\ntext\\ndata", |
|                      |                      |                      |
|                      |                      | "telephone":         |
|                      |                      | "123-345-5678",      |
|                      |                      |                      |
|                      |                      | "ip": "127.0.0.1",   |
|                      |                      |                      |
|                      |                      | "json": "{           |
|                      |                      | \\"property1\\":     |
|                      |                      | \\"value 1\\",       |
|                      |                      | \\"property2\\":     |
|                      |                      | true }",             |
|                      |                      |                      |
|                      |                      | "numeric": 123.4,    |
|                      |                      |                      |
|                      |                      | "numeric-list": [    |
|                      |                      |                      |
|                      |                      | 1,                   |
|                      |                      |                      |
|                      |                      | 2.2,                 |
|                      |                      |                      |
|                      |                      | 3.45,                |
|                      |                      |                      |
|                      |                      | -4                   |
|                      |                      |                      |
|                      |                      | ],                   |
|                      |                      |                      |
|                      |                      | "single-select":     |
|                      |                      | "value-2",           |
|                      |                      |                      |
|                      |                      | "multi-select": [    |
|                      |                      |                      |
|                      |                      | "one",               |
|                      |                      |                      |
|                      |                      | "three"              |
|                      |                      |                      |
|                      |                      | ],                   |
|                      |                      |                      |
|                      |                      | "radio-buttons":     |
|                      |                      | "option-2",          |
|                      |                      |                      |
|                      |                      | "checkboxes": [      |
|                      |                      |                      |
|                      |                      | "option-1",          |
|                      |                      |                      |
|                      |                      | "option-3"           |
|                      |                      |                      |
|                      |                      | ],                   |
|                      |                      |                      |
|                      |                      | "date--time":        |
|                      |                      | "20                  |
|                      |                      | 23-11-20T10:45:03Z", |
|                      |                      |                      |
|                      |                      | "date":              |
|                      |                      | "2023-11-20",        |
|                      |                      |                      |
|                      |                      | "timespan":          |
|                      |                      | "123456789",         |
|                      |                      |                      |
|                      |                      | "time": "10:45:03",  |
|                      |                      |                      |
|                      |                      | "usergroups":        |
|                      |                      | "swimlaneadmin",     |
|                      |                      |                      |
|                      |                      | "reference-single":  |
|                      |                      | [                    |
|                      |                      |                      |
|                      |                      | "ORT-4"              |
|                      |                      |                      |
|                      |                      | ],                   |
|                      |                      |                      |
|                      |                      | "reference-multi": [ |
|                      |                      |                      |
|                      |                      | "ORT-4",             |
|                      |                      |                      |
|                      |                      | "ORT-5"              |
|                      |                      |                      |
|                      |                      | ],                   |
|                      |                      |                      |
|                      |                      | "reference-grid": [  |
|                      |                      |                      |
|                      |                      | "ORT-4",             |
|                      |                      |                      |
|                      |                      | "ORT-5"              |
|                      |                      |                      |
|                      |                      | ]                    |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "block_2": [         |
|                      |                      |                      |
|                      |                      | "text1",             |
|                      |                      |                      |
|                      |                      | "text2",             |
|                      |                      |                      |
|                      |                      | "text3"              |
|                      |                      |                      |
|                      |                      | ],                   |
|                      |                      |                      |
|                      |                      | "true": true         |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "published": {},     |
|                      |                      |                      |
|                      |                      | "status": "success"  |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | },                   |
+----------------------+----------------------+----------------------+
| $a                   | Result of the        |                      |
| ctions.<name>.result | specified action     |                      |
+----------------------+----------------------+----------------------+
| $actions.<name>.post | Posted values from   |                      |
|                      | the specified action |                      |
+----------------------+----------------------+----------------------+
| $a                   | Status of the        |                      |
| ctions.<name>.status | specified action     |                      |
+----------------------+----------------------+----------------------+
| $act                 | Result of the        |                      |
| ions.$current.result | current action (not  |                      |
|                      | populated until the  |                      |
|                      | action has run)      |                      |
+----------------------+----------------------+----------------------+
| $a                   | Posted values from   |                      |
| ctions.$current.post | the current action   |                      |
|                      | (not populated until |                      |
|                      | the action has run)  |                      |
+----------------------+----------------------+----------------------+
| $ac                  | Result of the        |                      |
| tions.$parent.result | previous action      |                      |
+----------------------+----------------------+----------------------+
| $                    | Posted values from   |                      |
| actions.$parent.post | the previous action  |                      |
+----------------------+----------------------+----------------------+
| $assets              | Object of asset      | "$assets": {         |
|                      | names and their      |                      |
|                      | respective           | "vt_asset": {        |
|                      | parameters           |                      |
|                      |                      | "url":               |
|                      |                      | "https://            |
|                      |                      | www.virustotal.com", |
|                      |                      |                      |
|                      |                      | "x-apikey": "xxx",   |
|                      |                      |                      |
|                      |                      | },                   |
+----------------------+----------------------+----------------------+
| $published           | The current          |                      |
|                      | published object.    |                      |
|                      | Needed when mapping  |                      |
|                      | an output to an      |                      |
|                      | application record   | "$published": {      |
|                      | or to use outside of |                      |
|                      | the playbook         | "published_body": {  |
|                      |                      |                      |
|                      |                      | "access_token":      |
|                      |                      | "test_access_token"  |
|                      |                      |                      |
|                      |                      | },                   |
+----------------------+----------------------+----------------------+
| $repeat (deprecated) | If job is part of    |                      |
|                      | repeat, current      |                      |
|                      | iteration's          |                      |
|                      | key/value            |                      |
+----------------------+----------------------+----------------------+
| $loop                | If job is part of a  | "$loop": {           |
|                      | loop, current        |                      |
|                      | iteration's          | "index": 0,          |
|                      | key/value            |                      |
|                      |                      | "key": "0",          |
|                      |                      |                      |
|                      |                      | "value": "text1"     |
|                      |                      |                      |
|                      |                      | },                   |
+----------------------+----------------------+----------------------+
| $loop.index          | Index of the current |                      |
|                      | loop iteration       |                      |
+----------------------+----------------------+----------------------+
| $loop.key            | Key of the current   |                      |
|                      | loop iteration       |                      |
+----------------------+----------------------+----------------------+
| $loop.value          | Value of the current |                      |
|                      | loop iteration       |                      |
+----------------------+----------------------+----------------------+
| $loops               | If job is part of a  | "$loops": {          |
|                      | loop or nested loop, |                      |
|                      | current and nested   | "loop_aey0k": {      |
|                      | loop iteration       |                      |
|                      | keys/values          | "index": 0,          |
|                      |                      |                      |
|                      |                      | "key": "0",          |
|                      |                      |                      |
|                      |                      | "value": "text1"     |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | }                    |
+----------------------+----------------------+----------------------+
| $loops.<loop_name>   | Specific loop name   |                      |
|                      | in nested loops      |                      |
+----------------------+----------------------+----------------------+
| $loo                 | Index of the         |                      |
| ps.<loop_name>.index | specific loop        |                      |
|                      | iteration            |                      |
+----------------------+----------------------+----------------------+
| $l                   | Key of the specific  |                      |
| oops.<loop_name>.key | loop iteration       |                      |
+----------------------+----------------------+----------------------+
| $loo                 | Value of the         |                      |
| ps.<loop_name>.value | specific loop        |                      |
|                      | iteration            |                      |
+----------------------+----------------------+----------------------+
| $variables           | Current value of any | "$variables": {      |
|                      | variables defined    |                      |
|                      | upstream of this job | "string_at7xg":      |
|                      |                      | "new",               |
|                      |                      |                      |
|                      |                      | "number_ajpro": 1,   |
|                      |                      |                      |
|                      |                      | "boolean_a7qe9":     |
|                      |                      | true,                |
|                      |                      |                      |
|                      |                      | "object_a4k88": {    |
|                      |                      |                      |
|                      |                      | "string_amul7": ""   |
|                      |                      |                      |
|                      |                      | },                   |
|                      |                      |                      |
|                      |                      | "array_afhe7": [     |
|                      |                      |                      |
|                      |                      | {                    |
|                      |                      |                      |
|                      |                      | "array_agz7a": [     |
|                      |                      |                      |
|                      |                      | ""                   |
|                      |                      |                      |
|                      |                      | ]                    |
|                      |                      |                      |
|                      |                      | }                    |
|                      |                      |                      |
|                      |                      | ],                   |
|                      |                      |                      |
|                      |                      | "attachment_ah5dr":  |
|                      |                      | null,                |
|                      |                      |                      |
|                      |                      | "iterable": [1,2,0]  |
|                      |                      |                      |
|                      |                      | }                    |
+----------------------+----------------------+----------------------+
| $variables.<name>    | Value of a specific  |                      |
|                      | variable defined     |                      |
|                      | upstream             |                      |
+----------------------+----------------------+----------------------+

For a list of top-level properties that are defined on the $event.data
object when configuring webhook triggers, see event.data Properties in
the Webhook Triggers section.
