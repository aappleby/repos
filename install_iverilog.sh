git submodule init iverilog
git submodule update iverilog
sudo apt -y install build-essential bison flex gperf libreadline-dev autoconf
cd iverilog
sh autoconf.sh
./configure
make -j$(nproc)
sudo make install
