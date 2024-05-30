Conditions
==========

Workflow consists of conditions and actions. Each branch of the workflow
can contain multiple conditions and actions. Conditions are branches of
the workflow tree.

Conditional Operators
---------------------

You can set up different conditional operators for the field you choose
to conditionalize. The operators differ by field type.

The operators are mostly self-explanatory.

Here is a list of the conditional operators with which you can set up
conditions:

-  Equals
-  Does Not Equal
-  Contains
-  Excludes
-  Less Than
-  Less Than or Equal
-  Greater Than
-  Greater Than or Equal
-  Has Value
-  Does Not Have Value
-  Has Been Modified
-  Matches Regex

**Note:** When you use a Reference field as a conditional operator, it
is dependent upon the field type of the referenced field.

More on the Has Been Modified Conditional Operator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you use a Has Been Modified condition, you're setting a condition
that says, when the content of the selected field changes, then the
assigned action occurs.

**Note:** The field upon which you set the Has Been Modified condition
must change from existing content to new, existing content. The action
isn't triggered when the change on a field goes from an empty field, to
existing content in the field.
