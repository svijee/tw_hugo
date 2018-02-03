---
title: "Color Themes"
url: '/docs/themes.html'
---
<div class="col-md-10 main">
 <div class="row">
  <p>
   Taskwarrior supports color themes. These are simply configuration
              files with defined color rules and rule precedence, which can be
              included in your
   <code>
    .taskrc
   </code>
   file like this:
  </p>
  <pre>include /path/to/dark-blue-256.theme</pre>
  <p>
   There are several themes included with the distribution, and the
              default
   <code>
    .taskrc
   </code>
   file you have references all of them,
              but these lines are commented out. Uncomment one line to use the
              theme.
  </p>
  <a name="override">
  </a>
  <h4>
   Overriding Colors
  </h4>
  <p>
   You can override the color settings by placing changes
   <em>
    after
   </em>
   the include:
  </p>
  <pre>include /path/to/dark-blue-256.theme
color.overdue=bold white on red</pre>
  <p>
   In this way, themes are the basis upon which you specify your
              color preferences.
  </p>
  <a name="default">
  </a>
  <h4>
   Default Theme
  </h4>
  <p>
   By default, without any selected theme, Taskwarrior uses a simple
              dark theme (
   <code>
    dark-16.theme
   </code>
   or
   <code>
    dark-256.theme
   </code>
   depending on your system). This means there is the assumption of a
              dark-background in your terminal. If you use a light background
              this will look bad, and you should select a light theme instead.
  </p>
  <p>
   There is a
   <code>
    no-color.theme
   </code>
   file that has no color at all,
              and while this sounds useless, it allows you to start with no color,
              and add your own.  If you are building your own theme, this is what
              you would start with.
  </p>
  <a name="swatches">
  </a>
  <h4>
   Theme Swatches
  </h4>
  <p>
   Below are examples of each of the provided themes.
  </p>
  <h4>
   dark-16.theme
  </h4>
  <p>
   <a href="/docs/images/dark-16.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/dark-16.png"/>
   </a>
  </p>
  <h4>
   dark-256.theme
  </h4>
  <p>
   <a href="/docs/images/dark-256.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/dark-256.png"/>
   </a>
  </p>
  <h4>
   dark-blue-256.theme
  </h4>
  <p>
   <a href="/docs/images/dark-blue-256.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/dark-blue-256.png"/>
   </a>
  </p>
  <h4>
   dark-gray-256.theme
  </h4>
  <p>
   <a href="/docs/images/dark-gray-256.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/dark-gray-256.png"/>
   </a>
  </p>
  <h4>
   dark-gray-blue-256.theme
  </h4>
  <p>
   <a href="/docs/images/dark-gray-blue-256.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/dark-gray-blue-256.png"/>
   </a>
  </p>
  <h4>
   dark-green-256.theme
  </h4>
  <p>
   <a href="/docs/images/dark-green-256.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/dark-green-256.png"/>
   </a>
  </p>
  <h4>
   dark-red-256.theme
  </h4>
  <p>
   <a href="/docs/images/dark-red-256.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/dark-red-256.png"/>
   </a>
  </p>
  <h4>
   dark-violets-256.theme
  </h4>
  <p>
   <a href="/docs/images/dark-violets-256.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/dark-violets-256.png"/>
   </a>
  </p>
  <h4>
   dark-yellow-green-256.theme
  </h4>
  <p>
   <a href="/docs/images/dark-yellow-green-256.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/dark-yellow-green-256.png"/>
   </a>
  </p>
  <h4>
   light-16.theme
  </h4>
  <p>
   <a href="/docs/images/light-16.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/light-16.png"/>
   </a>
  </p>
  <h4>
   light-256.theme
  </h4>
  <p>
   <a href="/docs/images/light-256.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/light-256.png"/>
   </a>
  </p>
  <h4>
   solarized-dark-256.theme
  </h4>
  <p>
   <a href="/docs/images/solarized-dark-256.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/solarized-dark-256.png"/>
   </a>
  </p>
  <h4>
   solarized-light-256.theme
  </h4>
  <p>
   <a href="/docs/images/solarized-light-256.png">
    <img alt="Theme swatch" class="img-thumbnail" src="/docs/images/solarized-light-256.png"/>
   </a>
  </p>
 </div>
 <br/>
 <br/>
</div>

