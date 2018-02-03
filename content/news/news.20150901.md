---
date: 2015-09-01
title: 'Activity Digest: August 2015'
aliases: ['/news/news.20150901.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: August 2015
   <small>
    2015-09-01
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in the Taskwarrior project. Here is what
            happened in August 2015.
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
      2015-08-01
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Commands now have 'DNA', which determines how they behave, and allows more control than simply distinguishing between
       <code>
        read-only
       </code>
       and
       <code>
        write
       </code>
       commands.
      </li>
      <li>
       Task: An ISO year is now valid beyond 2100.
      </li>
      <li>
       Task: The new 'commands' command shows information about how the commands behave.  For debugging.
      </li>
      <li>
       Task: Documentation now indicates the replacement for
       <code>
        report.X.annotations
       </code>
       .
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-02
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Context filters now applied only when a command requests it.
      </li>
      <li>
       Task: Time-sensitive, floating point representation-sensitive, and color-sensitive unit tests fixed, which yields more consistent results.
      </li>
      <li>
       Task: When applying additional filters, the insertion occurs at the beginning, thus avoiding any
       <code>
        --
       </code>
       arguments.
      </li>
      <li>
       Task: GC now only run when a command requests it.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-03
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task:
       <code>
        rc.debug=1
       </code>
       now shows the parse tree, before command-specific processing.
      </li>
      <li>
       Task: Clarified DOM responses - it is an error to specify no reference, or a bad reference. It is not an error to specify a reference that yields no value.
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1629">
        TW-1629: Descriptions often get overwritten with "( or )"
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-04
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Man pages updated to cover the inequality operators.
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1648">
        TW-1648: Typo in Documentation
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1647">
        TW-1647: descriptions that are stringified ids
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1344">
        TW-1344: Filter due:yyyy-mm-dd is failing to display daily recurring tasks if there is deleted task in the series
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1496">
        TW-1496: Translation manuals are outdated/mis information
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1499">
        TW-1499: Invalid due date produces jump to begining of the unix epoch
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1537">
        TW-1537: soww Synonym produces wrong date
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1593">
        TW-1593: context and description substring
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1594">
        TW-1594: Filter "due.before" with relative dates stopped working
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1598">
        TW-1598: (Bulk) modification of tasks unintentionally overwrites description if a context is active
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1607">
        TW-1607: Theme Support for missing UDAs
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1611">
        TW-1611: soww weirdness
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1624">
        TW-1624: Report filters combine incorrectly with command line with terminator.
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1630">
        TW-1630: "Due" parsing behavior seems inconsistent
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1643">
        TW-1643: Batch modifying tasks under context sets description to '( )'
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-06
     </small>
    </td>
    <td>
     <ul>
      <li>
       TaskServer: The
       <code>
        diagnostics
       </code>
       commands now shows certificate file sizes.
      </li>
      <li>
       Task: The
       <code>
        diagnostics
       </code>
       commands now shows certificate file sizes.
      </li>
      <li>
       Task: Displays UUID instead of ID when completing a task.
      </li>
      <li>
       Task: Documented that comma-separated UUIDs are not supported, and comma-separated IDs are deprecated.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-07
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Documented the
       <code>
        !
       </code>
       negation operator.
      </li>
      <li>
       Task:
       <code>
        rc.sugar
       </code>
       enables/disables syntactic sugar for IDs and UUIDs only.
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1651">
        TW-1651: Provide opt-out of filter parser's id treatment
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1652">
        TW-1652: task rm misparsed
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1636">
        TW-1636: UUID with numeric-only first segment is not parsed properly
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-09
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: UUID is now validated on import.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-263">
        TW-263: Unexpected zsh autocomplete behaviour
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-12
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Merged Duration and ISO8601p objects. All durations are now ISO-centric.
      </li>
      <li>
       Task: Improved documentation in sample hook script.
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1653">
        TW-1653: info report regression; shouldn't be context sensitive
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-14
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Configuration: 'search.case.sensitive' now defaults to 'yes' on Cygwin
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1655">
        TW-1655: Inform "No changes made." when quitting early due to signal
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-17
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: The
       <code>
        is
       </code>
       and
       <code>
        isnt
       </code>
       attribute modifiers are now exact/inexact operators.
      </li>
      <li>
       Task: Improved documentation for attribute modifiers in the
       <code>
        help
       </code>
       command.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1666">
        TW-1666: import should reject invalid data
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-23
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: New
       <code>
        recur
       </code>
       verbosity token.
      </li>
      <li>
       Task: New
       <code>
        unwait
       </code>
       verbosity token.
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1664">
        TW-1664: Notify of waiting→pending promotion
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-27
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1670">
        TW-1670: Reversed ranges are parsed as a mathematician would expect
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1671">
        TW-1671 task add: segfault with foo-bar:1
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1675">
        TW-1675: project.not:something doesn't exclude project:something.subprojects
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-28
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task:
       <code>
        rc.report.&lt;name&gt;.sort:none
       </code>
       now performs no sorting, and retains the order of all UUID values specified.
      </li>
      <li>
       Task: the
       <code>
        columns
       </code>
       report gained a 'type' field.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-29
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: The
       <code>
        commands
       </code>
       report gained a 'description' field.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: The
       <code>
        TASKDATA
       </code>
       environment variable is now mandatory in Bash tests.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-08-31
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: The
       <code>
        LATEST
       </code>
       virtual tag indicates the most recently added task.
      </li>
      <li>
       Task: The
       <code>
        PROJECT
       </code>
       virtual tag indicates that a project is assigned.
      </li>
      <li>
       Task: The
       <code>
        PRIORITY
       </code>
       virtual tag indicates that a priority is assigned.
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

