======================
GitHub Issue Templates
======================

Introduction
============

GitHub Issue Templates streamline collaboration by providing pre-defined formats for reporting bugs, suggesting features, or requesting changes. These templates improve issue clarity, reduce back-and-forth communication, and ensure maintainers have all the context needed to take action.

Key Features
============

- **Structured Reporting**: Prompts users to include key details like reproduction steps and expected behavior.
- **Multiple Templates Support**: Different templates for bug reports, feature requests, and pull requests.
- **Custom Labels and Assignees**: Automatically apply labels or assign team members.
- **Easy Discovery**: Templates appear automatically when creating a new issue on GitHub.

Installation
============

To set up GitHub Issue Templates, follow these steps:

1. Create a `.github/ISSUE_TEMPLATE/` directory in the root of your repository.
2. Add Markdown (`.md`) files for each issue type, such as:

   - `bug_report.md`
   - `feature_request.md`

3. (Optional) Add a `config.yml` file to define default labels, assignees, or template ordering.

Example file structure:

.. code-block:: bash

   .github/
   ├── ISSUE_TEMPLATE/
   │   ├── bug_report.md
   │   ├── feature_request.md
   │   └── config.yml
   └── pull_request_template.md

Configuration
=============

You can add a `config.yml` to customize behavior:

.. code-block:: yaml

   blank_issues_enabled: false
   contact_links:
     - name: Documentation
       url: https://example.com/docs
       about: Please read our documentation before submitting a new issue.

- **blank_issues_enabled**: Set to `false` to prevent untemplated issues.
- **contact_links**: Direct users to external support channels or documentation.

Usage
=====

Once templates are in place:

1. Navigate to the repository’s **Issues** tab.
2. Click **New Issue**.
3. Choose from available templates (e.g., Bug Report, Feature Request).
4. Fill out the form and submit.

To use a pull request template, contributors just open a pull request; GitHub auto-inserts the content from `.github/pull_request_template.md`.

Template Examples
=================

**bug_report.md**

.. code-block:: markdown

   ---
   name: Bug report
   about: Create a report to help us improve
   title: "[BUG] "
   labels: bug
   assignees: sunil-fm
   ---

   **Describe the bug**
   A clear and concise description of what the bug is.

   **To Reproduce**
   Steps to reproduce the behavior:
   1. Go to '...'
   2. Click on '...'
   3. Scroll down to '...'
   4. See error

   **Expected behavior**
   A clear and concise description of what you expected to happen.

   **Screenshots**
   If applicable, add screenshots to help explain your problem.

   **Desktop (please complete the following information):**
   - OS: [e.g. iOS]
   - Browser [e.g. chrome, safari]
   - Version [e.g. 22]

   **Smartphone (please complete the following information):**
   - Device: [e.g. iPhone6]
   - OS: [e.g. iOS8.1]
   - Browser [e.g. stock browser, safari]
   - Version [e.g. 22]

   **Additional context**
   Add any other context about the problem here.

**feature_request.md**

.. code-block:: markdown

   ---
   name: Feature request
   about: Suggest an idea for this project
   title: "[RFC] "
   labels: enhancement
   assignees: sunil-fm
   ---

   **Is your feature request related to a problem? Please describe.**
   A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

   **Describe the solution you'd like**
   A clear and concise description of what you want to happen.

   **Describe alternatives you've considered**
   A clear and concise description of any alternative solutions or features you've considered.

   **Additional context**
   Add any other context or screenshots about the feature request here.

**pull_request_template.md**

.. code-block:: markdown

   ---
   name: Pull Request
   about: Submit a pull request to propose code changes
   title: "[PR] "
   labels: ""
   assignees: sunil-fm
   ---

   **What does this PR do?**
   <!-- A concise description of what this pull request does -->

   **Related Issue(s)**
   <!-- Link any related issues or feature requests here -->
   Closes #

   **Changes Made**
   <!-- List all major changes made in this pull request -->
   -
   -
   -

   **Checklist**
   - [ ] I have linked the related issue
   - [ ] I have run the tests and verified they pass
   - [ ] I have updated the documentation if needed
   - [ ] I have added or updated tests if applicable
   - [ ] I have followed the coding standards and guidelines
   - [ ] I have considered backward compatibility

   **Screenshots (if applicable)**
   <!-- Include screenshots or terminal output to illustrate impact -->

   **Additional Notes**
   <!-- Add anything else reviewers should be aware of -->

Additional Resources
====================

- `GitHub Docs: Configuring issue templates <https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-issue-templates-for-your-repository>`_
- `GitHub Docs: Using pull request templates <https://docs.github.com/en/pull-requests/using-templates-to-encourage-useful-issues-and-pull-requests>`_
- `YAML syntax guide <https://yaml.org/spec/>`_
