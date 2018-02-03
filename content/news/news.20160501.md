---
date: 2016-05-01
title: 'Activity Digest: April 2016'
aliases: ['/news/news.20160501.html']
---
<div class="col-md-8 main">
 <div class="row">
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in the Taskwarrior project. Here is what
            happened in April 2016.
  </p>
  <p>
   This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the git history of all
            the projects.
  </p>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2016-04-01
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1789">
        Support additional countable infinities
       </a>
       reported
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1790">
        Urgency computations involving NaN are incorrect
       </a>
       reported
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-02
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1791">
        TW-1791: taskrc(5) manpage: spurious "pri." in rule.precedence.color
       </a>
       fixed
      </li>
      <li>
       libshared: Added support for informal time:
       <code>
        8am
       </code>
       ,
       <code>
        2:34pm
       </code>
       ...
      </li>
      <li>
       taskwarrior.org: Compressed all the images on the site.
      </li>
      <li>
       taskwarrior.org: Replaced email addresses with mailing lists.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-03
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1792">
        TW-1792: The info command uses '0' to reference dependencies on non-pending tasks
       </a>
       fixed
      </li>
      <li>
       Task: When a task ID is not available, a UUID is now used instead.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-04
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Added JSON2 SAX parser.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-05
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Learns the
       <code>
        :quiet
       </code>
       hint.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-08
     </small>
    </td>
    <td>
     <ul>
      <li>
       Guides: Added OpenRheinRuhr presentation.
      </li>
      <li>
       Task: Runs under the Windows 10 Linux Subsystem.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-09
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-40">
        TD-40: Remove user command says user does not exist
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-102">
        TD-102: After creating a user aparently successful taskd says: User does not exists
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-117">
        TD-117: Wrong systemd target, taskd can fail if multi-user.target is up earlier than the network
       </a>
       fixed
      </li>
      <li>
       Task: Now uses the CMake CXXSniffer code.
      </li>
      <li>
       Taskd: Now uses the CMake CXXSniffer code.
      </li>
      <li>
       Taskd: Now builds all source as a temp library against which to link tests, for faster builds.
      </li>
      <li>
       Timewarrior: Learned to parse it's own command line.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-10
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Gains an extension API.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Added support for
       <code>
        socq
       </code>
       ,
       <code>
        eocq
       </code>
       ,
       <code>
        socy
       </code>
       and
       <code>
        eocy
       </code>
       .
      </li>
      <li>
       libshared: Removed Datetime abbreviations for some dates, i.e.
       <code>
        socm
       </code>
       ,
       <code>
        socy
       </code>
       .
      </li>
      <li>
       Timewarrior: Gains a
       <code>
        continue
       </code>
       command.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-13
     </small>
    </td>
    <td>
     <ul>
      <li>
       Guides: Added FOSS-GBG presentation.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-15
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1795">
        TW-1795: Calendar underline on Day padding
       </a>
       fixed
      </li>
      <li>
       libshared: Datetime can now work in look-forward or look-behind mode, i.e. what does
       <code>
        Monday
       </code>
       mean?
      </li>
      <li>
       libshared: Datetime disambiguated
       <code>
        som
       </code>
       from
       <code>
        someday
       </code>
       .
      </li>
      <li>
       Task: Removed a broken flapping test.
      </li>
      <li>
       Timewarrior: Defined what a filter is, and it's very simple.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-16
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-118">
        TD-118: Shebang issue
       </a>
       fixed
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-17
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Data access resolved down to
       <code>
        addInterval
       </code>
       and
       <code>
        deleteInterval
       </code>
       . Simple.
      </li>
      <li>
       Timewarrior: Properly handles intervals that span data files.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-18
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Learned that
       <code>
        day on
       </code>
       and
       <code>
        day off
       </code>
       are just holiday overrides.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-20
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared:
       <code>
        Pig::getHMS
       </code>
       can now read formally-specified time.
      </li>
      <li>
       Timewarrior: Learned how expand weekday exclusions into a set of date ranges.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-21
     </small>
    </td>
    <td>
     <ul>
      <li>
       Guides: Taskserver setup PDF completed.
      </li>
      <li>
       Timewarrior: Gained holiday file support.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Expanded set of report mockups for feedback.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-23
     </small>
    </td>
    <td>
     <ul>
      <li>
       Clog: Migrated to use libshared, updated thecode base for C++11.
      </li>
      <li>
       Flod2: Typo in build system linked to missing library that wasn't used.
      </li>
      <li>
       libshared: Color can now emit raw codes.
      </li>
      <li>
       Timewarrior:
       <code>
        diagnostics
       </code>
       now references the theme and shows swatches.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-24
     </small>
    </td>
    <td>
     <ul>
      <li>
       Flod: Learned how to clone and switch branches in one step.
      </li>
      <li>
       libshared: Switched all date arguments order to
       <code>
        Y
       </code>
       ,
       <code>
        M
       </code>
       ,
       <code>
        D
       </code>
       . The original US order of
       <code>
        M
       </code>
       ,
       <code>
        D
       </code>
       ,
       <code>
        Y
       </code>
       has caused unending confusion.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-25
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Added
       <code>
        Composite
       </code>
       object from Timewarrior.
      </li>
      <li>
       Timewarrior: Now has a default color palette, which is overridden by themes.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-28
     </small>
    </td>
    <td>
     <ul>
      <li>
       Task: Fixed ambiguity in the spa-ESP localization for the
       <code>
        yes/no/all/cancel
       </code>
       string.
      </li>
      <li>
       Timewarrior: The
       <code>
        track
       </code>
       ,
       <code>
        stop
       </code>
       and
       <code>
        start
       </code>
       commands now properly split intervals that cross boundaries.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-29
     </small>
    </td>
    <td>
     <ul>
      <li>
       Timewarrior: Gains a
       <code>
        cancel
       </code>
       command.
      </li>
      <li>
       Timewarrior: Gains a
       <code>
        day
       </code>
       report.
      </li>
      <li>
       Timewarrior: Each report now has a configuration rule.
      </li>
      <li>
       Timewarrior: The
       <code>
        day
       </code>
       report now renders in different experimental styles.
      </li>
      <li>
       Timewarrior: Gained bash unit test capability from Taskwarrior.
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-04-30
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Added
       <code>
        Palette
       </code>
       object from Timewarrior.
      </li>
      <li>
       Timewarrior: Gains a
       <code>
        summary
       </code>
       report.
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

