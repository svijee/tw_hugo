---
title: 'Command Line Syntax'
url: "/docs/syntax.html"
---
<div class="col-md-10 main">
 <div class="row">
  <a name="syntax">
  </a>
  <p>
   Taskwarrior has a flexible command line syntax, but it may not be
              clear at first what the underlying structure means. Here is the
              general form of the syntax:
  </p>
  <p>
   <img class="img-responsive" src="/docs/images/syntax.png"/>
  </p>
  <p>
   There are four parts to the syntax (
   <code>
    filter
   </code>
   ,
   <code>
    command
   </code>
   ,
   <code>
    modifications
   </code>
   , and
   <code>
    miscellaneous
   </code>
   ), and each part is optional.
  </p>
  <a name="command">
  </a>
  <h3>
   Command
  </h3>
  <p>
   Each time you run Taskwarrior, you are issuing a
   <code>
    command
   </code>
   either explicitly, or implicitly with the
              default command (the
   <code>
    default.command
   </code>
   configuration
              setting). The command you specify determines how the command
              line is understood by Taskwarrior. Here are some examples of
              that:
  </p>
  <p>
   <img class="img-responsive" src="/docs/images/syntaxes.png"/>
  </p>
  <p>
   The first example,
   <code>
    task list
   </code>
   is a report with no
              filter, and the second,
   <code>
    task +home list
   </code>
   is with a
              filter. The third,
   <code>
    task 12 modify project:Garden
   </code>
   has both a filter and modifications. The last example,
   <code>
    task show editor
   </code>
   has a miscellaneous argument.
  </p>
  <p>
   Taskwarrior looks for the first argument on the command line that
              looks like an exact command name, and failing that, looks for an
              abbreviated command name. It is better to use the full name of a
              command to avoid ambiguity.
  </p>
  <p>
   It is the position of the
   <code>
    command
   </code>
   argument, and the
              type of command that determines how the arguments are understood.
  </p>
  <a name="filter">
  </a>
  <h3>
   Filter
  </h3>
  <p>
   A filter is a means of addressing a subset of tasks. Because filters
              are optional, the simplest case is no filter. A command with no
              filter addresses all tasks.
  </p>
  <p>
   Generally filter arguments appear before the command, so any arguments
              to the left of the command are considered filter arguments.
  </p>
  <p>
   There is a special case, in which a command that does not support
              modifications or miscellaneous arguments, expects only filter arguments,
              and so they can appear before or after the command, without confusing
              Taskwarrior:
  </p>
  <p>
   <img class="img-responsive" src="/docs/images/filter.png"/>
  </p>
  <a name="mods">
  </a>
  <h3>
   Modifications
  </h3>
  <p>
   If a command accepts modifications, they generally appear after
              the command. Most command that accept modifications also accept
              filters, and so the filter arguments appear before the command,
              while the modifications appear after. Here is an example:
  </p>
  <p>
   <img class="img-responsive" src="/docs/images/modification.png"/>
  </p>
  <p>
   This command specifies a compound filter, consisting of more than
              one term. These terms are logically combined with an
   <code>
    and
   </code>
   operator by default, unless otherwise specified. In this case, tasks
              that have both the
   <code>
    home
   </code>
   tag, and a
   <code>
    status
   </code>
   value of
   <code>
    pending
   </code>
   are to be modified.
  </p>
  <p>
   The modifications, appearing after the command, set the
   <code>
    priority
   </code>
   to
   <code>
    H
   </code>
   igh, and the
   <code>
    due
   </code>
   date to the end of the month (
   <code>
    eom
   </code>
   ).
  </p>
  <p>
   Because the filter is evaluated at runtime, we don't know how many
              tasks will be modified. It could be none, one, many or all of the
              tasks. It could be determined with:
   <pre>task +home status:pending count</pre>
   The user writing this command would have an idea of how many tasks
              this will affect, but this is just an example, with no contextual
              data shown.
  </p>
  <a name="misc">
  </a>
  <h3>
   Miscellaneous
  </h3>
  <p>
   Some commands accept neither a filter, nor modifications, but do
              accept miscellaneous arguments. An example is the
   <code>
    show
   </code>
   command, that queries configuration settings, and does not accept
              a filter:
  </p>
  <p>
   <img class="img-responsive" src="/docs/images/miscellaneous.png"/>
  </p>
  <p>
   This is another special case, in which the command only accepts
              miscellaneous arguments, and so they can appear before or after the
              command.
  </p>
  <a name="override">
  </a>
  <h3>
   Overrides
  </h3>
  <p>
   Overrides are temporary values for configuration settings, and can
              be specified anywhere on the command line, because they are not
              considered to be either filter, modification or miscellaneous.
              In fact, the command itself doesn't see the overrides, instead they
              are handled before the command runs.
  </p>
  <p>
   <img class="img-responsive" src="/docs/images/override.png"/>
  </p>
  <p>
   There can be any number of overrides on the command line, and they
              have no effect on the syntax.
  </p>
 </div>
 <br/>
 <br/>
</div>

