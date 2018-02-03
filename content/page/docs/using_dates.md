---
title: 'Using Dates Effectively'
url: "/docs/using_dates.html"
---
<div class="col-md-10 main">
 <div class="row">
  <p>
   A task does not require a due date, and can simply be a statement of need:
  </p>
  <pre>$ task add Send Alice a birthday card</pre>
  <p>
   However this is exactly the kind of task can benefit from having a due date,
              and perhaps several other dates also.
  </p>
  <p>
   There are several dates that can decorate a task, each with its own meaning
              and effects. You can choose to use some, all or none of these, but like all
              Taskwarrior features, they are there in case your needs require it, but you
              do not pay a performance or friction penalty by not using them.
  </p>
  <a name="due">
  </a>
  <h4>
   The
   <code>
    due
   </code>
   Date
  </h4>
  <p>
   Use a
   <code>
    due
   </code>
   date to specify the exact date by which a task must be
              completed. This corresponds to the last possible moment when the task can be
              considered on-time. Using our example, we can set the
   <code>
    due
   </code>
   date
              to be Alice's birthday (line breaks added for clarity):
  </p>
  <pre>$ task add Send Alice a birthday card \
           due:2016-11-08</pre>
  <p>
   Now your task has an associated
   <code>
    due
   </code>
   date, to help you
              determine when you need to work on it. But what effect does this have on
              Taskwarrior? How can it be used to best advantage?
  </p>
  <p>
   We call the
   <code>
    due
   </code>
   date of a task 'metadata'. As such, it is just
              a piece of data associated with the task, and therefore it can become part
              of a filter:
  </p>
  <pre>$ task due:today list
...</pre>
  <p>
   This is one way to find out if any of your tasks are due today. You could also
              use:
  </p>
  <pre>$ task +TODAY list
...</pre>
  <p>
   That is an example of a virtual tag,
   <code>
    TODAY
   </code>
   , which is not a real
              tag, but is something you can query, and is equivalent to the previous
              example. Additionally you can use
   <code>
    DUE
   </code>
   which filters tasks that
              have a due date in the next week, or
   <code>
    WEEK
   </code>
   for all tasks due
              this week, including
   <code>
    YESTERDAY
   </code>
   ,
   <code>
    TOMORROW
   </code>
   ,
   <code>
    MONTH
   </code>
   and
   <code>
    YEAR
   </code>
   .
  </p>
  <p>
   You can find tasks that have any due date at all:
  </p>
  <pre>$ task due.any: list
...</pre>
  <p>
   Or no due date:
  </p>
  <pre>$ task due.none: list
...</pre>
  <p>
   There is also an
   <code>
    overdue
   </code>
   report that makes use of the
   <code>
    OVERDUE
   </code>
   virtual tag, to show you what is already late.
              If you run the
   <code>
    calendar
   </code>
   report, your due date will be
              highlighted on it.
  </p>
  <p>
   What we see here is that Taskwarrior leverages the metadata to drive
              various features. Several reports will sort by
   <code>
    due
   </code>
   date,
              and as we see above, a task that has a due date now belongs on your
              schedule.
  </p>
  <a name="scheduled">
  </a>
  <h4>
   The
   <code>
    scheduled
   </code>
   Date
  </h4>
  <p>
   A
   <code>
    scheduled
   </code>
   date is different from a
   <code>
    due
   </code>
   date,
              and represents the earliest opportunity to work on a task. Let's continue
              with the same example above.  You need to send a brithday card to Alice,
              but her birthday isn't until November, so it's not the kind of task that
              can be done in advance. Ideally this would be done a few days ahead of
              the
   <code>
    due
   </code>
   date:
  </p>
  <pre>$ task add Send Alice a birthday card \
           due:2016-11-08 \
           scheduled:2016-11-04</pre>
  <p>
   This means that you need to send Alice a birthday card, no later than 2016-11-08,
              and no earlier than 2016-11-04.
  </p>
  <p>
   If a task has a
   <code>
    scheduled
   </code>
   date, then once that date passes, the
              task is considered ready, and there is a
   <code>
    ready
   </code>
   report and a
   <code>
    READY
   </code>
   virtual tag for this:
  </p>
  <pre>$ task ready
...
$ task +READY list
...</pre>
  <p>
   Tasks that have no
   <code>
    scheduled
   </code>
   date are considered always ready.
              Again, metadata drives the sophistication of your task list.
  </p>
  <a name="wait">
  </a>
  <h4>
   The
   <code>
    wait
   </code>
   Date
  </h4>
  <p>
   Many people do not like to look at long task lists, finding them daunting, or
              just distracting. You can add a
   <code>
    wait
   </code>
   date to a task, which has
              the effect of hiding the task from you until that date. In our example,
              Alice's birthday isn't close yet, so we applied a
   <code>
    scheduled
   </code>
   date to indicate that we should not begin the task yet, as it is not ready.
              Now let's add a
   <code>
    wait
   </code>
   date to the task:
  </p>
  <pre>$ task add Send Alice a birthday card \
           due:2016-11-08 \
           scheduled:2016-11-04 \
           wait:november</pre>
  <p>
   Here the task is given a
   <code>
    wait
   </code>
   date of 2016-11-01, via the
              useful shortcut 'november', which means the task will not appear on lists
              until November. At that time, it will reappear, but it will still not be ready
              until 2016-11-04.
  </p>
  <p>
   You can view all the hidden waiting tasks using the
   <code>
    waiting
   </code>
   report:
  </p>
  <pre>$ task waiting
...</pre>
  <p>
   There is a
   <code>
    WAITING
   </code>
   virtual tag to select these tasks, but note
              that you have to use the
   <code>
    all
   </code>
   report with it, otherwise you get
              conflicts with the other reports that specify a 'pending' status, because a
              waiting task is not pending.
  </p>
  <a name="until">
  </a>
  <h4>
   The
   <code>
    until
   </code>
   Date
  </h4>
  <p>
   Now suppose I miss Alice's birthday completely. Shame on me. The task
              would be overdue, but this is the kind of task where I don't want to
              complete it late, I'd rather just forget it, and wish Alice a belated
              happy birthday in person. I could simple delete or complete the task,
              but there is another option, which is to add an
   <code>
    until
   </code>
   date:
  </p>
  <pre>$ task add Send Alice a birthday card \
           due:2016-11-08 \
           scheduled:2016-11-04 \
           wait:november \
           until:2016-11-10</pre>
  <p>
   This means that on 2016-11-10, the task self destructs, and is automatically
              deleted. This might be the right thing to do for a birthday card task,
              but is not suitable for a "Pay the rent" task. Beware!
  </p>
  <p>
   There is a DOM-based shortcut you can use, to make the command above a
              ittle more formulaic:
  </p>
  <pre>$ task add Send Alice a birthday card \
           due:2016-11-08 \
           scheduled:due-4d \
           wait:due-7d \
           until:due+2d</pre>
  <p>
   This are evaluated only at task creation time, so if you change the due
              date, you also need to change the other dates. Note there is an
   <code>
    UNTIL
   </code>
   virtual tag to show you all tasks that are set to
              auto-expire.
  </p>
  <a name="other">
  </a>
  <h4>
   Other Dates
  </h4>
  <p>
   There are other dates associated with a task, but these are more for internal
              use, and are less useful for you.
  </p>
  <p>
   Each task has an
   <code>
    entry
   </code>
   date which records when it was created.

              Each completed or deleted task has an
   <code>
    end
   </code>
   date, which records when
              it was completed or deleted.

              An active, or started task has a
   <code>
    start
   </code>
   date, but only while it
              is in the active state.

              Finally, every task has a
   <code>
    modification
   </code>
   date, which records when
              it was last modified. This is used as a hint when tasks are being synced.
  </p>
  <p>
   In addition, you may find you have a use case for a different kind of date
              for your task lists. For example, you may adhere to an agile development
              process, and a task may be assigned to a sprint, and that sprint may be
              identified by its end date. You can add arbitrary dates like this to Taskwarrior
              by defining a
   <a href="/docs/udas.html">
    User Defined Attribute
   </a>
   (UDA) and then storing that metadata with your tasks. In this case, Taskwarrior
              will do nothing with your UDA but store it, and let you use it in reports and
              filters.
  </p>
  <a name="urgency">
  </a>
  <h4>
   Urgency
  </h4>
  <p>
   The presence and values of date metadata in your tasks affects the urgency
              calculations. For example, if a task is blocked by a dependency, the urgency
              is reduced. Similarly tasks that are ready have an elevated urgency.
  </p>
  <a name="also">
  </a>
  <h4>
   See Also
  </h4>
  <p>
   For other discussions of dates see:
   <ul>
    <li>
     <a href="/docs/dates.html">
      Date &amp; Time
     </a>
    </li>
    <li>
     <a href="/docs/named_dates.html">
      Named Dates
     </a>
    </li>
    <li>
     <a href="/docs/udas.html">
      User Defined Attributes
     </a>
    </li>
    <li>
     <a href="/docs/best-practices.html">
      Best Practices
     </a>
    </li>
    <li>
     <a href="/docs/urgency.html">
      Urgency
     </a>
    </li>
   </ul>
  </p>
 </div>
 <br/>
 <br/>
</div>

