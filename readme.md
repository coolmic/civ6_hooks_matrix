# Civ hooks matrix

## requirements

Python >= 3.5

## setup with virtualenv


    python3 -m venv {project-dir}
    source ./bin/activate
    make init

Copy `.env.exemple` to `.env` and edit it

Copy `mapping.json.exemple` to `mapping.json` and edit it


Start the server with

    make run


## setup with pip

    pip install {project-dir}

Make a copy of `mapping.json.exemple` anywhere and edit it


Start the server with

> civ6_hooks_matrix {mapping-file}

Don't forget to define variable environment (see `.env.exemple`).

exemple :

    MATRIX_USER_ACCESS_TOKEN={token} MATRIX_URL={url} civ6_hooks_matrix mapping.json

