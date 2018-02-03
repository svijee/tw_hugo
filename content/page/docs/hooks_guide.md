---
title: "Hook Author's Guide"
url: '/docs/hooks_guide.html'
---
<div class="col-md-10 main">
 <div class="row">
  <a name="guide">
  </a>
  <p>
   This guide walks through the process of writing and testing a
              Taskwarrior hook script. While this is a simple and straightforward
              process for developers, there are still many considerations.

              A hooks script will be developed, and the various concerns
              discussed.
  </p>
  <p>
  </p>
  <a name="example">
  </a>
  <h4>
   Example Hook Script
  </h4>
  <p>
   As an example, we're going to create a hook script that detects
              tasks that refer to Taskwarrior bug numbers (ie 'TW-123') in the
              description, and replaces the bug number with a URL that links
              to the bug. Whenever the pattern
   <code>
    tw-123
   </code>
   is found in
              a task description, it should change to
   <code>
    https://bug.tasktools.org/browse/tw-123
   </code>
   .
  </p>
  <p>
   This script will simply need to search for a pattern, and perform
              a replacement, for new tasks only. This will be a very simple
              hook script.
  </p>
  <a name="language">
  </a>
  <h4>
   Choosing a Language
  </h4>
  <p>
   You can write a hook script in any language you wish. But there is
              more to consider:
  </p>
  <ul>
   <li>
    Is performance an issue? It is not likely that you need to worry
                about performance, because the time spent adding or modifying
                tasks is a one-time cost. Performance would be more important
                if it affected a report.
   </li>
   <li>
    Does your language have a readily available JSON parser? Most
                likely it does, but is it installed on the users machine?
                Are you going to be requiring that the user install additional
                software?
   </li>
   <li>
    If you are considering a compiled language, will you ship source
                or binaries? Developers typically have compilers installed, but
                regular users do not. Shipping binaries means you'll need to
                provide them for different OSes and versions.
   </li>
  </ul>
  <p>
   This example will be written in Python 2.6+, because Python is
              well known, modern, and commonly available. It has a built-in JSON
              parser. It is ideal for this task.
  </p>
  <a name="api">
  </a>
  <h4>
   Hooks API
  </h4>
  <p>
   Read and understand the
   <a href="/docs/hooks.html">
    Hooks API
   </a>
   .
              This is important because the hook script must comply with the API
              requirements.

              Taskwarrior is strict about compliance. Hook scripts have the
              ability to harm data, so they are carefully monitored.
  </p>
  <a name="framework">
  </a>
  <h4>
   Framework
  </h4>
  <p>
   From the API, we know that an
   <code>
    on-add
   </code>
   hook script will
              need to read a line of JSON from standard input, and emit an
              optionally modified line of JSON, optionally include feedback, and
              exit with a zero status indicating success.
  </p>
  <p>
   To begin with, here is a compliant
   <code>
    on-add
   </code>
   hook script
              that does nothing,
   <em>
    but does it properly
   </em>
   .
              It can be the basis for any
   <code>
    on-add
   </code>
   script.
  </p>
  <pre>#!/usr/bin/env python

import sys
import json

added_task = json.loads(sys.stdin.readline())
print(json.dumps(added_task))
sys.exit(0)</pre>
  <p>
   This script reads a line of JSON from input and parses it. This
              JSON represents the task being added. The JSON is then serialized
              and written to output, without modification. An exit code of zero
              indicates that the added task is accepted.
  </p>
  <p>
   Although this script does nothing to the task, it only requires
              a few more lines added to be complete.
  </p>
  <a name="testing">
  </a>
  <h4>
   Testing
  </h4>
  <p>
   You can test your hook script independently from Taskwarrior,
              which is a good idea.

              First we make our script executable, then we simply run it from
              the command line and feed it sample JSON. Here is an example
              test run, using valid JSON, but it is not a valid task - it's
              just a test.
  </p>
  <pre>$ chmod +x hook.py
$ echo '{"name":"value"}' | ./hook.py
{"name": "value"}
$ echo $?
0</pre>
  <p>
   Here the hook script was made executable, then sample JSON
   <code>
    {"name":"value"}
   </code>
   is provided as input. The script
              emits the JSON unmodified as output, and the exit code is zero.
              This script works.
  </p>
  <p>
   Now we add logic to the script to make it do something.
  </p>
  <a name="implementation">
  </a>
  <h4>
   Implementation
  </h4>
  <p>
   For the implementation, the script needs to look for bug numbers.
              Taskwarrior bug numbers can be represented with a regular expression
              like this:
  </p>
  <pre>\b(tw-\d+)\b</pre>
  <p>
   The script is now modified to
   <code>
    import re
   </code>
   , and perform
              the substitution on the description attribute. By comparing the
              original description to the modified description, the script knows
              when to provide feedback. Here is the updated script:
  </p>
  <pre>#!/usr/bin/env python

import sys
import re
import json

added_task = json.loads(sys.stdin.readline())
original = added_task['description']
added_task['description'] = re.sub(r'\b(tw-\d+)\b',
                                   r'https://bug.tasktools.org/browse/\1',
                                   original,
                                   flags=re.IGNORECASE)
print(json.dumps(added_task))

if original != added_task['description']:
    print 'Link added'

sys.exit(0)</pre>
  <p>
   Testing the script again with better input yields this:
  </p>
  <pre>$ echo '{"description":"foo tw-123 bar"}' | ./hook.py
{"description": "foo https://bug.tasktools.org/browse/tw-123 bar"}
Link added
$
$ echo $?
0</pre>
  <p>
   The script has correctly identified the bug number, and replaced
              it with the correct URL. The feedback message indicates this.
              We are ready to install this hook script and test it using
              Taskwarrior.
  </p>
  <a name="install">
  </a>
  <h4>
   Install and Enable
  </h4>
  <p>
   To install the script, copy it to the
   <code>
    ~/.task/hooks
   </code>
   directory, creating that directory if necessary, and make sure
              the script is executable.  It must also be associated with an
              event, which is done by naming it
   <code>
    on-add*
   </code>
   .
  </p>
  <pre>$ mkdir -p ~/.task/hooks
$ cp hook.py ~/.task/hooks/on-add-bug-link.py
$ chmod +x ~/.task/hooks/on-add-bug-link.py</pre>
  <p>
   There is a configuration setting that enables/disables hooks and
              you'll need to make sure hooks are enabled, although this is the
              default value:
  </p>
  <pre>$ task _get rc.hooks
on</pre>
  <p>
   Now run the
   <code>
    diagnostics
   </code>
   command, which will summarize
              the hooks it finds:
  </p>
  <pre>$ task diag
...
Hooks
    Scripts: Enabled
             &lt;user&gt;/.task/hooks/on-add-bug-link.py (executable)
...</pre>
  <p>
   We see that the hook script is found by Taskwarrior. Now let's
              see it in action, and note that the
   <code>
    --
   </code>
   terminator is
              being used so that
   <code>
    tw-123
   </code>
   is not perceived as a
              mathematical expression:
  </p>
  <pre>$ task add -- Contains no bug number
Created task 181.
$ task add -- Fix tw-123
Created task 182.
Link added
$
$ task _get 182.description
Fix https://bug.tasktools.org/browse/tw-123</pre>
  <p>
   It works, but we have done minimal testing here.  If you write a
              hook script with any non-trivial capabilities, your testing
              should be much more thorough. This is only an example.
  </p>
  <a name="debugging">
  </a>
  <h4>
   Debugging
  </h4>
  <p>
   Taskwarrior has a hook debug configuration setting, which will
              show you how Taskwarrior processes the hook input and output,
              what happened, and how long it took. Here a similar task is added
              with debug information requested. The output is edited to show
              just the relevant hook information.
  </p>
  <pre>$ task rc.debug.hooks=2 add -- Fix tw-98765
...
Found hook script &lt;user&gt;/.task/hooks/on-add-bug-link.py
...
Hook: Calling &lt;user&gt;/.task/hooks/on-add-bug-link.py
Hook: input
  {"description":"Fix tw-98765","entry":"20150301T154518Z","modified":"20150301T154518Z","status":"pending","uuid":"daa3ff05-f716-482e-bc35-3e1601e50778"}
Timer Hooks::execute (&lt;user&gt;/.task/hooks/on-add-bug-link.py) 0.031061 sec
Hook: output
  {"status": "pending", "entry": "20150301T154518Z", "uuid": "daa3ff05-f716-482e-bc35-3e1601e50778", "description": "Fix https://bug.tasktools.org/browse/tw-98765", "modified": "20150301T154518Z"}
  Link added
Hook: Completed with status 0
...
Perf task 2.4.2 f0cc015 20150301T154759Z init:3388 load:2001 gc:0 filter:0 commit:230 sort:0 render:0 hooks:33565 total:39184

Created task 183.
Configuration override rc.debug.hooks:2
Link added</pre>
  <p>
   The output shows that the hook script was found and run, the input
              and output is show, along with timing information, feedback and
              the status.
  </p>
  <p>
   In this case the hook script ran in 31ms, which is certainly fast
              enough to not cause the user to wonder what is happening. In this
              example all hook processing was completed in 33ms.
  </p>
  <a name="dist">
  </a>
  <h4>
   Distribute
  </h4>
  <p>
   With your hook script complete, will you be sharing your script?
              It's optional of course, but if you do, consider a license and
              copyright, establish a web presence so it can be found and
              downloaded, perhaps put contact info in the script so you can be
              told of problems, then tell people about it.
  </p>
  <p>
   You can tell us about your hook script, because we'd like to list
              it on the
   <a href="/tools">
    Tools
   </a>
   page, along with many others.
  </p>
 </div>
 <br/>
 <br/>
</div>

