---
date: 2015-04-04
title: Taskserver 1.1.0 beta1 Released
aliases: ['/news/news.20150504.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Taskserver 1.1.0 beta1 Released
   <small>
    2015-04-04
   </small>
  </h3>
  <p>
   Taskserver 1.1.0 is in beta, and we are asking you to please test
            this release in your environment.

            See http://taskwarrior.org/docs/taskserver/upgrade.html for
            instructions to upgrade your server.

            There have been a few changes:
  </p>
  <h4>
   Configuration
  </h4>
  <ul>
   <li>
    New setup helper script,
    <code>
     setup_server.bash
    </code>
    , which interactively leads the whole setup and configuration process.
   </li>
   <li>
    When hosting, the configured server name is no longer ignored.
   </li>
   <li>
    Taskserver can now be restricted to IPv4 or IPv6.
   </li>
   <li>
    New man page for
    <code>
     taskdctl
    </code>
    .
   </li>
   <li>
    Server now supports a configuration setting
    <code>
     trust
    </code>
    , which can be either
    <code>
     strict
    </code>
    or
    <code>
     allow all
    </code>
    , and defaults to
    <code>
     strict
    </code>
    .
   </li>
  </ul>
  <h4>
   Security
  </h4>
  <ul>
   <li>
    Configurable client certificate verification.
   </li>
   <li>
    Improved PKI scripts.
   </li>
   <li>
    Certificate examples now use CN, and not SANs.
   </li>
   <li>
    CRL certificate is now optional.
   </li>
   <li>
    Added certificate verification to GnuTLS versions older than 2.9.10.
   </li>
  </ul>
  <h4>
   Features
  </h4>
  <ul>
   <li>
    The
    <code>
     statistics
    </code>
    request is now supported.
   </li>
   <li>
    <code>
     validate
    </code>
    command will parse/validate a JSON string or file.  Used for debugging Taskserver clients.
   </li>
   <li>
    If the
    <code>
     trust
    </code>
    setting contains a bad value, the
    <code>
     diagnostics
    </code>
    command will indicate this, and the server will log it.
   </li>
   <li>
    Can log to STDOUT when configuration setting
    <code>
     log
    </code>
    is set to '-'.
   </li>
   <li>
    Improved
    <code>
     diagnostics
    </code>
    command output.
   </li>
   <li>
    Taskserver no longer ignore the host definition.
   </li>
   <li>
    Improved logging for erros, problems, data conflicts, JSON parsing ...
   </li>
   <li>
    Systemd script:
    <code>
     taskd.service
    </code>
    .
   </li>
  </ul>
  <h4>
   Portability
  </h4>
  <ul>
   <li>
    Taskserver builds with the musl library
   </li>
   <li>
    Removed linking of pthreads.
   </li>
  </ul>
  <h4>
   Miscellaneous
  </h4>
  <ul>
   <li>
    Improved I/O performance with better defaults for buffer sizes.
   </li>
   <li>
    Removed support for
    <code>
     client.allow
    </code>
    /
    <code>
     client.deny
    </code>
    settings.
   </li>
   <li>
    Documentation improvements.
   </li>
   <li>
    Most documentation moved online, to keep it more current and correct.
   </li>
   <li>
    Many bug fixes.
   </li>
  </ul>
  <p>
   For full details, see the ChangeLog file included in the release.

            The release is immediately available as a source
   <a href="/download/taskd-latest.tar.gz">
    tarball
   </a>
   .
  </p>
  <p>
   This is a beta release, and is not recommended for stable environments.
  </p>
  <br/>
  <br/>
 </div>
</div>

