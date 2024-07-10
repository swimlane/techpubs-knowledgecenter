Numeric
=======

Use a numeric field when you need to store numeric data in a record.

To create numeric fields:

From Application Builder's Field Types, select **Numeric.** Choose from
Numeric or List, and then drag and drop the field to the Form Layout.
Drop the field in the layout area, or within a Tab or Section layout
object.

Access the field's Field Properties and complete the following fields as
needed:

+----------------+-------------------------+-------------------------+
| Field          | Step                    | Example                 |
+================+=========================+=========================+
| **Name**       | Enter the name of the   | Phone Number            |
|                | field.                  |                         |
+----------------+-------------------------+-------------------------+
| **Help Text**  | Enter contextual help   | *Enter the phone number |
|                | text. You will first    | of the affected party   |
|                | need to specify whether | or parties.*            |
|                | the help text will      |                         |
|                | appear above or below   |                         |
|                | the field in the record |                         |
|                | form, and then you can  |                         |
|                | enter the text.         |                         |
+----------------+-------------------------+-------------------------+
| **Required**   | Click to indicate       | *checkmark*             |
|                | whether entering data   |                         |
|                | in the field is         |                         |
|                | required to process the |                         |
|                | record.                 |                         |
+----------------+-------------------------+-------------------------+
| **Read-only**  | Click to indicate that  | *checkmark*             |
|                | the field is read-only  |                         |
|                | for the record. The     |                         |
|                | field will not be       |                         |
|                | editable.               |                         |
+----------------+-------------------------+-------------------------+
| **Unique**     | Click to indicate that  | *checkmark*             |
|                | the field's value must  |                         |
|                | be unique for this      |                         |
|                | record. This field is   |                         |
|                | not available for list  |                         |
|                | fields.                 |                         |
+----------------+-------------------------+-------------------------+
| **Calculated** | Click to indicate that  | *                       |
|                | the field contains a    | TOTALMINUTES([Date/Time |
|                | mathematical            | Opened], [Date/Time     |
|                | calculation. Calculated | Closed])*               |
|                | fields are read-only    |                         |
|                | and the value is the    |                         |
|                | result of a calculation |                         |
|                | defined with a custom   |                         |
|                | formula. Once you       |                         |
|                | select this checkmark,  |                         |
|                | the Calculation         |                         |
|                | Expression Help opens,  |                         |
|                | and you can define your |                         |
|                | formula or function.    |                         |
|                | See `Calculation        |                         |
|                | Builder <../calc        |                         |
|                | ulation-builder.htm>`__ |                         |
|                | for more information.   |                         |
|                | This field is not       |                         |
|                | available for list      |                         |
|                | fields.                 |                         |
+----------------+-------------------------+-------------------------+

Next, consider the following advanced options in the Field Properties
tab:

+---------------+-----------------------------------------------------+
| Field         | Step                                                |
+===============+=====================================================+
| **Prefix**    | Enter text that will be prepended to the field's    |
|               | input.                                              |
+---------------+-----------------------------------------------------+
| **Suffix**    | Enter text that will be appended to the field's     |
|               | input.                                              |
+---------------+-----------------------------------------------------+
| **Min**       | Indicate the minimum-allowed value for the field.   |
+---------------+-----------------------------------------------------+
| **Max**       | Indicate the maximum-allowed value for the field.   |
+---------------+-----------------------------------------------------+
| **Min Items** | Indicate the minimum number of items to allow in a  |
|               | list field.                                         |
+---------------+-----------------------------------------------------+
| **Max Items** | Indicate the maximum number of items to allow in    |
|               | list field.                                         |
+---------------+-----------------------------------------------------+
