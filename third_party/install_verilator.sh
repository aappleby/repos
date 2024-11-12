sudo apt -y install git perl python3 make autoconf g++ flex bison ccache libgoogle-perftools-dev numactl perl-doc libfl2 libfl-dev zlib1g zlib1g-dev help2man
cd verilator
git checkout v5.018
autoconf
./configure
make -j$(nproc)
sudo make install
