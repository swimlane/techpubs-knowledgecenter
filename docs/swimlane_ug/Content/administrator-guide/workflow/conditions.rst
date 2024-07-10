Conditions
==========

Workflow consists of conditions and actions. Each branch of the workflow
can contain multiple conditions and actions. Conditions are branches of
the workflow tree. When you set up conditions, set them up according to
decision points in your business processing.

Conditional Branch: Example
---------------------------

Create conditional branches according to the flow of your business
processes. For example, if you are setting up a process for handling
phishing email scans, you can anticipate that some email accounts will
be compromised, while others will not, and still others might not even
need scanning. In this example, you can set up the branch with these
conditions and actions:

The Phishing Workflow is set to look for the Incident Type = "Phishing
Alert." It processes that condition and then branches to these
additional actions:

-  5 or More Hits
-  Scanned, No Hits
-  Never Scanned

Each branch in the above example can then have multiple actions branched
off, as necessary.

To add an additional condition, select the root node or another
conditional node and click **New Condition** on the Workflow toolbar.

Each workflow has a Default Action condition which, by default, does not
have any conditions. Any action defined within Default Action will run
once each time the workflow runs.

**TIP:** You can define multiple conditions in one step if you use
**Evaluation Type** as a secondary conditional field. Set the field to
*AND* to indicate that all the conditions defined within should be met
in order to execute the branch. Set it to *OR* to specify that a branch
should be executed upon one of the conditions being met.

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
