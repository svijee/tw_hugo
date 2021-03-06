---
title: "Best Practices"
url: '/docs/best-practices.html'
---
<div class="col-md-10 main">
 <div class="row">
  <p>
   If you have installed Taskwarrior and gone through the intro and
              some of the tutorials, you may be wondering how to start using
              some features to help you organize your work. This is a simple
              tutorial, not intended to be complete, or methodology-specific,
              but just a start, to get you thinking about your task list, and
              how you might better rely on it.
  </p>
  <p>
   The default report (the report that runs when you just enter
   <code>
    task
   </code>
   ) is the
   <code>
    next
   </code>
   report. This is a
              report where the tasks are sorted by urgency, with the most urgent
              at the top. The report cuts off after one page, so it is really
              just a list of the most urgent tasks. With a few tips to follow,
              the
   <code>
    next
   </code>
   report can be your most valuable resource.
              Here are the tips for making the
   <code>
    next
   </code>
   report work in
              your favor.
  </p>
  <a name="tips">
  </a>
  <h4>
   Tips
  </h4>
  <p>
   You'll notice that these tips are all about providing more context
              and metadata for tasks. If all you need is a simple shopping list,
              then switch back to pencil and paper, you'll be happier. But if
              you want some sophistication and the ability to manipulate and
              view the data...
  </p>
  <p>
   <ul>
    <li>
     Capture all the tasks and details that you can.  Getting the
                  information off your mind and onto the list reduces the amount
                  of details you need to remember, and reduces the things you
                  might forget.
    </li>
    <li>
     Assign a project to your tasks if possible:
     <pre>task ID modify project:Home</pre>
    </li>
    <li>
     Assign due dates where appropriate, for the important tasks:
     <pre>task ID modify due:31st</pre>
     Don't overdo this though, as a delay might force you to spend
                  too much time reorganizing everything.
    </li>
    <li>
     When you start working on a task, mark it started:
     <pre>task ID start</pre>
     This is a great reminder after a weekend, of what you were doing
                  on Friday that should be continued.
    </li>
    <li>
     If you know the priority of a task:
     <pre>task ID modify priority:M</pre>
     But don't fall into the trap of shifting the priorities too
                  often, as you'll waste a lot of time.
    </li>
    <li>
     Add useful tags to a task:
     <pre>task ID modify +problem +house</pre>
     This is very useful for filtering.
    </li>
    <li>
     Add the special tag +next to a task, to boost its urgency:
     <pre>task ID modify +next</pre>
    </li>
    <li>
     Represent dependencies, where appropriate, because there is a
                  big difference in the urgency of a blocking task, than that
                  of a blocked task:
     <pre>task ID modify depends:OTHER_ID</pre>
    </li>
    <li>
     Try not to have large, long-term tasks that will sit on your
                  list forever. It can be very satisfying and motivating to
                  complete tasks, so create more, but smaller, tasks.
                  Don't have a 'learn Japanese' task, instead have a 'Complete
                  chapter 1' task instead, it's more readily achievable, and
                  you can more easily see progress, which can be motivating.
    </li>
   </ul>
  </p>
  <a name="how">
  </a>
  <h4>
   How That Helps
  </h4>
  <p>
   The
   <code>
    next
   </code>
   report is sorted by urgency. Urgency is just
              a number, but a number calculated using a polynomial that
              considers many aspects of your tasks. What this means is that the
              more information you provide with your tasks, the more accurate
              the
   <code>
    next
   </code>
   report becomes, and the more closely it
              approximates your own notion of urgency.
  </p>
  <p>
   If you follow the above tips, your
   <code>
    next
   </code>
   report output
              should be starting to get useful. Furthermore, by modifying the
              urgency coefficients, you can make the
   <code>
    next
   </code>
   report
              adopt your own notion of whether, for example, a priority setting
              is more important than a specific project.  Here are some changes
              you could make:
   <pre>task config urgency.user.tag.problem.coefficient 4.5</pre>
   This means that any task having the
   <code>
    +problem
   </code>
   tag gets
              an urgency boost.  Conversely, you can reduce the urgency for
              unimportant things, using negative coefficients:
   <pre>task config urgency.user.tag.later.coefficient -6.0</pre>
   If you have a project that is more important, you can boost the
              whole project:
   <pre>task config urgency.user.project.Home.coefficient 2.9</pre>
   Suppose you do not agree that a blocked task should have a
              reduced urgency.  Override it:
   <pre>task config urgency.blocked.coefficient 0.0</pre>
   A zero coefficient means that blocked tasks now have
   <em>
    no
   </em>
   effect on the urgency.
  </p>
  <a name="desc">
  </a>
  <h4>
   Describe Carefully
  </h4>
  <p>
   Providing good descriptions for your tasks is enormously helpful.
              Here is a very bad example of a task:
   <pre>task add Renovate the kitchen</pre>
   While that may well be a perfect description of what you will be
              doing at the highest level, it is potentially an open-ended task,
              for which progress will be very hard to assess.

              This will be a task that sits on your task list for some time,
              and is not very helpful - you learn nothing from it, and its
              presence on the list will become demotivating.
  </p>
  <p>
   A much better approach would be this:
   <pre>task add project:Kitchen Select floor tiles
task add project:Kitchen Measure counter-top
task add project:Kitchen Design placement of electrical outlets
task add project:Kitchen Locate ideal placement for extractor duct
task add project:Kitchen Select and order counter-top material
task add project:Kitchen Talk to the Electrician about when the work can start
...</pre>
   Here
   <code>
    Kitchen
   </code>
   is now a project name, and the tasks
              represent smaller units of work. While this means more time will
              be spent breaking down the larger tasks, but planning is
              important.
  </p>
  <p>
   With smaller tasks, you have the opportunity to establish links
              between your tasks. For example, it would be wise to plan the
              placement of electrical outlets before asking the Electrician to
              start work. Measuring the counter-top is also needed before
              ordering the material. These are examples where you could use
              task dependencies to formalize the sequence.
  </p>
  <p>
   If you are wanting to estimate the completion of the project,
              having more tasks and more details will improve your ability to
              estimate. With enough detail in the tasks, you are more likely to
              be able to estimate the work.
  </p>
  <p>
   Break down tasks into smaller tasks - the extra effort required to
              be more precise can pay off in terms of efficiently performing the
              work in the right sequence, at the right time.
  </p>
  <a name="review">
  </a>
  <h4>
   Review Your Tasks
  </h4>
  <p>
   Go over your list periodically and correct any erroneous data,
              like an incorrect due date, or a priority that no longer applies
              because of external factors, or even delete tasks that are no
              longer relevant. This keeps your list current and up to date,
              more accurately reflecting the work you need to accomplish.
              Accurate metadata and good urgency coefficients mean that
              Taskwarrior's idea of urgency more closely matches yours.  That
              will be a big help.
  </p>
  <p>
   Consider installing and using the Taskwarrior Shell
              (
   <a href="https://taskwarrior.org/news/news.20160905.2.html">
    tasksh
   </a>
   )
              program, which among a few other things provides a
   <code>
    review
   </code>
   command that helps you cycle through your
              task list and keep it current.
  </p>
  <p>
   Some would argue that spending as little time on your task list
              as possible means more time for doing work. While this is true,
              it does assume that you are doing the
   <em>
    right
   </em>
   work. Good
              advice would be to spend as little time as you can on the task
              list, but enough to make sure that it is up to date, correct and
              complete. Then rely on the tools, and go get some work done.
  </p>
  <a name="sense">
  </a>
  <h4>
   Common Sense
  </h4>
  <p>
   Use a task list, look at it often, correct any mistakes and remove
              items that no longer apply. Choose a methodology that works for
              you (GTD, Pomodoro ...) or devise your own - it's not complicated.
              Be consistent. Backup your data.
  </p>
  <a name="future">
  </a>
  <h4>
   Future Enhancements
  </h4>
  <p>
   We are always looking into better ways to represent your task
              list, better ways to display it, and better ways to support
              methodologies that work. We will be adding features that help in
              some way, for some people, and we will be correcting what is not
              working. Taskwarrior is a toolkit, and a comprehensive one,
              intended to support the different ways people do work. You will
              not need every feature, but everyone uses a different set of
              features, according to their own approach.  But every feature
              that you do use will help you work with your list better.
  </p>
 </div>
 <br/>
 <br/>
</div>

