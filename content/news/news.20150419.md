---
date: 2015-04-19
title: Taskwarrior 2.4.3 Released
aliases: ['/news/news.20150419.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Taskwarrior 2.4.3 Released
   <small>
    2015-04-19
   </small>
  </h3>
  <p>
   User Defined Attributes (
   <a href="/docs/udas.html">
    UDAs
   </a>
   ) have
            been enhanced so that type
   <code>
    string
   </code>
   attributes may now
            designate the sort order of allowed values.  This enhancement permits
            the migration of the
   <code>
    priority
   </code>
   attribute to a UDA.
            This means you may now define your own priority levels, sorting and
            urgency coefficients.
  </p>
  <p>
   Although it may appear otherwise, there is no new monthly release cycle,
            it's all a coincidence.  The next release will likely take a little
            longer as we shift focus to Taskserver improvements.
  </p>
  <p>
   Although this is a minor release, there are significant bug fixes
            and new features make this a recommended upgrade.  Changes include:
  </p>
  <p>
   <ul>
    <li>
     <a href="/docs/design/hooks2.html">
      Hooks API v2
     </a>
     , which is backwards compatible with v1. This allows hooks to be more aware of the context in which they are run.
    </li>
    <li>
     Default values no longer are applied to recurring tasks.
    </li>
    <li>
     Default values no longer are applied to synced tasks.
    </li>
    <li>
     UDA sorting order can be defined.
    </li>
    <li>
     Priority attribute gone, replaced by a default UDA configuration.
    </li>
    <li>
     Command line lexer bugs fixed, which caused a hang.
    </li>
    <li>
     Urgency improvements for tasks with dependencies, which were repoting bad values.
    </li>
    <li>
     The
     <code>
      isnt
     </code>
     and
     <code>
      not
     </code>
     attribute modifiers were mapped to hte wrong operator.
    </li>
    <li>
     Invalid IDs were displayed after a
     <code>
      done
     </code>
     or
     <code>
      delete
     </code>
     command.
    </li>
    <li>
     Example export scripts have been updated so they work again.
    </li>
    <li>
     The
     <code>
      summary
     </code>
     report can now be configured to show old projects, not just current ones.
    </li>
    <li>
     The
     <code>
      info
     </code>
     report failed to show negative urgency values.
    </li>
    <li>
     Added a new
     <code>
      rc.bulk
     </code>
     value (0) that is interpreted as infinity.
    </li>
    <li>
     Minor command line parser improvements.
    </li>
    <li>
     Minor command performance improvements.
    </li>
    <li>
     Documentation improvements.
    </li>
    <li>
     Several bug fixes.
    </li>
   </ul>
   For full details, see the ChangeLog file included in the release.
  </p>
  <p>
   The release is immediately available as a source
   <a href="/download/task-latest.tar.gz">
    tarball
   </a>
   .
            Binary packages will soon be available via your Operating System's
            package manager.
  </p>
 </div>
</div>

