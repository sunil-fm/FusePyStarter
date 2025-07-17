.. _troubleshooting:

===============
Troubleshooting
===============

.. note:: Can you help improve this file? See `Edit this file`_ to contribute!
          Please create a feature branch and submit a pull request with your improvements.

.. _`Edit this file`: https://github.com/sunil-fm/FusePyStarter/tree/main/docs/troubleshooting.rst


Windows Issues
--------------

* Some users have reported issues using Git Bash on Windows; try using Command Prompt (CMD) or PowerShell instead.

* Virtual environments can sometimes behave unexpectedly on Windows. If you have Python **3.10 or above** installed (recommended), this will create a virtual environment named ``myenv`` in the current folder:

.. code-block:: powershell

    > python -m venv myenv

* If Python isn't available globally, use the full path:

.. code-block:: powershell

    > C:\Users\YourUsername\AppData\Local\Programs\Python\Python310\python.exe -m venv myenv

* After creating the environment, activate it using:

.. code-block:: powershell

    > .\myenv\Scripts\Activate.ps1

Or, for Command Prompt:

.. code-block:: cmd

    > .\myenv\Scripts\activate.bat

* Sometimes, you may need to re-activate the virtual environment after changing directories. Keep the path handy in case it becomes deactivated unexpectedly.
