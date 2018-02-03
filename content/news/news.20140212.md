---
date: 2014-02-12
title: 'Git Hosting has migrated'
aliases: ['/news/news.20140212.html']
---
<div class="col-md-8 main">
 <div class="row">
  <h3>
   Git Hosting has migrated
   <small>
    2014-02-12
   </small>
  </h3>
  <p>
   The new repository manager, Stash, is running on the new server:
  </p>
  <p>
   <code>
    https://git.tasktools.org
   </code>
  </p>
  <p>
   The old server will still be active for a little while longer, but
            will not be updated, so the repositories there are read-only and
            already out of date. You can re-clone your Taskwarrior repository
            from the new server, or update the origin URLs in your existing
            clone like this:
  </p>
  <pre>$ cd task.git
$ git config remote.origin.url https://git.tasktools.org/TM/task.git</pre>
  <p>
   Similarly for Taskserver:
  </p>
  <pre>$ cd taskd.git
$ git config remote.origin.url https://git.tasktools.org/TM/taskd.git</pre>
  <p>
   The continuous integration servers are currently offline, and will return shortly.
  </p>
 </div>
</div>

