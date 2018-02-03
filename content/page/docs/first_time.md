---
title: 'How to become an Open Source Contributor'
url: "/docs/first_time.html"
---
<div class="col-md-10 main">
 <div class="row">
  <p>
   Welcome, potential new Open Source contributor! This is a guide
              to show you exactly how to make a contribution, and will lead you
              through the entire process.
  </p>
  <p>
   There are many people who wish to start contributing, but don't
              know how or where to start.

              If this might be the case, then please read on, this guide is for
              you. Because we want you to join in the fun with Open Source - it
              can be fun and rewarding, improve your skills, or just give you a
              way to contribute back to a project.
  </p>
  <p>
   Where else can you combine the thrill of typing in a darkened
              room with the kindhearted love of an internet forum?  Just kidding!
  </p>
  <p>
   The goal of this document is to give you the ability to make your
              first contribution, and encourage you to make a second, by showing
              you how simple it is. Perhaps confidence and a little familiarity
              with the process are all you need to get started.
  </p>
  <p>
   We're going to pick the smallest contribution of all - a typo fix.
              While this may be a very small improvement, it is nevertheless a
              wanted improvement, and will be welcomed.

              Fixes such as this happen many times a day. Similar work on new
              features, new documents, rewriting help, refactoring code, fixing
              bugs and improving performance all combine to make a project grow
              and improve.
  </p>
  <p>
   Making a bigger change also is certainly an option, but the focus
              here is on going through the procedure, which is somewhat
              independent from the nature of the change.

              The steps are numbered, and it all fits on this one page. Get all
              the way to the end, and you will be an open source contributor.
  </p>
  <a name="setup">
  </a>
  <h4>
   <span class="label label-success">
    1
   </span>
   Development Environment Setup
  </h4>
  <p>
   In order to build and test software, you need a development
              environment. That's just a term that means you need certain tools
              installed before proceeding. Here are the tools that Taskwarrior
              needs:
  </p>
  <p>
   <ul>
    <li>
     Compiler: GCC 4.7 or newer, or Clang 3.4 or newer.
    </li>
    <li>
     Libraries: GnuTLS, and libuuid
    </li>
    <li>
     Tools: Git, CMake, make, Python
    </li>
   </ul>
  </p>
  <p>
   The procedure for installing this software is OS-dependent, but
              here are the commands you would use on Debian:
  </p>
  <pre>$ sudo apt-get install gcc
$ sudo apt-get install libgnutls28-dev
$ sudo apt-get install uuid-dev
$ sudo apt-get install git
$ sudo apt-get install cmake
$ sudo apt-get install make</pre>
  <a name="clone">
  </a>
  <h4>
   <span class="label label-success">
    2
   </span>
   Get the Code
  </h4>
  <p>
   Now you have the tools, next you need the code.
              This involves cloning the repository using git and looking at the
              development branch:
  </p>
  <pre>$ git clone --recursive -b 2.6.0 https://git.tasktools.org/TM/task.git task.git
Cloning into 'task.git'...
remote: Counting objects: 55345, done.
remote: Compressing objects: 100% (12655/12655), done.
remote: Total 55345 (delta 44868), reused 52340 (delta 42437)
Receiving objects: 100% (55345/55345), 25.04 MiB | 7.80 MiB/s, done.
Resolving deltas: 100% (44868/44868), done.
Checking connectivity... done.
$</pre>
  <p>
   The URL for the repository was obtained from looking around on
   <a href="https://git.tasktools.org">
    https://git.tasktools.org
   </a>
   where several repositories are public, including the one for this
              web site.
  </p>
  <p>
   The clone command above puts you on the right branch, so no need to
              switch.

              But it's a good idea to check anyway, so do this:
  </p>
  <pre>$ cd task.git
$ git branch -a
* 2.6.0
  remotes/origin/2.5.1
  remotes/origin/2.5.2
  remotes/origin/2.6.0
  remotes/origin/HEAD -&gt; origin/master
  remotes/origin/master
$</pre>
  <p>
   Here we see that 2.6.0 is the highest-numbered branch, and therefore
              the current development branch.  If there were a higher numbered branch,
              you would want to use that by doing this:
  </p>
  <pre>$ git checkout 2.7.0</pre>
  <p>
   Here's a thought - if this page does not show the latest branch
              names, then, you know, you could fix that...
  </p>
  <a name="fix">
  </a>
  <h4>
   <span class="label label-success">
    3
   </span>
   Fix Something
  </h4>
  <p>
   Now that you have the code, find something to fix. This may be the
              hardest step, but knowing how many typos there are in the source
              code and docs, it shouldn't take long to find one. Try looking in
              the files in these directories:
   <ul>
    <li>
     <code>
      task.git/doc/man
     </code>
    </li>
    <li>
     <code>
      task.git/scripts
     </code>
    </li>
    <li>
     <code>
      task.git/src
     </code>
    </li>
    <li>
     <code>
      task.git/test
     </code>
    </li>
   </ul>
  </p>
  <p>
   It also doesn't need to be a typo, it can instead be a poorly-worded
              sentence, or one that could be more clear. You'll find something,
              whether it is jargon, mixed tenses, mistakes, or just plain wrong.
  </p>
  <p>
   Then fix it, using a text editor. Try to make the smallest possible
              change to achieve what you want, because smaller changeѕ are easier
              to verify and approve, and no reviewer wants to receive a large
              change to approve.
  </p>
  <a name="test">
  </a>
  <h4>
   <span class="label label-success">
    4
   </span>
   Run the Test Suite
  </h4>
  <p>
   Taskwarrior has an extensive test suite to prove that things are
              still working as expected. You'll need to build the program and
              run this test suite in order to prove to yourself that your fix is
              good. It may seem like building the program is overkill, if you
              only make a small change, but no, it is not. The test suite is
              there to save you from submitting a bad change, and to save
              Taskwarrior from any mistakes you make.
  </p>
  <p>
   First you have to build the program.  Do this:
  </p>
  <pre>$ cd task.git
$ cmake .
-- The C compiler identification is ...
-- The CXX compiler identification is ...
-- Check for working C compiler: ...

...

-- Configuring done
-- Generating done
-- Build files have been written to: /home/user/task.git
$
$ make
Scanning dependencies of target columns
Scanning dependencies of target task
Scanning dependencies of target commands
[  2%] Building CXX object src/columns/CMakeFiles/columns.dir/ColDepends.cpp.o
[  2%] Building CXX object src/columns/CMakeFiles/columns.dir/Column.cpp.o
[  2%] Building CXX object src/CMakeFiles/task.dir/CLI2.cpp.o

...

[100%] Linking CXX executable task
[100%] Linking CXX executable lex
[100%] Linking CXX executable calc
[100%] Built target lex_executable
[100%] Built target task_executable
[100%] Built target calc_executable
$</pre>
  <p>
   If the above commands worked, there will be a binary, which you
              can find:
  </p>
  <pre>$ ls -l src/task
-rwxr-xr-x  1 user  group    Mar 25 18:43 src/task</pre>
  <p>
   The next step is to build the test suite. Do this:
  </p>
  <pre>$ cd test
$ make
[ 14%] Built target task
[ 25%] Built target columns
[ 45%] Built target commands
Scanning dependencies of target variant_subtract.t
Scanning dependencies of target variant_partial.t
Scanning dependencies of target variant_or.t

...

[ 98%] Built target i18n.t
[100%] Linking CXX executable view.t
[100%] Built target view.t</pre>
  <p>
   Now run the test suite, which can take anywhere from 10 - 500
              seconds, depending on your hardware and OS:
  </p>
  <pre>$ ./run_all
Passed:                          8300
Failed:                             0
Unexpected successes:               0
Skipped:                            3
Expected failures:                  5
Runtime:                        32.50 seconds</pre>
  <p>
   We are looking for zero failed tests, as shown.  This means all is well.
  </p>
  <a name="commit">
  </a>
  <h4>
   <span class="label label-success">
    5
   </span>
   Commit the Change
  </h4>
  <p>
   Now you've made a change, built and tested the code. The next step
              is to commit the change locally. This example assumes you fixed a
              typo in the man page. Check to see which file you changed, stage
              that file, then commit it:
  </p>
  <pre>$ cd task.git
$ git status
On branch 2.6.0
Your branch is up-to-date with 'origin/2.6.0'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   doc/man/task.1.in

no changes added to commit (use "git add" and/or "git commit -a")
$ git add doc/man/task.1.in
$ git commit -m 'Docs: corrected typo in the main man page'
[2.6.0 ddbb07e] Docs: corrected typo in the main man page
 1 file changed, 1 insertion(+)
$</file></file></pre>
  <p>
   Notice how the commit message looks like this:
   <code>
    Category: Brief description
   </code>
   , which is how the commit
              messages should look.
  </p>
  <a name="patch">
  </a>
  <h4>
   <span class="label label-success">
    6
   </span>
   Make a Patch
  </h4>
  <p>
   Once the commit is made, making a patch is simple:
  </p>
  <pre>$ git format-patch HEAD^
0001-Docs-corrected-typo-in-the-main-man-page.patch
$</pre>
  <a name="submit">
  </a>
  <h4>
   <span class="label label-success">
    7
   </span>
   Submit the Patch
  </h4>
  <p>
   Finally you just need to email that patch file to
   <code>
    taskwarrior-dev@googlegroups.com
   </code>
   .  You will need
              to attach it to an email, and not just paste it in, because the
              mail client will probably mess with the contents, wrapping lines
              etc, which can make it unusable.
  </p>
  <p>
   What happens next is that a developer will take your patch and
              study it, to ascertain whether it really does fix something that
              is broken. If there is a problem, you'll hear back with some
              gentle, constructive criticism. If the problem is small, it might
              just get fixed. Then your patch is applied, tested, and if all
              looks well, pushed to the public repository, and included in the
              the next release. Your name will go into the AUTHORS file, and
              you will be thanked.
  </p>
  <p>
   Congratulations! Welcome to the wonderful world of open source
              involvement. Now do it again...
  </p>
 </div>
 <br/>
 <br/>
</div>

