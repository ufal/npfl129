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

- _On GitHub, do not create a **public** fork with your solutions_

  If you keep your solutions in a GitHub repository, please do not create
  a clone of the repository by using the Fork button; this way, the cloned
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
  git remote add course_repo https://github.com/ufal/npfl129
  git fetch course_repo
  git checkout --track course_repo/master -b BRANCH_NAME
  ```
  This creates a branch `BRANCH_NAME`, and when you run `git pull` in that
  branch, it will be updated to the current state of the course repository.

- _How to merge the course repository updates with your modified branch?_

  If you want to store your solutions in your branch and gradually update this
  branch to track the changes in the course repository, you should start by
  ```
  git remote add course_repo https://github.com/ufal/npfl129
  git fetch course_repo
  git checkout --no-track course_repo/master -b BRANCH_NAME
  ```
  which creates a branch `BRANCH_NAME` with the current state of the
  course repository. However, unlike to the previous case, `git pull`
  and `git push` in this branch will not operate on the course repository.
  Therefore, you can then commit to this branch and push it to your own
  repository.

  To update your branch with the changes from the course repository, run
  ```
  git fetch course_repo
  git merge course_repo/master
  ```
  while in your branch. Of course, it might be necessary to resolve conflicts
  if both you and I modified the same lines in the templates.

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
