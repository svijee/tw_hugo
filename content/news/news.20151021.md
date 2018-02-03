---
date: 2015-10-21
title: 'Taskwarrior 2.5.0 Released'
aliases: ['/news/news.20151021.html']
---
<div class="col-md-8 main">
 <div class="row">
  <p>
   After an intense five months which focused mainly on a more capable
            command-line parser, more extension-friendly behavior, and
            significant improvements to testing, Taskwarrior 2.5.0 is now
            released.
  </p>
  <p>
   This is a major release, with 1300+ code changes and well over a
            hundred bug fixes. We recommend all users upgrade, this release
            represents a significant increase in quality.
  </p>
  <p>
   There have been a lot of changes. Here are the highlights:
  </p>
  <p>
   <ul>
    <li>
     Improved command line parser: terminator
     <code>
      --
     </code>
     handling, UUID recognition, DOM recognition, red-herring pairs (
     <code>
      foo:bar
     </code>
     ), escaped slashes in patterns (
     <code>
      /one\/two/
     </code>
     ), substitutions (
     <code>
      /one\/two/one-two/
     </code>
     ), Unicode
     <code>
      U+NNNN
     </code>
     and
     <code>
      \uNNNN
     </code>
     , escaped entities (
     <code>
      \n
     </code>
     ,
     <code>
      \t
     </code>
     etc) for use in descriptions/annotations, abbreviated day and month names, ISO-8601 durations (
     <code>
      PT4H
     </code>
     ,
     <code>
      P1Y
     </code>
     etc).
    </li>
    <li>
     New
     <a href="/docs/tags.html">
      virtual tags
     </a>
     <code>
      UDA
     </code>
     ,
     <code>
      ORPHAN
     </code>
     ,
     <code>
      PROJECT
     </code>
     ,
     <code>
      PRIORITY
     </code>
     , and
     <code>
      LATEST
     </code>
     .
    </li>
    <li>
     Improved support for DOM references in filters
     <code>
      task 'due.year = 2015 and due.week &gt; 20' list
     </code>
     .
    </li>
    <li>
     New configuration settings
     <code>
      urgency.inherit
     </code>
     ,
     <code>
      rule.color.merge
     </code>
     ,
     <code>
      urgency.user.tag.next.coefficient
     </code>
     ,
     <code>
      color.uda.&lt;name&gt;.none
     </code>
     ,
     <code>
      sugar
     </code>
     ,
     <code>
      report.&lt;name&gt;.sort:none
     </code>
     ,
     <code>
      json.depends.array
     </code>
     .
    </li>
    <li>
     Improved urgency: the
     <code>
      urgency.inherit
     </code>
     setting propagates urgency along dependency chains.
    </li>
    <li>
     Improved searching: more powerful regular expressions.
    </li>
    <li>
     Improved attribute modifiers:
     <code>
      is
     </code>
     /
     <code>
      isnt
     </code>
     are now consistent exact match operator equivalents to
     <code>
      ==
     </code>
     /
     <code>
      !==
     </code>
     .
    </li>
    <li>
     New command
     <a href="/docs/commands/_unique.html">
      <samp>
       _unique
      </samp>
     </a>
     , for generating unique lists of values, and will ultimately replace several helper commands.
    </li>
    <li>
     New command
     <a href="/docs/commands/commands.html">
      <samp>
       commands
      </samp>
     </a>
     , which lists commands and details about how they affect
     <a href="/docs/filter.html">
      filters
     </a>
     , GC, context, and
     <a href="/docs/syntax.html">
      syntax
     </a>
     .
    </li>
    <li>
     New verbosity tokens
     <code>
      recur
     </code>
     (feedback when a recurring task instance is created),
     <code>
      unwait
     </code>
     (for when a waiting task becomes visible).
    </li>
    <li>
     Improved extensions: zsh completion, Fish shell completion,
     <a href="/tools/#exts">
      add-on scripts
     </a>
     now online.
    </li>
    <li>
     Improved documentation:
     <code>
      help
     </code>
     command, man pages, more online docs, negation
     <code>
      !
     </code>
     operator, sample hook scripts.
    </li>
    <li>
     Improved sync: GnuTLS now mandatory, so everyone has the
     <code>
      sync
     </code>
     command.
    </li>
    <li>
     Improved JSON
     <code>
      import
     </code>
     /
     <code>
      export
     </code>
     support: free-format JSON, task arrays assumed (which makes import/export work with out-of-the-box parsers), dependencies optionally modeled as an array, UUIDs validated, tasks added/updated without duplication, import from STDIN using
     <code>
      -
     </code>
     .
    </li>
    <li>
     Improved performance: less data is read from disk depending on the filter.
    </li>
    <li>
     Improved diagnostics: duplicate dependency warnings, multi-task edit failures, changes to tasks without IDs, certificate file sizes.
    </li>
    <li>
     Improved testing: migrated all Perl tests to Python, parallelized test suite, colorized output, detection of newly passing tests, Python 2.7 and 3 support, better debug output, Bash test library, stress test tool, no more disabled tests - everything runs, test coverage is now 87.3%.
    </li>
    <li>
     Widespread code cleanup, removal of dead code, C++11 enhancements, improved portability, merged ISO-8601 and legacy durations, less code, happier developers.
    </li>
   </ul>
  </p>
  <p>
   For full details, see the ChangeLog file included in the release.

            The release is immediately available as a source
   <a href="/download/task-2.5.0.tar.gz">
    tarball
   </a>
   .
            Binary packages for your OS will no doubt appear soon.
  </p>
  <p>
   Recommended for all users.
  </p>
  <br/>
  <br/>
 </div>
</div>

