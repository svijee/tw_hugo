---
date: 2017-01-02
title: 'Activity Digest: December 2016'
aliases: ['/news/news.20170102.html']
---
<div class="col-md-8 main">
 <div class="row">
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in our projects. Here is what happened in
            December 2016.

            This is not a complete list of all activity, just work that results
            in a non-trivial change. For a full list, see the git history of all
            the projects.
  </p>
  <div class="callout callout-info">
   <h4>
    Summary
   </h4>
   <p>
    Both Taskwarrior and Taskserver improved
    <a href="http://gnutls.org/">
     GnuTLS
    </a>
    support, in particular with more robust certificate validation,
              and error reporting/logging.
   </p>
   <p>
    The rat parser is now handling complex grammars, such as the
    <a href="/docs/clog/index.html">
     clog
    </a>
    configuration file, and will later be used to handle command line
              parsing in all projects.
   </p>
   <p>
    The Taskwarrior overhaul of recurrence features has begun, which
              will culminate in the 2.6.0 release with new types of recurring
              tasks.
   </p>
  </div>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2016-12-03
     </small>
    </td>
    <td>
     <ul>
      <li>
       rat: Added test suite for all supported grammar
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-12-10
     </small>
    </td>
    <td>
     <ul>
      <li>
       Guides: Added license
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-12-11
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Pig inherits Nibbler optimization and no longer makes string copies
      </li>
      <li>
       libshared:
       <code>
        Pig::getUntil
       </code>
       was including the terminator by mistake
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-12-17
     </small>
    </td>
    <td>
     <ul>
      <li>
       libshared: Table supports data obfuscation
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-12-19
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-3">
        TD-3: Harden server against malformed requests
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-69">
        TD-69: Log permission errors
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-81">
        TD-81: Improve logging features and provide informative error messages
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-116">
        TD-116: Provided systemd unit file does not match recommended systemd unit file in docs
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TD-125">
        TD-125: taskd doesn't check ownership of files in $TASKDDATA, sync fails without error
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1873">
        TW-1873: Specify different path to extensions/hooks directory
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1855">
        TW-1855: "Well-known" CA certificates not properly auto-loaded
       </a>
       fixed
      </li>
      <li>
       rat: Added entity support
      </li>
      <li>
       Task:
       <code>
        show
       </code>
       command didn't include the
       <code>
        debug.tls
       </code>
       setting
      </li>
      <li>
       Task: Improved certificate validation diagnostics
      </li>
      <li>
       Task: Added GnuTLS 3.4.6 API support
      </li>
      <li>
       Taskd: Added GnuTLS 3.4.6 API support
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-12-22
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1878">
        TW-1878: uuids subcommand produces a space-delimited list, not comma-delimited
       </a>
       fixed
      </li>
      <li>
       libshared: Updated Uicode character classification
      </li>
      <li>
       rat: Supports the
       <code>
        &lt;punct&gt;
       </code>
       ,
       <code>
        &lt;eol&gt;
       </code>
       ,
       <code>
        &lt;sep&gt;
       </code>
       ,
       <code>
        &lt;ws&gt;
       </code>
       , and
       <code>
        &lt;alpha&gt;
       </code>
       intrinsics
      </li>
      <li>
       rat: Now reads files, as well as CLI samples
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-12-23
     </small>
    </td>
    <td>
     <ul>
      <li>
       rat: Documents the PEG format
      </li>
      <li>
       rat: Supports the
       <code>
        &lt;word&gt;
       </code>
       intrinsic
      </li>
      <li>
       rat: Now has a Color type grammar
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-12-26
     </small>
    </td>
    <td>
     <ul>
      <li>
       Guides: Updated taskserver-setup based on user feedback
      </li>
      <li>
       Holidata: Prototype for auto-generating holiday files
      </li>
      <li>
       libshared: Args supports option counting
      </li>
      <li>
       rat: Now has a Datetime and Duration grammar
      </li>
      <li>
       rat: Now has a Clog CLI grammar
      </li>
      <li>
       rat: Supports the
       <code>
        &lt;token&gt;
       </code>
       intrinsic
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-12-27
     </small>
    </td>
    <td>
     <ul>
      <li>
       Holidata: Can now generate source CSV files
      </li>
     </ul>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2016-12-31
     </small>
    </td>
    <td>
     <ul>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1858">
        TW‐1858 Change signature for dependencyGetBlocked
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1859">
        TW-1859 Change signature of Task::getTags
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1860">
        TW-1860 Change signature of Task::getAnnotations
       </a>
       fixed
      </li>
      <li>
       <a href="https://bug.tasktools.org/browse/TW-1878">
        TW-1878: uuids subcommand produces a space-delimited list, not comma-delimited
       </a>
       fixed
      </li>
      <li>
       Task: Fixed mis-labelled
       <code>
        scheduled
       </code>
       column
      </li>
      <li>
       Task: New
       <code>
        rtype
       </code>
       ,
       <code>
        last
       </code>
       and
       <code>
        template
       </code>
       attributes added
      </li>
     </ul>
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

