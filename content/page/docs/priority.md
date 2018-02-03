---
title: 'Priority'
url: "/docs/priority.html"
---
<div class="col-md-10 main">
 <div class="row">
  <p>
   Taskwarrior has supported the notion of task priority since the
              beginning. Priority was defined to have four allowable values,
   <code>
    H
   </code>
   ,
   <code>
    M
   </code>
   and
   <code>
    L
   </code>
   , with the
              additional option of having no priority at all.
              The values represent High, Medium, Low and No priority.
              The
   <code>
    L
   </code>
   value is considered a higher priority than no priority.
              Priority has been used to sort tasks in most built-in reports.
  </p>
  <p>
   Beginning with Taskwarrior 2.4.3, priority is no longer a core
              attribute, and is replaced with an equivalent
   <a href="/docs/udas.html">
    User Defined Attribute
   </a>
   .
              This offers several advantages, and users may now configure
              priority to more closely match their needs.
  </p>
  <p>
   This change should go unnoticed, but there are some differences.
              This document describes how you may further customize priority to
              match
   <em>
    your
   </em>
   notion of what priority means.
  </p>
  <a name="default">
  </a>
  <h4>
   Default Configuration
  </h4>
  <p>
   Here is the new default configuration for the UDA priority, which
              closely matches the old core attribute priority.
  </p>
  <pre>color.uda.priority.H=color255
color.uda.priority.L=color245
color.uda.priority.M=color250

uda.priority.label=Priority
uda.priority.type=string
uda.priority.values=H,M,L,

urgency.uda.priority.H.coefficient=6.0
urgency.uda.priority.L.coefficient=1.8
urgency.uda.priority.M.coefficient=3.9</pre>
  <p>
   There are several points to note, the first of which is that the
              color rules are now UDA color rules. The themes that are
              distributed with Taskwarrior have all been updated to accomodate
              this change, but you may have local overrides that have not yet
              been modified.
  </p>
  <p>
   The
   <code>
    uda.priority.values
   </code>
   setting specifies the possible
              values, which are
   <code>
    H
   </code>
   ,
   <code>
    M
   </code>
   ,
   <code>
    L
   </code>
   ,
              and no priority.

              Notice the comma at the end with no value after it - that is how
              you specify that an empty value is allowed.
  </p>
  <a name="custom">
  </a>
  <h4>
   Custom Configuration
  </h4>
  <p>
   If you believe that a priority level of
   <code>
    L
   </code>
   should be
              the lowest value, lower even than no value, you can do this:
   <pre>$ task config -- uda.priority.values  H,M,,L</pre>
   Those two commas indicate that the blank value lies between
   <code>
    M
   </code>
   and
   <code>
    L
   </code>
   .
  </p>
  <p>
   If you would like priorities that represent severity, then you can
              do something like this:
   <pre>$ task config -- uda.priority.values Critical,Important,</pre>
   There is no practical limit on what values, or how many values
              you use. This example suggests you might want to rename
   <code>
    priority
   </code>
   to be
   <code>
    severity
   </code>
   instead.
  </p>
  <a name="warning">
  </a>
  <h4>
   Warning
  </h4>
  <p>
   If you sync tasks between different clients, you will need to
              configure those clients in the same way, otherwise you'll find
              that Taskwarrior will enforce the default configuration.
  </p>
 </div>
 <br/>
 <br/>
</div>

