#!/bin/bash



(( EUID == 0 )) || { echo "Script must be run as root." ; exit 1 ; }

set -e

apt-get update 

apt-get install -yq libncurses5 libncurses5-dev libncursesw5 libncursesw5-dev \
    lib64ncurses5 lib64ncurses5-dev glusterfs-common

apt-get install -yq libglib2.0-dev libfdt-dev \
    libpixman-1-dev zlib1g-dev libaio-dev \
    libbluetooth-dev libbrlapi-dev libbz2-dev \
    libcap-dev libcap-ng-dev libcurl4-gnutls-dev \
    libgtk-3-dev libibverbs-dev libjpeg8-dev libncurses5-dev \
    libnuma-dev librbd-dev librdmacm-dev libsasl2-dev \
    libsdl1.2-dev libseccomp-dev libsnappy-dev \
    libssh2-1-dev libvde-dev libvdeplug-dev \
    libvte-2.91-dev libxen-dev liblzo2-dev \
    valgrind xfslibs-dev libopensm-dev librdmacm-dev \
    libibumad-dev libibverbs-dev librdmacm-dev


#git clone git://git.qemu-project.org/qemu.git

if [ -d qemu/build ]; then
	rm -rf qemu/build/*
else
	mkdir qemu/build
fi

cd qemu/build

../configure \
        --prefix=/opt/qemu \
    --enable-system \
    --enable-sdl \
    --enable-gtk \
    --enable-vte \
    --enable-kvm \
    --enable-bzip2 \
    --enable-libssh2 \
    --enable-linux-user \
    --enable-docs \
    --enable-gnutls \
    --enable-nettle \
    --enable-curses \
    --enable-modules \
    --enable-virtfs \
    --enable-curl \
    --enable-fdt \
    --enable-rdma \
    --enable-vde \
    --enable-linux-aio \
    --enable-cap-ng \
    --enable-attr \
    --enable-vhost-net \
    --enable-spice \
    --enable-rbd \
    --enable-libiscsi \
    --enable-libnfs \
    --enable-smartcard \
    --enable-libusb \
    --enable-usb-redir \
    --enable-lzo \
    --enable-snappy \
    --enable-seccomp \
    --enable-coroutine-pool \
    --enable-glusterfs \
    --enable-tpm \
    --enable-numa \
    --enable-tcmalloc

make -j4
make install

