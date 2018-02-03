---
date: 2017-04-01
title: 'Activity Digest: March 2017'
aliases: ['/news/news.20170401.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: March 2017
   <small>
    2017-04-01
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in our projects. Here is what happened in
            March 2017.

            This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the git history of all
            the projects.
  </p>
  <div class="callout callout-info">
   <h4>
    Summary
   </h4>
   <p>
    Timewarrior bug fixes are bringing the 1.1.0 release closer. We
              are down to 7 open issues currently needing to be fixed.
   </p>
   <p>
    Taskwarrior is undergoing big changes to incorporate the new
              recurrence features. This leads to instability, so if anyone is
              using the 2.6.0 development branch, this would be a good time to
              stop.
   </p>
   <p>
    The Taskwarrior 2.6.0 branch has a
    <code>
     stable
    </code>
    tag which
              indicates the last commit where all tests passed on all platforms.
   </p>
   <p>
    The libshared project got a major update to the date and duration
              handling features, fixing bugs and providing a consistent
              implementation for Taskwarrior and Timewarrior to use.
   </p>
  </div>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2017-03-02
     </small>
    </td>
    <td>
     <ul>
      <li>
       Flod: Now generates a project summary page listing latest status of all projects
      </li>
      <li>
       Task: Properly captures
       <code>
        errno
       </code>
       in CmdEdit
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-03-04
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Datetime now properly resets state after certain failed parse attempts
      </li>
      <li>
       Task: Nibbler eliminated
      </li>
      <li>
       Task: ISO8601d and ISO8601p eliminated
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-03-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Eliminated separate handling for named dates, now relying on libshared
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-03-06
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Fixed Datetime bugs in
       <code>
        eonm
       </code>
       ,
       <code>
        sopww
       </code>
       ,
       <code>
        som
       </code>
       , and
       <code>
        sow
       </code>
       calculations
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-03-07
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Datetime now supports abbreviated forms
       <code>
        {s,e}o{p,n,}{d,w,ww,m,q,y}
       </code>
      </li>
      <li>
       libshared: Taskwarrior and Timewarrior now have identical Datetime support, so that
       <code>
        9am
       </code>
       no longer means same day or next day
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-03-09
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-29">
        TI-29: Fix issue "timew config can't add new value"
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-03-14
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Pig can now skip over partial phrases
      </li>
      <li>
       libshared: ::matchLength can determine common root string lengths
      </li>
      <li>
       libshared: Inherited Taskwarrior's
       <code>
        lex
       </code>
       utility for parsing tests
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-03-15
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Duration now accepts
       <code>
        0
       </code>
       as valid again
      </li>
      <li>
       libshared: Configuration now properly captures original file name
      </li>
      <li>
       libshared: Durations like
       <code>
        1wk
       </code>
       now perform negative lookahead to avoid cases where a duration is found embedded in a larger context
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-03-19
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Added negative lookahead for day and month names so that the 'mon' in 'money' does not mean 'monday' because of the subsequent characters
      </li>
      <li>
       libshared: Ambiguous Datetime forms (
       <code>
        YYYYMMDD
       </code>
       ,
       <code>
        YYYYMM
       </code>
       ,
       <code>
        YYYY
       </code>
       ,
       <code>
        HHMMSS
       </code>
       and
       <code>
        HHMM
       </code>
       ) can now be disabled
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-32">
        TI-32: taskwarrior hook script doesn't stop recording waiting task
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-43">
        TI-43: :lastweek on sunday
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-03-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-67">
        TI-67: Assign ids to intervals after flattening but before filtering
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-03-23
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Table can now shut of word-wrapping for columns
      </li>
      <li>
       libshared: Fixed bug in Table that included color codes in length calculations
      </li>
      <li>
       Task: The
       <code>
        CHILD
       </code>
       ,
       <code>
        PARENT
       </code>
       ,
       <code>
        INSTANCE
       </code>
       , and
       <code>
        TEMPLATE
       </code>
       virtual tags are now backward/forward compatible
      </li>
      <li>
       Task: Finally fixed some TZ-dependent tests that fail when the clocks change
      </li>
      <li>
       Task: Fixed problems with the
       <code>
        history
       </code>
       ,
       <code>
        ghistory
       </code>
       and
       <code>
        summary
       </code>
       reports rendering incorrectly
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2017-03-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1903">
        TW-1903: grammar error -- There are 1 local changes
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

