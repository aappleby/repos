git submodule init icestorm
git submodule update icestorm
cd icestorm
sudo apt -y install build-essential libftdi-dev
make -j$(nproc)
sudo make install
