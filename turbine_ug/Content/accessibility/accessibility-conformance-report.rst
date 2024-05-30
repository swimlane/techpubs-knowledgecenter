Accessibility Conformance Report
================================

**Based on VPAT® Revision 2.4**

-  **Name of Product/Version:** Swimlane Turbine Cloud 23.5.1
-  **Report Date:** January 2024
-  **Product Description:** Swimlane Turbine is a low-code security
   automation platform. With Turbine you can prioritize alerts,
   re-mediate threats and improve your operational performance.
-  **Contact Information:** info@swimlane.com

**Note:** Turbine is a web-only application.

**Evaluation Methods Used:**

Swimlane is committed to providing an exceptional user experience to all
people. As part of that commitment, we aim to ensure the convenience of
our product is accessible to each person who wishes to use it by
designing and building our product to be consistent with the
accessibility guidelines and principles per the Section 508 Amendment to
the Rehabilitation Act of 1973 as well as WCAG Level 2.0/2.1 Level A
standards.

As part of this commitment, we utilize both manual and automated
assessment techniques to determine any areas for improvement. By
implementing these assessments into our development pipeline, we aim to
ensure that any issues that may cause accessibility issues within the
Swimlane platform are appropriately prioritized and addressed as we
continue to develop new experiences.

Manual assessment techniques using native `Google Chrome® browser
development tools <https://developer.chrome.com/docs/devtools/>`__ and
automated scans from `Accessibility
Insights <https://accessibilityinsights.io/>`__ are employed to test
Swimlane.

--------------

This report covers the degree of conformance for the following
accessibility standard or guidelines:

+----------------------------------+----------------------------------+
| Standard or Guideline            | Included in Report               |
+==================================+==================================+
| `Web Content Accessibility       | Level A (Yes) Level AA (No)      |
| Guidelines                       | Level AAA (No)                   |
| 2.0 <http://www.w3.org           |                                  |
| /TR/2008/REC-WCAG20-20081211>`__ |                                  |
+----------------------------------+----------------------------------+
| `Revised Section 508 standards   | Yes                              |
| published January 18, 2017 and   |                                  |
| corrected January 22,            |                                  |
| 2018 <https://www.access-bo      |                                  |
| ard.gov/guidelines-and-standards |                                  |
| /communications-and-it/about-the |                                  |
| -ict-refresh/final-rule/text-of- |                                  |
| the-standards-and-guidelines>`__ |                                  |
+----------------------------------+----------------------------------+

Terms
-----

The terms used in the Conformance Level information are defined as
follows:

-  **Supports:** The functionality of the product has at least one
   method that meets the criterion without known defects or meets with
   equivalent facilitation.
-  **Partially Supports:** Some functionality of the product does not
   meet the criterion.
-  **Does Not Support:** The majority of product functionality does not
   meet the criterion.
-  **Not Applicable:** The criterion is not relevant to the product.
-  **Not Evaluated:** The product has not been evaluated against the
   criterion. This can be used only in WCAG 2.0 Level AAA.

Success Criteria, Level A
-------------------------

+-----------------------+--------------------+-----------------------+
| Criteria              | Conformance Level  | Remarks and           |
|                       |                    | Explanations          |
+=======================+====================+=======================+
| `1.1.1 <http:         | Partially Supports | Some images that      |
| //www.w3.org/TR/WCAG2 |                    | contain text are      |
| 0/#text-equiv-all>`__ |                    | missing ``alt`` tags. |
| / Non-text Content    |                    | For non-text content  |
|                       |                    | of pure decoration,   |
|                       |                    | some images do not    |
|                       |                    | use ``role`` of       |
|                       |                    | ``none`` or           |
|                       |                    | ``presentation.``     |
+-----------------------+--------------------+-----------------------+
| `                     | Not Applicable     | The product does not  |
| 1.2.1 <http://www.w3. |                    | use prerecorded       |
| org/TR/WCAG20/#media- |                    | media.                |
| equiv-av-only-alt>`__ |                    |                       |
| / Audio-only and      |                    |                       |
| Video-only            |                    |                       |
| (Prerecorded)         |                    |                       |
+-----------------------+--------------------+-----------------------+
| `1.2.2 <http://www.   | Not Applicable     | The product does not  |
| w3.org/TR/WCAG20/#med |                    | use prerecorded       |
| ia-equiv-captions>`__ |                    | media.                |
| / Captions            |                    |                       |
| (Prerecorded)         |                    |                       |
+-----------------------+--------------------+-----------------------+
| `1.2.3 <http://www.w3 | Not Applicable     | The product does not  |
| .org/TR/WCAG20/#media |                    | use prerecorded       |
| -equiv-audio-desc>`__ |                    | media.                |
| / Audio Description   |                    |                       |
| or Media Alternative  |                    |                       |
| (Prerecorded)         |                    |                       |
+-----------------------+--------------------+-----------------------+
| `1.3.1 <http://www.   | Partially Supports | Content within the    |
| w3.org/TR/WCAG20/#con |                    | platform is missing   |
| tent-structure-separa |                    | consistent, semantic  |
| tion-programmatic>`__ |                    | heading structure.    |
| / Info and            |                    | Form controls         |
| Relationships         |                    | (inputs, selects) are |
|                       |                    | using neither         |
|                       |                    | ``aria`` attributes   |
|                       |                    | nor ``labels``.The    |
|                       |                    | platform does not use |
|                       |                    | ``aria-`` landmarks.  |
|                       |                    | Font icons within the |
|                       |                    | platform are not      |
|                       |                    | represented with      |
|                       |                    | ``role="img"``        |
+-----------------------+--------------------+-----------------------+
| `1.3.2 <http://       | Partially Supports | Dialogs and other     |
| www.w3.org/TR/WCAG20/ |                    | content overlays      |
| #content-structure-se |                    | within the platform   |
| paration-sequence>`__ |                    | do not appropriately  |
| / Meaningful Sequence |                    | trap focus. Pages     |
|                       |                    | within the platform   |
|                       |                    | do not adhere to a    |
|                       |                    | semantic structure.   |
+-----------------------+--------------------+-----------------------+
| `1.3.3 <http://www.w  | Partially Supports | Tips and user         |
| 3.org/TR/WCAG20/#cont |                    | notifications do not  |
| ent-structure-separat |                    | use adequately        |
| ion-understanding>`__ |                    | labeled context.      |
| / Sensory             |                    |                       |
| Characteristics       |                    |                       |
+-----------------------+--------------------+-----------------------+
| `1.4.1 <http:         | Partially Supports | Widget “charts”       |
| //www.w3.org/TR/WCAG2 |                    | exclusively use color |
| 0/#visual-audio-contr |                    | to represent chart    |
| ast-without-color>`__ |                    | data. In some cases,  |
| / Use of Color        |                    | form control errors   |
|                       |                    | are represented by    |
|                       |                    | color, and not        |
|                       |                    | accompanied by error  |
|                       |                    | text.                 |
+-----------------------+--------------------+-----------------------+
| `1.4.2 <h             | Not Applicable     | The product does not  |
| ttp://www.w3.org/TR/W |                    | use prerecorded       |
| CAG20/#visual-audio-c |                    | audio.                |
| ontrast-dis-audio>`__ |                    |                       |
| / Audio Control       |                    |                       |
+-----------------------+--------------------+-----------------------+
| `2.1.1 <http:/        | Partially Supports | Some elements are not |
| /www.w3.org/TR/WCAG20 |                    | accessible with the   |
| /#keyboard-operation- |                    | keyboard. Drag and    |
| keyboard-operable>`__ |                    | drop functionality is |
| / Keyboard            |                    | not available to      |
|                       |                    | non-mouse users.      |
+-----------------------+--------------------+-----------------------+
| `2.1.                 | Does Not Support   | Keyboard trap exists  |
| 2 <http://www.w3.org/ |                    | in time picker.       |
| TR/WCAG20/#keyboard-o |                    |                       |
| peration-trapping>`__ |                    |                       |
| / No Keyboard Trap    |                    |                       |
+-----------------------+--------------------+-----------------------+
| `2                    | Supports           | Meta, alt or opt keys |
| .1.4 <https://www.w3. |                    | are used in           |
| org/TR/WCAG21/#charac |                    | conjunction with any  |
| ter-key-shortcuts>`__ |                    | single keystroke.     |
| / Character Key       |                    |                       |
| Shortcuts             |                    |                       |
+-----------------------+--------------------+-----------------------+
| `2.2.1 <              | Partially Supports | Administrative users  |
| http://www.w3.org/TR/ |                    | can configure the     |
| WCAG20/#time-limits-r |                    | platform to extend    |
| equired-behaviors>`__ |                    | sessions beyond the   |
| / Timing Adjustable   |                    | 20 Hour Exception. No |
|                       |                    | user can extend or    |
|                       |                    | cancel a session      |
|                       |                    | timeout.              |
+-----------------------+--------------------+-----------------------+
| `2.2.2 <http://w      | Supports           | Dashboard cards       |
| ww.w3.org/TR/WCAG20/# |                    | display a countdown   |
| time-limits-pause>`__ |                    | timer that may be     |
| / Pause, Stop, Hide   |                    | paused.               |
+-----------------------+--------------------+-----------------------+
| `2                    | Supports           | The platform does not |
| .3.1 <http://www.w3.o |                    | contain any component |
| rg/TR/WCAG20/#seizure |                    | that flashes more     |
| -does-not-violate>`__ |                    | than three times in   |
| / Three Flashes or    |                    | any one second        |
| Below Threshold       |                    | period.               |
+-----------------------+--------------------+-----------------------+
| `2.4                  | Does Not Support   | The platform does not |
| .1 <http://www.w3.org |                    | offer bypass blocks.  |
| /TR/WCAG20/#navigatio |                    |                       |
| n-mechanisms-skip>`__ |                    |                       |
| / Bypass Blocks       |                    |                       |
+-----------------------+--------------------+-----------------------+
| `2.4.                 | Supports           | Titles are present    |
| 2 <http://www.w3.org/ |                    | but not descriptive   |
| TR/WCAG20/#navigation |                    | for all pages.        |
| -mechanisms-title>`__ |                    |                       |
| / Page Titled         |                    |                       |
+-----------------------+--------------------+-----------------------+
| `2.4.3 <htt           | Does Not Support   | Tab ordering does no  |
| p://www.w3.org/TR/WCA |                    | always preserve       |
| G20/#navigation-mecha |                    | meaning and sequence. |
| nisms-focus-order>`__ |                    |                       |
| / Focus Order         |                    |                       |
+-----------------------+--------------------+-----------------------+
| `2.4                  | Partially Supports | The Swimlane logo     |
| .4 <http://www.w3.org |                    | within the platform   |
| /TR/WCAG20/#navigatio |                    | is missing            |
| n-mechanisms-refs>`__ |                    | discernible text or   |
| / Link Purpose (In    |                    | ``aria`` label. Links |
| Context)              |                    | or buttons only       |
|                       |                    | containing an icon    |
|                       |                    | are missing           |
|                       |                    | discernible text or   |
|                       |                    | ``aria`` label.       |
+-----------------------+--------------------+-----------------------+
| `2.5.1 <https://      | Supports           | No complex gestures   |
| www.w3.org/TR/WCAG21/ |                    | are required to use   |
| #pointer-gestures>`__ |                    | the product.          |
| / Pointer Gestures    |                    |                       |
+-----------------------+--------------------+-----------------------+
| `2.5.2 <https://www.  | Partially Supports | Up reversal applies   |
| w3.org/TR/WCAG21/#poi |                    | to long press         |
| nter-cancellation>`__ |                    | elements.             |
| / Pointer             |                    |                       |
| Cancellation          |                    |                       |
+-----------------------+--------------------+-----------------------+
| `2.5.3 <https         | Supports           | For user interface    |
| ://www.w3.org/TR/WCAG |                    | components with       |
| 21/#label-in-name>`__ |                    | labels that include   |
| / Label in Name       |                    | text or images of     |
|                       |                    | text, the name        |
|                       |                    | contains the text     |
|                       |                    | that is presented     |
|                       |                    | visually.             |
+-----------------------+--------------------+-----------------------+
| `2.5.4 <https://      | Supports           | Usage is not tied to  |
| www.w3.org/TR/WCAG21/ |                    | free-moving           |
| #motion-actuation>`__ |                    | motion-enabled        |
| / Motion Actuation    |                    | devices.              |
+-----------------------+--------------------+-----------------------+
| `3.1.1 <http://www    | Supports           | The language of pages |
| .w3.org/TR/WCAG20/#me |                    | within Swimlane       |
| aning-doc-lang-id>`__ |                    | contain a ``lang``    |
| / Language of Page    |                    | attribute with the    |
|                       |                    | property of ``en``.   |
+-----------------------+--------------------+-----------------------+
| `3.2.1 <htt           | Supports           | A change of context   |
| p://www.w3.org/TR/WCA |                    | is not initiated when |
| G20/#consistent-behav |                    | user interface        |
| ior-receive-focus>`__ |                    | components within the |
| / On Focus            |                    | platform receive      |
|                       |                    | focus.                |
+-----------------------+--------------------+-----------------------+
| `3.2.2 <http://www    | Supports           | Changing the setting  |
| .w3.org/TR/WCAG20/#co |                    | of user interface     |
| nsistent-behavior-unp |                    | components do not     |
| redictable-change>`__ |                    | automatically cause a |
| / On Input            |                    | change of context.    |
|                       |                    | Forms and input       |
|                       |                    | fields within the     |
|                       |                    | platform offer submit |
|                       |                    | or save buttons where |
|                       |                    | applicable.           |
+-----------------------+--------------------+-----------------------+
| `3.                   | Partially Supports | Some notifications    |
| 3.1 <http://www.w3.or |                    | are not contextually  |
| g/TR/WCAG20/#minimize |                    | connected to the      |
| -error-identified>`__ |                    | invalid component.    |
| / Error               |                    | The platform does not |
| Identification        |                    | utilize ARIA19.       |
+-----------------------+--------------------+-----------------------+
| `3.3.2 <http://www    | Partially Supports | Most form input       |
| .w3.org/TR/WCAG20/#mi |                    | fields within the     |
| nimize-error-cues>`__ |                    | platform utilize      |
| / Labels or           |                    | grouping or labeling  |
| Instructions          |                    | to provide users with |
|                       |                    | context and           |
|                       |                    | instruction; however, |
|                       |                    | input format is not   |
|                       |                    | explicitly stated.    |
+-----------------------+--------------------+-----------------------+
| `4.1.1 <http://www.   | Partially Supports | Start and end tags    |
| w3.org/TR/WCAG20/#ens |                    | are utilized properly |
| ure-compat-parses>`__ |                    | within the platform.  |
| / Parsing             |                    | Duplicate IDs are     |
|                       |                    | used in the           |
|                       |                    | application builder   |
|                       |                    | and workflow editor.  |
+-----------------------+--------------------+-----------------------+
| `4.1.2 <http://w      | Does Not Support   | Roles are missing     |
| ww.w3.org/TR/WCAG20/# |                    | from dialogs, tables, |
| ensure-compat-rsv>`__ |                    | alerts, tabs, and     |
| / Name, Role, Value   |                    | other elements within |
|                       |                    | the platform. Some    |
|                       |                    | dialogs have only an  |
|                       |                    | X icon for the close  |
|                       |                    | action, without any   |
|                       |                    | additional text or    |
|                       |                    | ``aria-label`` usage. |
|                       |                    | Checkbox groups,      |
|                       |                    | radio groups, and     |
|                       |                    | other lists and       |
|                       |                    | complex UI elements   |
|                       |                    | are missing           |
|                       |                    | ``aria-labelledby``   |
|                       |                    | usage to associate    |
|                       |                    | purpose and           |
|                       |                    | relationship.         |
|                       |                    | Tooltips and their    |
|                       |                    | relationships to      |
|                       |                    | their parent element  |
|                       |                    | are not contextually  |
|                       |                    | described by          |
|                       |                    | ``aria-label``.Form   |
|                       |                    | elements do not have  |
|                       |                    | appropriate label     |
|                       |                    | usage or ARIA         |
|                       |                    | attributes for        |
|                       |                    | indicating            |
|                       |                    | relationships between |
|                       |                    | label and input, or   |
|                       |                    | invalid state. Focus  |
|                       |                    | state is not able to  |
|                       |                    | be programmatically   |
|                       |                    | determined for all    |
|                       |                    | elements.             |
+-----------------------+--------------------+-----------------------+
