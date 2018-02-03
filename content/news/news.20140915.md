---
date: 2014-09-15
title: Taskwarrior 2.4.0 beta1
aliases: ['/news/news.20140915.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Taskwarrior 2.4.0 beta1
   <small>
    2014-09-15
   </small>
  </h3>
  <p>
   Taskwarrior 2.4.0 is in beta, and available as a source
   <a href="/download/task-latest.tar.gz">
    tarball
   </a>
   .
   <ul>
    <li>
     Calc command
     <code>
      task calc '1 + 1'
     </code>
     Hint: it's '2', but
                it's a beta, so who knows? And yes, it can do more than that.
    </li>
    <li>
     Enhanced DOM support
     <code>
      task add due:123.due
     </code>
    </li>
    <li>
     Date math
     <code>
      task add ... due:eom wait:'due - 1week'
     </code>
    </li>
    <li>
     Unicode:
     <code>
      task add \\u2615
     </code>
    </li>
    <li>
     New command line parser. Why would you care? You wouldn't. But
                we do, because it lets us be creative and add more useful features.
    </li>
    <li>
     Better
     <code>
      task show
     </code>
     command, that includes default values.
    </li>
    <li>
     Hooks. Yeah.
    </li>
    <li>
     ISO-8601 date support
     <code>
      task add ... due:2014-09-15T18:59:00
     </code>
     and about 30 other formats too, independent of
     <code>
      rc.dateformat
     </code>
     .
    </li>
    <li>
     The
     <code>
      task info
     </code>
     report now shows more ... stuff.
    </li>
    <li>
     More virtual tags.  That work now.
    </li>
    <li>
     New localizations.  Now there are eng-USA, esp-ESP, fra-FRA,
                ita-ITA, por-PRT, epo-RUS.  Dolphin and Klingon next.
    </li>
   </ul>
  </p>
  <p>
   Tasksh 1.0.0 is also in beta, and available as a source
   <a href="/download/tasksh-latest.tar.gz">
    tarball
   </a>
   .
            Features in tasksh include:
   <ul>
    <li>
     Libreadline support for command line history.  So you can hit
     <code>
      Up-Arrow
     </code>
     , which we know you've dreamed of.
    </li>
    <li>
     Nothing else. Because this replaces the old one, which did nothing and also crashed.
    </li>
    <li>
     It doesn't crash.  Or does it?  Let us know.
    </li>
    <li>
     It is a separate project now, and not bundled with Taskwarrior.
    </li>
   </ul>
   Features are being planned for tasksh, and with subsequent releases
            you'll see it grow into a useful addition. Or not. Who knows what
            future portends?
  </p>
  <p>
   But seriously, we need your help and feedback testing this.  It's a
            big release.
  </p>
  <p>
   Please note that this is beta software, and not suitable for
            everyday use.  We welcome your feeback in the form of
   <a href="https://bug.tasktools.org">
    bug submissions
   </a>
   ,
            and general
   <a href="https://answers.tasktools.org">
    Questions &amp; Answers
   </a>
   .
  </p>
 </div>
</div>

