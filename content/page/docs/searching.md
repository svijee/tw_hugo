---
title: 'Searching'
url: '/docs/searching.html'
---
<div class="col-md-10 main">
 <div class="row">
  <a name="searching">
  </a>
  <p>
   Searching for keywords and patterns in tasks is straightforward,
              and uses the
   <code>
    /pattern/
   </code>
   syntax. First we create some
              sample tasks, then we'll search them.
  </p>
  <pre>$ task add foo
$ task add bar
$ task add baz</pre>
  <p>
   In order to locate that first task, by the keyword
   <code>
    foo
   </code>
   we do this:
  </p>
  <pre>$ task /foo/ list

ID Age   D Description Urg
-- ----- - ----------- ----
 1 1min    foo            0</pre>
  <p>
   The
   <code>
    /
   </code>
   characters delimit the search term, indicating
              what Taskwarrior should do. Because task annotations are also
              searchable text, we can be sure that any annotations containing
              the pattern
   <code>
    /foo/
   </code>
   will also be found. Let's add a
              task with such an annotation:
  </p>
  <pre>$ task 3 annotate footwear
$ task /foo/ long

ID Created    Mod   Recur Description
-- ---------- ----- ----- ---------------------
 3 2014-09-28 2min        baz
                            2014-09-28 footwear
 1 2014-09-28 2min       foo</pre>
  <p>
   Here the
   <code>
    long
   </code>
   report is used so we can see the full
              annotation text. Notice that the
   <code>
    foo
   </code>
   in the
              description of task 1, as well as the
   <code>
    footwear
   </code>
   in
              the annotation of task 3 were both found.
  </p>
  <a name="regexes">
  </a>
  <h4>
   Regular Expressions
  </h4>
  <p>
   Beginning in version
   <span class="label label-success">
    2.4.0
   </span>
   all search terms are by default
   <a href="/docs/glossary.html#regex">
    regular expressions
   </a>
   .
              This means we could have searched using this pattern, which means
              an
   <code>
    f
   </code>
   followed by two
   <code>
    o
   </code>
   characters:
  </p>
  <pre>$ task /fo{2}/ long

ID Created    Mod   Recur Description
-- ---------- ----- ----- ---------------------
 3 2014-09-28 3min        baz
                            2014-09-28 footwear
 1 2014-09-28 3min       foo</pre>
  <p>
   In older versions, you would need to explicitly enable regex
              support like this:
  </p>
  <pre>$ task rc.regex:on /fo{2}/ long

ID Created    Mod   Recur Description
-- ---------- ----- ----- ---------------------
 3 2014-09-28 3min        baz
                            2014-09-28 footwear
 1 2014-09-28 3min       foo</pre>
  <p>
   Or you could put the setting in your
   <code>
    .taskrc
   </code>
   file.
              You can also turn off regular expression support:
  </p>
  <pre>$ task rc.regex:off /fo{2}/ long

No matches.</pre>
  <p>
   This fails because the search term
   <code>
    /fo{2}/
   </code>
   is this
              time considered just text, not a regular expression and this term
              does not appear in any task.
  </p>
  <a name="shell">
  </a>
  <h4>
   Shell
  </h4>
  <p>
   If your search term contains one or more spaces, then your
   <a href="/docs/glossary.html#shell">
    shell
   </a>
   is going to break the search pattern into two arguments, and
              Taskwarrior will be confused. Solve this by either quoting or
              escaping like these examples:
  </p>
  <pre>$ task '/foo bar/' list
$ task /foo\ bar/ list</pre>
  <p>
   This guarantees that Taskwarrior sees one argument,
   <code>
    /foo bar/
   </code>
   instead of two,
   <code>
    /foo
   </code>
   ,
   <code>
    bar/
   </code>
   .
  </p>
  <a name="operators">
  </a>
  <h4>
   Operators
  </h4>
  <p>
   The search pattern syntax of
   <code>
    /pattern/
   </code>
   is there as a
              convenience, but there are more powerful low-level operators, such
              that the above pattern is equivalent to:
  </p>
  <pre>$ task description~foo list
</pre>
  <p>
   Here the
   <code>
    ~
   </code>
   match operator works much like that in Bash.
              To invert that, to search for descriptions that
   <em>
    do not
   </em>
   contain the pattern, use the no-match operator:
  </p>
  <pre>$ task 'desc!~foo' list
</pre>
  <p>
   Here you see the
   <code>
    !~
   </code>
   no-match operator, an abbreviated
   <code>
    desc
   </code>
   attribute name, and quoting, because Bash will
              interpret the
   <code>
    !
   </code>
   character in its own way.
  </p>
 </div>
 <br/>
 <br/>
</div>

