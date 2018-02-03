---
date: 2016-01-01
title: 'Activity Digest: December 2015'
aliases: ['/news/news.20160101.html']
---
<div class="col-md-8 main">
 <div class="row">
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in the Taskwarrior project. Here is what
            happened in December 2015.
  </p>
  <p>
   This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the
   <a href="https://git.tasktools.org/projects/TM/repos/task/commits?until=refs%2Fheads%2F2.5.1">
    full Git history
   </a>
   .
  </p>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2015-12-02
     </small>
    </td>
    <td>
     <ul>
      <li>
       timewarrior: Work began on sketching out a time-tracking solution, to integrate with task - details coming soon
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-12-07
     </small>
    </td>
    <td>
     <ul>
      <li>
       taskwarrior.org: Updated
       <a href="/tools/index.html">
        tools
       </a>
       page with taskwarrior-pomodoro compatibility information
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-12-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       taskwarrior.org: Updated
       <a href="/support/index.html">
        tools
       </a>
       page with IRC logging link
      </li>
      <li>
       task: UDA indicator column did not properly default to 'U' fixed
      </li>
      <li>
       task:
       <code>
        make install
       </code>
       was not installing the
       <code>
        license.txt
       </code>
       file fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-12-18
     </small>
    </td>
    <td>
     <ul>
      <li>
       Holidata: missing
       <code>
        de-AT
       </code>
       data fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-12-20
     </small>
    </td>
    <td>
     <ul>
      <li>
       task: Removed task.fish arguments until TW-1404 is fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-12-21
     </small>
    </td>
    <td>
     <ul>
      <li>
       Holidata:
       <code>
        de-DE
       </code>
       errors fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-12-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1738">
        TW-1738: add defined languages JAPANESE
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-12-23
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-100">
        TD-100: Log taskd messages to stdout if launched by systemd
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-110">
        TD-110: Question: About src/tls/*
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1733">
        TW-1733: taskwarrior 2.5.0 can not compile FreeBSD 10.1
       </a>
       fixed
      </li>
      <li>
       tasksh: Changed key assignments:
       <code>
        &lt;enter&gt;/r
       </code>
       for review,
       <code>
        s
       </code>
       for skip
      </li>
      <li>
       taskd: Refactored list functions for efficiency
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-12-25
     </small>
    </td>
    <td>
     <ul>
      <li>
       taskwarrior.org: Updated
       <a href="/tools/index.html">
        tools
       </a>
       page now that Mirakel no longer supports Taskserver
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-12-26
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1742">
        TW-1742: Indian Holiday Calendar (Master HolidayFile)
       </a>
       fixed
      </li>
      <li>
       Holidata: Added
       <code>
        en-IN
       </code>
       data
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-12-28
     </small>
    </td>
    <td>
     <ul>
      <li>
       taskwarrior.org: Updated
       <a href="/docs/commands/columns.html">
        columns
       </a>
       page which was missing information
      </li>
      <li>
       task: Date attributes now have a
       <code>
        relative
       </code>
       format, so address issues with
       <code>
        remaining
       </code>
       and
       <code>
        countdown
       </code>
       not providing complete coverage
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-12-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       taskwarrior.org: Updated
       <a href="/docs/urgency.html">
        urgency
       </a>
       page which was missing information
      </li>
      <li>
       task: No longer hardcodes libc++ on Darwin for users still using GCC
      </li>
      <li>
       task: Include sys/syslimits.h on OS X
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-12-31
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1749">
        TW-1749: PATH_MAX isn't defined in FS.cpp in some versions of OS X
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1750">
        TW-1750: REG_ENHANCED, used in RX.cpp, isn't defined in all versions of Darwin
       </a>
       fixed
      </li>
      <li>
       Task: Improved tests that always break at EOY
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

