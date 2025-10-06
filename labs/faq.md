### TOC: FAQ

### TOCEntry: Install

- _Installing to central user packages repository_

  You can install all required packages to central user packages repository using
 `pip3 install --user scikit-learn==1.7.2 numpy==2.3.3 scipy==1.16.2 pandas==2.3.2 matplotlib==3.10.6`.

- _Installing to a virtual environment_

  Python supports virtual environments, which are directories containing
  independent sets of installed packages. You can create a virtual environment
  by running `python3 -m venv VENV_DIR` followed by
  `VENV_DIR/bin/pip3 install scikit-learn==1.7.2 numpy==2.3.3 scipy==1.16.2 pandas==2.3.2 matplotlib==3.10.6`
  (or `VENV_DIR/Scripts/pip3` on Windows).

- _**Windows** installation_

  - On Windows, it can happen that `python3` is not in PATH, while `py` command
    is; in that case you can use `py -m venv VENV_DIR`, which uses the newest
    Python available, or for example `py -3.11 -m venv VENV_DIR`, which uses
    Python version 3.11.

### TOCEntry: Git

- _Is it possible to keep the solutions in a Git repository?_

  Definitely. Keeping the solutions in a branch of your repository,
  where you merge them with the course repository, is probably a good idea.
  However, please keep the cloned repository with your solutions **private**.

- _On GitHub, do not create a **public** fork containing **your solutions**._

  If you keep your solutions in a GitHub repository, please do not create
  a clone of the repository by using the Fork button; this way, the cloned
  repository would be **public**.
  - If you created a public fork and want to make it private, you need to start
    by pressing **Leave fork network** in the repository settings; only then you
    can change the visibility to **private**.

  Of course, if you want to create a pull request, GitHub requires a public
  fork and you need to create it, just do not store your solutions in it (so you
  might end up with two repositories, a public fork for pull requests and
  a private repo for your own solutions).

- _How to clone the course repository?_

  To clone the course repository, run
  ```
  git clone https://github.com/ufal/npfl129
  ```
  This creates the repository in the `npfl129` subdirectory; if you want a different
  name, add it as an additional parameter.

  To update the repository, run `git pull` inside the repository directory.

- _How to merge the course repository updates into a private repository with additional changes?_

  It is possible to have a private repository that combines your solutions and
  the updates from the course repository. To do that, start by cloning your
  empty private repository, and then run the following commands in it:
  ```
  git remote add course_repo https://github.com/ufal/npfl129
  git fetch course_repo
  git checkout --no-track course_repo/master
  ```
  This creates a new remote `course_repo` and a clone of the `master` branch
  from it; however, `git pull` and `git push` in this branch will operate
  on the repository your cloned originally.

  To update your branch with the changes from the course repository, run
  ```
  git fetch course_repo
  git merge course_repo/master
  ```
  while in your branch (the command `git pull --no-rebase course_repo master`
  has the same effect). Of course, it might be necessary to resolve conflicts
  if both you and the course repository modified the same lines in the same files.

### TOCEntry: ReCodEx

- _What files can be submitted to ReCodEx?_

  You can submit multiple files of any type to ReCodEx. There is a limit of
  **20** files per submission, with a total size of **20MB**.

- _What file does ReCodEx execute and what arguments does it use?_

  Exactly one file with `py` suffix must contain a line starting with `def main(`.
  Such a file is imported by ReCodEx and the `main` method is executed
  (during the import, `__name__ == "__recodex__"`).

  The file must also export an argument parser called `parser`. ReCodEx uses its
  arguments and default values, but it overwrites some of the arguments
  depending on the test being executed; the template always indicates which
  arguments are set by ReCodEx and which are left intact.

- _What are the time and memory limits?_

  The memory limit during evaluation is **1.5GB**. The time limit varies, but it should
  be at least 10 seconds and at least twice the running time of my solution. For
  competition assignments, the time limit is 5 minutes.
