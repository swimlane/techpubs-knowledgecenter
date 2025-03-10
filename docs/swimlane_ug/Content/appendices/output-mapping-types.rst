.. _appendix-output-mapping-types:

Mapping Types
=============

This appendix outlines the allowable output fields by field data type.

**Note:** If an application’s field doesn’t currently conform to the
allowable output mapping rules, you will need to create and map to a new
application field that does conform.

**Also Note:** If a plugin's output type changes in a new version or
update of the plugin, you will need to remap outputs.

Output Mapping Types
--------------------

+------------------+----------------------------+-------------------------------+
| Data type        | enum # (in Plugin Details) | Allowable Output Fields       |
+==================+============================+===============================+
| **text**         | 1                          | single-line text              |
+------------------+----------------------------+-------------------------------+
|                  |                            | rich text                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | attachment                    |
+------------------+----------------------------+-------------------------------+
|                  |                            | comments                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | date                          |
+------------------+----------------------------+-------------------------------+
|                  |                            | dateTime                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | numeric                       |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | numeric list                  |
+------------------+----------------------------+-------------------------------+
|                  |                            | email                         |
+------------------+----------------------------+-------------------------------+
|                  |                            | ip                            |
+------------------+----------------------------+-------------------------------+
|                  |                            | json                          |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-line text            |
+------------------+----------------------------+-------------------------------+
|                  |                            | telephone                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | url                           |
+------------------+----------------------------+-------------------------------+
|                  |                            | time                          |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-select/radio buttons   |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-select/radio buttons |
+------------------+----------------------------+-------------------------------+
|                  |                            | timespan                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | user/groups                   |
+------------------+----------------------------+-------------------------------+
| **text area**    | 2                          | multiple-line text            |
+------------------+----------------------------+-------------------------------+
|                  |                            | rich text                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-line text              |
+------------------+----------------------------+-------------------------------+
|                  |                            | comments                      |
+------------------+----------------------------+-------------------------------+
| **code**         | 3                          | multiple-line text            |
+------------------+----------------------------+-------------------------------+
|                  |                            | rich text                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-line text              |
+------------------+----------------------------+-------------------------------+
|                  |                            | comments                      |
+------------------+----------------------------+-------------------------------+
| **password**     | 4                          | single-line text              |
+------------------+----------------------------+-------------------------------+
|                  |                            | comments                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-line text            |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-select/radio buttons   |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-select/check boxes   |
+------------------+----------------------------+-------------------------------+
| **list**         | 5                          | text list                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | numeric list                  |
+------------------+----------------------------+-------------------------------+
|                  |                            | attachment                    |
+------------------+----------------------------+-------------------------------+
| **number**       | 6                          | numeric                       |
+------------------+----------------------------+-------------------------------+
|                  |                            | numeric list                  |
+------------------+----------------------------+-------------------------------+
|                  |                            | singletext                    |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-line text            |
+------------------+----------------------------+-------------------------------+
|                  |                            | rich text                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | datetime (epoch)              |
+------------------+----------------------------+-------------------------------+
|                  |                            | timespan                      |
+------------------+----------------------------+-------------------------------+
| **boolean**      | 7                          | single-select/radio buttons   |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-line text              |
+------------------+----------------------------+-------------------------------+
| **iso8601**      | 8                          | datetime                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | date                          |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
| **JSON**         | 9                          | JSON                          |
+------------------+----------------------------+-------------------------------+
|                  |                            | comments                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-line text            |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-line text              |
+------------------+----------------------------+-------------------------------+
| **epoch**        | 10                         | datetime                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
| **epochMs**      | 11                         | datetime                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
| **date**         | 12                         | date                          |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
| **email**        | 13                         | email                         |
+------------------+----------------------------+-------------------------------+
|                  |                            | comments                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-line text              |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-line text            |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | user/groups                   |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-select/radio buttons   |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-select/check boxes   |
+------------------+----------------------------+-------------------------------+
| **url**          | 14                         | url                           |
+------------------+----------------------------+-------------------------------+
|                  |                            | comments                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-text                   |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-line text            |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-select/radio buttons   |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-select/check boxes   |
+------------------+----------------------------+-------------------------------+
| **telephone**    | 15                         | telephone                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | comments                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-line text              |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-line text            |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-select/radio buttons   |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-select/check boxes   |
+------------------+----------------------------+-------------------------------+
| **ip**           | 16                         | ip                            |
+------------------+----------------------------+-------------------------------+
|                  |                            | comments                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-line text              |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-line text            |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
|                  |                            | single-select/radio buttons   |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-select/check boxes   |
+------------------+----------------------------+-------------------------------+
| **time**         | 17                         | time                          |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
| **attachment**   | 18                         | attachment                    |
+------------------+----------------------------+-------------------------------+
| **numeric list** | 19                         | numeric list                  |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
| **category**     | 20                         | single-select/radio buttons   |
+------------------+----------------------------+-------------------------------+
|                  |                            | comments                      |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-select/check boxes   |
+------------------+----------------------------+-------------------------------+
|                  |                            | single line text              |
+------------------+----------------------------+-------------------------------+
|                  |                            | multiple-line text            |
+------------------+----------------------------+-------------------------------+
|                  |                            | text list                     |
+------------------+----------------------------+-------------------------------+
