---
date: 2016-03-01
title: Activity Digest: February 2016
aliases: ['/news/news.20160301.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: February 2016
   <small>
    2016-03-01
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in the Taskwarrior project. Here is what
            happened in February 2016.
  </p>
  <p>
   This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the
   <a href="https://git.tasktools.org/projects/TM/repos/task/commits?until=refs%2Fheads%2F2.5.1">
    full Git history
   </a>
   .
  </p>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2016-02-01
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-188">
        TW-188: short help text
       </a>
       fixed
      </li>
      <li>
       task: Attribute modification delegated to tpye-specific objects
      </li>
      <li>
       task: UDA definitions made more robust
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-02
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1697">
        TW-1697: Inconsistent failure mode on invalid task id
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1710">
        TW-1710: Setting wait date on status:completed / status:deleted
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1754">
        TW-1754: '\' at end of description in 'task edit' merges task with following task
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1763">
        TW-1763: Removing the due date of a task with no due date modifies the task
       </a>
       fixed
      </li>
      <li>
       task: Various attribute accessors were autovivifying, only to have the attribute removed later, which is silly
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-03
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: FS gained automatic BOM-removal logic
      </li>
      <li>
       task: Assorted C++11-isms embraced
      </li>
      <li>
       task: DOM Object demoted to functions
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       task: 2.5.1 beta1 released
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-06
     </small>
    </td>
    <td>
     <ul>
      <li>
       anomaly: Test scripts copied to build dir
      </li>
      <li>
       clog: Test scripts copied to build dir
      </li>
      <li>
       clog: Fixed broken
       <code>
        run_all
       </code>
       script
      </li>
      <li>
       flod2: Test scripts copied to build dir
      </li>
      <li>
       flod2: Fixed broken
       <code>
        run_all
       </code>
       script
      </li>
      <li>
       libshared: Fixed broken
       <code>
        run_all
       </code>
       script
      </li>
      <li>
       taskd: Fixed broken
       <code>
        run_all
       </code>
       script
      </li>
      <li>
       tasksh: Fixed broken
       <code>
        run_all
       </code>
       script
      </li>
      <li>
       timew: Fixed broken
       <code>
        run_all
       </code>
       script
      </li>
      <li>
       vitapi: Fixed broken
       <code>
        run_all
       </code>
       script
      </li>
      <li>
       vramsteg: Fixed broken
       <code>
        run_all
       </code>
       script
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-07
     </small>
    </td>
    <td>
     <ul>
      <li>
       Holidata.net: Added
       <code>
        sk-SK
       </code>
       locale
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1768">
        TW-1768: Task sync failed: "Either your credentials are incorrect, or your account doesn't exist on the Taskserver."
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-13
     </small>
    </td>
    <td>
     <ul>
      <li>
       task: Some dates were being parsed twice
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-14
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: ISO8601 date handling now integrated and decoupled as Datetime
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: ISO8601 duration handling now integrated and decoupled as Duration
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-20
     </small>
    </td>
    <td>
     <ul>
      <li>
       task: Dev meetup in NYC - liquids consumed
      </li>
      <li>
       taskd: Inherited fixes and performance improvements from Taskwarrior
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-21
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-104">
        TD-104: Unrecognized taskwarrior file format
       </a>
       fixed
      </li>
      <li>
       taskd: Updated demo scripts
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       task: Removed circularity checking on
       <code>
        add
       </code>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-23
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1709">
        TW-1709: Parsing bug when doing "task undo"
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1773">
        TW-1773: one task eaten all my RAM
       </a>
       fixed
      </li>
      <li>
       task: Found that tag attribute column width was never actually calculated
      </li>
      <li>
       task: Found that line hyphenation has been broken for a long time
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-24
     </small>
    </td>
    <td>
     <ul>
      <li>
       task:
       <a href="/news/news.20160224.html">
        2.5.1 released
       </a>
       which focused entirely on bug fixes and performance
      </li>
      <li>
       task: 2.6.0 development begins, intending to greatly improve recurrence
      </li>
      <li>
       task: Removed deprecated
       <code>
        alias._query
       </code>
       default
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-25
     </small>
    </td>
    <td>
     <ul>
      <li>
       task: Eliminated
       <code>
        sprintf
       </code>
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-02-28
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-64">
        TD-64: sync conflict deleted all annotations of the task
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1741">
        TW-1741: Warning "ignoring return value of ‘int ftruncate" while doing make on xubuntu15.10
       </a>
       fixed
      </li>
      <li>
       taskd: Updated expired test certs
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

