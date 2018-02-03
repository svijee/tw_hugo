---
date: 2015-10-01
title: 'Activity Digest: September 2015'
aliases: ['/news/news.20151001.html']
---
<div class="col-md-8 main">
 <div class="row">
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in the Taskwarrior project. Here is what
            happened in September 2015.
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
      2015-09-01
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Added
       <code>
        rc.rules.color.merge
       </code>
       to control whether combined colors are merged (default) or overwritten.  This prevents some unusable color combinations.
      </li>
      <li>
       Task: Replaced
       <code>
        rc.urgency.next.coefficient
       </code>
       with
       <code>
        rc.urgency.user.tag.next.coefficient
       </code>
       .
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1375">
        TW-1375: Use of ^ in regex parsed as exponentiate operator
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1448">
        TW-1448: Add possibility to modify newest task
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1616">
        TW-1616: Intermittent lengthy delay when starting or completing a task
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1660">
        TW-1660: Disabled sorting option
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-03
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Removed colors that use underscores (
       <code>
        on_blue
       </code>
       ), a feature deprecated in 2009.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-04
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Added first man page references which are deliberately minimal, and refer to online resources.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Some unit tests were changed from being disabled to enabled and marked as 'exected to fail'. This means the test are now run, instead of ignored.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-06
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: If not explicitly stated on import, values with default dynamic values (such as modified, entry or end) can produce a false notion of incoming 'modified' data, where the only difference between the data in the database and data being imported is that the dynamic defaults differ, which are now ignored.
      </li>
      <li>
       Task: Not all commands were obeying the
       <code>
        rc.color
       </code>
       settng.
      </li>
      <li>
       Task: The command line parser can now detect cases where unwanted arguments are provided on the command line.
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1687">
        TW-1687: task add due:som appears to be interpreted as 'someday'
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-07
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task:
       <code>
        rc.debug.parser=2
       </code>
       now shows the full parse tree, whereas
       <code>
        rc.debug.parser=3
       </code>
       shows eval processing.
      </li>
      <li>
       Task: The
       <code>
        2.4.5
       </code>
       development branch is renamed to
       <code>
        2.5.0
       </code>
       , reflecting the scope of the work.
      </li>
      <li>
       Task: 2.5.0 beta1 released.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: All date attributes now have the same sorting behavior as
       <code>
        due
       </code>
       dates.
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1684">
        TW-1684 make no-date &gt; has-date for all date attributes
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-09
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1678">
        TW-1678: segfault in ~ViewTask()
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-10
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Removed the ability to build without color support.
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1683">
        TW-1683 Dom reference for project not properly evaluated
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: The test suite exits with non-zero when any test fails.
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-46">
        TW-46: Circular dependency detection broken for missing tasks
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1688">
        TW-1688: task fails to import
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-12
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: The
       <code>
        limit:N
       </code>
       feature is no longer a pseudo-attribute (there are no others), but is syntactic sugar that maps to
       <code>
        rc.limit:N
       </code>
       .
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1656">
        TW-1656: Implicitly parenthesize argv filter
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1692">
        TW-1692: 42//' segfaults
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-13
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1686">
        TW-1686: Sorting not working on udas
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-15
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Data copying inefficiencies are fixed, yielding a dramatic improvement to
       <code>
        import
       </code>
       speed.
      </li>
      <li>
       Task: Updated Unicode charcter list.
      </li>
      <li>
       Task: Performance testing improved (http://tasktools.org/projects/performance.html).
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: 2.5.0 beta2 released.
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1695">
        TW-1695: edit: Concurrent edits
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-19
     </small>
    </td>
    <td>
     <ul>
      <li>
       Vramsteg: Added 64-bit min/max/value support.
      </li>
      <li>
       Task: When GC is turned off, disable the query shortcuts, which do not apply.
      </li>
      <li>
       Task: Holiday files updated.
      </li>
      <li>
       Task: The
       <code>
        filter
       </code>
       verbosity token was lost in the CLI2 upgrade.
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1699">
        TW-1699: Command interpretation displayed incorrectly
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1701">
        TW-1701: Some generated UUIDs deemed invalid
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-20
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: The
       <code>
        new-uuid
       </code>
       verbosity token is deprecated.
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1662">
        TW-1662: filter before add becomes description
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-21
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1700">
        TW-1700: modify tags behavior changed
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: The
       <code>
        export
       </code>
       command no longer obeys context.
      </li>
      <li>
       Task: TDB2 Task lookup code improvements yields another significant
       <code>
        import
       </code>
       speedup.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-24
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1707">
        TW-1707: Context can leak into modifications
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-25
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Fixed segfault problem on exit.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-09-26
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="/news/news.20150926.html">
        Vramsteg: 1.1.0 released
       </a>
       .
      </li>
      <li>
       <a href="/news/news.20150927.html">
        Clog: 1.2.0 released
       </a>
       .
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

