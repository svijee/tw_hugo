---
title: '3rd-Party Application Guidelines'
url: "/docs/3rd-party.html"
---
<div class="col-md-10 main">
 <div class="row">
  <a name="3p">
  </a>
  <p>
   Taskwarrior can be extended by means of a third-party application,
              which can be a wrapper, or hook script.
              There are script examples of import and export add-ons that
              support many different formats (clone the repository, look in
   <code>
    task.git/scripts/add-ons
   </code>
   ).  Then there are more
              sophisticated applications such as
   <a href="http://tasktools.org/projects/vit.html">
    Vit
   </a>
   that provide a complete replacement UI.
  </p>
  <p>
   All of these provide interesting new features and improve ease of
              use for different kinds of users.  We encourage you to create
              such add-ons, but in doing so, there are some rules that must be
              followed, which will not only protect the users data from
              mistreatment, but also your application from being sensitive to
              changes in Taskwarrior.
  </p>
  <a name="rules">
  </a>
  <h4>
   Rules
  </h4>
  <p>
   <ul>
    <li>
     Produce, consume and handle UTF8 text properly.  UTF8 is the
                  only text encoding supported by Taskwarrior.
    </li>
    <li>
     Don't attempt to parse the pending.data file.  Here's why:
                  the
     <code>
      .data
     </code>
     file format is currently on its fourth
                  version. The very first version was never released, so if you
                  want to read Taskwarrior data properly, you will need to parse
                  the three supported formats. Those formats are not documented.
                  Additionally, you will need to handle the GC operations,
                  implement the task "unwait" feature, observe user defined
                  attribute handling restrictions, and implement recurring task
                  synthesis all of which require .taskrc and default value
                  access. You would essentially be rewriting the data access
                  and configuration portion of Taskwarrior, which is a major
                  undertaking. To support filters you would also need to
                  evaluate the supported clauses, provide DOM access and
                  implement aliases.  Then there is also the fifth data format,
                  which is planned...
    </li>
    <li>
     Use the
     <code>
      export
     </code>
     command to query data from
                  Taskwarrior.  The
     <code>
      export
     </code>
     command implements
                  filters which you can use, or you can omit a filter, get all
                  the data, and implement your own filtering.  JSON parsing is
                  very well supported in all relevant programming languages,
                  which means you should be using Taskwarrior itself to query
                  the data, with a commodity JSON parser in conjunction.  While
                  the JSON format will be tweaked over time, the general form
                  will not.
    </li>
    <li>
     Beginning with version
     <span class="label label-success">
      2.4.5
     </span>
     ,
                  use the
     <code>
      import
     </code>
     command to import modified JSON
                  back into Taskwarrior.
    </li>
    <li>
     Older versions: Use the command line interface to put data
                  into Taskwarrior.  Composing a valid command line is a simple
                  way to put data in to Taskwarrior.
    </li>
    <li>
     Use the
     <code>
      _get
     </code>
     helper command to access individual
                  data items. Note that multiple items can be retrieved by one
                  command. If accessing more than just a few items, use the
     <code>
      export
     </code>
     command.
    </li>
    <li>
     Verify feature support by running
     <code>
      task --version
     </code>
     .
                  This command returns the version number, which will help you
                  determine whether or not a particular feature is supported.
                  Note that this command does not scan for a configuration file,
                  and is therefore safe to run if Taskwarrior is not yet set up.
    </li>
    <li>
     UDAs (User Defined Attributes) must be preserved in the data.
                  When reading the JSON for a task, there may be attributes that
                  you have never encountered before.  If this is the case, you
                  must not modify them in any way.  This not only makes your
                  application future-proof, but allows it to tolerate UDAs from
                  other data sources.  It also prevents the Taskserver from
                  stripping out
     <em>
      your
     </em>
     data.
    </li>
   </ul>
  </p>
  <a name="guidelines">
  </a>
  <h4>
   Guidelines
  </h4>
  <p>
   <ul>
    <li>
     If you need to store additional data, consider putting your
                  own data file in the
     <code>
      ~/.task
     </code>
     directory.  Just
                  don't use the file names
     <code>
      pending.data
     </code>
     ,
     <code>
      completed.data
     </code>
     ,
     <code>
      backlog.data
     </code>
     ,
                  or
     <code>
      undo.data
     </code>
     .
    </li>
    <li>
     There are many helper commands designed to assist add-on
                  scripts such as shell completion scripts.  These commands all
                  begin with an underscore, see them with this command:
     <code>
      task help | grep ' _'
     </code>
     .
    </li>
    <li>
     Familiarize yourself with the means of forcing color on or
                  off, disabling word wrapping, disabling bulk operation
                  limitations, disabling confirmation, disabling gc, modifying
                  verbosity and so on.  There are ways around almost all the
                  restrictions, and while these don't make sense for regular
                  users, they can be critical for add-on authors.
    </li>
   </ul>
  </p>
 </div>
 <br/>
 <br/>
</div>

