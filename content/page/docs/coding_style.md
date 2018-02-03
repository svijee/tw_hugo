---
title: "Coding Style"
url: '/docs/coding_style.html'
---
<div class="col-md-10 main">
 <div class="row">
  <a name="style">
  </a>
  <p>
   The coding style used for the Taskwarrior, Taskserver, and other
              codebases is deliberately kept simple and a little vague. This is
              because there are many languages involved (C++, C, Python, sh,
              bash, HTML, troff and more), and specіfying those would be a major
              effort that detracts from the main focus which is improving the
              software.
  </p>
  <p>
   Instead, the general guideline is simply this:
  </p>
 </div>
 <div class="row">
  <div class="callout callout-info">
   <p>
    Make all changes and additions such that they blend in
                perfectly with the surrounding code, so it looks like only
                one person worked on the source, and that person is rigidly
                consistent.
   </p>
  </div>
 </div>
 <div class="row">
  <p>
   To be a little more explicit, the common elements across the
              languages are:
   <ul>
    <li>
     Indent code using two spaces, no tabs
    </li>
    <li>
     With Python, follow
     <a href="https://www.python.org/dev/peps/pep-0008/">
      PEP8
     </a>
     as much as possible
    </li>
    <li>
     Surround operators and expression terms with a space
    </li>
    <li>
     No cuddled braces
    </li>
    <li>
     Stick to 80 columns where possible, although exceptions are fine
    </li>
    <li>
     Class names are capitalized, variable names are not
    </li>
   </ul>
  </p>
 </div>
 <div class="row">
  <p>
   We target Python 2.7 so that our test suite runs on the broadest set
              of platforms.  This will likely change in the future and 2.7 will be
              dropped.
  </p>
 </div>
 <div class="row">
  <p>
   We can safely target C++11 because all the default compilers on our
              supported platforms are ready. Feel free to use C++14 and C++17
              provided that all build platforms support this.
  </p>
 </div>
 <br/>
 <br/>
</div>

