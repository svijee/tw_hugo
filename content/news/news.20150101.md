---
date: 2015-01-01
title: Taskwarrior 2.4.0 Released
aliases: ['/news/news.20150101.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Taskwarrior 2.4.0 Released
   <small>
    2015-01-01
   </small>
  </h3>
  <p>
   Taskwarrior 2.4.0 is released, it's a major release, and a
            recommended upgrade. Happy new year.
  </p>
  <p>
   After almost a year of development, 108 bug fixes, 47 new/improved
            features, 1,750 code changes and over 50 community-provided patches,
            version 2.4.0 represents a significant improvement to task list
            management. Changes include:
  </p>
  <p>
   <ul>
    <li>
     New localization: Portuguese and Esperanto translations
    </li>
    <li>
     New
     <code>
      dateformat
     </code>
     space handling
    </li>
    <li>
     New date support: 'february', extensive support for ISO-8601
    </li>
    <li>
     New column formats:
     <code>
      description.truncated_count
     </code>
     ,
     <code>
      uda.NAME.indicator
     </code>
     ,
     <code>
      recur.short
     </code>
     , tag sorting
    </li>
    <li>
     New color rules:
     <code>
      color.uda.NAME.VALUE
     </code>
     ,
     <code>
      color.label.sort
     </code>
     ,
     <code>
      color.until
     </code>
    </li>
    <li>
     New virtual tags: READY, YESTERDAY, TOMORROW, PENDING, DELETED, COMPLETED, TAGGED
    </li>
    <li>
     New verbosity tokens:
     <code>
      new-uuid
     </code>
    </li>
    <li>
     New command:
     <code>
      calc
     </code>
     ,
     <code>
      _zshattributes
     </code>
    </li>
    <li>
     New theme: dark-gray-blue­256.theme
    </li>
    <li>
     New report feature: listing breaks
    </li>
    <li>
     New Python testing framework for higher-level testing
    </li>
    <li>
     New DOM support:
     <code>
      ID.annotation.0.description
     </code>
     ,
     <code>
      ID.due.month
     </code>
     ...
    </li>
    <li>
     New Hooks support:
     <code>
      on-add
     </code>
     ,
     <code>
      on-modify
     </code>
     ,
     <code>
      on-launch
     </code>
     and
     <code>
      on-exit
     </code>
     event hook support
    </li>
    <li>
     New Regular Expression support enabled by default
    </li>
    <li>
     New algebraic expression support: date math, fuzzy matches
    </li>
    <li>
     Improved command line: handling of quoted and escaped content, partial UUIDs, searching all attributes, projects with spaces
    </li>
    <li>
     Improved utilities:
     <code>
      l10n
     </code>
    </li>
    <li>
     Improved
     <code>
      show
     </code>
     command: displays default settings
    </li>
    <li>
     Improved
     <code>
      information
     </code>
     command: urgency calculation details, runs by default when just an ID/UUID is specified
    </li>
    <li>
     Improved
     <code>
      diagnostics
     </code>
     command: shows environment variables, hooks, indicates configuration errors
    </li>
    <li>
     Improved urgency calculations: inherited urgency via dependencies, UDA participation, affects nag feature
    </li>
    <li>
     Improved documentation: redesigned reference PDF, man pages moved online
    </li>
    <li>
     Improved security: certificate validation, hostname validation
    </li>
    <li>
     Improved report filters
    </li>
    <li>
     Improved front-end support: file locking, confirmation suppression
    </li>
    <li>
     Improved debugging output, sync diagnostics
    </li>
    <li>
     Improved completion scripts: zsh, fish
    </li>
    <li>
     Improved Vim support files
    </li>
    <li>
     Updated holiday files
    </li>
    <li>
     Removed deprecated features:
     <code>
      push
     </code>
     ,
     <code>
      pull
     </code>
     ,
     <code>
      merge
     </code>
     , old file formats, unused configuration settings
    </li>
    <li>
     Removed the misunderstood 'total active time' feature, replaced by a 3rd party hook script
    </li>
    <li>
     Removed the shadow file feature, replaced by a hook script example
    </li>
   </ul>
   For full details, see the ChangeLog file included in the release.
  </p>
  <p>
   Look for a series of new online documents over the coming days,
            highlighting some of the new functionality.
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

