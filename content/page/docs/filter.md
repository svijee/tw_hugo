---
title: 'Filters'
url: '/docs/filter.html'
---
<div class="col-md-10 main">
 <div class="row">
  <a name="filters">
  </a>
  <p>
   A filter is a set of command line arguments that specify a set of
              tasks and filters can range from being simple to very complex.
              The simplest filter is an empty filter, and we can illustrate this
              with the
   <code>
    count
   </code>
   .
  </p>
  <pre>$ task count
100</pre>
  <p>
   These 100 tasks are the tasks, pending and completed, which
              represent are all the tasks known to Taskwarrior.  Any command
              that accepts a filter also accepts no filter, as shown above.

              Now we introduce a filter with one term.
  </p>
  <pre>$ task status:pending count
38</pre>
  <p>
   This is an example of the
   <code>
    name : value
   </code>
   form for
              specifying attribute values. This filter shows that there are 38
              pending tasks, and therefore 62 that are not pending in some way.
              This form of filter also works for other attributes:
  </p>
  <pre>$ task project:Home count
19</pre>
  <p>
   There are 19 tasks in the 'Home' project.
  </p>
  <p>
   The
   <code>
    value
   </code>
   parameter can be left empty in order to
              match only the items that do not have a value of the relevant kind
              assigned to them. For example, you can count the tasks that are not
              assigned to any project, like this:
  </p>
  <pre>$ task project: count
81</pre>
  <p>
   In this example, we can see that the tasks not assigned 'Home'
              project have not yet been assigned to any project at all.
  </p>
  <p>
   Taskwarrior has other filters besides
   <code>
    name : value
   </code>
   filters. Here are two examples, filtering on the presence and
              absence of a tag.
  </p>
  <pre>$ task +work count
14
$ task -work count
86</pre>
  <p>
   This shows us that 14 tasks have the 'work' tag, and 86 do not
              have the tag. To search for a word in the description or
              annotation:
  </p>
  <pre>$ task /m..ting/ count
3</pre>
  <p>
   Here we see that 3 tasks have the word 'm..ting' in the
              description. This is a regular expression, although it can also
              be just a simple word.
  </p>
  <p>
   This assumes you have enabled regular expression support, using
              the
   <code>
    rc.regex
   </code>
   configuration setting.
  </p>
  <a name="complex">
  </a>
  <h4>
   Complex Filters
  </h4>
  <p>
   Filters gain complexity by adding more filter terms and logic.
              Suppose we want to see the number of tasks that have the 'Home'
              project, and do not have the 'work' tag. Simply put both terms on
              the command line.
  </p>
  <pre>$ task project:Home -work count
18</pre>
  <p>
   The two terms in the filter are both applied to the set of all
              tasks, or in other words, a task must have both the 'Home' project
              and not have the 'work' tag to be counted.
  </p>
  <p>
   When a filter contains multiple terms like this, they are treated
              as a logical conjunction, which is to say that both terms must
              match for a task to be selected by the filter.  If there were
              three terms in the filter, then all three must match.
  </p>
  <p>
   This assumed conjunction is another command line syntax shortcut.
              The long form of this command line is:
  </p>
  <pre>$ task project:Home and -work count
18</pre>
  <p>
   See the
   <code>
    and
   </code>
   operator between the filter terms? That
              is assumed to be there if not specfically stated. The unstated
              implication is that the disjunction ('or') is also supported.
  </p>
  <pre>$ task project:Home or -work count
90</pre>
  <p>
   This example asks how many tasks are part of the 'Home' project,
              or do not have the 'work' tag - either is a match.
  </p>
  <a name="prec">
  </a>
  <h4>
   Precedence
  </h4>
  <p>
   It was mentioned earlier that the simplest filter was an empty
              filter, such as in use by the
   <code>
    count
   </code>
   command. Now we
              shall consider the
   <code>
    ls
   </code>
   report, which has a filter of:
  </p>
  <pre>$ task show report.ls.filter

Config Variable  Value
---------------- --------------
report.ls.filter status:pending</pre>
  <p>
   This report filter is combined with the command line filter that
              you specify:
  </p>
  <pre>$ task project:Home ls</pre>
  <p>
   This yields a combined filter of:
  </p>
  <pre>status:pending project:Home</pre>
  <p>
   Which has an implicit conjunction:
  </p>
  <pre>status:pending and project:Home</pre>
  <p>
   Now suppose we wanted to use a disjunction filter with the
   <code>
    ls
   </code>
   command:
  </p>
  <pre>$ task project:Home or project:Garden list</pre>
  <p>
   This is interpreted as:
  </p>
  <pre>status:pending and project:Home or project:Garden</pre>
  <p>
   Do you see the precedence problem?  The intended filter is this:
  </p>
  <pre>status:pending and (project:Home or project:Garden)</pre>
  <p>
   which includes the parentheses to group the disjunction.  Going
              back to the original filter, we now know that it needs this form:
  </p>
  <pre>$ task (project:Home or project:Garden) list
...</pre>
  <p>
   Except now we have one more problem - those parentheses have
              special meaning to the shell, and must be escaped in one of the
              following ways:
  </p>
  <pre>$ task \(project:Home or project:Garden\) list
...
$ task '(project:Home or project:Garden)' list
...
$ task "(project:Home or project:Garden)" list</pre>
  <p>
   Note that there are many characters used by the taskwarrior
              command line that have special meaning to the shell, and as such
              must be properly escaped, as
   <a href="/docs/escapes.html">
    described here
   </a>
   .
  </p>
  <a name="config">
  </a>
  <h4>
   Configuration
  </h4>
  <p>
   Regular expressions in pattern filters are only used when enabled
              with:
  </p>
  <pre>regex=on</pre>
  <p>
   This is the default in 2.4.0+. If not enabled, the patterns are
              literal strings to be matched.  Case sensitivity for string
              searches and regular expressions is controlled by:
  </p>
  <pre>search.case.sensitive=yes</pre>
  <p>
   The default is 'yes'.
  </p>
 </div>
 <br/>
 <br/>
</div>

