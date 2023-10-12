apt -y install build-essential bison flex gperf libreadline-dev autoconf
cd iverilog
sh autoconf.sh
./configure
make -j$(nproc)
make install
