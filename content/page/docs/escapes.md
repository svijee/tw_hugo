---
title: 'Escaping Command Line Characters'
url: '/docs/escapes.html'
---
<div class="col-md-10 main">
 <div class="row">
  <a name="escaping">
  </a>
  <p>
   Certain characters are interpreted by the shell. For example, the
   <code>
    &amp;
   </code>
   . If you wish to include the
   <code>
    &amp;
   </code>
   in a
              task description, you need to escape it, so the shell doesn't
              interpret it. For example:
  </p>
  <pre>$ task add Buy bread &amp; milk</pre>
  <p>
   This command is an error because of the
   <code>
    &amp;
   </code>
   . The shell
              will consider this to be two commands:
  </p>
  <pre>$ task add Buy bread &amp;
$ milk</pre>
  <p>
   The shell treats the
   <code>
    &amp;
   </code>
   character as an indicator that
              the command is complete and should be run in the background. Then
              the shell considers "milk" to be a command all by itself, which
              it is not.  One way to get around this is to individually escape
              the
   <code>
    &amp;
   </code>
   character:
  </p>
  <pre>$ task add Buy bread \&amp; milk</pre>
  <p>
   Another is to quote the entire description, with either
   <code>
    '
   </code>
   or
   <code>
    "
   </code>
   characters:
  </p>
  <pre>$ task add "Buy bread &amp; milk"</pre>
  <p>
   If you wish to use quotes in the task description itself, you can
              individually escape them:
  </p>
  <pre>$ task add Don\'t forget eggs</pre>
  <p>
   In other situations, the shell sees spaces and breaks up
              arguments.  For example, this command:
  </p>
  <pre>$ task 123 modify /from this/to that/</pre>
  <p>
   is broken up into several arguments, which is corrected with
              quotes:
  </p>
  <pre>$ task 123 modify "/from this/to that/"</pre>
  <a name="projects">
  </a>
  <h4>
   Projects with Spaces
  </h4>
  <p>
   Suppose you want to use a project name that contains spaces.  This
              requires escaped quotes:
  </p>
  <pre>$ task add Buy potatoes project:\'Food and Groceries\'</pre>
  <p>
   The reason for this is that when the shell sees quotes, it
              preserves the contents between the quotes as a single argument,
              but does not preserve the quotes themselves.  By adding the
              backslash to the quotes, you guarantee that taskwarrior gets to
              see the quotes.  This is an unfortunate situation, but a common
              one for programs that accept a wide variety of command line
              characters.
  </p>
  <a name="noparse">
  </a>
  <h4>
   Shutting Off Parsing
  </h4>
  <p>
   There is a special command line argument which is two hyphens
   <code>
    --
   </code>
   , and when this is used, special command line
              handling is disabled from that point onwards, which means all
              subsequent arguments are considered part of a task description:
  </p>
  <pre>$ task add -- project:Home needs scheduling</pre>
  <a name="silver_bullet">
  </a>
  <h4>
   When All Else Fails...
  </h4>
  <p>
   There is a solution.  We don't like it, but it exists for
              difficult cases.  The
   <a href="#">
    <code>
     edit
    </code>
    command
   </a>
   is a way to bypass all the shell problems.  Simply do this:
  </p>
  <pre>$ task add placeholder
$ task 1 edit</pre>
  <p>
   The
   <a href="#">
    <code>
     edit
    </code>
    command
   </a>
   drops you into a text editor where you can compose arbitrarily
              complex task descriptions and annotations without the need to
              consider quoting and escapes.
  </p>
  <a name="characters">
  </a>
  <h4>
   Special Shell Characters
  </h4>
  <p>
   There are many characters that are considered special by the
              shell, and may need to be escaped in order that they may be used
              on the taskwarrior command line.  Those characters include:
  </p>
  <pre>$ ! ' " ( ) ; \ ` * ? { } [ ] &lt; &gt; | &amp; % # ~ @</pre>
 </div>
 <br/>
 <br/>
</div>

