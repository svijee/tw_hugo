---
date: 2014-04-29
title: 'Teaching the Parser New Tricks'
aliases: ['/news/news.20140429.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Teaching the Parser New Tricks
   <small>
    2014-04-29
   </small>
  </h3>
  <p>
   With Taskwarrior version 2.4.0, we are building a better command
            line parser. In addition to fixing a lot of annoying little bugs,
            we would like it to be more flexible and robust. That means it will
            be able to handle more strange inputs than before, but can it do
            better?
  </p>
  <p>
   We would like to see your most strange, supported or unsupported,
            twisted, Taskwarrior command line that you think should
   <em>
    just work
   </em>
   .
  </p>
  <p>
   For example, we dislike escaping shell characters, so I want this to
   <em>
    just work
   </em>
   :
  </p>
  <pre>$ task "(project = foo or project = bar) and +tag" list</pre>
  <p>
   We want to be able to quote the whole command line as one big
            argument, so the parentheses don't need to be individually escaped.
  </p>
  <p>
   What do you want to
   <em>
    just work
   </em>
   ? Please submit answers here:
   <a href="https://answers.tasktools.org/questions/1114275/what-is-your-most-complexawful-taskwarrior-command-line">
    https://answers.tasktools.org
   </a>
  </p>
  <p>
   <a href="https://bug.tasktools.org/secure/Signup!default.jspa">
    Registration
   </a>
   for the site is here.  Thank you.
  </p>
 </div>
</div>

