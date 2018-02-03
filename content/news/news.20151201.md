---
date: 2015-12-01
title: 'Activity Digest: November 2015'
aliases: ['/news/news.20151201.html']
---
<div class="col-md-8 main">
 <div class="row">
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in the Taskwarrior project. Here is what
            happened in November 2015.
  </p>
  <p>
   This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the
   <a href="https://git.tasktools.org/projects/TM/repos/task/commits?until=refs%2Fheads%2F2.4.5">
    full Git history
   </a>
   .
  </p>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2015-11-01
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Migrated code from using C-style string formatting to C++11-style.
      </li>
      <li>
       Task: Began resolving
       <a href="https://github.com/L2Program/FlintPlusPlus">
        Flint++
       </a>
       issues.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-02
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Significant performance enhancements (~45-55%) in string colorization.
      </li>
      <li>
       Task: Many C++11 changes reverted because it was discovered that Cygwin doesn't support several C++11 features with GCC 4.9
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-03
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Performance enhancements (~3%) in JSON composition.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-04
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Performance enhancements (~1-3%) in ID/UUID lookups.
      </li>
      <li>
       Task: Performance enhancements (~7-12%) by changing Task inheritance and enabling move semantics
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-06
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Fixed broken build for older GCC on Cygwin
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-07
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-38">
        TW-38: Dates in the far future give bad estimates in burndown
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-311">
        TW-311: Estimated completion in burndown.daily shows impossible results
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1313">
        TW-1313: some recurring intervals reset due time to midnight
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1446">
        TW-1446: Difference in how relative dates are specified in report filters since 2.3.0
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       Taskd: Inherited code fixes and enhancements from Taskwarrior codebase
      </li>
      <li>
       Task: Performance enhancements (~4-21%) gained from rRelocating TDB2::gc to TDB2::load_tasks almost eliminates GC processing times, reducing them by ~96%
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-106">
        TD-106: The recurrence value '2m' is not valid
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-10
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1582">
        TW-1582: Wrong urgency for first report after reviving task
       </a>
       fixed
      </li>
      <li>
       Task: Performance enhancements (minimal) made by reordering date parsing formats, most common first
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Performance enhancements (9-45%) with file writes on high-latency systems
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-12
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Performance enhancements (~20%) for data load by improving the quoted string parsing
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-15
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Added missing colors from some themes
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1723">
        TW-1723: task info causes segfault
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1724">
        TW-1724: some commands show color codes when redirected
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1500">
        TW-1500: Dates formatted as ".age", ".remaining", or ".countdown" often give blank results
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-17
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Fixed a race condition in the test suite that caused odd test failure counts
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1425">
        TW-1425: The 'age' format rounds in odd ways
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1481">
        TW-1481: Unable to assign a completed task as dependency
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-18
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1658">
        TW-1658: rc override to non-existent alternate rc quietly uses default
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Performance enhancements (~2%) to JSON encoding, using lookup table
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-11-24
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Performance enhancements by reducing string copies un
       <code>
        journal.info
       </code>
       lookups in
       <code>
        undo.data
       </code>
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1729">
        TW-1729: zsh completion: zregexparse:4: not enough regex argument
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

