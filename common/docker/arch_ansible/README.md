
# Dockerfile for Running Ansible in an 
Arch Linux Container

This exists because I need to run the 
same version of Python in a container as 
that running on the Arch Linux Raspberry 
Pi images which the Ansible playbooks in 
this repository run against.

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


