---
title: "Configuration"
url: '/docs/configuration.html'
---
<div class="col-md-10 main">
 <div class="row">
  <a name="config">
  </a>
  <p>
   Taskwarrior stores all configuration information in a file in
              your home directory, named
   <code>
    .taskrc
   </code>
   .

              The default
   <code>
    .taskrc
   </code>
   file contains a minimal set of
              entries, with only one required setting, which is:
  </p>
  <pre>data.location=~/.task</pre>
  <p>
   This is the only setting you need because Taskwarrior has senѕible
              defaults for all the settings.  This file is really just a list of
              settings for which you wish to override those defaults.
  </p>
  <a name="config_cmd">
  </a>
  <h4>
   Config Command
  </h4>
  <p>
   The
   <code>
    config
   </code>
   command can be used to modify your
   <code>
    .taskrc
   </code>
   file.  In this example we enable regular
              expression support in filters, by doing this:
  </p>
  <pre>$ task config regex on
Are you sure you want to change the value of 'regex' from 'off' to 'on'? (yes/no) yes
Config file ~/.taskrc modified.</pre>
  <p>
   You can use 'on', or '1', 'yes' or 'true', all of which are
              synonyms which will enable the feature.  You are asked to confirm
              the change, which is controlled by the
   <code>
    confirmation
   </code>
   setting which of course you can disable with:
  </p>
  <pre>$ task config confirmation off</pre>
  <p>
   The general form of the command can be either of these:
  </p>
  <pre>task config name value
task config name ''
task config name</pre>
  <p>
   These three example show, respectively, setting
   <code>
    name
   </code>
   to
   <code>
    value
   </code>
   , setting
   <code>
    name
   </code>
   to an empty
              value, and deleting the setting.  Note that only deleting the
              setting removes the override and therefore restores the default.
  </p>
  <a name="show_cmd">
  </a>
  <h4>
   Show Command
  </h4>
  <p>
   The
   <code>
    show
   </code>
   command displays all the current
              configuration settings, which is a list of all the settings and
              default values, with your local settings overriding those, and
              furthermore with any command line overrides.  The show command
              will also filter the settings by a keyword you specify, so to look
              at the
   <code>
    next
   </code>
   report definition, you can run this:
  </p>
  <pre>$ task show report.minimal

Config Variable            Value
-------------------------- ----------------------------------------
report.minimal.columns     id,project,tags.count,description.count
report.minimal.description Pending tasks by project and description
report.minimal.filter      ( status:pending or status:waiting )
report.minimal.labels      ID,Project,Tags,Description
report.minimal.sort        project+,description+,entry+</pre>
  <p>
   The
   <code>
    show
   </code>
   command will highlight values that differ
              from the defaults, and will also tell you if there are settings
              which are not recognized. This might indicate ѕpelling mistakes
              or obsolete settings.
  </p>
  <a name="include">
  </a>
  <h4>
   Includes
  </h4>
  <p>
   The
   <code>
    .taskrc
   </code>
   file supports inclusion, which is used
              for example, for theme files.
  </p>
  <pre>include ~/themes/solarized-dark-256.theme</pre>
  <p>
   The file included is expected to contain Taskwarrior configuration
              settings, or nested includes.
  </p>
  <a name="override">
  </a>
  <h4>
   Command Line Override
  </h4>
  <p>
   The
   <code>
    config
   </code>
   command makes permanent changes to your
   <code>
    .taskrc
   </code>
   files, but you can temporarily override these
              settings for a single command, using this technique:
  </p>
  <pre>$ task rc.regex=on /[Tt]otal/ list</pre>
  <p>
   One possible use of this feature is to override the
   <code>
    data.location
   </code>
   setting to use an alternate task list:
  </p>
  <pre>$ task rc.data.location=/alternate/path/.task ...</pre>
  <a name="env">
  </a>
  <h4>
   Environment Variables
  </h4>
  <p>
   There are two environment variables that can be used to specify
              an alternate configuration file, and an alternate data location.
  </p>
  <pre>TASKRC=~/.taskrc TASKDATA=~/.task task list</pre>
  <p>
   This example uses environment variables to specify both the
              configuration file and the data directory.
  </p>
 </div>
 <br/>
 <br/>
</div>

