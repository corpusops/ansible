# differences with pristine ansible

## Backport on 2.4
- [debug should have item (#36534)](https://github.com/ansible/ansible/commit/2f13ddbd694e8c6ae2f5d1737796c7a75109eda5#diff-ab09fa2a9291a017c38c5db420d7ee0f)
- [Only template each hostvars var on-demand (fixes #33259)](https://github.com/ansible/ansible/commit/dae737c8b714f2c6d28663ef0afeab10e6d3a667)

## Ongoing PR included to the fork
- Submitted
    - [include_role](https://github.com/ansible/ansible/pull/32565)
      **ABANDONNED** cause splitted in more scopped sub PR
        - [Include roles with tags in meta/main.yml make a role run more than neccesary](https://github.com/ansible/ansible/pull/35133)
        - [fix Include role: exposed/shared vars](https://github.com/ansible/ansible/pull/35131)
        - [FIX: multiple nested tasks include levels](https://github.com/ansible/ansible/pull/35107) MERGED ON 2.5 but not on 2.4
        - [include role honour allow duplicates](https://github.com/ansible/ansible/pull/35132)
        - [Include role: serialization: (de)pickling support](https://github.com/ansible/ansible/pull/35134)

## divergences
- [Workaround to speed up facts building](https://github.com/ansible/ansible/commit/d7d76e1871388e688dabcdccb64b3c9f2a878dc4)

## Reverted commits
- **REALLY TO BE CAREFUL FOR 2.5 AS IT WILL NOT BE REVERTED ON THAT BRANCH !!!**<br/>
  Upstream reverted it too in [#35247](https://github.com/ansible/ansible/pull/35247) only for **2.4**<br/>
  [Don't use getattr inget_parent_attribute to avoid recursion issues](https://github.com/ansible/ansible/commit/0b7d78d67f962a2605c84a39fb3c8ef449701264)
    - [included include_role fails to escalate since ebf971f](https://github.com/ansible/ansible/issues/35065)
    - ask kiorky: irclog chat with sivel:  ven. janv. 19 2018 18:24:56
    - only workaround is to define a var in parent and then use it in children roles (like with a wrapping block)...
## abandoned changes
- no more diff in time for recent ansible code: [include_role optimizations](https://github.com/ansible/ansible/commit/bf9fb2bc503da692be788eabdd0c7746ae7318d1)
