---
title: 'Reports'
url: '/docs/report.html'
---
<div class="col-md-10 main">
 <div class="row">
  <a name="reports">
  </a>
  <p>
   Taskwarrior has three kinds of reports. There are built-in reports
              that cannot be modified, such as
   <code>
    info
   </code>
   and
   <code>
    summary
   </code>
   . There are built-in reports which can be
              redefined completely or eliminated, such as
   <code>
    list
   </code>
   ,
   <code>
    next
   </code>
   . And finally there are your own custom reports.
              To generate a list of *all* the reports, use the
   <code>
    reports
   </code>
   command:
  </p>
  <pre>$ task reports

Report           Description
---------------- --------------------------------------------------
active           Active tasks
all              Pending, waiting and completed tasks by age
blocked          Lists all blocked tasks
blocking         Blocking (and blocked) tasks
burndown.daily   Shows a graphical burndown chart, by day
burndown.monthly Shows a graphical burndown chart, by month
burndown.weekly  Shows a graphical burndown chart, by week
completed        Completed tasks
ghistory.annual  Shows a graphical report of task history, by year
ghistory.monthly Shows a graphical report of task history, by month
history.annual   Shows a report of task history, by year
history.monthly  Shows a report of task history, by month
information      Shows all data and metadata
list             Actionable tasks by due date, project and urgency
long             All details of pending tasks by creation date
ls               Pending tasks sorted by description
minimal          Pending tasks by project and description
newest           The newest pending tasks
next             The top 7 most urgent actionable tasks
oldest           The oldest pending tasks
overdue          These task are late!
projects         Shows all project names used
ready            The most urgent actionable tasks
recurring        Repeating Tasks
summary          Shows a report of task status by project
tags             Shows a list of all tags used
unblocked        Lists all unblocked
waiting          Waiting tasks

28 reports</pre>
  <a name="static">
  </a>
  <h4>
   Built-In Static Reports
  </h4>
  <p>
   Typically a report consists of a table of data, with one row of
              data corresponding to a single task, with the task attributes
              represented as columns.  But there are other reports which do not
              conform to this structure.  Those are the built-in static reports,
              and they are not modifiable, because they are quirky and require
              custom code.  These reports are:
  </p>
  <pre>burndown.daily
burndown.monthly
burndown.weekly
calendar
colors
export
ghistory.annual
ghistory.monthly
history.annual
history.monthly
information
summary
timesheet</pre>
  <p>
   Each of these reports takes non-standard arguments, may or may not
              support filters, and generates distinctive output.
  </p>
  <a name="modifiable">
  </a>
  <h4>
   Built-In Modifiable Reports
  </h4>
  <p>
   These reports are standard format, using standard arguments, and
              are also modifiable.
  </p>
  <pre>active
all
blocked
blocking
completed
list
long
ls
minimal
newest
next
oldest
overdue
ready
recurring
unblocked
waiting</pre>
  <p>
   Suppose you wanted to remove a column from one of these reports,
              for example removing
   <code>
    tags
   </code>
   from the
   <code>
    minimal
   </code>
   report.  First look at the existing columns
              and labels of the
   <code>
    minimal
   </code>
   report:
  </p>
  <pre>$ task show report.minimal.labels

Config Variable       Value
--------------------- ---------------------------
report.minimal.labels ID,Project,Tags,Description

$ task show report.minimal.columns

Config Variable        Value
---------------------- ---------------------------------------
report.minimal.columns id,project,tags.count,description.count</pre>
  <p>
   Having determined what the current values are, simply override
              with the new values:
  </p>
  <pre>$ task config report.minimal.labels  'ID,Project,Description'
...
$ task config report.minimal.columns 'id,project,description.count'</pre>
  <p>
   You can think of the built-in modifiable reports as a set of
              default custom reports.
  </p>
  <a name="custom">
  </a>
  <h4>
   Custom Reports
  </h4>
  <p>
   Defining a custom report is straightforward. You have control over
              the data shown, the sort order and the column labels. A custom
              report is simply a set of configuration values, and those values
              include:
  </p>
  <ul>
   <li>
    description
   </li>
   <li>
    columns
   </li>
   <li>
    labels
   </li>
   <li>
    sort
   </li>
   <li>
    filter
   </li>
  </ul>
  <p>
   Let us quickly create a custom report, which will be named
   <code>
    simple
   </code>
   . This report will display the task ID, project
              name and description. We will need to gather the five settings
              listed above.
  </p>
  <p>
   The description is the easiest, and in this case the report will
              be described:
  </p>
  <pre>Simple list of open tasks by project</pre>
  <p>
   This is just a descriptive label that will be used when the report
              is listed.  Next we need to specify the columns in the report, and
              the order in which those are shown. Here the
   <code>
    _columns
   </code>
   helper command will show the columns available:
  </p>
  <pre>$ task _columns
depends
description
due
end
entry
foo
id
imask
mask
modified
parent
priority
project
recur
scheduled
start
status
tags
until
urgency
uuid
wait</pre>
  <p>
   That represents all the data that Taskwarrior stores, and
              therefore all the data that may be shown in a report. Our
   <code>
    simple
   </code>
   report will show id, project and description,
              which are all in the list.  This means our column list is simply:
  </p>
  <pre>id,project,description</pre>
  <p>
   But there are also formats for each column, and the
   <code>
    columns
   </code>
   command shows them, with examples. Here are
              the formats for our three columns:
  </p>
  <pre>$ task columns id

Columns Supported Formats Example
------- ----------------- ------------------------------------
id      number*           123
uuid    long*             f30cb9c3-3fc0-483f-bfb2-3bf134f00694
        short             f30cb9c3</pre>
  <p>
   This is easy, because there is only one
   <code>
    id
   </code>
   format.
  </p>
  <pre>$ task columns project

Columns Supported Formats Example
------- ----------------- -------------
project full*             home.garden
        parent            home
        indented            home.garden</pre>
  <p>
   There are three formats for the
   <code>
    project
   </code>
   column, and
              the default,
   <code>
    full
   </code>
   is the one we want.
  </p>
  <pre>$ task columns description

Columns     Supported Formats Example
----------- ----------------- -----------------------------------------------------------------------------
description combined*         Move your clothes down on to the lower peg
                                2014-02-08 Immediately before your lunch
                                2014-02-08 If you are playing in the match this afternoon
                                2014-02-08 Before you write your letter home
                                2014-02-08 If you're not getting your hair cut
            desc              Move your clothes down on to the lower peg
            oneline           Move your clothes down on to the lower peg 2014-02-08 Immediately before ...
                              this afternoon 2014-02-08 Before you write your letter home 2014-02-08 If ...
            truncated         Move your clothes do...
            count             Move your clothes down on to the lower peg [4]</pre>
  <p>
   There are five formats for description.  This time we prefer the
   <code>
    count
   </code>
   format, so our columns list is now:
  </p>
  <pre>id,project,description.count</pre>
  <p>
   Labels are the column heading labels in the report.  There are
              defaults, but we wish to specify these like this:
  </p>
  <pre>ID,Proj,Desc</pre>
  <p>
   Sorting is also straightforward, and we want the tasks sorted by
              project, and then by entry, which is the creation date for a
              task.  This illustrates that a task attribute that is not visible
              can be used in the sort.  The sort order is then:
  </p>
  <pre>project+/,entry+</pre>
  <p>
   The
   <code>
    +
   </code>
   means an ascending order, but we could have
              used
   <code>
    -
   </code>
   for descending. The
   <code>
    /
   </code>
   solidus
              indicates that
   <code>
    project
   </code>
   is a break column, which
              means a blank line is inserted between unique values, for a
              visual grouping effect.
   <span class="label label-success">
    2.4.0
   </span>
  </p>
  <p>
   Finally we need a filter,
              otherwise our report will just display all tasks, which is rarely
              wanted.  Here we wish to see only pending tasks, and that means
              the filter is:
  </p>
  <pre>status:pending</pre>
  <p>
   Now we have our report definition, so we just create the five
              configuration entries like this:
  </p>
  <pre>$ task config report.simple.description 'Simple list of open tasks by project'
$ task config report.simple.columns     'id,project,description.count'
$ task config report.simple.labels      'ID,Proj,Desc'
$ task config report.simple.sort        'project+/,entry+'
$ task config report.simple.filter      'status:pending'</pre>
  <p>
   And it is finished.  Run the report like this:
  </p>
  <pre>$ task simple

ID Proj Desc
-- ---- -----------------
 1 Home Wash the windows
 3 Home Vacuum the floors

 2      Food shopping</pre>
  <p>
   Custom reports also show up in the help output.
  </p>
  <pre>$ task help | grep simple
task <filter> sime                  Simple list of open tasks by project</filter></pre>
  <p>
   I can inspect the configuration.
  </p>
  <pre>$ task show report.simple

Config Variable           Value
------------------------- ------------------------------------
report.simple.columns     id,project,description.count
report.simple.description Simple list of open tasks by project
report.simple.filter      status:pending
report.simple.labels      ID,Proj,Desc
report.simple.sort        project+/,entry+</pre>
  <p>
   Now the report is fully configured, it joins the others and is
              used in the same way.
  </p>
 </div>
 <br/>
 <br/>
</div>
