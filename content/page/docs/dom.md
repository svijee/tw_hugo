---
title: "DOM - Document Object Model"
url: '/docs/dom.html'
---
<div class="col-md-10 main">
 <div class="row">
  <a name="dom">
  </a>
  <p>
   Taskwarrior has a Document Object Model, or DOM, which defines a
              way to reference all the data managed by taskwarrior. You may be
              familiar with the DOM implemented by web browsers that let you
              access details on a page programmatically. For example:
  </p>
  <pre>document.getElementById("myAnchor").href</pre>
  <p>
   Taskwarrior allows the same kind of data access in a similar form,
              for example:
  </p>
  <pre>1.description</pre>
  <p>
   This references the description text of task 1. There is a
   <a href="/docs/commands/_get.html">
    <code>
     _get
    </code>
    helper command
   </a>
   that queries data using a DOM reference. Let's see it in action,
              by first creating a detailed task.
  </p>
  <pre>$ task add Buy milk due:tomorrow +store project:Home pri:H
$ task 1 info

Name          Value
------------- ------------------------------------------
ID            1
Description   Buy milk
Status        Pending
Project       Home
Priority      H
Entered       2014-09-28 21:53:59 (4 seconds)
Due           2014-09-29 00:00:00
Last modified 2014-09-28 21:53:59 (4 seconds)
Tags          store
UUID          c0ab2bf6-b4f5-45c2-8420-18ab4f1ba7e7
Urgency       16.56
                           project     1  *    1 =     1
                          priority     1  *    6 =     6
                              tags   0.8  *    1 =   0.8
                               due  0.73  *   12 =  8.76</pre>
  <p>
   All the attributes of that task are available via DOM references.
              Here are some examples:
  </p>
  <pre>$ task _get 1.description
Buy milk

$ task _get 1.uuid
c0ab2bf6-b4f5-45c2-8420-18ab4f1ba7e7

$ task _get c0ab2bf6-b4f5-45c2-8420-18ab4f1ba7e7.id
1

$ task _get 1.due.year
2014

$ task _get 1.due.julian
272

</pre>
  <a name="supported">
  </a>
  <h4>
   Supported References
  </h4>
  <p>
  </p>
  <p>
   <table class="table table-striped table-condensed">
    <!--
                <tr>
                  <td><code>context.program</code></td>
                  <td>
                    The name of the program, usually <code>task</code>.
                    Not useful from the <code>_get</code> command.
                  </td>
                </tr>
                <tr>
                  <td><code>context.args</code></td>
                  <td>
                    The full command line.
                    Not useful from the <code>_get</code> command.
                  </td>
                </tr>
                <tr>
                  <td><code>context.width</code></td>
                  <td>
                    The detected width, in character cells, of the terminal window.
                    If not run from a tty, returns a default value.
                  </td>
                </tr>
                <tr>
                  <td><code>context.height</code></td>
                  <td>
                    The detected height, in lines, of the terminal window.
                    If not run from a tty, returns a default value.
                  </td>
                </tr>
-->
    <tr>
     <td>
      <code>
       system.version
      </code>
     </td>
     <td>
      The version of taskwarrior, for example:
      <pre>$ task _get system.version
2.4.0</pre>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       system.os
      </code>
     </td>
     <td>
      The operating system, for example:
      <pre>$ task _get system.os
FreeBSD</pre>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       rc.&lt;name&gt;
      </code>
     </td>
     <td>
      Any configuration value default, with any overrides from the
      <code>
       .taskrc
      </code>
      applied, then with any command line overrides
                    applied last. For example:
      <pre>$ task _get rc.data.location
~/.task</pre>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       &lt;attribute&gt;
      </code>
     </td>
     <td>
      Any task attribute. Note that no task ID or UUID is specified,
                    so this variant is only useful on the command line like this:
      <pre>$ task add Pay rent due:eom wait:'due - 3days'</pre>
      Note that 'due' is a DOM reference from earlier on the command line.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       &lt;id&gt;.&lt;attribute&gt;
      </code>
     </td>
     <td>
      Any attribute of the specified task ID. For example:
      <pre>$ task add Fix the leak depends:3 scheduled:3.due</pre>
      This makes the new task dependent on task 3, and scheduled on
                    the due date of task 3.  Note that '3.due' is a DOM reference
                    of a specific task.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       &lt;uuid&gt;.&lt;attribute&gt;
      </code>
     </td>
     <td>
      Any attribute of the specified task UUID, as above.
     </td>
    </tr>
   </table>
  </p>
  <p>
   Any attribute that is of type
   <code>
    date
   </code>
   can be directly
              accessed as a date, or it can be accessed by the elements of that
              date. For example:
  </p>
  <p>
   <table class="table table-striped table-condensed">
    <tr>
     <td>
      <code>
       &lt;date&gt;.year
      </code>
     </td>
     <td>
      <span class="label label-success">
       2.4.0
      </span>
      The year, for example:
      <pre>$ task _get 1.due.year
2014</pre>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       &lt;date&gt;.month
      </code>
     </td>
     <td>
      <span class="label label-success">
       2.4.0
      </span>
      The month, for example:
      <pre>$ task _get 1.due.month
9</pre>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       &lt;date&gt;.day
      </code>
     </td>
     <td>
      <span class="label label-success">
       2.4.0
      </span>
      The day of the month, for example:
      <pre>$ task _get 1.due.day
29</pre>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       &lt;date&gt;.week
      </code>
     </td>
     <td>
      <span class="label label-success">
       2.4.0
      </span>
      The week number of the date, for example:
      <pre>$ task _get 1.due.week
40</pre>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       &lt;date&gt;.weekday
      </code>
     </td>
     <td>
      <span class="label label-success">
       2.4.0
      </span>
      The numbered weekday of the date, where 0 is Sunday
                    and 6 is Saturday. For example:
      <pre>$ task _get 1.due.weekday
1</pre>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       &lt;date&gt;.julian
      </code>
     </td>
     <td>
      <span class="label label-success">
       2.4.0
      </span>
      The Julian day of the date, which is the day number of the
                    date in the year. For example, January 1st is 1,
                    February 10th is 41. For example:
      <pre>$ task _get 1.due.julian
272</pre>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       &lt;date&gt;.hour
      </code>
     </td>
     <td>
      <span class="label label-success">
       2.4.0
      </span>
      The hour of the day, for example:
      <pre>$ task _get 1.due.hour
0</pre>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       &lt;date&gt;.minute
      </code>
     </td>
     <td>
      <span class="label label-success">
       2.4.0
      </span>
      The minute of the hour, for example:
      <pre>$ task _get 1.due.minute
0</pre>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       &lt;date&gt;.second
      </code>
     </td>
     <td>
      <span class="label label-success">
       2.4.0
      </span>
      The seconds of the minute, for example:
      <pre>$ task _get 1.due.second
0</pre>
     </td>
    </tr>
   </table>
  </p>
  <p>
   Tags can be accessed as a single item as an
   <code>
    &lt;attribute&gt;
   </code>
   ,
              of the individual tags can be accessed:
  </p>
  <p>
   <table class="table table-striped table-condensed">
    <tr>
     <td>
      <code>
       tags.&lt;literal&gt;
      </code>
     </td>
     <td>
      <span class="label label-success">
       2.4.0
      </span>
      Direct access, per-tag, for example:
      <pre>$ task _get 1.tag.home
home</pre>
      If the tag is present, it is shown, otherwise the
                    result is blank, and Taskwarrior exits with a non-zero
                    status.
      <pre>$ task _get 1.tag.DUE
DUE
$ task _get 1.tag.OVERDUE

</pre>
      Workѕ for virtual tags too, in the same manner.
     </td>
    </tr>
   </table>
  </p>
  <p>
   Annotations are compound data structures, with two elements, which
              are
   <code>
    description
   </code>
   and
   <code>
    entry
   </code>
   . Annotations
              are accessed by an ordinal.
  </p>
  <p>
   <table class="table table-striped table-condensed">
    <tr>
     <td>
      <code>
       annotations.&lt;N&gt;.description
      </code>
     </td>
     <td>
      <span class="label label-success">
       2.4.0
      </span>
      The description of the Nth annotation, for example:
      <pre>$ task _get 1.annotations.0.description</pre>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       annotations.&lt;N&gt;.entry
      </code>
     </td>
     <td>
      <span class="label label-success">
       2.4.0
      </span>
      The creation timestamp of the Nth annotation, for example:
      <pre>$ task _get 1.annotations.0.entry</pre>
      Note that because
      <code>
       entry
      </code>
      is of type
      <code>
       date
      </code>
      ,
                    the individual elements can be addressed, as above, for example:
      <pre>$ task _get 1.annotations.0.entry.year
2014</pre>
     </td>
    </tr>
   </table>
  </p>
  <p>
   UDA values can be accessed in the same manner.
  </p>
 </div>
 <br/>
 <br/>
</div>

