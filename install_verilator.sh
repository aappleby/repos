apt -y install git perl python3 make autoconf g++ flex bison ccache libgoogle-perftools-dev numactl perl-doc libfl2 libfl-dev zlib1g zlib1g-dev help2man
cd verilator
autoconf
./configure
make -j$(nproc)
make install
