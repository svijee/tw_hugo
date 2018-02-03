---
date: 2016-02-01
title: Activity Digest: January 2016
aliases: ['/news/news.20160201.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: January 2016
   <small>
    2016-02-01
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in the Taskwarrior project. Here is what
            happened in January 2016.
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
      2016-01-04
     </small>
    </td>
    <td>
     <ul>
      <li>
       clog: Code cleanup, inherited fixes and tests from task
      </li>
      <li>
       taskd: The pki scripts now respect expiration date
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       flod: Began building on-demand system
      </li>
      <li>
       taskwarrior.org: Added
       <code>
        systemd
       </code>
       integration to the
       <a href="/docs/taskserver/control.html">
        taskserver control
       </a>
       page
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       task: Fix invalid context command example in man page fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-09
     </small>
    </td>
    <td>
     <ul>
      <li>
       task: Removed lots of obsolete and unused code
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TS-24">
        TS-24: add review option (m)odify
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1705">
        TW-1705: Directories in .task/hooks should not be reported as invalid hooks
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1714">
        TW-1714: Starting recurring task starts all recurrences
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1734">
        TW-1734: calendar gives an error when context is set
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1735">
        TW-1735: context with no subcommand should do something
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1736">
        TW-1736: Error on detection of BOM in files
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1741">
        TW-1741: Warning "ignoring return value of ‘int ftruncate" while doing make on xubuntu15.10
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1748">
        TW-1748: CMakeLists shouldn't hardcode libc++ on Darwin
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1752">
        TW-1752: cleanup of diag output
       </a>
       fixed
      </li>
      <li>
       task: Logic that determined
       <code>
        BLOCKING
       </code>
       and
       <code>
        BLOCKED
       </code>
       tasks that was different in two locations fixed
      </li>
      <li>
       taskwarrior.org: Added
       <code>
        on-modify.timetrack.pl
       </code>
       to the
       <a href="/tools/index.html">
        tools
       </a>
       page
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-12
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1719">
        TW-1719: Description cannot contain improper ordinals
       </a>
       fixed
      </li>
      <li>
       taskd: New pki script for checking cert expiration
      </li>
      <li>
       tasktools.org: Updated
       <code>
        clog
       </code>
       homebrew instructions
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-15
     </small>
    </td>
    <td>
     <ul>
      <li>
       task: OpenBSD also puts
       <code>
        libuuid
       </code>
       functions inside
       <code>
        libc
       </code>
       fixed
      </li>
      <li>
       taskd: Large improvements to the pki scripts
      </li>
      <li>
       taskwarrior.org: Better defaults for the
       <a href="/docs/taskserver/control.html">
        taskserver control
       </a>
       page
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       anomaly: The signal and system rections were switched fixed
      </li>
      <li>
       anomaly: Incorrect error message wording
      </li>
      <li>
       anomaly: Improved C++11 CppCoreGuidelines compliance
      </li>
      <li>
       clog: Improved C++11 CppCoreGuidelines compliance
      </li>
      <li>
       clog: Improved handling for suppressed lines, with documentation updates
      </li>
      <li>
       task: Missing include that broke Cygwin fixed
      </li>
      <li>
       vramsteg: Improved C++11 CppCoreGuidelines compliance
      </li>
      <li>
       vramsteg: Cannot trap SIGKILL fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-18
     </small>
    </td>
    <td>
     <ul>
      <li>
       common: Began work on breaking out code shared between projects into a separate repository, to reduce bug fix latency and duplication
      </li>
      <li>
       task: Bad link in man pages fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-23
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-107">
        TD-107: Bash dependency not documented
       </a>
       fixed
      </li>
      <li>
       task: The text certs all expired on the 19th fixed
      </li>
      <li>
       task: Bug where 'rc.allow.empty.filter' was not behaving properly fixed
      </li>
      <li>
       task: The
       <code>
        task sync init
       </code>
       command now uploads all tasks, not just pending tasks
      </li>
      <li>
       taskd: Modified code to allow a
       <code>
        subtype:
       </code>
       message header without ill effects, allowing for the
       <code>
        sync
       </code>
       message to have speicalized options
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-27
     </small>
    </td>
    <td>
     <ul>
      <li>
       task: Man page bugs fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-28
     </small>
    </td>
    <td>
     <ul>
      <li>
       taskwrrior.org: Unique page titles for more readable bookmarking
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       flod: Central dispatcher replaced
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-01-31
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1756">
        TW-1756: The columns.t unit test fails two tests after 2300 local
       </a>
       fixed
      </li>
      <li>
       task: Now delegates attribute modification to
       <code>
        Column
       </code>
       objects, which will allow a whole class of bugs to be fixed
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

