Widget Code Structure
=====================

The widget is implemented as an anonymous class which extends the
``HTMLElement`` class. The preferred method to create a widget is to
extend the ``SwimlaneElement`` which extends the ``LitElement`` class
which itself extends ``HTMLElement`` class.

Here is an example of the default widget with annotation added:

/\*\* \* Import \`SwimlaneElement\` class. \* The \`css\` and \`html\`
methods are also imported from \`swimlane-element\`. \*/ import {
SwimlaneElement, css, html } from '@swimlane/swimlane-element@1'; /\*\*
\* The \`recordFrameTemplate\` is a template helper function see
templates below. \*/ import { recordFrameTemplate } from
'@swimlane/swimlane-element@1/templates.js'; /\*\* \* A Swimlane widget
is implemented as an anonymous class which extends the
\`SwimlaneElement\` class. \*/ export default class extends
SwimlaneElement { /\*\* \* The \`styles()\` getter is a static class
getter, in other words, it is a property defined on the class
constructor. \* This style getter method does not have access to any
properties stored in the objects (i.e. \`record\` and \`report\` data).
\* This getter defines styles common to all instances of this widget. \*
Defining this in your widget is optional. \*/ static get styles() {
return [super.styles, css\` .frame::after { content: "Record Output"; }
\`]; } /\*\* \* The \`render\` method is an instance method and,
therefore, has access to properties stored in the object (i.e.
\`record\` and \`report\` data), see properties below. \* The render
method is scheduled by \`LitElement\` Lifecycle events and must return a
\`lit-html\` template. \* Defining this method in your widget is
required. \*/ render() { return recordFrameTemplate(html\`
<pre>${JSON.stringify(this.record, undefined, 2)}</pre> \`); } }

Properties
----------

``SwimlaneElement`` defines the following properties:

-  ``this.record`` - Available to record widgets, an object containing
   key-value pairs for each field on the record.
-  ``this.report`` - Available to report widgets, an object containing
   ``data``, ``rawData``, and ``query``.
-  ``this.contextData`` - Available to both record and report widgets,
   an object containing data such as ``application``, ``currentUser``,
   ``origin``, and ``token``.

**Note:** Documentation on how ``LitElement`` handles properties and
attributes can be found
`here <https://lit-element.polymer-project.org/guide/properties>`__.

Lifecycle
---------

In addition to the ``HtmlElement`` and ``LitElement`` lifecycle methods,
``SwimlaneElement`` adds the ``resizedCallback`` method.

-  ``resizedCallback`` - This method (called whenever the element is
   resized) but default simply calls
   ```requestUpdate`` <https://lit-element.polymer-project.org/guide/lifecycle#requestupdate>`__.

**Note:** Documentation of ``LitElement`` lifecycle methods and
properties can be found
`here <https://lit-element.polymer-project.org/guide/lifecycle>`__.

Events
------

``SwimlaneElement`` adds the following methods for emitting Swimlane
widget events:

-  ``this.updateRecordValue(key, value)`` : Available to record widgets.
   Updates record data by field key.
-  ``this.addComment(key, value)`` : Available to record widgets. Adds a
   new comment by field key.
-  ``this.triggerIntegration(taskId)`` : Available to record widgets.
   Triggers an integration.
-  ``this.triggerSave()`` : Available to record widgets. Triggers record
   save on the record page.

**Note:** Documentation on how to handle events in ``LitElement`` can be
found `here <https://lit-element.polymer-project.org/guide/events>`__.

For single value fields (text/numeric/date fields, etc) or single-select
fields types simply emit the new value:

// value can be a string or number type.
this.updateRecordValue('field-key', 'new value');

For text and numeric list field types, emit an array of new values. If
duplicate values exist, their ``id``\ s get reused.

// value is an array of strings for text list, and numbers for numeric
list. this.updateRecordValue('field-key', ['First item', 'Third item']);

For multi-select field types (selects, radio buttons, checkboxes), emit
an array of new values. Every element in the value must exist in the
``contextData``.

// value is an array of strings this.updateRecordValue('field-key',
['First item', 'Third item']); // Every element in value must exist in
the \`contextData\`. // e.g. this.updateRecordValue('field-key',
["Fourth item"]) // ERROR

To add a comment emit the new comment as a string.

this.addComment('comments-key', 'Hello World!');
