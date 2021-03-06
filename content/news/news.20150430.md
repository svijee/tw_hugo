---
date: 2015-04-30
title: 'Activity Digest: April 2015'
aliases: ['/news/news.20150430.html']
---
<div class="col-md-8 main">
 <div class="row">
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in the Taskwarrior project. Here is what
            happened in April 2015.
  </p>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2015-04-01
     </small>
    </td>
    <td>
     The Hooks v2 API was implemented. While nothing changed with
                respect to the events or interfaces to the hooks scripts, there
                are now arguments passed to the hooks script. Whereas in the
                v1 Hooks API a hook script was effectively called like this:
     <pre>script \
    &lt;input \
    &gt;output</pre>
     The v2 API now effectively does this:
     <pre>script \
    'api:v2' \
    'args:task list' \
    'command:list' \
    'rc:~/.taskrc' \
    'data:~/.task' \
    'version:2.4.3' \
    &lt;input \
    &gt;output</pre>
     This allows a hook script to determine which API is in effect,
                and offers access to some important information.
                What will hook scripts do with this information? Who knows,
                let's see, and hope it isn't all used for evil purposes.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-01
     </small>
    </td>
    <td>
     Taskwarrior learned that running hooks scripts while attempting
                to run shell completion is a bad idea.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-02
     </small>
    </td>
    <td>
     The command line lexer was improved, or perhaps just made less
                awful, now allowing both
     <code>
      task calc now + 3 days
     </code>
     work as well as
     <code>
      task calc now+3days
     </code>
     , making
                whitespace irrelevant.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-02
     </small>
    </td>
    <td>
     Recurring tasks now inherit more attributes from the parent
                task, and
     <code>
      rc.default.*
     </code>
     settings are no longer
                applied.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-02
     </small>
    </td>
    <td>
     The
     <code>
      .isnt
     </code>
     and
     <code>
      .not
     </code>
     attribute modifiers
                are now the performing exact non-match, therefore providing
                symmetry to the
     <code>
      .is
     </code>
     modifier.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-03
     </small>
    </td>
    <td>
     Tasks that are downloaded during a
     <code>
      sync
     </code>
     no longer
                get local default settings applied to them.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-03
     </small>
    </td>
    <td>
     Taskwarrior learned that
     <code>
      \n
     </code>
     in a description does
                not have a character width of -1, which borked the formatting.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-04
     </small>
    </td>
    <td>
     Objects returning
     <code>
      std::string
     </code>
     , now return
     <code>
      const std::string&amp;
     </code>
     . This can reduce the number
                of data copies in memory, which makes things better on the inside.
                How about that for a crowd-pleasing improvement!
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-04
     </small>
    </td>
    <td>
     All task attributes are now sortable. "Why weren't they before?"
                you might ask.  Umm...
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-04
     </small>
    </td>
    <td>
     Task sorting duplicated code that was implemented better
                elsewhere, and so this was eliminated.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-04
     </small>
    </td>
    <td>
     UDA
     <code>
      string
     </code>
     attributes that specify discrete values
                are now sorted (high-to-low) in the order that they are defined.
                If one day the priority attribute is removed, then this means
                the priority UDA that replaces it can now have an arbitrary set
                of priority values that sort properly.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-04
     </small>
    </td>
    <td>
     The
     <code>
      priority
     </code>
     attribute is removed from the core,
                and reimplemented as a (standard) UDA. The change is made such
                that users should not notice. Unless they read.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-05
     </small>
    </td>
    <td>
     The
     <code>
      info
     </code>
     command urgency display was cleaned up
                and fixed.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-05
     </small>
    </td>
    <td>
     The
     <code>
      rc.debug.hooks=2
     </code>
     setting now shows the arguments
                that are passed to hook scripts.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-05
     </small>
    </td>
    <td>
     The color themes were updated to accomodate the new form of the
     <code>
      priority
     </code>
     attribute.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-05
     </small>
    </td>
    <td>
     When calculating report formatting, fixed-width columns are now
                only sized once, not once per task.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-05
     </small>
    </td>
    <td>
     The
     <code>
      rc
     </code>
     file syntax was described in the man page,
                finally.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-06
     </small>
    </td>
    <td>
     The test framework is updated to handle the Hooks v2 API.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-06
     </small>
    </td>
    <td>
     The codebase took some early steps towards using C++11 features.
                It's been four years after all, and compilers have caught up,
                somewhat. Future releases will mandate newer Clang/GCC versions
                in order to use new features.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-06
     </small>
    </td>
    <td>
     The
     <code>
      summary.all.projects
     </code>
     setting allows the summary
                report to consider all finished projects.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-06
     </small>
    </td>
    <td>
     Some spa-ESP localization changes were made. The other languages
                are getting quite out of date. Any volunteers?
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-12
     </small>
    </td>
    <td>
     The
     <code>
      info
     </code>
     command now prints urgency details when
                the urgency values is negative.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-16
     </small>
    </td>
    <td>
     Various text-themed helper code was migrated into the Lexer.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-18
     </small>
    </td>
    <td>
     32-bit systems have ambіguous
     <code>
      int
     </code>
     /
     <code>
      time_t
     </code>
     types, which are now disambiguated, which means Taskwarrior now
                builds for 32-bit OSes.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-19
     </small>
    </td>
    <td>
     Taskwarrior 2.4.3 released, which includes the Hooks v2 API,
                and the conversion of
     <code>
      priority
     </code>
     from a core attribute
                to a UDA.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-21
     </small>
    </td>
    <td>
     Starting with the 2.4.4 release, Taskwarrior will require a
                compiler that supports most of the C++11 standard, for example
                GCC 4.7 and Clang 3.3.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-21
     </small>
    </td>
    <td>
     With Taskwarrior released, the development focus now shifts to
                Taskserver 1.1.0. Taskserver inherits a lot of code improvements
                from Taskwarrior because they share code. Obsolete code removed.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-24
     </small>
    </td>
    <td>
     The Taskserver setup script is renamed to 'setup_server.bash',
                and walks the user through the whole setup process for a server,
                and users. Although not for advanced users, this script will
                automate the steps that cause much difficulty among Taskserver
                users.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-24
     </small>
    </td>
    <td>
     Starting with the 1.1.0 release, Taskserver will require a
                compiler that supports most of the C++11 standard, for example
                GCC 4.7 and Clang 3.3.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-25
     </small>
    </td>
    <td>
     Taskserver inherits Taskwarrior's Python test framework, so
                future tests can be written in Python.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-25
     </small>
    </td>
    <td>
     Taskserver documentation begins to mention the new
                setup_server.bash script, which, come to think of it, really
                ought to be tested.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-25
     </small>
    </td>
    <td>
     Taskserver documentation hallucinated functionality triggered
                by SIGHUP and SIGUSR1. The code was improved to the point where
                it now just looks like an omission.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-25
     </small>
    </td>
    <td>
     Taskserver inherits Taskwarrior's I18N/L10N framework, as the
                basis for possible localizations.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-25
     </small>
    </td>
    <td>
     Taskserver tests now include a 'statistics' request that
                doesn't work. Progress!
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-25
     </small>
    </td>
    <td>
     Taskserver loses some vestigial (broken) code that supported
                hooks and extension scripts. Future releases will include a
                proper hook system, once we figure out what that is.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-26
     </small>
    </td>
    <td>
     Taskwarrior and Taskserver no longer report 'pthreads' linkage in
                diagnostic output. There will be no pthreads usage, instead the
                C++11 std::thread will be used, one day.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-26
     </small>
    </td>
    <td>
     Taskwarrior gains a nearly useless feature: when using the new
                configuration setting:
     <pre>$ task rc.obfuscate=1 ...</pre>
     All output text is replaced by xxx, xxx xxxxxxx xx, so that we
                can share formatted output without revealing private task data.
                This eliminates the need to task-anon.pl.  xxxx.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-26
     </small>
    </td>
    <td>
     The Taskserver PKI scripts now use CN properly, and no longer
                specify DNSNAMES and IPADDRS.  This is better.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-26
     </small>
    </td>
    <td>
     Taskserver reluctantly now provides more clues in debug mode
                as to why certificate validation failed.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-26
     </small>
    </td>
    <td>
     Taskserver's malformed request tests now fail because they are
                deliberately malformed. They did fail because the
     <code>
      client
     </code>
     command was broken.  Progress!
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-26
     </small>
    </td>
    <td>
     Recent Taskserver fixes now allow tests to run with strict
                certificate validation.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-28
     </small>
    </td>
    <td>
     The beginnings of a Japanese translation is submitted for
                Taskwarrior.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-26
     </small>
    </td>
    <td>
     Taskwarrior displays more details in debug mode when sync
                fails certificate validation.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-26
     </small>
    </td>
    <td>
     Reduced the number of segfaults in Taskserver when the incoming
                request contains incorrect types.  For the children.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-04-26
     </small>
    </td>
    <td>
     Taskserver statistics request is working again.
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

