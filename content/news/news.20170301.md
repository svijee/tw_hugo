---
date: 2017-03-01
title: Activity Digest: February 2017
aliases: ['/news/news.20170301.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: February 2017
   <small>
    2017-03-01
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in our projects. Here is what happened in
            February 2017.

            This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the git history of all
            the projects.
  </p>
  <p>
   <img class="img-responsive" src="/news/images/perbacco.png"/>
  </p>
  <div class="callout callout-info">
   <h4>
    Summary
   </h4>
   <p>
    <a href="news.20170208.html">
     The team attended FOSDEM
    </a>
    in Brussels, all meeting for the first time. No one was hurt.
              Although we had hoped to accomplish a lot during this time, we
              instead fell in love with a certain restaurant and Belgian beer.
   </p>
   <p>
    We would like to welcome Thomas Lauf, who is now pushing to the
              Timewarrior repository, and Timewarrior is now being fixed and
              improved at a much faster rate. Welcome, Thomas.
   </p>
   <p>
    The flod2 CI system is coming online, which means that Taskwarrior
              is now being built in parallel by two CI systems as we prepare for
              a more general transition.
    <ul>
     <li>
      <a href="https://central.tasktools.org/task-2.6.0.html">
       Taskwarrior 2.6.0 on Flod
      </a>
     </li>
     <li>
      <a href="https://tyuratam.tasktools.org/task.2.6.0.html">
       Taskwarrior 2.6.0 on Flod2
      </a>
     </li>
    </ul>
   </p>
   <p>
    A generous donation from
    <a href="https://www.digitalocean.com">
     DigitalOcean
    </a>
    is making this possible.
   </p>
  </div>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2017-02-02
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-27">
        TI-27: Add tests for continue with ids
       </a>
       tests added
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-02-03
     </small>
    </td>
    <td>
     <ul>
      <li>
       FOSDEM: Team meets up in Brussels for FOSDEM, beer.
      </li>
      <li>
       FOSDEM: Team immediately recognizeѕ the importance of hotel meeting spaces that include large tables. It's not something we thought about, but now always will.
      </li>
      <li>
       FOSDEM: Team discovers great restaurant.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-02-04
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Fixed a test that assumes every month had 29 days. Not good.
      </li>
      <li>
       libshared: Merged the JSON and JSON2 (SAX) parsers.
      </li>
      <li>
       FOSDEM: Conference underway. Team is pleasantly surprised when people recognize the logo on our clothing/laptops and say nice things to us.
      </li>
      <li>
       FOSDEM: Team returns to same restaurant, displaying the kind of creativity you've come to expect from us.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-02-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       Tasksh: the
       <code>
        _reviewed
       </code>
       report now defaults to 6 days, rather than 7 days, to ensure weekly review as the default.
      </li>
      <li>
       FOSDEM: More people recognize our logo. This is nice.
      </li>
      <li>
       FOSDEM: Fixed an odd C++ syntax error that only affected a few platforms:
       <code>
        auto infix {true};
       </code>
       which clearly wasn't uniformly supported. During a FOSDEM break, in the cafeteria, we created a new Flod2 build satellite for CentOS 7.3, proviѕioned the VM, and debugged. Three people sharing two laptops extended a CI system on another continent, while drinking some very good coffee, surrounded by our fellow attendees, all doing the same thing. This is why we love conferences.
      </li>
      <li>
       FOSDEM: Team shamefully returns to the restaurant again, because it was so good. Also laziness.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-02-06
     </small>
    </td>
    <td>
     <ul>
      <li>
       FOSDEM: Breakfast, then we all head to different corners of the globe. Great trip, well worth it.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-02-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskwarrior: New
       <code>
        history.daily
       </code>
       ,
       <code>
        history.weekly
       </code>
       ,
       <code>
        ghistory.daily
       </code>
       and
       <code>
        ghistory.weekly
       </code>
       commands.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-02-09
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-64">
        TI-64: Command 'stop' with date before current interval's start date causes segfault
       </a>
       fixed
      </li>
      <li>
       libshared: Table now offers control over the alternating row coloring.
      </li>
      <li>
       Taskwarrior: The
       <code>
        timesheet
       </code>
       report was rewritten to accept a filter, provide more compact output, and provide daily grouping of started and completed tasks.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-02-10
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Now has weekday hints (
       <code>
        :monday
       </code>
       ,
       <code>
        :tuesday
       </code>
       ,
       <code>
        :wednesday
       </code>
       ,
       <code>
        :thursdday
       </code>
       ,
       <code>
        :friday
       </code>
       ,
       <code>
        :saturday
       </code>
       ,
       <code>
        :sunday
       </code>
       ) to simplify historic data tracking.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-02-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Can now parse IPv4 and IPv6 addresses. This is used when trying to determine whether SNI is enabled.
      </li>
      <li>
       Taskwarrior: Now supports SNI.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-02-12
     </small>
    </td>
    <td>
     <ul>
      <li>
       Flod2: The
       <a href="https://tyuratam.tasktools.org/task.2.6.0.html">
        commit status report
       </a>
       now uses a color palette that is less saturated and doesn't transition through brown twice. The colors indicating status now range from black (did not build) through dark red (bad), orange and yellow (better), finally green (100% good). A good commit is then marked as 'clean' if all the test platforms not only pass, but agree. This will later lead to automatic tagging and dev snapshot tarball creation.
      </li>
      <li>
       Taskwarrior: The build process now clones/updates
       <code>
        libshared
       </code>
       if necessary. This removes a manual step.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-02-13
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-39">
        TI-39: Bogus command line option causes segfault
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-02-14
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-40">
        TI-40: totals.py extension script fails with an error
       </a>
       fixed
      </li>
      <li>
       Flod2: The
       <a href="https://tyuratam.tasktools.org">
        summary report
       </a>
       , although incomplete, now provides an overall assessment of a commit. In this example, the status
       <span style="color:#ffafd7; background-color:#822453;">
        Funky
       </span>
       is common, and indicates that there is an important disagreement between the results. This is a new feature that better highlights problems to be addressed.
      </li>
     </ul>
    </td>
   </tr>
  </table>
 </div>
</div>
