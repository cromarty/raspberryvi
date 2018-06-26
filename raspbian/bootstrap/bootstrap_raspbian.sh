#!/bin/bash
#
# you need: 
#
# binfmt-support, qemu, qemu-user-static, debootstrap, kpartx, lvm2, dosfstools
#
# You also need rpi-image-tool:
#
# git clone https://github.com/cromarty/rpi-image-tool
# cd rpi-image-tool
# make
# sudo make install
#


. rpi-image-tool.lib

usage() {
	echo "This is the usage"
}

(( EUID == 0 )) || { echo "Script must be run as root." ; exit 1 ; }

set -e

: ${WORKDIR:=.}
: ${HOSTNAME_:=raspberrypi}
: ${BLOCKCOUNT:=1900}
: ${BLOCKSIZE:=1M}
: ${SPLIT:=64}

deb_mirror="http://archive.raspbian.org/raspbian"
deb_local_mirror="http://archive.raspbian.org/raspbian"
deb_release="stretch"

cleanup=0
dryrun=0

qemu_emulator=qemu-arm-static

while getopts ':CH:dc:hi:s:w:z:' flag ; do
	case $flag in
		h)
			usage
			exit 0
		;;
		C)
			cleanup=1
		;;
		H)
			HOSTNAME_="${OPTARG}"
		;;
		d)
			dryrun=1
		;;
		c)
			BLOCKCOUNT="${OPTARG}"
			validate_blockcount "${BLOCKCOUNT}"
		;;
		s)
			SPLIT="${OPTARG}"
			validate_split "${SPLIT}"
		;;
		w)
			WORKDIR="${OPTARG}"
		;;
		z)
			BLOCKSIZE="${OPTARG}"
			validate_blocksize "${BLOCKSIZE}"
		;;
		i)
			IMAGENAME="${OPTARG}"
		;;
		(?)
			echo "${flag}"
			echo "Invalid option" >&2
			echo >&2
			usage
			exit 1
		;;
		:)
			echo "Option $OPTARG requires an argument" >&2
			echo >&2
			usage
			exit 1
		;;
	esac
done

: ${IMAGENAME:=mike_raspbian_$(date +%F | sed 's:-::g').img}

echo "Image file name will be: ${IMAGENAME}"
echo "Working directory will be: ${WORKDIR}"
echo "Block count will be: ${BLOCKCOUNT}"
echo "Block size will be: ${BLOCKSIZE}"
echo "Split will be: ${SPLIT}"
echo "Host name will be: ${HOSTNAME_}"

if (( dryrun )) ; then
	echo "Dry-run, stopping"
	exit 0
fi

bootmp="${WORKDIR}/boot"
rootmp="${WORKDIR}/root"

rpi-image-tool -N "${IMAGENAME}" -c "${BLOCKCOUNT}" \
	-z "${BLOCKSIZE}" -s "${SPLIT}" -w "${WORKDIR}"


pushd "${rootmp}"

echo "debootstrap first stage..."
debootstrap --no-check-gpg \
	--foreign --arch=armhf \
	--variant=minbase ${deb_release} . ${deb_local_mirror}

echo "Passed first stage..."

echo "debootstrap second stage..."
cp /usr/bin/${qemu_emulator} usr/bin/
LANG=C chroot . /debootstrap/debootstrap --second-stage

echo -e "deb $deb_local_mirror $deb_release main contrib non-free\n" > etc/apt/sources.list

echo "dwc_otg.lpm_enable=0 console=ttyUSB0,115200 kgdboc=ttyUSB0,115200 root=/dev/mmcblk0p2 rootfstype=ext4 rootwait" > boot/cmdline.txt

cat <<EOF > etc/fstab
proc            /proc           proc    defaults        0       0
/dev/mmcblk0p1  /boot           vfat    defaults        0       0

EOF

echo "${HOSTNAME_}" > etc/hostname
[ -d etc/network ] || mkdir etc/network

cat <<EOF > etc/network/interfaces
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp

EOF

cat <<EOF >> etc/modules
vchiq
snd_bcm2835

EOF


cat <<EOF > debconf.set
console-common	console-data/keymap/policy	select	Select keymap from full list
console-common	console-data/keymap/full	select	de-latin1-nodeadkeys

EOF

echo "Passed second stage..."


cat <<EOF > third-stage
#!/bin/bash
set -e
debconf-set-selections /debconf.set
rm -f /debconf.set
apt-get update 
apt-get -yq install git-core binutils ca-certificates wget curl
update-ca-certificates
wget http://goo.gl/1BOfJ -O /usr/bin/rpi-update
chmod +x /usr/bin/rpi-update
kversion=3.1.9+
mkdir -p "/lib/modules/${kversion}"
touch /boot/start.elf
echo "Running rpi-update..."
rpi-update
apt-get -yq install locales console-common ntp ntpdate openssh-server less nano
echo "root:raspberry" | chpasswd
#sed -i -e 's/KERNEL\!=\"eth\*|/KERNEL\!=\"/' /lib/udev/rules.d/75-persistent-net-generator.rules
rm -f /etc/udev/rules.d/70-persistent-net.rules
rm -f third-stage

EOF

chmod +x third-stage
echo "Third stage..."
LANG=C chroot . /third-stage

echo "Passed third stage script..."

echo -e "deb $deb_mirror $deb_release main contrib non-free\n" > etc/apt/sources.list

cat <<EOF > cleanup
#!/bin/bash
set -e
apt-get clean
rm -f cleanup

EOF

chmod +x cleanup
echo "Clean-up..."
LANG=C chroot . /cleanup


echo "Passed clean-up stage script..."
popd

# move boot files into boot partition
mv ${rootmp}/boot/* ${bootmp}

if (( cleanup )) ; then
	rpi-image-tool -C "${WORKDIR}"
fi

echo "All done"

exit 0


