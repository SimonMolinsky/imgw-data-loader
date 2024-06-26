# Contribution to the package

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's

* Reporting a bug
* Discussing the current state of the code
* Submitting a fix
* Proposing new features
* Becoming a maintainer

## Where should I start?

Here, on **GitHub**! We use **GitHub** to host the code, track issues, and feature requests, and accept pull requests.

---

## Developer setup

Setup for developers differs from the package installation from `PyPI`.

1. Fork the `imgw-data-loader` repository.
2. Clone forked repository.
3. Connect the main repository with your fork locally:

```shell
git remote add upstream https://github.com/SimonMolinsky/imgw-data-loader.git

```

4. Synchronize your repository with the core repository.

```shell
git checkout main
git pull upstream main

```

5. Create your branch.

```shell
git checkout -b name-of-your-branch

```

6. Create [virtual environment](https://docs.python.org/3/library/venv.htmlc) or [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands).
7. Activate your environment.
8. Install requirements listed in the `requirements-dev.txt` file.

**Virtual Environment**

```shell
>> (your-virtual-environment) pip install -r requirements-dev.txt

```

**Conda**

```shell
>> (your-conda-environment) conda install -c conda-forge --file requirements-dev.txt

```

9. Make changes in a code or write something new.
10. Write tests if required.
11. Perform tests with `pytest`. (Run tests from the `tests` directory).

```shell
>> (your-environment) (your-username:~/path/wsknn/tests) pytest

```

12. If all tests pass, push changes into your fork.

```shell
git add .
git commit -m "description what you have done"
git push origin name-of-your-branch

```

13. Navigate to your repository. You should see a button `Compare and open a pull request`. Use it to make a pull request! Send it to the `dev` branch in the main repository. **Don't send pull requests into the `main` branch of the core repository!**

## We Use [Github Flow](https://guides.github.com/introduction/flow/index.html), So All Code Changes Happen Through Pull Requests
Pull requests are the best way to propose changes to the codebase (we use [Github Flow](https://guides.github.com/introduction/flow/index.html)). We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests in the `test` package. We use Python's `pytest` package to perform testing.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes. Run tests from `tests` directory, otherwise you will encounter an error.
5. Make sure your code lints, you can use `flake8` or linters included in IDE (e.g.: *Pycharm*). Linters check [PEP8 Python Guidelines](https://www.python.org/dev/peps/pep-0008/), and it is recommended to read them first.
6. Issue that pull request.

## Any contributions you make will be under the BSD 3-Clause "New" or "Revised" License
In short, when you submit code changes, your submissions are understood to be under the same [BSD 3-Clause "New" or "Revised" License] that covers the project. Feel free to contact the maintainers if that's a concern.

## Report bugs using Github's [issues](https://github.com/SimonMolinsky/imgw-data-loader/issues)
We use GitHub issues to track public bugs. Report a bug by opening a new issue.

## Write bug reports with detail, background, and sample code

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
- Be specific!
- Give sample code if you can.
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

People *love* thorough bug reports.

## License
By contributing, you agree that your contributions will be licensed under its BSD 3-Clause "New" or "Revised" License.

## References
This document was adapted from the open-source contribution guidelines for [Facebook's Draft](https://github.com/facebook/draft-js/blob/a9316a723f9e918afde44dea68b5f9f39b7d9b00/CONTRIBUTING.md)

## Example of Contribution

1. You have an idea to speed-up computation. You plan to use `multiprocessing` package for it.
2. Fork repo from `main` branch and at the same time propose change or issue in the [project issues](https://github.com/SimonMolinsky/imgw-data-loader/issues).
3. Create the new child branch from the forked `main` branch. Name it as `dev-your-idea`. In this case, `dev-multiprocessing` is descriptive enough.
4. Code in your branch.
5. Create a few unit tests in the `tests` directory or re-design actual tests if needed. For programming cases, write unit tests, for mathematical and logic problems, write functional tests. Use data from the `tests/tdata` directory.
6. Multiprocessing may not require new tests. But always run `pytest` in the `tests` directory after any change in the code and check if every test has passed.
7. Run all tutorials (`demo-notebooks`). Their role is more than just informational. They serve as a functional test playground.
8. If everything is okay, make a pull request from your forked repo.