btcWallet
=========

Getting Started
---------------

- Change directory into your newly created project.

    cd pythonTest

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Upgrade to that revision.

    env/bin/alembic -c development.ini upgrade head
    
- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
