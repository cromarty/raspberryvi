
# `common/ansible/playbooks`

In here you will find `Ansible playbooks` designed to run the
`accessiblepi` role to install accessibility software on a Raspberry
Pi.

In the `ansible_vault.md` file you will find an explanatin of creating
and using `Ansible vault` files in any of these playbooks, or new ones
you create.

## Existing `playbooks`

There are two playbooks in this directory to begin with:

console
mate

The `console` playbook installs accessibility tools, either the
SpeakUp screen reader or the Fenrir screen reader. Both of which are
designed to make the Linux console accessible.

In `mate` is a playbook which can optionally install the console
tools, and then the `Mate` desktop along with the `Orca` screen
reader.


