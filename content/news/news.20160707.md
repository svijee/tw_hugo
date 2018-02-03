---
date: 2016-07-07
title: 'Activity Digest: June 2016'
aliases: ['/news/news.20160707.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: June 2016
   <small>
    2016-07-07
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in our projects. Here is what happened in
            June 2016.

            This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the git history of all
            the projects.
  </p>
  <div class="callout callout-info">
   <h4>
    Summary
   </h4>
   <p>
    The main focus for June is getting
    <a href="/docs/timewarrior/index.html">
     Timewarrior
    </a>
    ready for an alpha, and subsequent beta release. The purpose of an alpha release is to
              gather feedback that guides the subsequent beta release. Timewarrior
              is a new project that introduces new concepts. This new functionality
              needs to be refined before a beta release.
   </p>
   <p>
    The
    <a href="https://bug.tasktools.org/browse/TI">
     Timewarrior bug tracker
    </a>
    is now open for business.
   </p>
   <p>
    Although comparatively minor,
    <a href="/news/news.20160627.html">
     Clog 1.3.0
    </a>
    was released.
   </p>
  </div>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2016-06-01
     </small>
    </td>
    <td>
     <ul>
      <li>
       Flod: Removed glyphs from tinderbox report, for a more compact appearance
      </li>
      <li>
       Timewarrior: Learned the new
       <code>
        :ids
       </code>
       hint
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-04
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Learned how to
       <code>
        tag
       </code>
       an interval
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Learned how to
       <code>
        shorten
       </code>
       an interval
      </li>
      <li>
       Timewarrior: Learned how to
       <code>
        untag
       </code>
       an interval
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-06
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-4">
        TI-4: The 'timew' command considers only the last interval
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-5">
        TI-5: Unicode tags not working
       </a>
       fixed
      </li>
      <li>
       libshared: Fixed date bug with quarter calculations
      </li>
      <li>
       Timewarrior: Learned how to
       <code>
        lengthen
       </code>
       an interval
      </li>
      <li>
       Timewarrior: Learned the
       <code>
        :lastyear
       </code>
       ,
       <code>
        :lastquarter
       </code>
       and
       <code>
        :lastmonth
       </code>
       hints
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-07
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Supports
       <code>
        theme.colors.debug
       </code>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-6">
        TI-6: Exception after shortening task
       </a>
       fixed
      </li>
      <li>
       Timewarrior: Learned how to
       <code>
        move
       </code>
       an interval
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-10
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Learned how to
       <code>
        split
       </code>
       intervals apart
      </li>
      <li>
       Timewarrior: Added fully detailed help for dates and durations
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Charts now support the
       <code>
        :ids
       </code>
       hint
      </li>
      <li>
       Timewarrior: Commands now obey the
       <code>
        :quiet
       </code>
       hint
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-12
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-61">
        TW-61: Extract only tasks with annotations
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1813">
        TW-1813: Range filter doesn't work
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-3">
        TI-3: The month report shows multi-days current task truncated
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-8">
        TI-8: Only the day's last interval is considered in the month report
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-13
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-7">
        TI-7: Stop command shouldn't interrupt unrelated tags
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-14
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1820">
        TW-1820: Install with -DLANGUAGE=2 flag not work
       </a>
       fixed
      </li>
      <li>
       Task: Corrected L10N strings that were breaking the spa-ESP build
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-15
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-120">
        TD-120: Missing cmakedefine for HAVE_GET_CURRENT_DIR_NAME
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskserver: Now finds the threads lib
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-18
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Integrated list templates from Taskwarrior
      </li>
      <li>
       Timewarrior: Learned how to
       <code>
        join
       </code>
       intervals together
      </li>
      <li>
       Timewarrior: Themes and holidays are now installed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-20
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-121">
        TD-121: Log time in user's specified timezone
       </a>
       fixed
      </li>
      <li>
       Timewarrior
       <a href="/news/news.20160620.html">
        Timewarrior 0.9.5 alpha
       </a>
       released
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Fixed missing file install bug
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-23
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/CL-10">
        CL-10: The suppress context doesn't suppress the newline character
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-24
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/CL-12">
        CL-12: Overlapping rules are not respected
       </a>
       fixed
      </li>
      <li>
       Clog: Test suite converted to Python
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-25
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-119">
        TD-119: Build fails on Debian (no C++11 support)
       </a>
       fixed
      </li>
      <li>
       Clog: Man pages significantly updated
      </li>
      <li>
       libshared: Inherited JSON tests from Taskwarrior
      </li>
      <li>
       libshared: Integrated Lexer from Timewarrior
      </li>
      <li>
       Task: Began integration of libshared
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-26
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskserver: Integrated libshared
      </li>
      <li>
       Taskwarrior.org: Added all
       <a href="/docs/timewarrior">
        Timewarrior docs
       </a>
      </li>
      <li>
       Taskwarrior.org: Added all
       <a href="/docs/clog">
        Clog docs
       </a>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-27
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/CL-3">
        CL-3: clog; nested include files
       </a>
       fixed
      </li>
      <li>
       Clog: Test suite grew to include rules parsing tests
      </li>
      <li>
       <a href="/news/news.20160627.html">
        Clog: 1.3.0 released
       </a>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-28
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TI-16">
        TI-16: Should handle case where taskwarrior hook is used before timew
       </a>
       fixed
      </li>
      <li>
       Timewarrior: The
       <code>
        rc.reports.&lt;type&gt;.totals
       </code>
       now controls the 'Totals' label
      </li>
      <li>
       Timewarrior: Fixed out of source builds
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-06-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Supports
       <code>
        rc.reports.&lt;type&gt;.cell
       </code>
       to limit chart width
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

