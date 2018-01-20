# differences with pristine ansible

## Ongoing PR included to the fork
- [include_role](https://github.com/ansible/ansible/pull/32565) **ABANDONNED** but splitted into the following:
    - [Include roles with tags in meta/main.yml make a role run more than neccesary](https://github.com/ansible/ansible/pull/35133
    - [fix Include role: exposed/shared vars](https://github.com/ansible/ansible/pull/35131)
    - [FIX: multiple nested tasks include levels](https://github.com/ansible/ansible/pull/35107)
    - [include role honour allow duplicates](https://github.com/ansible/ansible/pull/35132)
    - [Include role: serialization: (de)pickling support](https://github.com/ansible/ansible/pull/35134)

## Reverted commits
- [0b7d78d67f962a2605c84a39fb3c8ef449701264](https://github.com/ansible/ansible/commit/0b7d78d67f962a2605c84a39fb3c8ef449701264)

## abandoned changes
- no more diff in time for recent ansible code: [include_role optimizations](https://github.com/ansible/ansible/commit/bf9fb2bc503da692be788eabdd0c7746ae7318d1)
