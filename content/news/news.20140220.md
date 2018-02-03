---
date: 2014-02-20
title: 'VIT 1.2 beta1 is available'
aliases: ['/news/news.20140220.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   VIT 1.2 beta1 is available
   <small>
    2014-02-20
   </small>
  </h3>
  <p>
   Beta1 of the VIT front-end for Taskwarrior is available for download now.
  </p>
  <p>
   Download here:
   <a href="http://taskwarrior.org/download/vit-latest.tar.gz">
    vit-1.2.beta1.tar.gz
   </a>
   .
  </p>
  <p>
   VIT 1.2 brings a customizable way to interact with your tasks with
            user-defined shortcuts. You can now define keys to launch external
            commands with the currently selected task as input. Keybinds can now
            be specified in ~/.vitrc. For example, to use the external script
   <a href="">
    tasknote
   </a>
   (http://taskwarrior.org/projects/1/wiki/Tasknote)
            when you press "ctrl + n", you can do:
   <pre>map \cn=:!wr tasknote %TASKID&lt;Return&gt;</pre>
   Suppose you currently have highlighted a task with ID 20. Then the
            command
   <code>
    tasknote 20
   </code>
   would be run by your shell.
   <code>
    !:
   </code>
   is the VIT command to run external commands;
   <code>
    w
   </code>
   tells VIT to wait until that process finishes and to
            show you the result before going back to the VIT screen (this
            allows you to write the note for tasknote in your editor); and
   <code>
    r
   </code>
   tells VIT to reread your task data after the process
            finishes.
  </p>
  <p>
   See
   <code>
    man vitrc
   </code>
   for more information and examples.
  </p>
  <p>
   Navigation is improved: in the prompts, backspace now removes a
            character and the arrow keys can be used.
  </p>
  <p>
   Key changes:
   <ul>
    <li>
     <code>
      gg
     </code>
     moves to the top of the task list
    </li>
    <li>
     <code>
      D
     </code>
     now deletes a task when not over an annotation
    </li>
    <li>
     <code>
      s
     </code>
     runs
     <code>
      task sync
     </code>
     (task &gt; 2.30 required)
    </li>
    <li>
     <code>
      !:
     </code>
     runs a command in the shell (and replaces %TASKID with the selected task ID)
    </li>
    <li>
     <code>
      c
     </code>
     is renamed to
     <code>
      m
     </code>
     (for
     <em>
      modify
     </em>
     so more consistent with Taskwarrior)
    </li>
    <li>
     <code>
      P [hmln]
     </code>
     now sets priority
    </li>
    <li>
     <code>
      q
     </code>
     (
     <code>
      Q
     </code>
     ) now quits with(out) confirmation
    </li>
   </ul>
  </p>
  <p>
   Misc:
   <ul>
    <li>
     Fix freezing behavior (caused because Taskwarrior was waiting for input)
    </li>
    <li>
     Fix a bug where prompt text was invisible when switching tabs in gnome-terminal
    </li>
    <li>
     Clear project prompt string with escape
    </li>
   </ul>
  </p>
  <p>
   Please email
   <a href="mailto:skostysh@princeton.edu">
    skostysh@princeton.edu
   </a>
   if you have any problems or questions.
  </p>
 </div>
</div>

