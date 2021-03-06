---
date: 2015-03-31
title: 'Activity Digest: March 2015'
aliases: ['/news/news.20150331.html']
---
<div class="col-md-8 main">
 <div class="row">
  <p>
   This is an ongoing series of activity reports, published monthly,
            to highlight activity in the Taskwarrior project. Here is what
            happened in March 2015.
  </p>
  <table class="table table-striped table-compact">
   <tr>
    <td style="white-space: nowrap;">
     <small>
      2015-03-01
     </small>
    </td>
    <td>
     The
     <a href="/docs/hooks.html">
      Hooks Design
     </a>
     page was moved
                out of the design section onto the main page.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-01
     </small>
    </td>
    <td>
     Scott pointed out that there is a performance drop since 2.3.0,
                which was fixed and further improved. The major cause of this
                was on-load recurrence value mapping, which was not being done
                efficiently.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-01
     </small>
    </td>
    <td>
     A new
     <a href="/docs/hooks_guide.html">
      Hook Author's Guide
     </a>
     shows how to write and test a hook script.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-03
     </small>
    </td>
    <td>
     Renato gives the test suite the option to use task/taskd from
                $PATH.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-05
     </small>
    </td>
    <td>
     Wim finds an fixes a particularly nasty hook bug, that is causing
     <code>
      on-modify
     </code>
     hook scripts to fail to update the actual
                tasks. This also exposes a weakness in the unit testing. This
                find will likely lead to a release of 2.4.2.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-07
     </small>
    </td>
    <td>
     The test suite undergoes reorganization, to combine like tests,
                remove redundant tests, and migrate bug tests into feature test
                scripts. While this is happening, tests are being converted from
                Perl to Python.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-09
     </small>
    </td>
    <td>
     The
     <code>
      _version
     </code>
     command now shows both the version
                number and the commit hash all the time.  Prior to this, the
                different information was shown depending on whether Taskwarrior
                was built from git or from a tarball.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-12
     </small>
    </td>
    <td>
     Renato gives the Python unit tests some color, which makes the
                output more readable in a tty.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-15
     </small>
    </td>
    <td>
     The color themes are updated to remove all the very-low
                contrast and inappropriate colors. The online theme swatches
                are updated.
     <a href="http://taskwarrior.org/docs/themes.html">
      http://taskwarrior.org/docs/themes.html
     </a>
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-16
     </small>
    </td>
    <td>
     Taskwarrior 2.4.2 released, mainly to address the hook problem,
                but has the nice side effect of releasing the context features
                and updated themes.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-18
     </small>
    </td>
    <td>
     Tomas updates the bash completion script to solve a problem
                when it tries to get confirmation from the user.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-18
     </small>
    </td>
    <td>
     Tomas adds the
     <code>
      calc
     </code>
     command to the man page,
                which was oddly missing.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-21
     </small>
    </td>
    <td>
     Tomas gives the
     <code>
      bulk
     </code>
     setting a new meaning for
                the value zero - infinity, which means that Taskwarrior never
                considers an modification to be too big.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-23
     </small>
    </td>
    <td>
     Wim fixes a bug so that all local modifications update the
     <code>
      modified
     </code>
     attribute, and these modifications are
                hidden from the journal.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-26
     </small>
    </td>
    <td>
     Wim fixes a dependency chain urgency calculation bug, which
                was reporting the wrong value after a
     <code>
      done
     </code>
     /
     <code>
      delete
     </code>
     command.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-28
     </small>
    </td>
    <td>
     The new Lexer gains a few hundred new tests, to make sure
                that all types are properly recognized. The full integration
                of the new Lexer begins soon.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-29
     </small>
    </td>
    <td>
     Wim enables compiler warnings. The removal effort begins.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-30
     </small>
    </td>
    <td>
     Wim fixes the export scripts, which has rotted, as software
                does, when ignored for long enough.
    </td>
   </tr>
   <tr>
    <td>
     <small>
      2015-03-31
     </small>
    </td>
    <td>
     Wim improves the on-exit sample hook, which was misleading.
    </td>
   </tr>
  </table>
  <br/>
  <br/>
 </div>
</div>

