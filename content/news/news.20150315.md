---
date: 2015-03-15
title: Taskwarrior 2.4.2 Released
aliases: ['/news/news.20150315.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Taskwarrior 2.4.2 Released
   <small>
    2015-03-15
   </small>
  </h3>
  <p>
   Taskwarrior 2.4.2 is released. This is primarily a bug fix release
            to address a bad hook problem that prevented on-modify hooks from
            modifying tasks.
  </p>
  <p>
   Additionally the new
   <code>
    context
   </code>
   command is included, as
            are updated themes with higher contrast.
            Although this is a minor release, there are significant bug fixes
            and new features make this a recommended upgrade.  Changes include:
  </p>
  <p>
   <ul>
    <li>
     New
     <code>
      context
     </code>
     command.  See the
     <a href="/docs/context.html">
      online documentation
     </a>
     for full details.
    </li>
    <li>
     Theme fixes, eliminating the very low contrast problems reported
    </li>
    <li>
     Minor built-in report changes
    </li>
    <li>
     Assorted color fixes
    </li>
    <li>
     Recur column now properly suppressed when there is no data
    </li>
    <li>
     UDA values now accessible via DOM reference
    </li>
    <li>
     Fixed some code that was not UTF8-aware
    </li>
    <li>
     Removed pthreads linkage
    </li>
    <li>
     Fixed hooks problem
    </li>
    <li>
     <code>
      info
     </code>
     command now shows virtual tags
    </li>
    <li>
     Several bug fixes
    </li>
   </ul>
   For full details, see the ChangeLog file included in the release.
  </p>
  <p>
   The release is immediately available as a source
   <a href="/download/task-latest.tar.gz">
    tarball
   </a>
   .
            Binary packages will soon be available via your Operating System's
            package manager.
  </p>
 </div>
</div>

