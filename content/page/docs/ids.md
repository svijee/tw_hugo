---
title: "ID Numbers"
url: '/docs/ids.html'
---
<div class="col-md-10 main">
 <div class="row">
  <a name="cipher">
  </a>
  <p>
   Taskwarrior assigns ID numbers to tasks. The ID number is
              actually a simple line count of the entries in the
   <code>
    pending.data
   </code>
   file. When a task is completed or
              deleted, it is moved to the
   <code>
    completed.data
   </code>
   file, and
              loses the ID. All tasks, pending or otherwise, have a UUID, and
              are always addressable by UUID.
  </p>
  <p>
   By keeping the tasks in two separate files, average performance
              is improved. This works because most of the commands and reports
              are based on only the pending tasks, which are in the
   <code>
    pending.data
   </code>
   file. This file tends to stabilize at a
              constant size, regardless of the amount of work you are getting
              done [1]. The
   <code>
    completed.data
   </code>
   file, on the other hand,
              grows unbounded. This means that some reports, such as the
   <code>
    completed
   </code>
   or
   <code>
    all
   </code>
   report will run slower
              over time because there is more data to read and display.
  </p>
  <p>
   One nice side effect of this mechanism is that the ID numbers of
              pending tasks remain small, and less prone to error during data
              entry.
  </p>
  <p>
   One downside is that ID numbers change occasionally, although in
              a predictable way.
  </p>
  <a name="gc">
  </a>
  <h4>
   Garbage Collection
  </h4>
  <p>
   When a task is marked as deleted, it gets a new status, and an
   <code>
    end
   </code>
   attribute, among other things. The task is
              written back into the
   <code>
    pending.data
   </code>
   file, but it
              doesn't belong there - it belongs in the
   <code>
    completed.data
   </code>
   file. There is an operation called
              Garbage Collection (gc) that is automatically run by taskwarrior
              to move tasks into the correct files. When moving tasks between
              the files, ID numbers are affected, because they are simply line
              numbers in the
   <code>
    pending.data
   </code>
   file.
  </p>
  <p>
   But gc is only run occasionally: it is run immediately before any
              command that displays ID numbers, such as a report, but not when
              a task is modified in any way. The reason is concerned with
              general usage. Here is a typical taskwarrior usage scenario for a
              few commands:
  </p>
  <pre>$ task list
...
$ task 34 done
$ task 45 modify priority:H
$ task 56 delete
$ task list
...</pre>
  <p>
   The first command shows a report that contains ID numbers.
              The next three commands use the ID numbers shown in the report.
              The last command shows ID numbers again. Clearly, while the
              middle three commands are being run, it would be a mistake to
              renumber any tasks. When the last command is run, new ID numbers
              are shown, and any subsequent commands would use those. This is
              why only commands that display ID numbers perform a gc first.
  </p>
  <a name="config">
  </a>
  <h4>
   Configuration
  </h4>
  <p>
   The
   <code>
    gc
   </code>
   configuration setting may be set to 'off' to
              disable the gc operation. This has the effect of letting data
              accumulate in the
   <code>
    pending.data
   </code>
   file, and effectively
              making the ID numbers static. This slows down almost every
              command. Disabling gc should be used on a per-command basis, if
              at all, in this way:
  </p>
  <pre>$ task rc.gc=off list
...</pre>
  <p>
   The setting can be made permanent, but this is not recommended.
  </p>
  <p>
   <small>
    [1] Based on more than 7 years of monitored usage.
   </small>
  </p>
 </div>
 <br/>
 <br/>
</div>

