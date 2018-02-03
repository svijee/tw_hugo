---
title: "How To Build Taskwarrior"
url: '/docs/build.html'
---
<div class="col-md-10 main">
 <div class="row">
  <a name="how">
  </a>
  <p>
   This is for developers. Specifically those who know how to use
              tools, satisfy dependencies, and want to set up a development
              environment. It is not user-friendly.
  </p>
  <p>
   You'll need these tools:
   <ul>
    <li>
     <a href="http://git-scm.com/">
      git
     </a>
    </li>
    <li>
     <a href="http://cmake.org">
      cmake
     </a>
    </li>
    <li>
     make
    </li>
    <li>
     C++ compiler, currently gcc 4.7+ or clang 3.3+ for full C++11 support
    </li>
    <li>
     Python 2.7 or later (for tests)
    </li>
    <li>
     Bash (for tests)
    </li>
   </ul>
  </p>
  <p>
   You'll need these libraries:
   <ul>
    <li>
     <a href="http://www.gnutls.org/">
      GnuTLS
     </a>
    </li>
    <li>
     libuuid (unless on Darwin/BSD)
    </li>
   </ul>
   Specifically the development versions,
   <code>
    uuid-dev
   </code>
   on Debian, for example.
  </p>
  <a name="clone">
  </a>
  <h3>
   Cloning the Repo
  </h3>
  <p>
   For those of you with Stash accounts on
   <a href="https://git.tasktools.org">
    git.tasktools.org
   </a>
   :
  </p>
  <pre>$ git clone ssh://git@git.tasktools.org/tm/task.git task.git</pre>
  <p>
   General public:
  </p>
  <pre>$ git clone https://git.tasktools.org/TM/task.git task.git</pre>
  <a name="stable">
  </a>
  <h3>
   Building the Stable Version
  </h3>
  <p>
   The master always represents the more recently released version,
              and should be your preferred choice.
  </p>
  <pre>$ cd task.git
$ git checkout master                # Master is the stable branch.
$ cmake -DCMAKE_BUILD_TYPE=release . # 'release' for performance.
$ make                               # Just build it.</pre>
  <a name="build">
  </a>
  <h3>
   Building the Dev Branch
  </h3>
  <p>
   The dev branch is always the highest numbered branch, in this
              example,
   <code>
    2.6.0
   </code>
   .
  </p>
  <pre>$ cd task.git
$ git checkout 2.6.0                 # Dev branch
$ git submodule init                 # Register submodule
$ git submodule update               # Get the submodule
$ cmake -DCMAKE_BUILD_TYPE=debug .   # debug or release, default: neither
$ make VERBOSE=1                     # Shows details</pre>
  <p>
   Build the debug type if you want symbols in the binary.
  </p>
  <a name="tests">
  </a>
  <h3>
   Running the Test Suite
  </h3>
  <p>
   There are scripts to facilitate running the test suite. In
              particular, the
   <a href="http://tasktools.org/projects/vramsteg.html">
    vramsteg
   </a>
   utility provides blinkenlights for test progress.
  </p>
  <pre>$ cd task.git/test
$ make VERBOSE=1     # Shows details
$ ./run_all          # Runs all tests silently &gt; all.log
$ ./problems         # Find errors in all.log</pre>
  <a name="patch">
  </a>
  <h3>
   Submitting a Patch
  </h3>
  <p>
   Talk to us first - make sure you are working on something that is
              wanted. Patches will not be applied simply because you did the work.
              Remember the various forms of documentation involved, and the test
              suite. Work on the dev branch, not
   <code>
    master
   </code>
   . When you
              are are ready to submit, do this:
  </p>
  <pre>$ git commit</pre>
  <p>
   Follow the standard form for commit messages, which looks like this:
  </p>
  <pre>Category: Short message

- Details
- Details</pre>
  <p>
   Here is a good example:
  </p>
  <pre>TW-1636: UUID with numeric-only first segment is not parsed properly

- Switched Nibbler::getUUID to Nibbler::getPartialUUID, which caused partial
  UUID matching to fail sometimes.
- Changed precedence to search for UUID before ID, which solves the numeric
  UUID problem.</pre>
  <p>
   Create the patch using this:
  </p>
  <pre>$ git format-patch HEAD^</pre>
  <p>
   Mail the patch to
   <a href="mailto:taskwarrior-dev@googlegroups.com">
    taskwarrior-dev@googlegroups.com
   </a>
   or attach it to the appropriate ticket in the
   <a href="https://bug.tasktools.org">
    bug tracker
   </a>
   .
              If you do the latter, make sure someone knows about it, or it
              could go unnoticed.
  </p>
  <p>
   Expect feedback. It is unlikely your patch will be accepted
              unmodified. Usually this is because you violated the coding
              style, worked in the wrong branch, or
   <em>
    forgot
   </em>
   about
              documentation and unit tests.
  </p>
  <br/>
  <br/>
  <br/>
 </div>
</div>

