
# Dockerfile for Running Ansible in an 
Arch Linux Container

This exists because I need to run the 
same version of Python in a container as 
that running on the Arch Linux Raspberry 
Pi images which the Ansible playbooks in 
this repository run against.

This is because if I use a host such as 
a Debian machine, running Python 3.5.x 
to run my Ansible code against an Arch 
Linux Pi running Python 3.6.x, some 
modules fail.

## Createing keys

Before running the `docker build` for 
this container, you need to create:

* id_rsa
* id_rsa.pub

In the `keys/` subdirectory.

```
ssh-keygen -t rsa
```

When asked where to store the keys, 
reply:

```
keys/id_rsa
```


