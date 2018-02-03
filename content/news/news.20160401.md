---
date: 2016-04-01
title: Activity Digest: March 2016
aliases: ['/news/news.20160401.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: March 2016
   <small>
    2016-04-01
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in the Taskwarrior project. Here is what
            happened in March 2016.
  </p>
  <p>
   This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the
   <a href="https://git.tasktools.org/projects/TM/repos/task/commits?until=refs%2Fheads%2F2.6.0">
    full Git history
   </a>
   .
  </p>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2016-03-01
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Gained JSON parser from Taskwarrior
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-02
     </small>
    </td>
    <td>
     <ul>
      <li>
       Guides: New repo for Taskwarrior presentations online
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-13
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Design outline complete
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Renamed from the older 'common' - a git submodule to share code across projects
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-17
     </small>
    </td>
    <td>
     <ul>
      <li>
       Flod: Added support for submodules, using
       <code>
        git clone --recursive ...
       </code>
      </li>
      <li>
       Flod2: Migrated to use
       <code>
        libshared.git
       </code>
      </li>
      <li>
       libshared: Can now join strings
      </li>
      <li>
       libshared: Log object added
      </li>
      <li>
       Timewarrior: Migrated to use
       <code>
        libshared.git
       </code>
      </li>
      <li>
       Timewarrior: Repo goes public
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-19
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskwarrior.org: Added
       <a href="https://github.com/envolyse/estact">
        estact
       </a>
       to the
       <a href="/tools/index.html">
        Tools
       </a>
       page
      </li>
      <li>
       Timewarrior: Now has a working
       <code>
        help
       </code>
       command
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-20
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Gained a new
       <code>
        purge
       </code>
       command to eliminate old data
      </li>
      <li>
       Timewarrior: Can now load data
      </li>
      <li>
       Timewarrior: Now has a working
       <code>
        extensions
       </code>
       command
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-21
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Duration class can now format in a human-readable way
      </li>
      <li>
       Timewarrior: Now tracks time using a
       <code>
        start
       </code>
       and
       <code>
        stop
       </code>
       command
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1772">
        TW-1772: Implementation of circular dependency detection is inefficient
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1788">
        TW-1788: Closing a reopened task does not update the end time
       </a>
       fixed
      </li>
      <li>
       Timewarrior: Now has a working
       <code>
        log
       </code>
       command
      </li>
      <li>
       Timewarrior: Now has a working
       <code>
        export
       </code>
       command
      </li>
      <li>
       Timewarrior: Now has a working
       <code>
        continue
       </code>
       command
      </li>
      <li>
       Timewarrior: Now has a working default command
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-23
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-103">
        TD-103: Incorrect error when org does not exists
       </a>
       fixed
      </li>
      <li>
       Taskwarrior.org: Added mailing lists to the contribution page
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-25
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Now has a working
       <code>
        stop
       </code>
       command
      </li>
      <li>
       Timewarrior: Added the extension API
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-26
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-49">
        TD-49: Log when file management fails
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-115">
        TD-115: Throw error when config file is missing or not readable
       </a>
       fixed
      </li>
      <li>
       Taskwarrior.org: Added
       <a href="/docs/first_time.html">
        First Time Contributor
       </a>
       page/
      </li>
      <li>
       Timewarrior: Now has a working
       <code>
        diagnostics
       </code>
       command
      </li>
      <li>
       Timewarrior: Added the first color theme
      </li>
      <li>
       Timewarrior: Added the first holiday file
      </li>
      <li>
       Timewarrior: Added a debug report to test the extension API
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-27
     </small>
    </td>
    <td>
     <ul>
      <li>
       Flod: Documentation fixes
      </li>
      <li>
       libshared: Now has a split function that coallesces whitespace
      </li>
      <li>
       task/libshared: Now knows when 'juhannus' is
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-28
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Table now switches to hyphen underlines when output is not to a TTY
      </li>
      <li>
       Timewarrior: Now colorizes tags
      </li>
      <li>
       Timewarrior: Now has a working
       <code>
        tags
       </code>
       command
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-03-29
     </small>
    </td>
    <td>
     <ul>
      <li>
       All: Colored test script output propagated to all projects
      </li>
      <li>
       Task: Deprecated the
       <code>
        DUETODAY
       </code>
       virtual tag
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

