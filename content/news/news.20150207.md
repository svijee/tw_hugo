---
date: 2015-02-07
title: 'Activity Digest: January 2015'
aliases: ['/news/news.20150207.html']
---
<div class="col-md-8 main">
 <div class="row">
  <p>
   This is the first of an ongoing series of activity reports,
            published monthly, to highlight activities in the Taskwarrior
            project. Here is what happened in January 2015.
  </p>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2015-01-01
     </small>
    </td>
    <td>
     <a href="http://taskwarrior.org/news/news.20150101.html">
      Taskwarrior 2.4.0
     </a>
     released.  Including ISO date support, algebraic expressions
                and more.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-02
     </small>
    </td>
    <td>
     Some people are seeing unreadable color combination in 2.4.0
                color themes. Some contrast and color improvements were made in
                the 2.4.1 branch.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-03
     </small>
    </td>
    <td>
     People are finding that 2.4.0 introduces a tri-state 'taskd.trust'
                setting, which needs to be updated with a good value. The
     <a href="http://taskwarrior.org/docs/taskserver/troubleshooting-sync.html">
      troubleshooting sync
     </a>
     docs are updated accordingly.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-03
     </small>
    </td>
    <td>
     The Taskwarrior data anonymizer is now available for download.
     <em>
      Edit: The anoonymizer is now replaced by
     </em>
     <pre>task ... rc.obfuscate:1</pre>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-03
     </small>
    </td>
    <td>
     The
     <code>
      waiting
     </code>
     report is broken in 2.4.0, and shows
                all tasks that have the waiting attribute, past or future.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-03
     </small>
    </td>
    <td>
     People are finding that the
     <code>
      due.age
     </code>
     column used
                in some reports is not showing data in the future, which makes
                it useless.  Fixed in 2.4.1.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-03
     </small>
    </td>
    <td>
     Tomas introduces
     <a href="https://github.com/tbabej/tasklib">
      tasklib
     </a>
     which provides a Python API to access Taskwarrior data.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-03
     </small>
    </td>
    <td>
     New documentation to help developers
     <a href="http://taskwarrior.org/docs/build.html">
      build
     </a>
     Taskwarrior is introduced.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-04
     </small>
    </td>
    <td>
     <a href="http://taskwarrior.org/docs/dates.html">
      New documentation
     </a>
     listing the 47 new ISO date formats supported is added.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-04
     </small>
    </td>
    <td>
     Changes made to support building with musl (libc) in 2.4.1.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-04
     </small>
    </td>
    <td>
     A script to generate a test data file, that we could use
                as a common basis for checking functionality was discussed, but
                no one wants to do it.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-05
     </small>
    </td>
    <td>
     The first step is take towards using modern C++11 features,
                where N1984 (auto type derivation) is used in one place, and
                implies a minimum gcc 4.4 or clang 2.9, both of which are
                several years old.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-08
     </small>
    </td>
    <td>
     The
     <code>
      diag
     </code>
     command is improved so that it offers
                information when hook scripts are minamed, or not executable.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-08
     </small>
    </td>
    <td>
     Jens contributes a German localization for Taskwarrior,
                included in 2.4.1.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-18
     </small>
    </td>
    <td>
     Diagnostic and debug output is improved for authors of hook
                scripts.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-19
     </small>
    </td>
    <td>
     Renato adds support to the test framework for hook script
                tests. These are needed before the 2.4.1 release.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-19
     </small>
    </td>
    <td>
     Tomas makes several useful hook scripts available from
                the
     <a href="http://taskwarrior.org/tools">
      tools page
     </a>
     .
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-28
     </small>
    </td>
    <td>
     Leo announces
     <a href="https://gitlab.com/WzukW/oclaunch">
      oclaunch
     </a>
     , which can
                be used to run commands at login.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-31
     </small>
    </td>
    <td>
     Hook scripts which create additional tasks are causing problems,
                resulting in the hooks interface being restricted for 2.4.1.
                Hook scripts can no longer modify out-of-context tasks, or add
                arbitrary new tasks. Unit tests for hooks are introduced, which
                will lead to more stringent checking in Taskwarrior.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-01-31
     </small>
    </td>
    <td>
     Downloads for January for the 2.4.0 source tarball: 1773.
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

