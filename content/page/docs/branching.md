---
title: 'Branching Model'
url: "/docs/branching.html"
---
<div class="col-md-10 main">
 <div class="row">
  <p>
   Software development typically requires a standardized branching
              model, to manage complexity and parallel efforts.

              The branching model can be a source of confusion for developers,
              so this document describes how branching is used.
  </p>
  <p>
   Taskwarrior and Taskserver use the same branching model.
  </p>
  <a name="git">
  </a>
  <h4>
   Git Branching
  </h4>
  <p>
   Git allows arbitrary and low-cost branching, which means that any
              branching model can be used. A new Git repository has one branch,
              the default branch, named
   <code>
    master
   </code>
   , but even this is
              not required.
  </p>
  <p>
   <a href="/docs/images/master.png">
    <img alt="master" class="img-thumbnail" src="/docs/images/master.png"/>
   </a>
  </p>
  <p>
   No development occurs on the
   <code>
    master
   </code>
   branch.
  </p>
  <a name="dev">
  </a>
  <h4>
   Development Branch
  </h4>
  <p>
   A development branch is created from the
   <code>
    master
   </code>
   branch,
              and work proceeds on the development branch. Development branches
              are pushed to the server.

              Note that there are no changes on
   <code>
    master
   </code>
   - all work
              is done on dev branches.
  </p>
  <p>
   <a href="/docs/images/dev.png">
    <img alt="dev" class="img-thumbnail" src="/docs/images/dev.png"/>
   </a>
  </p>
  <p>
   All work on dev branches is pushed to the server.
  </p>
  <a name="topic">
  </a>
  <h4>
   Topic Branch
  </h4>
  <p>
   A topic branch is created from a dev branch. This can be a useful
              way to manage parallel efforts on a single development machine.
              Topic branches are also useful for merging in submitted patches,
              because the patch can be merged, tested and corrected independently
              of other efforts before being merged and pushed. A topic branch
              is ideal for storage of changes before an eventual merge back to
              the development branch.
  </p>
  <p>
   <a href="/docs/images/topic.png">
    <img alt="topic" class="img-thumbnail" src="/docs/images/topic.png"/>
   </a>
  </p>
  <p>
   No topic branches are pushed to the server, they are kept local to
              the development machine. They are private, and therefore hidden
              from the server.
  </p>
  <a name="release">
  </a>
  <h4>
   Release
  </h4>
  <p>
   When a release is made, the development branch is merged back to
              the
   <code>
    master
   </code>
   branch, and a tag is applied that
              indicates which commit represents the release.
  </p>
  <p>
   <a href="/docs/images/release.png">
    <img alt="release" class="img-thumbnail" src="/docs/images/release.png"/>
   </a>
  </p>
  <p>
   Because only releases are merged back, the
   <code>
    master
   </code>
   branch always represent the stable release.
  </p>
  <a name="newdev">
  </a>
  <h4>
   New Development Branches
  </h4>
  <p>
   Immediately after a release, one or more new branches are created.
              Typically after a major '1.0.0' release, there will be two branches
              created.  First the '1.0.1' branch is a patch development branch,
              intended to be used if an emergency patch is required. It therefore
              sits unused until an emergency arises. No work is performed on a
              patch development branch.
  </p>
  <p>
   The second branch, with the higher release number is the development
              branch for fixes and features. This is where all the work occurs.
              Any fix made on the development branch can be cherry-picked onto
              the patch branch, if necessary.
  </p>
  <p>
   <a href="/docs/images/dev2.png">
    <img alt="dev2" class="img-thumbnail" src="/docs/images/dev2.png"/>
   </a>
  </p>
  <p>
   To address the confusion around branching, namely determining which
              branch is active. the answer is that the highest numbered branch
              is the one that patches should be applied to.
  </p>
  <a name="old">
  </a>
  <h4>
   Old Branches
  </h4>
  <p>
   Old branches are not retained, but there are tags marking the
              beginning and end of development on a branch.
  </p>
  <a name="rebase">
  </a>
  <h4>
   Rebasing
  </h4>
  <p>
   No.
  </p>
 </div>
 <br/>
 <br/>
</div>

