---
date: 2017-05-09
title: 'Activity Digest: April 2017'
aliases: ['/news/news.20170509.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: April 2017
   <small>
    2017-05-09
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in our projects. Here is what happened in
            April 2017.

            This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the git history of all
            the projects.
  </p>
  <div class="callout callout-info">
   <h4>
    Summary
   </h4>
   <p>
    April was a relatively quiet month, but with two main efforts:
              Timewarrior 1.1.0 bug fixing, and deployment of our Flod CI system
              for all projects.
   </p>
   <p>
    Flod CI is now operating on five platforms (more coming soon),
              for every commit on every branch for every project.
              This transition allowed us to decommission several old machines.
   </p>
   <p>
    <img class="img-responsive" src="/news/images/central.png"/>
   </p>
   <p>
    <img class="img-responsive" src="/news/images/tw.png"/>
   </p>
  </div>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2017-04-04
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-70">
        TI-70: Timew starts a new interval even if a current interval contains the same set of tags
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-04-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-58">
        TI-58: Fix bug 'Delete command is not always deleting'
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-04-06
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-27">
        TI-27: Continue tracking by ID
       </a>
       fixed
      </li>
      <li>
       task: Separated processing of expired tasks (
       <code>
        until:
       </code>
       ) from the existing recurrence processing
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-04-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-68">
        TI-68: Let commands convert synthetic intervals before modifying them
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-04-10
     </small>
    </td>
    <td>
     <ul>
      <li>
       flod: Integrated flod reports with
       <a href="https://git.tasktools.org">
        Gitea
       </a>
      </li>
      <li>
       flod: Implemented summary report at
       <a href="https://central.tasktools.org/">
        https://central.tasktools.org/
       </a>
      </li>
      <li>
       task: Implemented framework for supporting the
       <a href="https://taskwarrior.org/docs/design/recurrence.html">
        new recurrence model
       </a>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-04-11
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
       Flod: Deployed
       <a href="https://central.tasktools.org">
        Flod CI testing for all projects
       </a>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-04-14
     </small>
    </td>
    <td>
     <ul>
      <li>
       timew: The totals.py extension now supports both Python 2.x and 3.x
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-04-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       timew: The future command line syntax design is progressing.
       <a href="https://git.tasktools.org/TM/timew/src/1.1.0/doc/rfc_command_definition.md">
        Follow it here
       </a>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-04-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       task: Implemented new DOM resolver tree to simplify existing DOM support and enable
       <a href="https://taskwarrior.org/docs/design/recurrence.html">
        greater DOM support
       </a>
       , including formats
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

