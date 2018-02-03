---
date: 2015-05-10
title: 'Taskwarrior 2.4.4 Released'
aliases: ['/news/news.20150510.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Taskwarrior 2.4.4 Released
   <small>
    2015-05-10
   </small>
  </h3>
  <p>
   Taskwarrior 2.4.4 is released.

            Although a minor release, there are significant bug fixes
            which make this a recommended upgrade. Changes include:
  </p>
  <p>
   <ul>
    <li>
     Fixed a problem where the wrong task may be updated, if GC is disabled. This is the primary reason for the release.
    </li>
    <li>
     Fixed a problem where filters including parenthesized tags (
     <code>
      ... and (+DUE or +OVERDUE)
     </code>
     ) were incorrectly handled.
    </li>
    <li>
     32-bit platform support.
    </li>
    <li>
     The
     <code>
      obfuscate
     </code>
     configuration setting will hide private data, intended for bug reporting.
    </li>
    <li>
     An early Japanese localization.
    </li>
    <li>
     Several bug fixes.
    </li>
   </ul>
   For full details, see the ChangeLog file included in the release.
  </p>
  <p>
   Please bear in mind that
   <a href="http://gnutls.org/">
    GnuTLS
   </a>
   is a security product, and it is important that you use the most
            recent version available.  Please upgrde GnuTLS before building
            Taskwarrior and Taskserver.
  </p>
  <p>
   The release is immediately available as a source
   <a href="/download?pk_campaign=twitter&amp;pk_kwd=task-2.4.4">
    tarball
   </a>
   .
            Binary packages will soon be available via your Operating System's
            package manager.
  </p>
  <br/>
  <br/>
 </div>
</div>

