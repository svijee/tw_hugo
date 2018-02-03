---
date: 2015-11-01
title: 'Activity Digest: October 2015'
aliases: ['/news/news.20151101.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: October 2015
   <small>
    2015-11-01
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in the Taskwarrior project. Here is what
            happened in October 2015.
  </p>
  <p>
   This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the
   <a href="https://git.tasktools.org/projects/TM/repos/task/commits?until=refs%2Fheads%2F2.4.5">
    full Git history
   </a>
   .
  </p>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2015-10-07
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1620">
        TW-1620: Dateformat wrongly interpreted
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-10
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/CL-8">
        CL-8: clog 1.2.0 fails to build
       </a>
       fixed
      </li>
      <li>
       Holidata: Added Ecuador dates
      </li>
      <li>
       Holidata: Added Colombia dates
      </li>
      <li>
       Task: Added Ecuador and Colombia holidays
      </li>
      <li>
       Task: Fixed crash bug in regex support
      </li>
      <li>
       Task: Allows zero-padded single-digit
       <code>
        rc.dateformat
       </code>
       elements
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskd: Improved error messages for the common case where
       <code>
        task sync init
       </code>
       was skipped
      </li>
      <li>
       Taskd: User may now override
       <code>
        dh_bits
       </code>
       , which has a better default of 2048
      </li>
      <li>
       Taskd: Per Mozilla guidelines, now prefers server-side ordering of ciphers
      </li>
      <li>
       Taskd: Removed default support for broken algorithms (SSLv3, TLSv1.0 (POODLE), 3DES in CBC mode, RC4, MD5)
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-12
     </small>
    </td>
    <td>
     <ul>
      <li>
       Clog: 1.2.1 released
      </li>
      <li>
       Vramsteg: 1.1.1 released
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-13
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Fixed very old bug in date coercion
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-15
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: The Bash test framework gets an update
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1715">
        TW-1715: Dates misinterpreted when no dateformat active
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-17
     </small>
    </td>
    <td>
     <ul>
      <li>
       Tasksh: Automatic report and UDA setup for
       <code>
        review
       </code>
       command
      </li>
      <li>
       Tasksh: The
       <code>
        diag
       </code>
       command is now complete
      </li>
      <li>
       Task: 2.5.0.beta3 released
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-18
     </small>
    </td>
    <td>
     <ul>
      <li>
       Tasksh: Inherits the parallel test framework from taskwarrior
      </li>
      <li>
       Tasksh: The
       <code>
        exec
       </code>
       (or
       <code>
        !
       </code>
       ) command is now complete
      </li>
      <li>
       Tasksh: The
       <code>
        review
       </code>
       command now takes a numeric argument indicating how many tasks should be reviewed, e.g.
       <code>
        review 10
       </code>
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1716">
        TW-1716: on-modify hooks fail if `date.iso` is not set
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-21
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="/news/news.20151021.html">
        Task: 2.5.0 released
       </a>
      </li>
      <li>
       Task: 2.5.1 begins, which will be a bugfix and performance release
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-24
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: JSON decoder performance increased
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-28
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Code test coverage raised to 90.6%, which helps find problems
      </li>
      <li>
       Task: Lots of unused code removed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-29
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Now defaults to 256-colors on all platforms
      </li>
      <li>
       Task: The
       <code>
        columns
       </code>
       command now shows whether an attribute is modifiable or read only
      </li>
      <li>
       Task: Mailing list for user discussions back in use:
       <a href="https://groups.google.com/forum/#!forum/taskwarrior-user">
        https://groups.google.com/forum/#!forum/taskwarrior-user
       </a>
       .
      </li>
      <li>
       Task: Mailing list for developer discussions back in use:
       <a href="https://groups.google.com/forum/#!forum/taskwarrior-dev">
        https://groups.google.com/forum/#!forum/taskwarrior-dev
       </a>
       .
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-10-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1704">
        TW-1704: Task: Use Task::identifier to reference the task
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1720">
        TW-1720: CmdContext uses a mix of both throw and std::cout to convey errors
       </a>
       fixed
      </li>
      <li>
       Task: The
       <code>
        diagnostics
       </code>
       command now finds broken references between recurring task instances and templates
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

