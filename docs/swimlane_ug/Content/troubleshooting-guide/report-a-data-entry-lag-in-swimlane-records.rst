Report a Data Entry Lag in Swimlane Records
===========================================

Occasionally a Swimlane user will contact the Swimlane support team to
report data entry lags in Swimlane record fields (typically single-line
text, multi-line text, and comments fields).

Most of the time characters appear in the field’s display area as fast
as you can strike the corresponding keys on the keyboard. However, with
a lag you can see that there are obvious delays between the time at
which the keystrokes are made and the time at which the attendant
characters appear in the display area. These delays may be intermittent
or ongoing.

This symptom has multiple root causes including:

-  Too many fields, sections, tab controls in each record

   -  The easiest remedy for this root cause is to hide as many
      fields/sections as possible. The more page elements are visible,
      the greater the memory required as each page element has its own
      JavaScript listener. If possible, expose only the fields/sections
      that are needed at each phase of your work in the record.

-  Memory leaks in Swimlane’s UI code

   -  Previously identified memory leaks have been fixed, but new ones
      may arise.

-  Other, yet-to-be identified causes

In order to identify the root cause, possibly find a temporary
workaround, and bring about a permanent solution, Swimlane support needs
to understand clearly how and when the symptom arises, and how its
severity may vary.

To provide support with this insight, make a screen capture video
recording to document the steps that you take before and during the lag
symptom.

To report a data entry lag in Swimlane records:

#. Open record X1 from application X.

#. Change a value in Selection field S1 so that Section Z appears. (Z
   happens to house a tab control with 4 tabs.)

#. Select each tab in Z in turn, and then return to the first tab.

#. Begin typing in the multi-line Text field M1 in the first tab of Z at
   the highest possible speed, even if this creates nonsense text.

Alternatively, and perhaps even better, press down one character key,
such as the letter 'a', and hold it for 5+ seconds. If a string of 'a's
appear at a steady rate for the entire 5 seconds, then there is no lag.
If there are lapses when no new instances of 'a' appear on the current
line, then this is the lag.
