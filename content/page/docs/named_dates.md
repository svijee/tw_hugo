---
title: 'Named Dates'
url: "/docs/named_dates.html"
---
<div class="col-md-10 main">
 <div class="row">
  <a name="title">
  </a>
  <p>
   The term 'date' is used here to describe a timestamp of varying
              precision and specificity. The terms 'timestamp', or 'datetime'
              also apply.
  </p>
  <p>
   Taskwarrior supports the notion of specifying dates in several
              ways. There are ISO-8601 dates:
  </p>
  <pre>2014-06-07T16:55:04-05:00
2014-W23
20140607</pre>
  <p>
   There are
   <code>
    rc.dateformat
   </code>
   dates, the default being
   <code>
    Y-M-D
   </code>
   :
  </p>
  <pre>2014-06-07</pre>
  <p>
   This document enumerates and defines other dates, such as
   <code>
    tomorrow
   </code>
   and many others.
  </p>
  <a name="days">
  </a>
  <h4>
   Days of the Week
  </h4>
  <p>
   The days of the week are interpreted as the next day in the
              future.  To specify a day in the past, use a different date
              format.
  </p>
  <p>
   <table class="table table-striped table-compact">
    <tr>
     <td>
      <code>
       mon
      </code>
      ,
      <code>
       monday
      </code>
     </td>
     <td>
      The date of the nearest future monday at 0:00:00 local.
     </td>
    </tr>
   </table>
  </p>
  <p>
   The days are recognized in three-letter abbreviated form and the
              full day name only.
  </p>
  <a name="ordinals">
  </a>
  <h4>
   Day Ordinals
  </h4>
  <p>
   Day ordinals are the days in the month, numbered starting from 1,
              to either the 28th, 29th, 30th or 31st, depending on the current
              month.
  </p>
  <p>
   <table class="table table-striped table-compact">
    <tr>
     <td>
      <code>
       1st
      </code>
      ,
      <code>
       2nd
      </code>
      ,
      <code>
       3rd
      </code>
      ...
     </td>
     <td>
      The date of the nearest future Nth day at 0:00:00 local.
     </td>
    </tr>
   </table>
  </p>
  <p>
   Note that if today is February 20th, specifying
   <code>
    31st
   </code>
   is an error, and does not mean March 31. For this, use a precise
              date format.
  </p>
  <a name="months">
  </a>
  <h4>
   Months of the Year
  </h4>
  <p>
   The months of the year are interpreted as the first day of the
              next month of that name in the future.  To specify a month in the
              past, use a different date format.
  </p>
  <p>
   <table class="table table-striped table-compact">
    <tr>
     <td>
      <code>
       jan
      </code>
      ,
      <code>
       january
      </code>
     </td>
     <td>
      The date of the nearest future January 1st, at 0:00:00
                    local.
     </td>
    </tr>
   </table>
  </p>
  <p>
   The months are recognized in three-letter abbreviated form and the
              full month name only.
  </p>
  <a name="year">
  </a>
  <h4>
   Year Dates
  </h4>
  <p>
   Year dates are abbreviated names for dates within the year, that
              occur at various boundaries. The abbreviations use 's' to mean the
              start, and 'e' to mean the end of the period. The periods are
              indicated using 'm' (month), 'q' (quarter) and 'y' (year). So the
              date 'socy' means 'start of current year'.
  </p>
  <p>
   <table class="table table-striped table-compact">
    <tr>
     <td>
      <code>
       socy
      </code>
      ,
      <code>
       eocy
      </code>
     </td>
     <td>
      Start of the current year.
                    End of the current year.
                    Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       socq
      </code>
      ,
      <code>
       eocq
      </code>
     </td>
     <td>
      Start of the current quarter.
                    End of the current quarter.
                    Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       socm
      </code>
      ,
      <code>
       eocm
      </code>
     </td>
     <td>
      Start of the current month.
                    End of the current month.
                    Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       soy
      </code>
      ,
      <code>
       eoy
      </code>
     </td>
     <td>
      Start of the next year.
                    End of the year.
                    Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       soq
      </code>
      ,
      <code>
       eoq
      </code>
     </td>
     <td>
      Start of the next quarter.
                    End of the quarter.
                    Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       som
      </code>
      ,
      <code>
       eom
      </code>
     </td>
     <td>
      Start of the next month.
                    End of the month.
                    Time is 0:00:00 local.
     </td>
    </tr>
   </table>
  </p>
  <p>
   There is redundancy in this table, and it exists for the sake of
              symmetry. For example, 'eom' and 'eocm' are always the same, but
              exist so that every date has a matching pair.
  </p>
  <p>
   <div class="col-xs-12 col-sm-12">
    <a class="thumbnail" href="/docs/design/year.png">
     <img src="/docs/design/year.png">
     </img>
    </a>
   </div>
  </p>
  <a name="week">
  </a>
  <h4>
   Week Dates
  </h4>
  <p>
   Week dates are abbreviated names for dates within the week, that
              occur at various boundaries. The abbreviations use 's' to mean the
              start, and 'e' to mean the end of the period. The periods are
              indicated using 'd' (day), 'w' (week).
  </p>
  <p>
   <table class="table table-striped table-compact">
    <tr>
     <td>
      <code>
       socw
      </code>
      ,
      <code>
       eocw
      </code>
     </td>
     <td>
      Start of the current week.
                    End of the current week.
                    Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       sow
      </code>
      ,
      <code>
       eow
      </code>
     </td>
     <td>
      Start of the next week.
                    End of the week.
                    Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       soww
      </code>
      ,
      <code>
       eoww
      </code>
     </td>
     <td>
      Start of the next work week.
                    End of the work week.
                    Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       sod
      </code>
      ,
      <code>
       eod
      </code>
     </td>
     <td>
      Start of today.
                    End of today.
                    Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       yesterday
      </code>
     </td>
     <td>
      Start of yesterday.
                    Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       today
      </code>
     </td>
     <td>
      Start of today.
                    Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       now
      </code>
     </td>
     <td>
      Right now.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       tomorrow
      </code>
     </td>
     <td>
      Start of tomorrow.
                    Time is 0:00:00 local.
     </td>
    </tr>
   </table>
  </p>
  <p>
   Again, there is redundancy in the table, for the sake of symmetry.
  </p>
  <p>
   <div class="col-xs-12 col-sm-12">
    <a class="thumbnail" href="/docs/design/week.png">
     <img src="/docs/design/week.png">
     </img>
    </a>
   </div>
  </p>
  <a name="calculated">
  </a>
  <h4>
   Calculated Dates
  </h4>
  <p>
   These dates are from algorithms, and easily calculated.
  </p>
  <p>
   <table class="table table-striped table-compact">
    <tr>
     <td>
      <code>
       later
      </code>
      ,
      <code>
       someday
      </code>
     </td>
     <td>
      January 18th, 2038 - the end of time.
                    Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       easter
      </code>
      ,
      <code>
       eastermonday
      </code>
      ,
      <code>
       pentecost
      </code>
      ,
      <code>
       ascension
      </code>
      ,
      <code>
       goodfriday
      </code>
     </td>
     <td>
      Time is 0:00:00 local.
     </td>
    </tr>
    <tr>
     <td>
      <code>
       midsommarafton
      </code>
      ,
      <code>
       midsommar
      </code>
     </td>
     <td>
      First Friday and Saturday after 19th June.
                    Time is 0:00:00 local.
     </td>
    </tr>
   </table>
  </p>
 </div>
 <br/>
 <br/>
</div>

