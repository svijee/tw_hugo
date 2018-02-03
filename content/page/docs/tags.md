---
title: 'Tags & Virtual Tags'
url: '/docs/tags.html'
---
<div class="col-md-10 main">
 <div class="row">
  <a name="tags">
  </a>
  <p>
   The basic tag syntax is very powerful and simple to use.  There
              are two ways to use this, shown here:
  </p>
  <pre>$ task +HOME list
$ task -WORK list</pre>
  <p>
   These two commands illustrate the complete tag interface. The
              first command is a filter that lists only tasks that have the
   <code>
    HOME
   </code>
   tag. The second command is a filter that lists
              only tasks that
   <em>
    do not
   </em>
   have the
   <code>
    WORK
   </code>
   tag. The + and - syntax
              therefore means presence and absence of a tag. This is simple to
              use, and can be combined like this:
  </p>
  <pre>$ task +HOME -WORK list</pre>
  <p>
   This shows tasks that have the
   <code>
    HOME
   </code>
   tag, but do not
              have the
   <code>
    WORK
   </code>
   tag. This is a very simple and easy to
              use mechanism, but it does require that your tasks are properly
              tagged. In other words, it is based directly on task metadata.
  </p>
  <p>
   A tag may be any single word that does not start with a digit,
              punctuation, or mathematical operator.
  </p>
  <a name="complex">
  </a>
  <h4>
   Complex Filters
  </h4>
  <p>
   Some Taskwarrior filters are simple in concept, but the syntax is
              not that straightforward.  For example, to determine whether a
              task has a due date that falls on the current day, you need to
              use this filter:
  </p>
  <pre>$ task due.after:yesterday and due.before:tomorrow list</pre>
  <p>
   This filters tasks with a due date during the narrow time window
              of 'today'. Note that is is not sufficient to just specify the
              date, because due dates all have associated times (defaulting to
              0:00:00), and if you want to match the date, you need to consider
              the time. So for example, this command
   <em>
    does not
   </em>
   list
              tasks due today:
  </p>
  <pre>$ task due:today list</pre>
  <p>
   Instead, this filter matches tasks with a due date of today, and
              a time of 0:00.  In order to see all tasks due today, you need to
              provide proper range bracketing.
  </p>
  <a name="simplification">
  </a>
  <h4>
   Simplification
  </h4>
  <p>
   Here is where virtual tags can help, by providing a simple tag
              interface to more complex state conditions of the task. There is
              a virtual tag, named
   <code>
    TODAY
   </code>
   that can be used in
              filters, and it means that instead of this filter:
  </p>
  <pre>$ task due.after:yesterday and due.before:tomorrow list</pre>
  <p>
   We can now use this:
  </p>
  <pre>$ task +TODAY list</pre>
  <p>
   Which is a much simpler way of filtering tasks due today. Because
              this is a tag interface, we can also invert it:
  </p>
  <pre>$ task -TODAY list</pre>
  <p>
   This shows only tasks that are not due today.
  </p>
  <p>
   Virtual tags are built in to Taskwarrior. They are evaluated at
              run time, which means they do not require direct metadata, and
              therefore do not occupy space in the data files, but are
              determined according to the state of the task in the same way
              that the complex filter example above is determined.
  </p>
  <p>
   Thus virtual tags combine the simplicity of the tag interface
              with more complex defined conditions, for convenience.
  </p>
  <a name="supported">
  </a>
  <h4>
   Supported Virtual Tags
  </h4>
  <p>
   Since version 2.2.0, Taskwarrior has supported virtual tags, and
              the list will continue to grow. Here is the full list of supported
              virtual tags:
  </p>
  <p>
   <table class="table table-striped table-condensed">
    <tr>
     <td>
      <code>
       BLOCKED
      </code>
     </td>
     <td>
      Is the task dependent on another incomplete task?
     </td>
    </tr>
    <tr>
     <td>
      <code>
       UNBLOCKED
      </code>
     </td>
     <td>
      The opposite of BLOCKED, for convenience. Note +BLOCKED == -UNBLOCKED and vice versa.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       BLOCKING
      </code>
     </td>
     <td>
      Does another task depend on this incomplete task?
     </td>
    </tr>
    <tr>
     <td>
      <code>
       DUE
      </code>
     </td>
     <td>
      Is this task due within 7 days? Determined by rc.due
     </td>
    </tr>
    <tr>
     <td>
      <code>
       DUETODAY
      </code>
     </td>
     <td>
      Is this task due sometime today?
     </td>
    </tr>
    <tr>
     <td>
      <code>
       TODAY
      </code>
     </td>
     <td>
      Is this task due sometime today?
     </td>
    </tr>
    <tr>
     <td>
      <code>
       OVERDUE
      </code>
     </td>
     <td>
      Is this task past it’s due date?
     </td>
    </tr>
    <tr>
     <td>
      <code>
       WEEK
      </code>
     </td>
     <td>
      Is this task due this week?
      <span class="label label-success">
       2.3.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       MONTH
      </code>
     </td>
     <td>
      Is this task due this month?
      <span class="label label-success">
       2.3.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       QUARTER
      </code>
     </td>
     <td>
      Is this task due this quarter?
      <span class="label label-success">
       2.6.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       YEAR
      </code>
     </td>
     <td>
      Is this task due this year?
      <span class="label label-success">
       2.3.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       ACTIVE
      </code>
     </td>
     <td>
      Is the task active, ie does it have a start date?
     </td>
    </tr>
    <tr>
     <td>
      <code>
       SCHEDULED
      </code>
     </td>
     <td>
      Is the task scheduled, ie does it have a scheduled date?
     </td>
    </tr>
    <tr>
     <td>
      <code>
       PARENT
      </code>
     </td>
     <td>
      Is the task a hidden parent recurring task?
      <span class="label label-success">
       2.3.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       CHILD
      </code>
     </td>
     <td>
      Is the task a recurring child task?
     </td>
    </tr>
    <tr>
     <td>
      <code>
       UNTIL
      </code>
     </td>
     <td>
      Does the task expire, ie does it have an until date?
     </td>
    </tr>
    <tr>
     <td>
      <code>
       WAITING
      </code>
     </td>
     <td>
      Is the task hidden, ie does it have a wait date?
     </td>
    </tr>
    <tr>
     <td>
      <code>
       ANNOTATED
      </code>
     </td>
     <td>
      Does the task have any annotations?
     </td>
    </tr>
    <tr>
     <td>
      <code>
       READY
      </code>
     </td>
     <td>
      Is the task pending, not blocked, and either not scheduled,
                    or scheduled before now.
      <span class="label label-success">
       2.4.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       YESTERDAY
      </code>
     </td>
     <td>
      Was the task due yesterday?
      <span class="label label-success">
       2.4.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       TOMORROW
      </code>
     </td>
     <td>
      Is the task due tomorrow?
      <span class="label label-success">
       2.4.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       TAGGED
      </code>
     </td>
     <td>
      Does the task have any tags?
     </td>
    </tr>
    <tr>
     <td>
      <code>
       PENDING
      </code>
     </td>
     <td>
      Is the task in the pending state?
      <span class="label label-success">
       2.4.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       COMPLETED
      </code>
     </td>
     <td>
      Is the task in the completed state?
      <span class="label label-success">
       2.4.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       DELETED
      </code>
     </td>
     <td>
      Is the task in the deleted state?
      <span class="label label-success">
       2.4.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       UDA
      </code>
     </td>
     <td>
      Does the task contain any UDA values?
      <span class="label label-success">
       2.5.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       ORPHAN
      </code>
     </td>
     <td>
      Does the task contain any orphaned UDA values?
      <span class="label label-success">
       2.5.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       PRIORITY
      </code>
     </td>
     <td>
      Does the task have a priority?
      <span class="label label-success">
       2.5.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       PROJECT
      </code>
     </td>
     <td>
      Does the task have a project?
      <span class="label label-success">
       2.5.0
      </span>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       LATEST
      </code>
     </td>
     <td>
      Is the task the most recently added task?
      <span class="label label-success">
       2.5.0
      </span>
     </td>
    </tr>
   </table>
  </p>
 </div>
 <br/>
 <br/>
</div>

