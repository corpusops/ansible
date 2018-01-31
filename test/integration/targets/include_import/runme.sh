#!/usr/bin/env bash

set -eux

export ANSIBLE_ROLES_PATH=./roles

## Import (static)

# Playbook
ANSIBLE_STRATEGY='linear' ansible-playbook playbook/test_import_playbook.yml -i ../../inventory "$@" --skip-tags never
ANSIBLE_STRATEGY='free' ansible-playbook playbook/test_import_playbook.yml -i ../../inventory "$@" --skip-tags never
ANSIBLE_STRATEGY='linear' ansible-playbook playbook/test_import_playbook_tags.yml -i ../../inventory "$@" --tags canary1,canary22,validate --skip-tags skipme,never

# Tasks
ANSIBLE_STRATEGY='linear' ansible-playbook tasks/test_import_tasks.yml -i ../../inventory "$@" --skip-tags never
ANSIBLE_STRATEGY='free' ansible-playbook tasks/test_import_tasks.yml -i ../../inventory "$@" --skip-tags never
ANSIBLE_STRATEGY='free' ansible-playbook tasks/test_import_tasks_tags.yml -i ../../inventory "$@" --tags tasks1,canary1,validate --skip-tags never

# Role
ANSIBLE_STRATEGY='linear' ansible-playbook role/test_import_role.yml -i ../../inventory "$@" --skip-tags never
ANSIBLE_STRATEGY='free' ansible-playbook role/test_import_role.yml -i ../../inventory "$@" --skip-tags never


## Include (dynamic)

# Tasks
ANSIBLE_STRATEGY='linear' ansible-playbook tasks/test_include_tasks.yml -i ../../inventory "$@" --skip-tags never
ANSIBLE_STRATEGY='free' ansible-playbook tasks/test_include_tasks.yml -i ../../inventory "$@" --skip-tags never
ANSIBLE_STRATEGY='free' ansible-playbook tasks/test_include_tasks_tags.yml -i ../../inventory "$@" --tags tasks1,canary1,validate --skip-tags never

# Role
ANSIBLE_STRATEGY='linear' ansible-playbook role/test_include_role.yml -i ../../inventory "$@" --skip-tags never
ANSIBLE_STRATEGY='free' ansible-playbook role/test_include_role.yml -i ../../inventory "$@" --skip-tags never


## Recursion
# https://github.com/ansible/ansible/issues/23609
ANSIBLE_STRATEGY='linear' ansible-playbook test_recursion.yml -i ../../inventory "$@" --skip-tags never


## shared vars
# https://github.com/ansible/ansible/issues/21890
ANSIBLE_STRATEGY='linear' ansible-playbook -i ../../inventory playbook/sharedvars.yml -v "$@" --skip-tags never
ANSIBLE_STRATEGY='free' ansible-playbook -i ../../inventory playbook/sharedvars.yml -v "$@" --skip-tags never


## Nested tasks
# https://github.com/ansible/ansible/issues/34782
ANSIBLE_STRATEGY='linear' ansible-playbook nested.yml  -i ../../inventory "$@" --skip-tags never
ANSIBLE_STRATEGY='free' ansible-playbook nested.yml  -i ../../inventory "$@" --skip-tags never


## Include role honour allow duplicates
# https://github.com/ansible/ansible/pull/35164
ANSIBLE_STRATEGY='linear' ansible-playbook playbook/honour_duplicates.yml -i ../../inventory "$@" --skip-tags never
ANSIBLE_STRATEGY='free' ansible-playbook playbook/honour_duplicates.yml -i ../../inventory "$@" --skip-tags never


## Include roles with tags in meta/main.yml make a role run more than neccesary
# https://github.com/ansible/ansible/pull/35166
ANSIBLE_STRATEGY='linear' ansible-playbook playbook/cached_role.yml -i ../../inventory -v "$@" --skip-tags never
ANSIBLE_STRATEGY='free' ansible-playbook playbook/cached_role.yml -i ../../inventory -v "$@" --skip-tags never
