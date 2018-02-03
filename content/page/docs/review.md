---
title: 'Tasksh Review'
url: '/docs/review.html'
---
<div class="col-md-10 main">
 <div class="row">
  <p>
   Beginning with release
   <span class="label label-success">
    1.1.0
   </span>
   the Taskwarrior shell (
   <code>
    tasksh
   </code>
   ) has a
   <code>
    review
   </code>
   command that lets you review your tasks.
  </p>
  <p>
   Reviewing your task list is important because you need to make sure
              you work on the more urgent tasks first, and also make sure your list
              is up to date. Only with accurate metadata (due dates, priorities ...)
              will your task list reflect real world needs.

              Periodic review will help you maintain the right due dates, priorities,
              dependencies, tags, project assignments and so on, while removing
              tasks that are no longer needed.
  </p>
  <p>
   Here is a quick demo of the review feature:
  </p>
  <p>
   <script async="" id="asciicast-84844" src="https://asciinema.org/a/84844.js" type="text/javascript">
   </script>
  </p>
  <a name="how">
  </a>
  <h4>
   How it Works
  </h4>
  <p>
   Ideally you would review your task list reguarly, once a week.
              If you find yourself making no changes to the tasks, perhaps you
              should review less often. The goal is for the review process to
              be effective at cleaning up the list, but not a burden, or a waste
              of time.
  </p>
  <p>
   Tasksh implements the review by creating a Taskwarrior report just for
              this purpose. It is named
   <code>
    _reviewed
   </code>
   and simply lists
              the UUID values of tasks that need to be reviewed. This report then
              drives an interactive session where you go through that list of
              tasks one at a time, and have the chance to modify, skip or mark
              the task as reviewed.
  </p>
  <p>
   When you mark a task as reviewed, Tasksh adds a
   <code>
    reviewed
   </code>
   timestamp to the task, as a
   <a href="/docs/udas.html">
    UDA
   </a>
   defined for this purpose. This attribute is used in the
   <code>
    _reviewed
   </code>
   report filter to make sure you don't
              review the same task more often than weekly.
  </p>
  <p>
   The combination of the
   <code>
    reviewed
   </code>
   timestamp, and the
   <code>
    _reviewed
   </code>
   report means that if you were to review all
              your tasks today, then immediately performing another review would
              yields no tasks to review. After a week has passed, you will be
              able to review all the tasks again.
  </p>
  <p>
   This ability to 'resume' a review session means that you can
              stop a review session at any time, and resume later. You can even
              specify how many tasks you would like to review, which means you
              can review a small set of tasks more frequently, making the review
              process shorter.
  </p>
  <p>
   When you first review, Tasksh will automatically configure
              Taskwarrior to create the
   <code>
    _reviewed
   </code>
   report, and the
   <code>
    reviewed
   </code>
   UDA. Once the report is created, you can
              modify it. Here is the report definition:
  </p>
  <pre>$ task show report._reviewed

Config Variable              Value
---------------------------- -------------------------------------------------------
report._reviewed.columns     uuid
report._reviewed.description Tasksh review report.  Adjust the filter to your needs.
report._reviewed.filter      ( reviewed.none: or reviewed.before:now-1week ) and
                             ( +PENDING or +WAITING )
report._reviewed.sort        reviewed+,modified+</pre>
  <p>
   The filter term
   <code>
    reviewed.before:now-1week
   </code>
   can be
              changed to suit your needs.
  </p>
  <a name="tasksh">
  </a>
  <h4>
   Launch Tasksh
  </h4>
  <p>
   Launch tasksh, and you will immediately see a summary of available
              commands, followed by a prompt:
  </p>
  <pre>$ tasksh

tasksh 1.1.0

    tasksh&gt; review [N]       Task review session, with optional cutoff after N tasks
    tasksh&gt; list             Or any other Taskwarrior command
    tasksh&gt; diagnostics      Tasksh diagnostics
    tasksh&gt; help             Tasksh help
    tasksh&gt; exec ls -al      Any shell command.  May also use '!ls -al'
    tasksh&gt; quit             End of session. May also use 'exit'

tasksh&gt; </pre>
  <p>
   You see here that
   <code>
    review
   </code>
   is one of the commands. You
              can simply start a review session, which can be quit at any time:
  </p>
  <pre>tasksh&gt; review
...</pre>
  <p>
   Or you can review a fixed quantity of tasks:
  </p>
  <pre>tasksh&gt; review 12
...</pre>
  <p>
   Reviewing a fixed quantity can help you iteratively review all
              your tasks at convenient times, without having to go through the
              entire list at once.
  </p>
 </div>
 <br/>
 <br/>
</div>

