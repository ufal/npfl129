### TOC: FAQ

### TOCEntry: Install

- _Installing to central user packages repository_

  You can install all required packages to central user packages repository using
 `pip3 install --user scikit-learn==1.3.0 numpy==1.25.2 scipy==1.11.2 pandas==2.1.0 matplotlib==3.7.2`.

- _Installing to a virtual environment_

  Python supports virtual environments, which are directories containing
  independent sets of installed packages. You can create a virtual environment
  by running `python3 -m venv VENV_DIR` followed by
  `VENV_DIR/bin/pip3 install scikit-learn==1.3.0 numpy==1.25.2 scipy==1.11.2 pandas==2.1.0 matplotlib==3.7.2`
  (or `VENV_DIR/Scripts/pip3` on Windows).

- _**Windows** installation_

  - On Windows, it can happen that `python3` is not in PATH, while `py` command
    is – in that case you can use `py -m venv VENV_DIR`, which uses the newest
    Python available, or for example `py -3.9 -m venv VENV_DIR`, which uses
    Python version 3.9.

### TOCEntry: Git

- _Is it possible to keep the solutions in a Git repository?_

  Definitely. Keeping the solutions in a branch of your repository,
  where you merge them with the course repository, is probably a good idea.
  However, please keep the cloned repository with your solutions **private**.

- _On GitHub, do not create a **public** fork with your solutions_

  If you keep your solutions in a GitHub repository, please do not create
  a clone of the repository by using the Fork button – this way, the cloned
  repository would be **public**.

  Of course, if you just want to create a pull request, GitHub requires a public
  fork and that is fine – just do not store your solutions in it.

- _How to clone the course repository?_

  To clone the course repository, run
  ```
  git clone https://github.com/ufal/npfl129
  ```
  This creates the repository in the `npfl129` subdirectory; if you want a different
  name, add it as a last parameter.

  To update the repository, run `git pull` inside the repository directory.

- _How to keep the course repository as a branch in your repository?_

  If you want to store the course repository just in a local branch of your
  existing repository, you can run the following command while in it:
  ```
  git remote add upstream https://github.com/ufal/npfl129
  git fetch upstream
  git checkout -t upstream/master
  ```
  This creates a branch `master`; if you want a different name, add
  `-b BRANCH_NAME` to the last command.

  In both cases, you can update your checkout by running `git pull` while in it.

- _How to merge the course repository with your modifications?_

  If you want to store your solutions in a branch merged with the course
  repository, you should start by
  ```
  git remote add upstream https://github.com/ufal/npfl129
  git pull upstream master
  ```
  which creates a branch `master`; if you want a different name,
  change the last argument to `master:BRANCH_NAME`.

  You can then commit to this branch and push it to your repository.

  To merge the current course repository with your branch, run
  ```
  git merge upstream master
  ```
  while in your branch. Of course, it might be necessary to resolve conflicts
  if both you and I modified the same place in the templates.

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
  depending on the test being executed – the template should always indicate which
  arguments are set by ReCodEx and which are left intact.

- _What are the time and memory limits?_

  The memory limit during evaluation is **1.5GB**. The time limit varies, but it should
  be at least 10 seconds and at least twice the running time of my solution. For
  competition assignments, the time limit is 5 minutes.
