---
title: "Hooks v2"
url: '/docs/hooks2.html'
---
<div class="col-md-10 main">
 <div class="row">
  <div class="callout callout-info">
   <h4>
    Hooks v2
   </h4>
   <p>
    The API defined here is the
    <kbd>
     Hooks v2
    </kbd>
    API.
                This API is part of the TaskWarrior 2.4.3 release.
   </p>
  </div>
  <a name="hooks">
  </a>
  <p>
  </p>
  <a name="events">
  </a>
  <h4>
   Events
  </h4>
  <p>
   No change.
  </p>
  <a name="input">
  </a>
  <h4>
   Input
  </h4>
  <p>
   No change.
  </p>
  <a name="output">
  </a>
  <h4>
   Output
  </h4>
  <p>
   No change.
  </p>
  <a name="status">
  </a>
  <h4>
   Exit Status
  </h4>
  <p>
   No change.
  </p>
  <a name="interfaces">
  </a>
  <h4>
   Interfaces
  </h4>
  <p>
   No change.
  </p>
  <a name="args">
  </a>
  <h4>
   Command Line Arguments
  </h4>
  <p>
   To support an evolving Hooks API, Taskwarrior must provide hook
              scripts with a mechanism for determining which version of the
              Hooks API is providing the context for the script.

              It is anticipated that in future versions, new events will be
              added, and changes to the interfaces will occur. A hook script
              needs to act according to the API version, otherwise it risks
              incompatibility with Taskwarrior.
  </p>
  <p>
   The interfaces define what is provided as standard input, and
              what is expected on standard output.  With
   <code>
    v2
   </code>
   there
              will also be command line arguments provided to the script.
  </p>
  <p>
   A script may take advantage of the
   <code>
    v2
   </code>
   enhancements
              though, to extend its capabilities.
  </p>
  <p>
   <table class="table table-striped table-condensed">
    <tr>
     <th>
      Argument
     </th>
     <th>
      Meaning
     </th>
    </tr>
    <tr>
     <td>
      <code>
       api:2
      </code>
     </td>
     <td>
      <p>
       The
       <code>
        2
       </code>
       specified means Hooks API
       <code>
        v2
       </code>
       .
                      This will be a monotonically increasing number, as the
                      Hooks API evolves.
      </p>
      <p>
       The only possible value for this argument is currently
       <code>
        2
       </code>
       , because the
       <code>
        v1
       </code>
       API does not
                      provide command line arguments.
      </p>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       args:task ...
      </code>
     </td>
     <td>
      <p>
       The script has read-only access to the command line that
                      Taskwarrior received.
      </p>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       command:add|done|sync|...
      </code>
     </td>
     <td>
      <p>
       The command Taskwarrior recognized in its command line
                      arguments.
      </p>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       rc:/path/to/.taskrc
      </code>
     </td>
     <td>
      <p>
       Absolute path of rc file used by Taskwarrior after all
                      overrides have been applied.
      </p>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       data:/path/to/task/folder
      </code>
     </td>
     <td>
      <p>
       Absolute path of folder containing Taskwarrior's *.data
                      files.
      </p>
     </td>
    </tr>
    <tr>
     <td>
      <code>
       version:x.y.z
      </code>
     </td>
     <td>
      <p>
       Taskwarrior version calling the hook. Same as the one
                      reported by "task --version", e.g. "2.4.3"
      </p>
     </td>
    </tr>
   </table>
  </p>
  <p>
   Here is a contrived example simulating how a hook script will be
              invoked:
  </p>
  <pre> $ ~/.task/hooks/on-xxx.yyy \
    api:2 \
    args:'task rc:~/mytaskrc list' \
    command:add \
    rc:/home/foo/mytaskrc \
    data:/home/foo/.task \
    version:2.4.3 \
    &lt;input.txt \
    &gt;output.txt</pre>
  <p>
   This information can be used by the script to see that an
              alternate
   <code>
    rc
   </code>
   file was specified on the command
              line.
  </p>
  <a name="compat">
  </a>
  <h4>
   Backward Compatibility
  </h4>
  <p>
   The
   <code>
    v1
   </code>
   and
   <code>
    v2
   </code>
   API is identical, so any hook
              script will run unmodified in both scenarios. This may not be
              true for future versions.
  </p>
  <p>
   A script that requires
   <code>
    v2
   </code>
   but is run in a
   <code>
    v1
   </code>
   context should issue a warning that it is not able to perform its
              function, but it should not fail.
  </p>
 </div>
 <br/>
 <br/>
</div>

