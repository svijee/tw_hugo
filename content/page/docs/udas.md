---
title: 'User Defined Attributes (UDA)'
url: "/docs/udas.html"
---
<div class="col-md-10 main">
 <div class="row">
  <a name="udas">
  </a>
  <p>
   Taskwarrior supports a set of standard attributes for a task,
              known as the core attributes. These include
   <code>
    project
   </code>
   ,
   <code>
    description
   </code>
   ,
   <code>
    due
   </code>
   and so on. There are
              more than 20 standard attributes (see
   <a href="/docs/commands/columns.html">
    columns
   </a>
   for a full list). They are necessary to provide all the
              functionality of Taskwarrior. For example, the
   <code>
    project
   </code>
   attribute is used to provide feedback on
              completion of a project, the
   <code>
    projects
   </code>
   command itself,
              and project hierarchy filtering. The
   <code>
    project
   </code>
   attribute has a lot of functionality associated with it, and this
              is why
   <code>
    project
   </code>
   is a core attribute.
  </p>
  <p>
   Other attributes, such as
   <code>
    priority
   </code>
   do not have much
              associated functionality. In fact, beyond storing the value,
              allowing modification, sorting and inclusion in reports, the
   <code>
    priority
   </code>
   field contributes nothing. This is why
   <code>
    priority
   </code>
   is not really a core attribute, and will
              be migrated out of the code and into configuration.
  </p>
  <p>
   Occasionally people will ask for new attributes, because their
              workflow includes more metadata than Taskwarrior supports. A very
              common request is for an
   <code>
    estimate
   </code>
   attribute, which
              would store a scalar quantity of some kind, perhaps a number of
              days, or large/medium/small. Until now, the answer to most of
              these requests is to use tags or annotations to approximate the
              storage of the metadata. Now we have UDAs to achieve this.
  </p>
  <a name="what">
  </a>
  <h4>
   What is a UDA?
  </h4>
  <p>
   A UDA is a new metadata item that you define, and taskwarrior
              faithfully stores, displays, and modifies. But that is the
              extent of it, because Taskwarrior does not leverage it for
              functionality like the
   <code>
    project
   </code>
   attribute, but simply
              treats it as a data value with a name, allowing you to sort by it,
              use it in a report, import and export it.
  </p>
  <p>
   It is intended that, once configured, a UDA is indistinguishable
              from core attributes, and will not impart performance penalties.
  </p>
  <a name="types">
  </a>
  <h4>
   Data Types
  </h4>
  <p>
   A UDA has a type, which may be one
   <code>
    string
   </code>
   ,
   <code>
    numeric
   </code>
   ,
   <code>
    date
   </code>
   or
   <code>
    duration
   </code>
   .
              If a UDA has type
   <code>
    date
   </code>
   , then it will naturally only
              accept date values, just like the core attribute
   <code>
    due
   </code>
   .
              The
   <code>
    string
   </code>
   UDA type is special, in that a list of
              acceptable values may also be provided, and taskwarrior will only
              allow modifications if the new value is in the list.
  </p>
  <a name="estimate">
  </a>
  <h4>
   Example: estimate
  </h4>
  <p>
   A UDA is created by modifying configuration. There are two or
              three configuration settings involved. Let's create an
   <code>
    estimate
   </code>
   UDA that is numeric:
  </p>
  <pre>$ task config uda.estimate.type numeric
$ task config uda.estimate.label Est</pre>
  <p>
   That's all - but note there are three pieces of information there:
              first there is "estimate", which is the attribute name, then
              "numeric" which is the type, and finally "Est", which is the
              default label used when the UDA is included in a report. Now you
              can add or modify a task to include an estimate.
  </p>
  <pre>$ task add "Paint the door" project:Home estimate:4
...</pre>
  <a name="size">
  </a>
  <h4>
   Example: size
  </h4>
  <p>
   Now suppose you are developing software in an Agile environment.
              You may wish to have a
   <code>
    size
   </code>
   attribute that may
              contain a fixed set of values, such as "large", "medium" or
              "small". This is achieved using an additional configuration
              setting:
  </p>
  <pre>$ task config uda.size.type string
$ task config uda.size.label Size
$ task config uda.size.values large,medium,small</pre>
  <p>
   Now if you attempt to store a value such as "tiny", taskwarrior
              will disallow it.
  </p>
  <a name="defaults">
  </a>
  <h4>
   Default Values
  </h4>
  <p>
   Default values may be defined. Continuing the example above, to
              specify a
   <code>
    medium
   </code>
   size default for each task, use
              this setting:
  </p>
  <pre>uda.size.default=medium</pre>
  <p>
   This default value will be applied to any task that does not
              otherwise have a
   <code>
    size
   </code>
   value.
  </p>
  <a name="urgency">
  </a>
  <h4>
   Urgency
  </h4>
  <p>
   You can specify that a UDA contributes to the urgency calculation
              of a task. As an example, the above
   <code>
    size
   </code>
   UDA could
              be given an urgency coefficient like this:
  </p>
  <pre>urgency.uda.size.coefficient=2.8</pre>
  <p>
   Then whenever a task has a non-trivial value in the
   <code>
    size
   </code>
   UDA, the urgency is boosted by 2.8.
  </p>
  <a name="orphans">
  </a>
  <h4>
   Orphaned UDAs
  </h4>
  <p>
   Suppose you define an
   <code>
    estimate
   </code>
   UDA and use it. Then
              you remove the configuration for the UDA. You have just created
              a situation where the data is stored, but is no longer something
              that can be used in a report or a filter. This is an orphan UDA.
  </p>
  <p>
   You might think this is an unusual situation, but it is exactly
              what happens if you sync data with UDAs to a taskwarrior
              installation that does not have the UDA configured. Data loss
              would be unacceptable, so taskwarrior will preserve all orphan
              UDA data, but will not let you manipulate it. Only defined UDAs
              can be manipulated. There is one exception -
              the
   <code>
    edit
   </code>
   command will let you remove UDA orphans by
              making their values blank, which eliminates any attribute.
  </p>
  <a name="reports">
  </a>
  <h4>
   Custom Reports
  </h4>
  <p>
   UDA fields may be used in custom reports, just like any other
              attribute. A report containing an attribute that is an orphan
              UDA is not a valid report.
  </p>
  <a name="other">
  </a>
  <h4>
   Other UDA Uses
  </h4>
  <p>
   The
   <code>
    priority
   </code>
   attribute is soon to be replaced by a
              UDA equivalent. This is not something that anyone will notice,
              but it will make for a smaller, more stable core product. UDAs
              are useful for other capabilities though. An example would be the
              import of bugs from a Request Tracker. The additional metadata
              in the Request Tracker could be created as UDAs in taskwarrior,
              which will then allow for a full import without data loss.
  </p>
 </div>
 <br/>
 <br/>
</div>

