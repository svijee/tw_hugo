---
title: 'Unicode'
url: '/docs/unicode.html'
---
<div class="col-md-10 main">
 <div class="row">
  <p>
   All text in Taskwarrior is UTF8, which means any Unicode characters
              can be entered and stored. Here is a demo:
  </p>
  <script async="" id="asciicast-28269" src="https://asciinema.org/a/28269.js" type="text/javascript">
  </script>
  <script async="" id="asciicase-28269" src="https://asciinema.org/a/28269" type="text.javascript">
  </script>
  <p>
   Both the
   <code>
    U+NNNN
   </code>
   and
   <code>
    \\uNNNN
   </code>
   specifiers
              are supported, but it is usually simpler to use the first, which
              does not require the backslashes to be escaped in shells and
              scripts.
  </p>
  <p>
   Note that the font you use in your terminal
              determines whether those characters are rendered, so it is possible
              to enter characters for which there is no glyph.
  </p>
 </div>
 <br/>
 <br/>
</div>

