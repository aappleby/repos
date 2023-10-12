apt -y install git build-essential ninja-build python3 libicu-dev libsdl2-dev gcc-riscv64-unknown-elf srecord gcc-arm-none-eabi xxd nodejs
npm install -g typescript

./install_emscripten.sh
source emsdk/emsdk_env.sh

./install_icarus.sh
./install_icestorm.sh
./install_nextpnr.sh
./install_verilator.sh
./install_yosys.sh