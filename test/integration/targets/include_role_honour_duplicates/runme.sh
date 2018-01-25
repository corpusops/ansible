#!/usr/bin/env bash
W=$(cd "$(dirname "$0")" && pwd)
export ANSIBLE_ROLES_PATH="$W/roles"
set -ux
ret=
ansible-playbook -i../../inventory test.yml -v
ret=$(printf "$?\n$ret")
ansible-playbook -i../../inventory test2.yml -v
ret=$(printf "$?\n$ret")
if ( echo "$ret"|grep -vq 0 );then exit 1;fi
