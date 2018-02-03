---
title: 'Workflow Examples'
url: "/docs/workflow.html"
---
<div class="col-md-10 main">
 <div class="row">
  <p class="lead">
   Everyone uses Taskwarrior differently.
              Here are some example workflows, to make you think about your own
              particular approach.
  </p>
  <a name="joshua">
  </a>
  <div class="panel panel-primary">
   <div class="panel-heading">
    <h3 class="panel-title">
     Joshua
    </h3>
   </div>
   <ul class="list-group">
    <li class="list-group-item">
     <strong>
      Where do you use Taskwarrior?
     </strong>
     <br/>
     Everywhere to get track of things.

                  I keep my personal thing separated
                  and two zones for work projects
                  each on it's own git repository.
    </li>
    <li class="list-group-item">
     <strong>
      For what kind of work do you use Taskwarrior?
     </strong>
     <br/>
     At work to organize my projects,
                  chop them into small tasks
                  have a log of what I am doing,
                  and log of how did I solved problems.
    </li>
    <li class="list-group-item">
     <strong>
      How do you sync? What kind of devices do you use?
     </strong>
     <br/>
     I use a custom git hook that commits only
     <code>
      pending.data
     </code>
     and
     <code>
      completed.data
     </code>
     and push to a local private repository where the team also commits,
                  The script also detects completed tasks and the latest version of the task
                  in case multiple versions of the same tasks are found.

                  Currently i'm implementing an annotator to document projects.
    </li>
    <li class="list-group-item">
     <strong>
      Which is your default report?
     </strong>
     <br/>
     Task next, with customized filter and sort order:
     <code>
      rc.report.next.filter=status:pending,+UNBLOCKED
     </code>
     <br/>
     <code>
      report.next.sort=status-,start-,priority-,project+,due+
     </code>
    </li>
    <li class="list-group-item">
     <strong>
      Do you use a standard or customized methodology?
     </strong>
     <br/>
     Mostly GTD, but will try to add kanban elements.
    </li>
    <li class="list-group-item">
     <strong>
      Do you use extensions? Hook scripts?
     </strong>
     <br/>
     Custom git synchronization script.

                  Posibly custom git editor script.
    </li>
    <li class="list-group-item">
     <strong>
      What features do you rely on most?
     </strong>
     <br/>
     I use start to see what I'm doing,
                  but i'd like to use it to keep track of the time,
                  so I'll need another mecanism to use kanban like «In progress».

                  I use annotations to document procedures or important things.

                  I also use projects, tags, scheduled and due dates to classify tasks.
    </li>
    <li class="list-group-item">
     <strong>
      What features do you deliberately not use?
     </strong>
     <br/>
     No urgency.

                  No undo (as that goes in git).
    </li>
    <li class="list-group-item">
     <strong>
      How do you review your list?
     </strong>
     <br/>
     I usually use
     <code>
      task
     </code>
     to see what's in progress and continue doing that.

                  I have my tasks sorted by projects and priority,
                  so I'll seek the project that needs to advance and check the most important task for that.
    </li>
    <li class="list-group-item">
     <strong>
      Other Notes
     </strong>
     <br/>
     I'd like an easy to deploy kanban like project visualization tool.
    </li>
   </ul>
  </div>
  <a name="paul">
  </a>
  <div class="panel panel-primary">
   <div class="panel-heading">
    <h3 class="panel-title">
     Paul
    </h3>
   </div>
   <ul class="list-group">
    <li class="list-group-item">
     <strong>
      Where do you use Taskwarrior?
     </strong>
     <br/>
     I use Taskwarrior at home.
    </li>
    <li class="list-group-item">
     <strong>
      For what kind of work do you use Taskwarrior?
     </strong>
     <br/>
     I mostly use it for software development projects, but there are
                  some other projects including training.

                  Taskwarrior was mostly developed using Taskwarrior to track
                  features and bugs.
    </li>
    <li class="list-group-item">
     <strong>
      How do you sync? What kind of devices do you use?
     </strong>
     <br/>
     I use Taskserver, set up on a VPS, to sync two clients, a
                  laptop and desktop. I am one of several people using that Taskserver.
    </li>
    <li class="list-group-item">
     <strong>
      Which is your default report?
     </strong>
     <br/>
     I use the
     <code>
      next
     </code>
     report most often, and have tweaked
                  the coefficients to represent my definition of urgent.
                  The
     <code>
      next
     </code>
     report doesn't yield surprises, so I can
                  rely on it.  I don't have any of my own custom reports.
    </li>
    <li class="list-group-item">
     <strong>
      Do you use a standard or customized methodology?
     </strong>
     <br/>
     I don't follow any standard methodology.

                  I use project hierarchies (tw, tw.242, tw.250 ...) so I can
                  look at projects at different levels.
    </li>
    <li class="list-group-item">
     <strong>
      Do you use extensions? Hook scripts?
     </strong>
     <br/>
     I have two hook scripts active.  One is an on-add hook script
                  that converts 'tw-123' to 'https://bug.tasktools.org/browse/TW-123'.

                  The other is also an on-add hook that warns me when I add a
                  task without a project.
    </li>
    <li class="list-group-item">
     <strong>
      What features do you rely on most?
     </strong>
     <br/>
     I rely on
     <code>
      sync
     </code>
     ,
     <code>
      next
     </code>
     and virtual tags
                  a lot.

                  I use 'wait' to hide things.  This is because I prefer to
                  look at shorter lists.
    </li>
    <li class="list-group-item">
     <strong>
      What features do you deliberately not use?
     </strong>
     <br/>
     I do not use priorities at all. I did use them, but found that
                  I spent too much time fiddling with the values.
                  I think priority is a fluid thing, shifting a lot, and having
                  these values assigned just means a lot of maintenance work.
    </li>
    <li class="list-group-item">
     <strong>
      How do you review your list?
     </strong>
     <br/>
     I use a new review feature in tasksh, which is not completed
                  yet but is proving effective already. This will be released
                  in early 2016.

                  I have not yet developed good review habits, so it happens
                  less often that it should.
    </li>
    <li class="list-group-item">
     <strong>
      Other Notes
     </strong>
     <ul>
      <li>
       I don't use due dates unless there really is a hard, real-world due date.
      </li>
      <li>
       I use dependencies when there are several related tasks and a clear sequence, but there aren't that many.
      </li>
      <li>
       I use
       <code>
        start
       </code>
       and
       <code>
        stop
       </code>
       to indicate what I am currently working on, so I can remember where to pick up the next day.
      </li>
      <li>
       I use a few keyword-based color rules so that groups of things I care about stand out in lists. I color the
       <code>
        Documentation
       </code>
       and
       <code>
        Performance
       </code>
       keywords, and the
       <code>
        +bug
       </code>
       tag.
      </li>
      <li>
       My list is mainly things I don't want to forget, not a list of things I need to do today.
      </li>
     </ul>
    </li>
   </ul>
  </div>
  <a name="tomas">
  </a>
  <div class="panel panel-primary">
   <div class="panel-heading">
    <h3 class="panel-title">
     Tomas
    </h3>
   </div>
   <ul class="list-group">
    <li class="list-group-item">
     <strong>
      Where do you use Taskwarrior?
     </strong>
     <br/>
     I use a separate Taskwarrior database for tracking of my daily habits. This is achieved by setting
     <code>
      alias habit="task rc.data.location=~/.habit"
     </code>
     in my .bashrc.
    </li>
    <li class="list-group-item">
     <strong>
      For what kind of work do you use Taskwarrior?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      How do you sync? What kind of devices do you use?
     </strong>
     <br/>
     Currently, I am using only one laptop, so I am not using sync.
                  Nevertheless, in the past I did use sync.
    </li>
    <li class="list-group-item">
     <strong>
      Which is your default report?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      Do you use a standard or customized methodology?
     </strong>
     <br/>
     I have a default.project set to Inbox, where every task goes initially, unless I assign its particular project directly when adding it. Every task belongs to a project. Project hierarchy corresponds to different areas of my life, and I use subprojects a lot. Project examples include 'Work.Tickets', 'Home' or 'Volunteering.Floss.Taskwarrior'.
    </li>
    <li class="list-group-item">
     <strong>
      Do you use extensions? Hook scripts?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      What features do you rely on most?
     </strong>
     <br/>
     Since I use projects to distinguish areas in which the tasks fall, I tend to use tags to distinguish what kind of a task it is. Currently, I only use this consistently for programming-related activities (+bug, +rfe, +test, etc.), but I plan to expand that in the future. I try to not add new tags carelessly. I use new tags only after careful consideration.
                  I use due dates both for real-world deadlines and self-imposed deadlines. This is probably wrong, since I tend to shift tasks a lot then, and I treat the 'due date' with much less importance than it deserves. I should move to scheduled for self-imposed deadlines.
                  I use dependencies for enumerating sub-tasks of any bigger tasks that need to be broken down into individual steps. Since entering dependencies requires more work (enumerating IDs), I usually do this step in taskwiki, which can set dependencies by indentation. I do not have multiple blocked task for one task, so my task lists can be shown in the form of a dependency tree.
    </li>
    <li class="list-group-item">
     <strong>
      What features do you deliberately not use?
     </strong>
     <br/>
     I do not use priorities much. I just never felt the need to.
                  I do not use reports very often. This is due to the fact that Taskwarrior currently cannot display dependency trees, which coupled with my habit of breaking down tasks into small subtasks makes the task lists often confusing. I suppose I could try configuring Taskwarrior to exclude the child tasks by default, but it only occurred to me now.
                  I do not use any custom color rules yet.
    </li>
    <li class="list-group-item">
     <strong>
      How do you review your list?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      Other Notes
     </strong>
     <ul>
      <li>
       When deciding how to continue with a given project, I open the corresponding taskwiki file, which serves as a permanent dynamic report coupled with project-related notes.
      </li>
      <li>
       I use simple contexts that usually are just implicit project selectors, such as
       <code>
        project:Work
       </code>
       .
      </li>
      <li>
       I use
       <code>
        start
       </code>
       and
       <code>
        stop
       </code>
       to indicate what I am currently working on. I have a little tmux powerline plugin, which displays the description of the currently active task (within the selected context), which helps me to focus back on the currently active task if I manage to distract myself.
      </li>
      <li>
       I use taskwiki to generate a daily journal of tasks that need to be completed on the given day. I also use this file to review my day in few lines. This gives me an ability to quickly see what I did on an particular day.
      </li>
      <li>
       My list attempts to be not only a list of tasks I must remember, but a somewhat accurate description of what I did. I even tend to create and log new completed tasks for stuff that was not planned, but was achieved on any given day.
      </li>
     </ul>
    </li>
   </ul>
  </div>
  <a name="dirk">
  </a>
  <div class="panel panel-primary">
   <div class="panel-heading">
    <h3 class="panel-title">
     Dirk
    </h3>
   </div>
   <ul class="list-group">
    <li class="list-group-item">
     <strong>
      Where do you use Taskwarrior?
     </strong>
     <br/>
     I do not use Taskwarrior at work, because my work systems are
                  behind strict proxies, but I manage my work tasks with private
                  devices to have all todo-items in one solution.

                  I experimented a lot with nearly each and every features of
                  Taskwarrior and came back to the basics recently.
    </li>
    <li class="list-group-item">
     <strong>
      For what kind of work do you use Taskwarrior?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      How do you sync? What kind of devices do you use?
     </strong>
     <br/>
     I use Taskwarrior on every device with a full, non-proxied
                  internet connection and sync those installations with a self-hosted
                  Taskserver on the net. All devices have the same configuration.
                  "Every device" includes my notebook (Fedora Linux), a fix home-based
                  computer (CentOS), four servers on the net (CentOS) and my mobile
                  phone and my tablet as well (both Android).
    </li>
    <li class="list-group-item">
     <strong>
      Which is your default report?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      Do you use a standard or customized methodology?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      Do you use extensions? Hook scripts?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      What features do you rely on most?
     </strong>
     <br/>
     Nearly all of my tasks have due dates, even though I am not able to do some of them in time.
                  My most important modifier is wait. This is how I keep my todolist clean.
                  I am using projects and subprojects to organize my tasks. That makes filtering easy for me.
                  On the other hand I do not use any tags apart from virtual tags.
                  To do work in a specific area I filter my tasks with projects, but I think I will change to use contexts instead.
                  I like annotations and use them a lot. On the one hand to set my longterm goals (private and business wise), on the other hand I annotate tasks with links.
                  To make handling of annotations easier, I love
     <a href="https://github.com/ValiValpas/taskopen">
      taskopen
     </a>
     on my desktop and strictly recommend this to everyone.
    </li>
    <li class="list-group-item">
     <strong>
      What features do you deliberately not use?
     </strong>
     <br/>
     Very seldom I use dependencies, mostly I steer that with time
                  constraints. Task B has a due date end-of-work-week and task B
                  has a wait-date till beginning of next work-week. I do not use
                  priorities at all.
    </li>
    <li class="list-group-item">
     <strong>
      How do you review your list?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      Other Notes
     </strong>
     <ul>
      <li>
       I run a minimal configuration, choosing a theme that pleases me, Monday as weekstart,
       <code>
        calendar.details=full
       </code>
       and
       <code>
        calendar.holidays=sparse
       </code>
       .
      </li>
      <li>
       Even though that does not make much sense I use
       <code>
        wait:someday
       </code>
       sometimes to move tasks completely out of the way. (Hint: you can find them with
       <code>
        task waiting
       </code>
       ).
      </li>
      <li>
       I do not write everything into Taskwarrior. I have a brain and I am willing to use it ;-)
      </li>
     </ul>
    </li>
   </ul>
  </div>
  <a name="Fredde">
  </a>
  <div class="panel panel-primary">
   <div class="panel-heading">
    <h3 class="panel-title">
     Fredde
    </h3>
   </div>
   <ul class="list-group">
    <li class="list-group-item">
     <strong>
      Where do you use Taskwarrior?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      For what kind of work do you use Taskwarrior?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      How do you sync? What kind of devices do you use?
     </strong>
     <br/>
     Taskserver for "backup" - have used git on the task folder previously.
                  Two separate (logical and physical (different computers/servers)) task installations - one for work, one for private tasks.
    </li>
    <li class="list-group-item">
     <strong>
      Which is your default report?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      Do you use a standard or customized methodology?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      Do you use extensions? Hook scripts?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      What features do you rely on most?
     </strong>
     <br/>
     Projects and tags to simulate state of tasks like in Kanban.
                  Easy basic reports to filter on project and then on "state tags".
                  Annotations to record information or refer to my big-arse-text-file-from-hell.
                  Task calendar is used a lot to find out about calendar weeks and dates at work.
    </li>
    <li class="list-group-item">
     <strong>
      What features do you deliberately not use?
     </strong>
     <br/>
     No due dates at all.
                  No urgency; I read through the list and decide on the most "obvious” task (whatever that means).
    </li>
    <li class="list-group-item">
     <strong>
      How do you review your list?
     </strong>
     <br/>
    </li>
    <li class="list-group-item">
     <strong>
      Other Notes
     </strong>
     <ul>
     </ul>
    </li>
   </ul>
  </div>
 </div>
 <br/>
 <br/>
</div>

