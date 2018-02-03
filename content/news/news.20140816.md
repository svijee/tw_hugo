---
date: 2014-08-16
title: Development Status
aliases: ['/news/news.20140816.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Development Status
   <small>
    2014-08-16
   </small>
  </h3>
  <p>
   Development is shifting focus for Taskwarrior and Taskserver. No
            more features will be added, and completeness, stability and testing
            become the new focus.
  </p>
  <p>
   The goal is to work towards good beta releases. There is no schedule
            for this work for a couple of reasons; we are more concerned with
            quality than delivery date, and as an all-volunteer organization,
            participation is not predictable
            (
   <a href="/docs/contribute.html">
    you can help
   </a>
   ).
  </p>
  <p>
   Although Taskwarrior 2.3.0, 2.4.0, and Taskserver 1.0.0, 1.1.0 are
            all compatible with each other, there will be an almost simultaneous
            release of the updates, as they work together better.
  </p>
  <p>
   The
   <code>
    tasksh
   </code>
   program, which was bundled with Taskwarrior,
            is now broken out as a separate project, which allows it to follow
            its own release schedule and not be slowed down by the less frequent
            Taskwarrior releases. This also allows it to implement features that
            are a little outside the scope of Taskwarrior.
  </p>
  <h4>
   Taskwarrior 2.4.0
  </h4>
  <p>
   This is a major update for Taskwarrior, probably the largest. The
            main focus is a new command line parser, which brings with it new
            capabilities, mainly the ability to perform calculations at the
            command line.
   <ul>
    <li>
     New command line parser, with fewer quirks and support for new
                features.
    </li>
    <li>
     New
     <code>
      calc
     </code>
     command, which shows off the expression
                evaluation capabilities that are built in to many other commands.
                This allows you to refer to a task's due date, for example, and
                add a week to it, in addition to basic math.
    </li>
    <li>
     Lots of new virtual tags, which are now used in the custom report
                definitions, for simpler filters.
    </li>
    <li>
     New report improvements and streamlining - the result of many
                years of use and consideration by our designer, urgency calculation
                details, configuration default values, listing breaks.
    </li>
    <li>
     Features: multiline task descriptions, UUID partial matching,
                default
     <code>
      info
     </code>
     report when just an ID/UUID is specified,
                propagated urgency values, improved color rules, new themes,
                default support for regular expressions.
    </li>
    <li>
     Documentation: new command reference design.
    </li>
    <li>
     I18N: more languages, better coverage.
    </li>
    <li>
     Add-ons: improved completion support.
    </li>
    <li>
     Portability: improvements for Solaris, NetBSD, fewer sh/bash
                assumptions, musl C library support.
    </li>
    <li>
     Security: better GnuTLS support, better certificate verification
                and handling, better sync diagnostics.
    </li>
    <li>
     Many documentation improvements, in both man pages and online.
    </li>
    <li>
     Bug fixes, currently around 100 issues resolved, with more coming.
    </li>
   </ul>
  </p>
  <h4>
   Taskserver 1.1.0
  </h4>
  <p>
   This is a much smaller release, which is focusing on improved security,
           stability and diagnostics, with simplified setup.
   <ul>
    <li>
     Diagnostic improvements: can log to stdout, includes line numbers
               for data issues, uses more consistent language, log indicates when
               server is ready, shows data statistics with the diagnostic command
               is provided with '--data'.
    </li>
    <li>
     Portability fixes for NetBSD, Solaris, musl C library, fewer
               sh/bash assumptions.
    </li>
    <li>
     Networking: Improved IPv6 support, now obeys hostname.
    </li>
    <li>
     Security: certificates are now validated for older GnuTLS versions.
    </li>
    <li>
     Configutaion: improved PKI scripts, CRL cert is now optional,
               optional hostname verification, removed client.allow/client.deny
               confirugation, new interactive script for easy setup.
    </li>
    <li>
     Documentation corrections, improvements.
    </li>
    <li>
     Add-ons: systemd startup script.
    </li>
    <li>
     Bug fixes, currently around 20 issues resolved, with more coming.
    </li>
   </ul>
  </p>
  <h4>
   Tasksh 1.0.0
  </h4>
  <p>
   The
   <code>
    tasksh
   </code>
   program has been rewritten. This gives it a
            more solid foundation, and potential for future improvements that
            may include timing, reminders, extensions and complementary features.

            Initially,
   <code>
    tasksh
   </code>
   will be a minimally functional release.
   <ul>
    <li>
     Stability: as a standalone program with no dependency on
                Taskwarrior, the shell is more lightweight and stable.
    </li>
    <li>
     libreadline support.
    </li>
   </ul>
  </p>
 </div>
</div>

