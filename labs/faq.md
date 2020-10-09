### TOC: FAQ

### TOCEntry: Install

- _Installing to central user packages repository_

  You can install all required packages to central user packages repository using
 `pip3 install --user scikit-learn==0.23.2 pandas==1.1.2 numpy==1.18.5 scipy==1.5.2 matplotlib==3.3.2`.

- _Installing to a virtual environment_

  Python supports virtual environments, which are directories containing
  independent sets of installed packages. You can create the virtual environment
  by running `python3 -m venv VENV_DIR` followed by
  `VENV_DIR/bin/pip3 install scikit-learn==0.23.2 pandas==1.1.2 numpy==1.18.5 scipy==1.5.2 matplotlib==3.3.2`.

### TOCEntry: ReCodEx

- _What files can be submitted to ReCodEx?_

  You can submit multiple files of any type to ReCodEx. There is a limit of
  **20** files per submission, with a total size of **20MB**.

- _What file does ReCodEx execute and what arguments does it use?_

  Exactly one file with `py` suffix must contain a line starting with `def main(`.
  Such a file is imported by ReCodEx and the `main` method is executed
  (during the import, `__name__ == "__recodex__"`).

  The file must also export an argument parser called `parser`. ReCodEx uses its
  arguments and default values, but is overwrites some of the arguments
  depending on the test being executed – the template should always indicate which
  arguments are set by ReCodEx and which are left intact.

- _What are the time and memory limits?_

  The memory limit during evaluation is 1.5GB. The time limit varies, but should
  be at least 10 seconds and at least twice the running time of my solution.
