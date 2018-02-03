---
date: 2016-08-10
title: 'Activity Digest: July 2016'
aliases: ['/news/news.20160810.html']
---
<div class="col-md-8 main">
 <div class="row">
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in our projects. Here is what happened in
            July 2016.

            This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the git history of all
            the projects.
  </p>
  <div class="callout callout-info">
   <h4>
    Summary
   </h4>
   <p>
    July was spent mostly getting Timewarrior ready for beta.
   </p>
  </div>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2016-07-02
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-10">
        TI-10: The 'total' summands in the month report are not aligned with the column name
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-14">
        TI-14: Warn when new tags are being created
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-20">
        TI-20: Week number does not agree with Taskwarrior
       </a>
       fixed
      </li>
      <li>
       libshared: End of day is now
       <code>
        24:00:00
       </code>
       and not
       <code>
        23:59:59
       </code>
      </li>
      <li>
       libshared: Week start is Monday, per isO-8601
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-07-03
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-9">
        TI-9: Task spanning over whole day should show up as taking 24:00 instead of 23:59
       </a>
       fixed
      </li>
      <li>
       taskwarrior.org: The
       <a href="/tools/index.html">
        tools page
       </a>
       now shows Github star ratings
      </li>
      <li>
       Timewarrior: Added basic themes
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-07-04
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-12">
        TI-12: report command does not find extensions
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-22">
        TI-22: The 'day' chart crashes if there is an open interval and no others
       </a>
       fixed
      </li>
      <li>
       Timewarrior: Fixed bug with
       <code>
        :lastweek
       </code>
       ,
       <code>
        :lastmonth
       </code>
       ,
       <code>
        :lastquarter
       </code>
       and
       <code>
        :lastyear
       </code>
       hints
      </li>
      <li>
       Timewarrior: Added
       <code>
        merge
       </code>
       command
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-07-06
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-11">
        TI-11: Ids displayed incorrectly
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-17">
        TI-17: ids of tracked activities should not change when editing
       </a>
       fixed
      </li>
      <li>
       Timewarrior: Fixed UTF-8 encoding in Taskwarrior hook
      </li>
      <li>
       Timewarrior: Charts now always show the week number for the first line
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-07-09
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Most commands now support
       <code>
        :fill
       </code>
       hint, via validation
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-07-10
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Fixed errors
       <code>
        8am
       </code>
       and other informal time formats
      </li>
      <li>
       libshared: Fixed daylight savings adjustment error
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-07-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Added DOM access and
       <code>
        get
       </code>
       command
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-07-17
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Renamed
       <code>
        reports.&lt;type&gt;.style=compact
       </code>
       to
       <code>
        reports.&lt;type&gt;.axis=internal
       </code>
      </li>
      <li>
       Timewarrior: Detects when
       <code>
        @id
       </code>
       values are missing
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-07-18
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Fixed errors with
       <code>
        eocw
       </code>
       ,
       <code>
        sow
       </code>
       ,
       <code>
        eow
       </code>
       ,
       <code>
        soww
       </code>
       and
       <code>
        eoww
       </code>
      </li>
      <li>
       Timewarrior: New
       <code>
        delete
       </code>
       command
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-07-23
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: New extension script
       <code>
        totals.py
       </code>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-07-24
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Errors now yield a non-zero exit code
      </li>
      <li>
       Timewarrior: Now detects
       <code>
        @id
       </code>
       range errors
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-07-25
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior:
       <a href="/news/news.20160725.html">
        beta release
       </a>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-07-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: The
       <code>
        totals.py
       </code>
       extension now obeys color settings
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

