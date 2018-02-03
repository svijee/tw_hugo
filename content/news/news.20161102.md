---
date: 2016-11-02
title: 'Activity Digest: October 2016'
aliases: ['/news/news.20161102.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: October 2016
   <small>
    2016-11-02
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in our projects. Here is what happened in
            October 2016.

            This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the git history of all
            the projects.
  </p>
  <div class="callout callout-info">
   <h4>
    Summary
   </h4>
   <p>
    Flod2 is now being rolled out for testing. This is a CI system
              rewrite that eliminates build server daemons and the pull model.
              This will allow greater use of virtual machines, and more
              automation. For example, we will now be able to automatically
              generate coverage reports and snapshot tarballs, based on
              build characteristics.
   </p>
   <p>
    The focus is now Taskserver 1.2.0, which begins with code
              modernization and integration of
    <code>
     libshared
    </code>
    .
              The 1.2.0 release will be more reliable with easier diagnostics,
              and all the bug fixes we can make.
   </p>
   <p>
    What is Rat? It's the beginning of the new rule system that will
              work its way into most projects. More details soon.
   </p>
  </div>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2016-10-04
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Taskwarrior projects are now used intact as Timewarrior tags, in addition to being split on '.' for hierarchical tags
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-10-07
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/WWW-18">
        WWW-18: documentation typo
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-10-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       Flod: Now builds tinderbox report with minimal I/O
      </li>
      <li>
       Flod: New report template (
       <a href="http://tasktools.org/prototype/anomaly-1.2.0.html">
        prototype
       </a>
       ) with collapsible sections
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-10-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       WWW: Transferred all DNS handling over to
       <a href="http://dnsimple.com/">
        DNSimple
       </a>
      </li>
      <li>
       WWW: Acknowledged generous support from
       <a href="http://digitalocean.com/">
        Digitalocean
       </a>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-10-13
     </small>
    </td>
    <td>
     <ul>
      <li>
       Flod: Incorporates build times in report
      </li>
      <li>
       Flod: Configurable report length
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-10-14
     </small>
    </td>
    <td>
     <ul>
      <li>
       Flod: Can now execute remote build/test over ssh
      </li>
      <li>
       libshared: Improved C++ Core Guidelines compliance
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-10-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1857">
        TW-1857 Change Task::get call to the more efficient Task::has
       </a>
       fixed
      </li>
      <li>
       Task: Migrated more code to use
       <code>
        libshared
       </code>
       objects, instead of Taskwarrior objects
      </li>
      <li>
       Task: Improved C++ Core Guidelines compliance
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-10-17
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: The
       <code>
        Timer
       </code>
       object was migrated to
       <code>
        libshared
       </code>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-10-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskserver: Updated test framework in preparation for migrating all tests to Python
      </li>
      <li>
       Taskserver: Eliminated all references to the unimplemented 'group' feature
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-10-23
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Migrated several utility functions from Taskserver
      </li>
      <li>
       Taskserver: Updated compiler requirements to GCC 4.9/Clang 3.4
      </li>
      <li>
       Taskserver: Now uses the name 'api' instead of 'client' when describing certs/keys, to avoid misinterpretation
      </li>
      <li>
       Taskserver: Renamed the 'client' command to 'api'
      </li>
      <li>
       Taskserver: Removed unimplemented 'status' command
      </li>
      <li>
       Taskserver: Converted all tests to Python
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-10-29
     </small>
    </td>
    <td>
     <ul>
      <li>
       Rat: Fixed a 'This should never happen' exception that was actually quite common
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-10-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-52">
        TD-52: No errors in log in case of "No space left on device", but task data corrupted
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-112">
        TD-112: warning: missing initializer for member
       </a>
       fixed
      </li>
      <li>
       libshared: Improved error handling for assorted file system calls
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-10-31
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Updated
       <code>
        Log
       </code>
       object to incorporate Taskserver features
      </li>
      <li>
       Task: Made an error message more accurated, to reduce some confusion when a filter does not limit an operation to just the pending tasks
      </li>
      <li>
       Taskserver: Improved C++ Core Guidelines compliance
      </li>
      <li>
       Taskserver: Cleanup of unnused methods
      </li>
      <li>
       Taskserver: Now use the
       <code>
        libshared
       </code>
       <code>
        Log
       </code>
       object
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

