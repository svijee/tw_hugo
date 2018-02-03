---
date: 2017-02-09
title: 'Activity Digest: January 2017'
aliases: ['/news/news.20170209.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: January 2017
   <small>
    2017-02-09
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in our projects. Here is what happened in
            January 2017.

            This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the git history of all
            the projects.
  </p>
  <div class="callout callout-info">
   <h4>
    Summary
   </h4>
   <p>
    The rat parser is now mostly complete, and ready to take on the
              syntax of the rules system.
   </p>
   <p>
    The
    <a href="https://bug.tasktools.org">
     Taskwarrior bug database
    </a>
    haѕ had another cleanup pass that removed obsolete or
              accidentally fixed issues.
   </p>
   <p>
    The flod2 CI system is now online and is about to begin processing
              builds instead of the old flod system. Both system will be online
              until the switchover is complete.
   </p>
   <p>
    Finally, the team spent a little time getting ready for FOSDEM.
   </p>
  </div>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2017-01-02
     </small>
    </td>
    <td>
     <ul>
      <li>
       rat: Now has grammar to parse Datetime
      </li>
      <li>
       rat: Now has grammar to parse Duration
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-07
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TS-34">
        TS-34: Tasksh throw a warning at the end of a review command
       </a>
       fixed
      </li>
      <li>
       task: Gained new
       <code>
        TEMPLATE
       </code>
       and
       <code>
        INSTANCE
       </code>
       virtual tags, used by the (coming) recurrence model
      </li>
      <li>
       task: Column objects cleaned up, ready for refactoring
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       anomaly: Integrated libshared.git
      </li>
      <li>
       rat: Now supports entity definitions via the command line
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-09
     </small>
    </td>
    <td>
     <ul>
      <li>
       rat: PEG can now be parsed in strict mode, which upgrades warnings to errors
      </li>
      <li>
       rat: PEG supports new
       <code>
        &lt;entity:XXX&gt;
       </code>
       intrinsic
      </li>
      <li>
       rat: PEG files now support nested imports
      </li>
      <li>
       taskd: Fixed build in SunOS-like environments
      </li>
      <li>
       timew: Now has a
       <code>
        resize
       </code>
       command
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-10
     </small>
    </td>
    <td>
     <ul>
      <li>
       rat: Now reports runtime in debug mode
      </li>
      <li>
       rat: Now has grammar to parse clog rule sets
      </li>
      <li>
       rat: PEG is no longer parsed in strict mode by default
      </li>
      <li>
       rat: PEG supports new
       <code>
        &lt;external:XXX&gt;
       </code>
       intrinsic
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       rat: Now has grammar to parse DOM references
      </li>
      <li>
       rat: Now has grammar to parse UUIDs
      </li>
      <li>
       rat: Now protects against multiple imports
      </li>
      <li>
       rat: PEG supports new
       <code>
        &lt;hex&gt;
       </code>
       intrinsic
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-14
     </small>
    </td>
    <td>
     <ul>
      <li>
       task: Build fixed in SunOS-like environments: OpenIndiana, Omnios, SmartOS
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-15
     </small>
    </td>
    <td>
     <ul>
      <li>
       taskd: Do not use 'which' for finding gnutls certool path
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-213">
        TW-213: Align countdown column on boundary between number and text.
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1572">
        TW-1572: Alternative approach to urgency inheritance
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1667">
        TW-1667: hooks: upon failure indicate which hook failed
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1823">
        TW-1823: Incorrect unicode text wrapping / justifying
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1827">
        TW-1827: Extract annotations from a task
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1877">
        TW-1877: task done, task edit, task is now pending
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1880">
        TW-1880: Missing last character(s) in Description field
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1881">
        TW-1881: default.scheduled seems not to work
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1861">
        TW-1861: Truncated description when adding annotation
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-49">
        TI-49: new theme files aren't installed
       </a>
       fixed
      </li>
      <li>
       libshared: Duration::formatVague can now pad all values to the same length
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-21
     </small>
    </td>
    <td>
     <ul>
      <li>
       flod: Project no longer updated or supported
      </li>
      <li>
       flod2: Project now public and begins deployment
      </li>
      <li>
       flod2: Now detects clean builds across all platforms
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-24
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1869">
        TW-1869 segmentation fault (on unusual installation)
       </a>
       fixed
      </li>
      <li>
       task: Updated expired test certs/keys
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-25
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-61">
        TI-61: Typo in exclusion.t.cpp
       </a>
       fixed
      </li>
      <li>
       flod2: Publish script working
      </li>
      <li>
       task: Migrated to use libshared Color
      </li>
      <li>
       task: Variant no longer uses localied strings
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-26
     </small>
    </td>
    <td>
     <ul>
      <li>
       flod2: Combined multiple ssh calls into one, to reduce network traffic
      </li>
      <li>
       flod2: Report now has collapsible platform details
      </li>
      <li>
       flod2: Reports test failure details
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-27
     </small>
    </td>
    <td>
     <ul>
      <li>
       task:
       <code>
        ghistory
       </code>
       command code refactoring
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-28
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-62">
        TI-62: TimeWarrior should not ignore invalid command
       </a>
       fixed
      </li>
      <li>
       flod2: Now detects when a platform runs an unexpectedly different number of tests
      </li>
      <li>
       flod2: Now links back to Gitea commit page
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-29
     </small>
    </td>
    <td>
     <ul>
      <li>
       flod2: Now auto-generates a summary page for all projects
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-01-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       task:
       <code>
        history
       </code>
       command code refactoring
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

