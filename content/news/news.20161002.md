---
date: 2016-10-02
title: 'Activity Digest: September 2016'
aliases: ['/news/news.20161002.html']
---
<div class="col-md-8 main">
 <div class="row">
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in our projects. Here is what happened in
            September 2016.

            This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the git history of all
            the projects.
  </p>
  <div class="callout callout-info">
   <h4>
    Summary
   </h4>
   <p>
    Tasksh 1.1.0 released, Anomaly 1.1.0 released.
              Flod2 is a major update that greatly improves speed and reliability
              of the CI system. It is working well, and will be rolled out in
              October, with new features and greater automation.
   </p>
  </div>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2016-09-02
     </small>
    </td>
    <td>
     <ul>
      <li>
       Anomaly: Converted test suite to Python
      </li>
      <li>
       Task: Now with correct build instructions for the dev branch
      </li>
      <li>
       Tasksh: Integrated libshared
      </li>
      <li>
       Tasksh: Converted test suite to Python
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-04
     </small>
    </td>
    <td>
     <ul>
      <li>
       Anomaly:
       <a href="https://tasktools.org/download/anomaly-1.1.0.tar.gz">
        Version 1.1.0
       </a>
       released
      </li>
      <li>
       Task: Updated test suite to use only non-deprecated Boolean config values
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TS-11">
        TS-11: Autoclear in the Task Shell
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TS-28">
        TS-28: Please add a (m)odify feature for review
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       Tasksh:
       <a href="news/news.20160905.2.html">
        Version 1.1.0
       </a>
       released, with new review feature
      </li>
      <li>
       Flod: All satellite build servers updated to latest releases
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-06
     </small>
    </td>
    <td>
     <ul>
      <li>
       Tasksh: ∀ixed build on Cygwin
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TS-29">
        TS-29: tasksh hangs trying to read task from stdin
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-13
     </small>
    </td>
    <td>
     <ul>
      <li>
       Rat: Modernized Tree object to use
       <code>
        std::shared_ptr
       </code>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-15
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Lexer can now disable individual features
      </li>
      <li>
       Rat: Upgraded from BNF to PEG
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Added Lexer tests when features are disabled
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-17
     </small>
    </td>
    <td>
     <ul>
      <li>
       Guides: Setup guide now explicitly mentions taskd-user
      </li>
      <li>
       libshared: Migrated Tree object from the rat project
      </li>
      <li>
       libshared: Added Pig::getcharacter, which was unexpectedly missing
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-18
     </small>
    </td>
    <td>
     <ul>
      <li>
       Rat: Now recognized junk at EOS
      </li>
      <li>
       Rat: Now implements positive/negative lookahead
      </li>
      <li>
       Rat: Now offers trace in debug mode
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-19
     </small>
    </td>
    <td>
     <ul>
      <li>
       Guides: Taskd setup guides now references the troubleshooting guide
      </li>
      <li>
       Rat: Now supports
       <code>
        &lt;character&gt;
       </code>
       intrinsic
      </li>
      <li>
       tasktools.org: Central (Flod) pages are now HTTPS always
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-25
     </small>
    </td>
    <td>
     <ul>
      <li>
       Flod2: Reworked scripts for efficiency, converted to Python, changed to a non-daemon model
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-27
     </small>
    </td>
    <td>
     <ul>
      <li>
       Holidata: Added US 2017, 2018; GB 2017, 2018 dates
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-29
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/WWW-16">
        WWW-16: Fix holiday type on en-GB Christmas 2016
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/WWW-17">
        WWW-17: I think some files weren't added after the last build
        <paste>
        </paste>
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-09-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       Guides: Taskd troubleshooting guides gains more diagnostic commands
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

