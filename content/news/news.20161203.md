---
date: 2016-12-03
title: 'Activity Digest: November 2016'
aliases: ['/news/news.20161203.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: November 2016
   <small>
    2016-12-03
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in our projects. Here is what happened in
            November 2016.

            This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the git history of all
            the projects.
  </p>
  <div class="callout callout-info">
   <h4>
    Summary
   </h4>
   <p>
    The focus has been on migrating code back to libshared.git, and in
              turn making use of that code. This not only shrinks the size of the
              projects, but means that bug fixes in libshared.git benefit all
              projects, and reduces effort.
   </p>
   <p>
    The Taskserver codebase is being cleaned up in preparation for a
              major fix and test cycle coming up.
   </p>
  </div>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2016-11-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-51">
        TI-51: in the taskwarrior hook, deleting a task doesn't stop the watch
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-06
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-52">
        TI-52: The 'refresh' scripts overwrites previous years data
       </a>
       fixed
      </li>
      <li>
       Timew: Holiday data updated
      </li>
      <li>
       Taskd: Improved GnuTLS 3.3.0+ support
      </li>
      <li>
       Taskd: Improved GnuTLS 3.5.6+ support for GNUTLS_SEC_PARAM_HIGH
      </li>
      <li>
       Guides: Added OpenRheinRuhr slides
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TS-32">
        TS-32: control-d to exit
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-12
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskd: Improved demo tests
      </li>
      <li>
       libshared: Migrated Timer to use C++11 std::chrono
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-13
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Integrated libshared.git Timer
      </li>
      <li>
       libshared: Added millisecond, microsecond and nanosecond Timer support
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-15
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-53">
        TI-53: Fix musl-libc compatibility
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       WWW: DNS now being resolved by
       <a href="https://dnsimple.com/resolving/taskwarrior">
        dnsimple.com
       </a>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-19
     </small>
    </td>
    <td>
     <ul>
      <li>
       WWW: RSS feed cleaned up and validated
      </li>
      <li>
       Task: Improved diagnostics regarding missing/unreadable files
      </li>
      <li>
       libshared: Made error handling for FS objects very strict, so the error messages are meaningful
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-20
     </small>
    </td>
    <td>
     <ul>
      <li>
       hd.net: Cleaned up holiday definitions for upcoming automation
      </li>
      <li>
       holidata: Created new holidata automation utility
      </li>
      <li>
       holidata: Abstracted all holiday definitions
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-21
     </small>
    </td>
    <td>
     <ul>
      <li>
       Vramsteg: Now properly installs man page
      </li>
      <li>
       Vramsteg: Test suite converted to Python
      </li>
      <li>
       All: Fixed test suite problem with Python 3.5.2
      </li>
      <li>
       libshared: Refactored Args object, adding features
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskd: Increased use of libshared.git code
      </li>
      <li>
       Taskd: Added error messages when suspending already suspended node, resuming an unsuspended node
      </li>
      <li>
       libshared: Fixed Lexer::dequote minimum length bug
      </li>
      <li>
       libshared: Merged Configuration with Taskd enhancements
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-24
     </small>
    </td>
    <td>
     <ul>
      <li>
       rat: Now has PEG syntax tests
      </li>
      <li>
       rat: Migrated to libshared.git Args
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-25
     </small>
    </td>
    <td>
     <ul>
      <li>
       tw.org: Fixed typos in
       <a href="/download/task-2.5.1.ref.pdf">
        task-2.5.1.ref.pdf
       </a>
       online
      </li>
      <li>
       WWW: HTTP now served and deployed by
       <a href="https://caddyserver.com/">
        caddy
       </a>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-26
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskd: Inherited bug fixes from Taskwarrior
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-11-27
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: join() now supports vector&lt;int&gt;
      </li>
      <li>
       libshared: Improved Path tests
      </li>
      <li>
       libshared: Migrated find functions from Taskd
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

