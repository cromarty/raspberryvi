
# Ansible Vault File

In:

group_vars/all

You will find two files:

vars.yml
vault.yml

The `vault.yml` file is an encrypted file holding secrets needed by
Ansible when running against remote hosts.

In this case it stores at least the two variables:

	ansible_user
	ansible_become_pass

In the two lines:

	ansible_user: "{{ vault_ansible_user }}"
	ansible_become_pass: "{{ vault_ansible_become_pass }}"

You will need to create a:

	group_vars/all/vault.yml

File containing the two variables above with the `vault_` prefix.

Create an unencrypted version with these contents:

```
---

vault_ansible_user: <user>
vault_ansible_become_pass: <password>
```

Where <user> is the user on the remote host(s) against which the
playbook is being run.

For a `Raspbian` image provided by [The Raspberry Pi Foundation][rpi]
this is `pi`.

And <password> is the password which that user would provide if `sudo`
on the remote host(s) were configured to require it.

## Encrypting the `vault.yml` file

The `vault.yml` file now needs to be encrypted with the following
command:

ansible-vault encrypt vault.yml

You will be asked for the password for accessing the vault.

And you will be asked for it a second time.

## Running a `playbook` or an Ansible command using the vault

To run a playbook which uses the vault to access encrypted secrets,
you will need to include the:

--ask-vault-pass

Command-line switch.

To run a playbook called `site.yml`:

ansible-playbook --ask-vault-pass site.yml

Ansible will ask you for the vault password.

To run an Ansible command, for example to run the `setup` command:

ansible all --ask-vault-pass -m setup ...

Where `all` is the host against which to run the command. The above
command is incomplete but shows how to ask for the vault password.

## Decrypt the File Again

If you need to decrypt the vault file at any time:

ansible-vault decrypt vault.yml

You will be asked once for the password.

[rpi]: https://www.raspberrypi.org/



