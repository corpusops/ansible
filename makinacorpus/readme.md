# differences with pristine ansible

## Ongoing PR included to the fork
- Submitted
    - [include_role](https://github.com/ansible/ansible/pull/32565)
      **ABANDONNED** cause splitted in more scopped sub PR
        - [Include roles with tags in meta/main.yml make a role run more than neccesary](https://github.com/ansible/ansible/pull/35133)
        - [fix Include role: exposed/shared vars](https://github.com/ansible/ansible/pull/35131)
        - [FIX: multiple nested tasks include levels](https://github.com/ansible/ansible/pull/35107)
        - [include role honour allow duplicates](https://github.com/ansible/ansible/pull/35132)
        - [Include role: serialization: (de)pickling support](https://github.com/ansible/ansible/pull/35134)
    

## Reverted commits
- [Don't use getattr inget_parent_attribute to avoid recursion issues](https://github.com/ansible/ansible/commit/0b7d78d67f962a2605c84a39fb3c8ef449701264)
    - [included include_role fails to escalate since ebf971f](https://github.com/ansible/ansible/issues/35065)
    - ask kiorky: irclog chat with sivel:  ven. janv. 19 2018 18:24:56
    - only workaround is to define a var in parent and then use it in children roles (like with a wrapping block)...
## abandoned changes
- no more diff in time for recent ansible code: [include_role optimizations](https://github.com/ansible/ansible/commit/bf9fb2bc503da692be788eabdd0c7746ae7318d1)
