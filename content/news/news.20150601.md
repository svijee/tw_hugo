---
date: 2015-06-01
title: 'Activity Digest: May 2015'
aliases: ['/news/news.20150601.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Activity Digest: May 2015
   <small>
    2015-06-01
   </small>
  </h3>
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in the Taskwarrior project. Here is what
            happened in May 2015.
  </p>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2015-05-02
     </small>
    </td>
    <td>
     Taskwarrior and Taskserver learned how to lock files the POSIX
                way, instead of a platform-specific implementation. This should
                have happened years ago.  Moving on...
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-02
     </small>
    </td>
    <td>
     The 'Taskwarrior' name was standardized throughout the code.
                Something you would think had happened a long time ago.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-02
     </small>
    </td>
    <td>
     Taskserver no longer misleads when asked to modify a configuration
                setting with a read-only config file.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-02
     </small>
    </td>
    <td>
     Taskserver can now restrict itself to the IPv4 or IPv6 protocol.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-02
     </small>
    </td>
    <td>
     Taskserver inherited Taskwarrior's
     <code>
      l10n
     </code>
     utility,
                and finds unused strings.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-03
     </small>
    </td>
    <td>
     Taskwarrior documentation interchangeably used ambiguous terms
                to describe sync server configuration.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-04
     </small>
    </td>
    <td>
     A problem was found, then fixed, with some write commands, when
                GC (Garbage Collection) was manually shut off. Although a bug,
                don't turn off GC.

                It has been harming the bee populations. This should help.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-04
     </small>
    </td>
    <td>
     Taskserver now recognizes libc++ memory errors. It doesn't do
                anything about it, but at least it knows what's happening.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-04
     </small>
    </td>
    <td>
     Taskserver 1.1.0 beta1 was released.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-04
     </small>
    </td>
    <td>
     The fish completion script is improved.  Yes, fish is a real
                shell name.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-05
     </small>
    </td>
    <td>
     The
     <code>
      setup_server.bash
     </code>
     script is significantly
                improved for correctness and usability. It was much needed.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-06
     </small>
    </td>
    <td>
     The Taskwarrior test suite is now parallelized, and runs in far
                less time than before. On some systems,
     <code>
      ./run_all --fast
     </code>
     now runs in around 20 seconds.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-09
     </small>
    </td>
    <td>
     Some old bugs are closed, because they were fixed a while ago,
                but not recorded.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-09
     </small>
    </td>
    <td>
     Taskwarrior lexer is improved to better detect tags on the
                command line when there is preceding text, like
     <code>
      (+tag)
     </code>
     .
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-10
     </small>
    </td>
    <td>
     Example export scripts were not properly handling UTF-8, and
                were fixed.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-10
     </small>
    </td>
    <td>
     Taskwarrior 2.4.4 was
     <a href="/news/news.20150510.html">
      released
     </a>
     .
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-11
     </small>
    </td>
    <td>
     Taskserver 1.1.0 was
     <a href="/news/news.20150511.html">
      released
     </a>
     .
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-13
     </small>
    </td>
    <td>
     Taskserver learns to listen on
     <code>
      ::
     </code>
     , which means dual
                IPv4/IPv6 localhost. Obviously.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-14
     </small>
    </td>
    <td>
     Taskserver learns to not fail silently on signal handler errors.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-23
     </small>
    </td>
    <td>
     Tasksh lost it's rudimentary
     <code>
      context
     </code>
     feature, which
                was eclipsed by a much more powerful Taskwarrior equivalent.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-24
     </small>
    </td>
    <td>
     Taskwarrior, Taskserver and Tasksh start using C++11 N1984 and
                N2672, and it feels oh, so good.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-24
     </small>
    </td>
    <td>
     Through the power of copy/paste, Taskserver fixes bugs by
                inheriting fixed code from Taskwarrior.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-24
     </small>
    </td>
    <td>
     Taskwarrior implements an experimental, recursive, O(N^2) urgency
                inheritance algorithm that may cause your lights to dim and power
                utility bills to increase.

                It may also be killing the bee populations.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-24
     </small>
    </td>
    <td>
     Tasksh is getting a
     <code>
      review
     </code>
     command.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-25
     </small>
    </td>
    <td>
     Taskwarrior and Taskserver combined
     <code>
      Path
     </code>
     ,
     <code>
      File
     </code>
     and
     <code>
      Directory
     </code>
     classes into one
                source file and test program named
     <code>
      FS
     </code>
     .  While this
                has no benefit at all (you're welcome users!) it keeps the three
                together, as they are a hierarchy and cannot operate alone.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-25
     </small>
    </td>
    <td>
     Test suite now better differentiate between tests that pass and
                tests that are skipped. It's important.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-25
     </small>
    </td>
    <td>
     Taskwarrior can now import tasks from STDIN if
     <code>
      -
     </code>
     is
                specified as the input file.  Or if nothing is specified.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-25
     </small>
    </td>
    <td>
     Taskwarrior now has a
     <code>
      test/README
     </code>
     document that
                defines how unit tests should be written, in a desperate attempt
                to get more tests.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-28
     </small>
    </td>
    <td>
     The test suite learns how to intrinsically support export.
                For the bees.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-29
     </small>
    </td>
    <td>
     Taskwarrior
     <code>
      import
     </code>
     can now
     <code>
      add
     </code>
     or
     <code>
      update
     </code>
     a task as appropriate. Finally.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-31
     </small>
    </td>
    <td>
     Task
     <code>
      modify
     </code>
     code got refactored nicely, which makes
                it easier for the developers to look at without convulsions.
                You're welcome users!
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-05-31
     </small>
    </td>
    <td>
     Some Taskwarrior code that was commented out a long time ago,
                that we subsequently forgot the intent thereof, was quietly and
                shamefully deleted.
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

