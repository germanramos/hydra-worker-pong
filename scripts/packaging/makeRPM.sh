#!/bin/bash

### http://tecadmin.net/create-rpm-of-your-own-script-in-centosredhat/#

sudo yum install rpm-build rpmdevtools
rm -rf ~/rpmbuild
rpmdev-setuptree

mkdir ~/rpmbuild/SOURCES/hydra-worker-pong-1
cp ./fixtures/hydra-worker-pong.conf  ~/rpmbuild/SOURCES/hydra-worker-pong-1
cp hydra-worker-pong-init.d.sh ~/rpmbuild/SOURCES/hydra-worker-pong-1
cp ../../bin/hydra-worker-pong ~/rpmbuild/SOURCES/hydra-worker-pong-1

cp hydra-worker-pong.spec ~/rpmbuild/SPECS

pushd ~/rpmbuild/SOURCES/
tar czf hydra-worker-pong-1.0.tar.gz hydra-worker-pong-1/
cd ~/rpmbuild 
rpmbuild -ba SPECS/hydra-worker-pong.spec

popd
cp ~/rpmbuild/RPMS/x86_64/hydra-worker-pong-1-0.x86_64.rpm .
