---
date: 2014-07-04
title: 'Taskwarrior 2.4.0 Preview'
aliases: ['/news/news.20140704.html']
---
<div class="col-md-8 main">
 <div class="row">
  <p>
   The Taskwarrior 2.4.0 development branch has been unusable for a
            a few weeks
            (
   <a href="/news/news.20140524.html">
    mentioned here
   </a>
   )
            while new functionality was integrated. It has been a
            long process, with about 750 code changes so far, but now all the
            tests are passing again.
  </p>
  <p>
   Does this mean it's ready for alpha and beta? No, not yet, because
            now there is a need for a lot of new tests to cover all the new
            functionality. This is the next phase of cycle, improving tests,
            fixing open bugs, and updating documentation.
  </p>
  <p>
   Now it's time for a preview of some of the new features...
  </p>
  <h4>
   Virtual Tags
  </h4>
  <p>
   Lots of new virtual tags are added, including:
   <code>
    YESTERDAY
   </code>
   ,
   <code>
    TOMORROW
   </code>
   ,
   <code>
    READY
   </code>
   ,
   <code>
    PENDING
   </code>
   ,
   <code>
    COMPLETED
   </code>
   ,
   <code>
    DELETED
   </code>
   and
   <code>
    TAGGED
   </code>
   .
            Virtual tags run faster than algebraic equivalents, so report
            filters have been updated.

            See the man page (
   <code>
    man task
   </code>
   ) for the complete set.
  </p>
  <h4>
   Default
   <code>
    info
   </code>
   Command
  </h4>
  <p>
   With the updated command line parser, an old favorite feature
            returns - when you specify an ID but not command, the info command
            is assumed:
   <pre>$ task 243

Name          Value
------------­ ------------------------------------------
ID            243
Description   Something is wrong with TDB2::dump
Status        Pending
Project       tw.240
Entered       2014-05-25 13:06:47 (5 weeks)
Last modified 2014-05-25 13:06:52 (5 weeks)
Tags          bug
UUID          9c2bfdd4-87d5-4396-97e2-ee1a980b9237
Urgency       4.907
                           project     1  *    1 =     1
                              tags   0.8  *    1 =   0.8
                               age 0.107  *    1 = 0.107
                           TAG bug     1  *    3 =     3

Date                Modification
------------------- --------------------------------------
2014-05-25 13:06:52 Modified set to '2014-05-25 13:06:52'.
                    Tags set to 'bug'.</pre>
   This coexists with the
   <code>
    rc.default.command
   </code>
   feature.
            Additionally the
   <code>
    info
   </code>
   command now shows how the urgency
            values are calculated.
  </p>
  <h4>
   Hooks
  </h4>
  <p>
   The new hook system will allow a new class of extensions and add-ons.
            Just copy a script into your
   <code>
    ~/.task/hooks
   </code>
   directory,
            give it the right name, and it will be run.
   <a href="/docs/design/hooks.html">
    Design details here
   </a>
   .
  </p>
  <h4>
   ISO-8601 Dates
  </h4>
  <p>
   The
   <code>
    rc.dateformat
   </code>
   method of specifying dates is still
            supported, and used for rendering dates in reports, but regardless
            of your settings, you can also specify dates and times in the
            various ISO-8601 formats.  Here are some:
   <pre>$ task add Buy lamp due:2014-W45
$ task add Buy rug due:2014-W40-3
$ task add Buy chair due:2014-154
$ task add Buy table due:10:30</pre>
   There is now a more comprehensive set of
   <a href="/docs/design/dates.html">
    named dates
   </a>
   .
  </p>
  <h4>
   ISO-8601 Durations
  </h4>
  <p>
   Dates and durations can be calculated:
   <pre>$ task calc eom + 3 weeks - 100 hours + 27 minutes -10 seconds
2014-08-17T20:26:49</pre>
   For example, how much time is left until the end of the month?
   <pre>$ task calc eocm - now
P27DT23H33M20S</pre>
   How long is a million seconds?
   <pre>$ task calc 1000000 seconds
P11DT13H46M40S</pre>
  </p>
  <h4>
   Calc Command and Expressions
  </h4>
  <p>
   Oh yes, there is a calc command also:
   <pre>$ task calc '(3 * 2) + 1'
7</pre>
   There is also a standalone
   <code>
    calc
   </code>
   utility, which can do
            more:
   <pre>$ calc --postfix '3 2 * 1 +'
7</pre>
   <a href="/docs/commands/calc.html">
    Take a look here
   </a>
   at a more detailed look at the
   <code>
    calc
   </code>
   capabilities.
            The
   <code>
    calc
   </code>
   command in Taskwarrior also has DOM access.
  </p>
  <h4>
   Extended DOM
  </h4>
  <p>
   The DOM has been extended so that
   <em>
    all
   </em>
   Taskwarrior data
            can now be externally referenced:
   <pre>$ task calc 123.due
$ task calc 123.due.year
$ task calc 123.due.week
$ task calc 123.annotations.0.description</pre>
   Additionally attributes for a task can now be referenced on
            the command line while a task is being created:
   <pre>$ task add Plan the party due:eoy wait:due-1month</pre>
  </p>
  <h4>
   And more...
  </h4>
  <p>
   New and updated themes.
            New and updated report definitions.
            New
   <code>
    tasksh
   </code>
   .
            Improved
   <code>
    sync
   </code>
   diagnostics.
            Better certificate validation.
            Portuguese and French localizations.
            UUID abbreviations.
            The
   <code>
    show
   </code>
   command includes default values.
            New command reference PDF.
            60% more unit tests, and a new test framework.
            Lots of bug fixes.
  </p>
  <p>
   Taskwarrior 2.4.0 is a major release, and although it still needs a
           lengthy shakedown period, to fix all the bugs we can, it is going to
           provide a lot of new capabilities.
  </p>
 </div>
</div>

