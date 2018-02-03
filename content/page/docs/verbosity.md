---
title: 'Verbosity'
url: "/docs/verbosity.html"
---
<div class="col-md-10 main">
 <div class="row">
  <a name="verbosity">
  </a>
  <p>
   Taskwarrior provides feedback when commands are run, the amount
              of which can be controlled.  There is a configuration variable
              named
   <code>
    verbose
   </code>
   that can be set to different values
              to control verbosity.  By default, the value is:
  </p>
  <pre>verbose=yes</pre>
  <p>
   This value causes Taskwarrior to show all feedback.  Conversely
              it can be set to:
  </p>
  <pre>verbose=no</pre>
  <p>
   This restricts the amount of feedback, but still retains useful
              information.  To remove all feedback, use the setting:
  </p>
  <pre>verbose=nothing</pre>
  <a name="control">
  </a>
  <h4>
   Fine Control
  </h4>
  <p>
   Individual verbosity settings can be specified, in this form:
  </p>
  <pre>verbose=footnote,label</pre>
  <p>
   The value in this case consists of two tokens which cause
              footnotes to be shown after the tasks in a report, and table
              column labels.
  </p>
  <a name="tokens">
  </a>
  <h4>
   Verbosity Tokens
  </h4>
  <p>
   <table class="table table-striped table-condensed">
    <tr>
     <th>
      Token
     </th>
     <th>
      Meaning
     </th>
    </tr>
    <tr>
     <td>
      blank
     </td>
     <td>
      Inserts blank lines in the output to separate the task lists from other feedback.
     </td>
    </tr>
    <tr>
     <td>
      header
     </td>
     <td>
      Shows information before the task list, regarding aliases or the default command.
     </td>
    </tr>
    <tr>
     <td>
      footnote
     </td>
     <td>
      Shows information after the task list, such as configuration overrides.
     </td>
    </tr>
    <tr>
     <td>
      label
     </td>
     <td>
      Shows column labels for tabular output.
     </td>
    </tr>
    <tr>
     <td>
      new-id
     </td>
     <td>
      When adding a task, shows the newly-created ID value.
     </td>
    </tr>
    <tr>
     <td>
      affected
     </td>
     <td>
      Shows how many tasks were affected by a bulk modification.
     </td>
    </tr>
    <tr>
     <td>
      edit
     </td>
     <td>
      Shows a preamble and additional text in the template when using the
      <code>
       edit
      </code>
      command.
     </td>
    </tr>
    <tr>
     <td>
      special
     </td>
     <td>
      Shows feedback when special tags are used.
     </td>
    </tr>
    <tr>
     <td>
      project
     </td>
     <td>
      Shows feedback on project status changes.
     </td>
    </tr>
    <tr>
     <td>
      sync
     </td>
     <td>
      Shows feedback during sync.
     </td>
    </tr>
    <tr>
     <td>
      filter
     </td>
     <td>
      Shows the complete filter used.
      <span class="label label-success">
       2.4.0
      </span>
     </td>
    </tr>
   </table>
  </p>
 </div>
 <br/>
 <br/>
</div>

