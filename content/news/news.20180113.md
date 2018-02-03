---
date: 2018-01-13
title: Timewarrior 1.1.0 Released
aliases: ['/news/news.20180113.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Timewarrior 1.1.0 Released
   <small>
    2018-01-13
   </small>
  </h3>
  <p>
   Timewarrior 1.1.0 is released. With 18 months of updates, many
            bugs fixed, and new convenience features added, Timewarrior 1.1.0 is
            stable and ready.
  </p>
  <p>
   Timewarrior tracks your time from the command line and generates
            reports. Your data is stored locally in clear text. It integrates well
            with Taskwarrior.
  </p>
  <p>
   <img class="img-responsive" src="/news/images/ti.png"/>
  </p>
  <p>
   Here are the changes in 1.1.0:
  </p>
  <p>
   <ul>
    <li>
     Taskwarrior integration hook now uses a project
     <code>
      Home.Garden
     </code>
     as a single tag
     <code>
      Home.Garden
     </code>
     as well as individual
     <code>
      Home
     </code>
     ,
     <code>
      Garden
     </code>
     tags
    </li>
    <li>
     Taskwarrior integration hook now stops the clock in more situations, such as deleting or waiting a task
    </li>
    <li>
     The
     <code>
      tags
     </code>
     command now supports filters
    </li>
    <li>
     New date names supported (see
     <code>
      timew help date
     </code>
     or
     <code>
      man timew
     </code>
     )
    </li>
    <li>
     Timewarrior and Taskwarrior now use the same date handling
    </li>
    <li>
     The
     <code>
      continue
     </code>
     command can resume tracking by
     <code>
      @id
     </code>
    </li>
    <li>
     When specifying a time without a date (e.g. '10:00am'), the day is assumed to be today, and is no longer projected back in time
    </li>
    <li>
     Fixed Python 3 support of the holiday/refresh script
    </li>
    <li>
     Added missing man page link
    </li>
    <li>
     Taskwarrior projects are now used as-is as tags, and also split on the '.' to present project hierarchy as separate tags
    </li>
    <li>
     Named dates
     <code>
      socw
     </code>
     ,
     <code>
      socm
     </code>
     ,
     <code>
      socq
     </code>
     and
     <code>
      socy
     </code>
     are now named
     <code>
      sow
     </code>
     ,
     <code>
      som
     </code>
     ,
     <code>
      soq
     </code>
     and
     <code>
      soy
     </code>
     . Similarly the
     <code>
      eocw
     </code>
     etc are modified. The
     <code>
      c
     </code>
     is now implicit.
    </li>
    <li>
     <a href="https://bug.tasktools.org/browse/TD-120">
      TD-120
     </a>
     Missing cmakedefine for HAVE_GET_CURRENT_DIR_NAME
    </li>
    <li>
     <a href="https://bug.tasktools.org/browse/TW-1845">
      TW-1845
     </a>
     Cygwin build fails, missing get_current_dir_name
    </li>
    <li>
     <a href="https://bug.tasktools.org/browse/TW-1936">
      TW-1936
     </a>
     Tweak tests to have fuller TAP compliance
    </li>
    <li>
     <a href="https://bug.tasktools.org/browse/TI-27">
      TI-27
     </a>
     Continue tracking by ID
    </li>
    <li>
     <a href="https://bug.tasktools.org/browse/TI-29">
      TI-29
     </a>
     timew config can't add new value
    </li>
    <li>
     <a href="https://bug.tasktools.org/browse/TI-32">
      TI-32
     </a>
     taskwarrior hook script doesn't stop recording waiting task
    </li>
    <li>
     <a href="https://bug.tasktools.org/browse/TI-39">
      TI-39
     </a>
     Bogus command line option causes segfault
    </li>
    <li>
     <a href="https://bug.tasktools.org/browse/TI-40">
      TI-40
     </a>
     totals.py extension script fails with an error
    </li>
    <li>
     <a href="https://bug.tasktools.org/browse/TI-42">
      TI-42
     </a>
     refresh holiday script throws an error on nb-NO locale
    </li>
    <li>
     <a href="https://bug.tasktools.org/browse/TI-44">
      TI-43
     </a>
     :lastweek on sunday
    </li>
    <li>
     <a href="https://bug.tasktools.org/browse/TI-46">
      TI-46
     </a>
     Display error in visual reports (day,week,month)
    </li>
    <li>
     <a href="https://bug.tasktools.org/browse/TI-47">
      TI-47
     </a>
     first call successfully creates new database but returns exit status 1
    </li>
   </ul>
  </p>
 </div>
</div>
