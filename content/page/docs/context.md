---
title: "Context"
url: '/docs/context.html'
---
<div class="col-md-10 main">
 <div class="row">
  <a name="context">
  </a>
  <p>
   A context is associated with a location. An example of this might
              be that you perform tasks in three locations:
   <ul>
    <li>
     At the office
    </li>
    <li>
     At home
    </li>
    <li>
     Study
    </li>
   </ul>
   The tasks that pertain to your time in the office are meaningless
              if you are at home, and vice versa. This is just an example, and
              your contexts will likely be very different.
  </p>
  <p>
   If Taskwarrior allowed you to specify which context is currently
              active, then the tasks listed could be filtered accordingly. You
              would then be working within a context.

              A context is therefore a named filter, and the current context is
              a form of default filter.
  </p>
  <a name="define">
  </a>
  <h4>
   Defining a Context
  </h4>
  <p>
   In order to work within a context, you first need to define that
              context. Because a context is essentially a task filter, defining
              a context is really defining a named filter. In this example, we
              define our contexts from the list above using the new
   <code>
    context define
   </code>
   command:
  </p>
  <pre>$ task context define work +work or +freelance
$ task context define study +school or +homework or +lab
$ task context define home -work -freelance -school -homework -lab</pre>
  <p>
   The context definition may contain any form of algebraic expression
              just like a filter. In the example, the contexts are based entirely
              on tags. Notice that
   <code>
    home
   </code>
   is defined as neither
   <code>
    work
   </code>
   nor
   <code>
    study
   </code>
   . This means that every
              task is accounted for, although this is not necessary.
  </p>
  <p>
   It is an error to try to define a context with the names
   <code>
    define
   </code>
   ,
   <code>
    list
   </code>
   ,
   <code>
    show
   </code>
   ,
   <code>
    none
   </code>
   , or
   <code>
    delete
   </code>
   .
  </p>
  <a name="set">
  </a>
  <h4>
   Setting the Context
  </h4>
  <p>
   To set or switch the current context, simply:
  </p>
  <pre>$ task context home
$ task list
...</pre>
  <p>
   If you try to use an undefined context, Taskwarrior will report an
              error.
  </p>
  <p>
   Now with the context set to
   <code>
    home
   </code>
   , all the tasks
              listed will pertain to the
   <code>
    home
   </code>
   context, as defined.
              There will be a footnote after every report that reminds you of
              the current context.
  </p>
  <a name="show">
  </a>
  <h4>
   Showing the Context
  </h4>
  <p>
   Although the current context is included in a footnote after every
              report, this can be disabled with the verbosity controls. To show
              the current context:
  </p>
  <pre>$ task context show
home</pre>
  <p>
   This can also be obtained using
   <code>
    _get
   </code>
   :
  </p>
  <pre>$ task _get rc.context
home</pre>
  <a name="list">
  </a>
  <h4>
   Listing All Contexts
  </h4>
  <p>
   You can list all the contexts using the new
   <code>
    context list
   </code>
   command:
  </p>
  <pre>$ task context list
Context Filter
------- ----------------------------------
home    -work -freelance -school -homework
study   +school or +homework
work    +work or +freelance</pre>
  <a name="clear">
  </a>
  <h4>
   Clearing the Context
  </h4>
  <p>
   To clear the current context:
  </p>
  <pre>$ task context none</pre>
  <p>
   The context
   <code>
    none
   </code>
   has special meaning.
              All subsequent commands will not have any implicit context filters
              applied.
  </p>
  <a name="delete">
  </a>
  <h4>
   Deleting a Context
  </h4>
  <p>
   To delete one of the contexts:
  </p>
  <pre>$ task context delete study</pre>
  <p>
   Now you can no longer set the context to
   <code>
    study
   </code>
   .  If
              the current context was already
   <code>
    study
   </code>
   when you deleted
              it, the context is cleared.
  </p>
  <a name="impact">
  </a>
  <h4>
   Impact on Commands
  </h4>
  <p>
   All reports that accept filters will use the context if one is
              defined and set.
  </p>
  <a name="related">
  </a>
  <h4>
   Related Support
  </h4>
  <p>
   The
   <code>
    tasksh
   </code>
   program will show the current context in its
              prompt.
  </p>
  <a name="implementation">
  </a>
  <h4>
   Implementation Details
  </h4>
  <p>
   Context will be stored in
   <code>
    rc.context
   </code>
   and defined contexts
              will be stored as
   <code>
    rc.context.&lt;name&gt;
   </code>
   in the
   <code>
    .taskrc
   </code>
   file.
  </p>
  <p>
   When a context filter is used, it will be implicitly surrounded by
              parentheses, so that it may contain arbitrary logic.
  </p>
 </div>
 <br/>
 <br/>
</div>

