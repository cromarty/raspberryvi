
# To remove a key from authorized_keys

ssh user@host -o PasswordAuthentication=no "sed -i.bak 's#`cat ~/.ssh/id_rsa.pub`##' ~/.ssh/authorized_keys"



