#!/bin/bash
#
# Run Docker container from an image created from:
#
#  common/docker/arch_ansible
#
# This is needed when the machine on which you are running the playbooks has a Python version
# significantly behind the one on the host machine(s).
#
# Example is running playbooks on 
# Ubuntu/Xenial with Python 3.5.3 against machines running 3.6.x, which leads
# to failures in a Python module or modules on the host.
#
# Docker image contains Ansible and playbooks can be run from inside
# the container.
#
# Running from this directory results in this
# directory appearing in /opt inside the container.
#

IMAGE=mike/arch
NAME=mike

docker run -it \
    --rm \
    --name ${NAME} \
    -v `pwd`:/opt \
    ${IMAGE} \
    /bin/bash

