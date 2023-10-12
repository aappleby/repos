cd nextpnr
apt -y install python3 python3-dev cmake libboost-dev libboost-filesystem-dev libboost-thread-dev libboost-program-options-dev libboost-iostreams-dev libboost-dev libeigen3-dev
cmake . -DARCH=ice40
make -j$(nproc)
make install
