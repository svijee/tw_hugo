---
date: 2015-03-01
title: 'Activity Digest: February 2015'
aliases: ['/news/news.20150301.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: February 2015
   <small>
    2015-03-01
   </small>
  </h3>
  <p>
   This is the second of an ongoing series of activity reports,
            published monthly, to highlight activity in the Taskwarrior
            project. Here is what happened in February 2015.
  </p>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2015-02-01
     </small>
    </td>
    <td>
     Renato adds a wrapper script that instruments all hooks scripts
                which gives the test framework an inspectable data structure
                that details hook script activity.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-03
     </small>
    </td>
    <td>
     It was reiterated that there is a place to check, to see what
                latest release of Taskwarrior is:
     <a href="http://tasktools.org/latest">
      http://tasktools.org/latest
     </a>
     .
                This is suitable for anyone who needs to programmatically scan
                for notification of a release.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-07
     </small>
    </td>
    <td>
     A bug in the code that executes hook scripts is fixed, which
                allows hook script testing on FreeBSD and Cygwin to proceed.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-07
     </small>
    </td>
    <td>
     A preliminary design for supporting the notion of active
                contexts was agreed upon, written up and placed among the
     <a href="http://taskwarrior.org/docs/design/index.html">
      design docs
     </a>
     .
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-08
     </small>
    </td>
    <td>
     The document describing
     <a href="http://taskwarrior.org/docs/design/plans.html">
      future plans
     </a>
     was updated. This document shows a high-level overview of what
                areas of Taskwarrior are planned for future work. While there is
                minimal detail, it does represent all the planning that exists.
                It lists the current release, the next release (short term) and
                future releases (long term) milestones.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-09
     </small>
    </td>
    <td>
     More "category" values were addd to Jira to allow more useful
                grouping of issues.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-13
     </small>
    </td>
    <td>
     Renato adds a
     <code>
      status
     </code>
     command to the
                Taskserver
     <code>
      taskdctl
     </code>
     launcher.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-14
     </small>
    </td>
    <td>
     The hook script interface is made much more strict, with lots
                more consistency checking. This will help deal with non-compliant
                hook scripts, and scripts in development.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-14
     </small>
    </td>
    <td>
     Taskwarrior 2.4.1 is ready to release, pending testing by
     <a href="https://github.com/ralphbean/bugwarrior">
      Bugwarrior
     </a>
     ,
     <a href="https://inthe.am/about">
      inthe.am
     </a>
     , and
     <a href="https://github.com/tbabej/tasklib">
      tasklib
     </a>
     .
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-15
     </small>
    </td>
    <td>
     The
     <a href="http://taskwarrior.org/docs/design/plans.html">
      future plans
     </a>
     document was updated to include Taskserver plans (which are
                currently sparse).  More details were added to the Taskwarrior
                plans.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-15
     </small>
    </td>
    <td>
     Testing showed that 2.4.1 does not degrade performance any more
                than 2.4.0 did.
                See the
     <a href="http://tasktools.org/projects/performance.html">
      Performance Comparison
     </a>
     for charts.
                Note that 2.4.0 contains on-load legacy value mapping for
                durations, which introduced a perofrmance hit.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-16
     </small>
    </td>
    <td>
     <a href="/download/task-latest.tar.gz">
      Taskwarrior 2.4.1
     </a>
     is released. Although a minor release, there are significant bug
                fixes and improvements to the
     <a href="/docs/design/hooks.html">
      Hook system
     </a>
     that make this
                a recommended upgrade.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-16
     </small>
    </td>
    <td>
     Taskwarrior 2.4.2 work begins, with this effort being mostly
                concerned with bugs and performance.  Mostly.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-16
     </small>
    </td>
    <td>
     Ralph Bean releases
     <a href="https://pypi.python.org/pypi/taskw">
      taskw
     </a>
     with support for Taskwarrior 2.4.1.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-16
     </small>
    </td>
    <td>
     Renato doubles the speed of the test suite. We're not sure how.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-16
     </small>
    </td>
    <td>
     Taskwarrior 2.4.2 work begins, with this effort being mostly
                concerned with bugs and performance.  Mostly.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-17
     </small>
    </td>
    <td>
     The INSTALL file gets a fresh set of instructions which now
                mention the dependencies and requirements.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-17
     </small>
    </td>
    <td>
     The website gains a page devoted to showing
     <a href="/docs/examples.html">
      Command Line Examples
     </a>
     intended to answer a few common questions and showcase
                some tricks.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-19
     </small>
    </td>
    <td>
     Renato converts more Perl unit tests to Python, raising the
                percentage to 22.8% Python. The goal is ultimately 100%.
                Additionally, some of the individual test scripts are being
                merged into higher-level feature test scripts.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-21
     </small>
    </td>
    <td>
     Wim fixes C++11 build issues, which means Taskwarrior can
                begin to take advantage of C++11 capabilities, after a 4 year
                grace period to let compilers catch up.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-22
     </small>
    </td>
    <td>
     Wim fixes a dangling pipe problem that prevents forking hook
                scripts from running.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-22
     </small>
    </td>
    <td>
     Taskserver gained a new man page for
     <code>
      taskdctl
     </code>
     .
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-23
     </small>
    </td>
    <td>
     Tomas implements the new
     <a href="/docs/design/context.html">
      context
     </a>
     feature and commands.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-24
     </small>
    </td>
    <td>
     The
     <code>
      list
     </code>
     report loses listing breaks by default.
                The
     <code>
      minimal
     </code>
     report shows the feature.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-25
     </small>
    </td>
    <td>
     The Taskwarrior
     <code>
      info
     </code>
     command gains the ability to
                show virtual tags.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-25
     </small>
    </td>
    <td>
     Bash completion script learns about new
     <code>
      context
     </code>
     commands.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-28
     </small>
    </td>
    <td>
     Tomas added a GC call before the
     <code>
      projects
     </code>
     command
                runs, to make the output current.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-28
     </small>
    </td>
    <td>
     Tomas added aggregated task counts to the
     <code>
      projects
     </code>
     reports, where sub-projects contributed to the super-projects.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-02-28
     </small>
    </td>
    <td>
     Taskwarrior 2.4.1 is available in binary and source package
                form for Cygwin 32- and 64-bit systems.
    </td>
   </tr>
   <!--
            <tr>
              <td><small>2015-02-01</small></td>
              <td>
              </td>
            </tr>

            <tr>
              <td><small>2015-02-01</small></td>
              <td>
              </td>
            </tr>

            <tr>
              <td><small>2015-02-01</small></td>
              <td>
              </td>
            </tr>
-->
  </table>
  <br/>
  <br/>
 </div>
</div>

