cd prjtrellis/libtrellis
cmake -DCMAKE_INSTALL_PREFIX=/usr/local .
make -j$(nproc)
sudo make install
