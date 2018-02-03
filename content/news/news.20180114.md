---
date: 2018-01-14
title: 'Activity Digest: May - December 2017'
aliases: ['/news/news.20180114.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: May - December 2017
   <small>
    2018-01-14
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in our projects. Here is what happened between
            May and December 2017.

            This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the git history of all
            the projects.
  </p>
  <p>
   This covers a seven month period. Due to unforeseen circumstances,
            there was a lengthy break in 2017. We're back.
  </p>
  <div class="callout callout-info">
   <h4>
    Summary
   </h4>
   <p>
    Most of the time was spent moving Timewarrior 1.1.0 closer to release.
   </p>
  </div>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2017-05-03
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: doc: Update command definition document
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-05-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1910">
        TW-1910: Remove unreachable statement
       </a>
       fixed
      </li>
      <li>
       Taskwarrior, Taskserver: TLSClient: Remove double include
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-05-10
     </small>
    </td>
    <td>
     <ul>
      <li>
       Tasksh: 1.2.0 released
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-05-21
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-73">
        TI-73: timew move with a specific time broken on 1.1.0
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-77">
        TI-77: timew track seems to think today is tomorrow
       </a>
       fixed
      </li>
      <li>
       libshared: Added ::timeRelative support for dates that project either forwards or backwards in time
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-05-28
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: validate: Uses helper function to find overlaps
      </li>
      <li>
       Timewarrior: data: Added better error when an attempt is made to track a future interval
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-06-12
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskwarrior: tests: Add tests for complex and-or queries
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-06-14
     </small>
    </td>
    <td>
     <ul>
      <li>
       Twarrior: Quote tags containing underscores
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-07-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskwarrior: Recurrence: Updated 'until' handling
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-07-27
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskwarrior: context: Do not allow show, list or none as new context names
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-07-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-69">
        TI-69: timew config converts integers to times
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-08-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-78">
        TI-78 Tag parsing broken for tags starting with "or_"
       </a>
       fixed
      </li>
      <li>
       Flod: Improved test report formatting
      </li>
      <li>
       Flod: Added test count for 100% case
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-08-18
     </small>
    </td>
    <td>
     <ul>
      <li>
       All: Update git repo url
      </li>
      <li>
       Timewarrior: CONTRIBUTING: Update repo url and add recursive flag
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-10-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskwarrior: Changed (1) error format
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-10-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-136">
        TD-136: systemd service: logging to standard out with --log=- no longer works
       </a>
       fixed
      </li>
      <li>
       All: Removed obsolete URLs from source
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-10-23
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Added Packrat
       <code>
        external
       </code>
       tests
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-11-21
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Commands: Reduce code duplication
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-11-24
     </small>
    </td>
    <td>
     <ul>
      <li>
       All: Improve TAP compliance in test suite
      </li>
      <li>
       Taskwarrior: CLI2,Config: Add 'override' verbosity options
      </li>
      <li>
       Docs/CLI2: Additional dev docs for applyOverrides
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-12-01
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-75">
        TI-75: Fix cases where interval borders match when applying :fill hint
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-12-02
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1930">
        TW-1930: Typo in help
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1935">
        TW-1935: Separate verbosity category for rc overrides
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1936">
        TW-1936: Tweak tests to have fuller TAP compliance
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-12-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-90">
        TI-90: Update help for command 'continue'
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-90">
        TI-90: Make 'continue' accept a date range
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-12-07
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Fix filter for summary when only a date is given
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-12-09
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1936">
        TW-1936: Tweak tests to have fuller TAP compliance
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1938">
        TW-1938: Adjust behaviour of new-uuid and new-id verbosity levels
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-12-10
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-91">
        TI-91: Timewarrior does not compile on DragonFly
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-12-14
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-66">
        TI-66: Move with :adjust leaves overlapping intervals
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-12-19
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Fix number of expected tests
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-12-31
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Added Dragonfly support
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

