apt update
apt -y install git nano
# tzdata wants user interaction by default, so we install it first with interaction turned off
DEBIAN_FRONTEND=noninteractive apt install -y tzdata
git submodule init
git submodule update
apt -y install git build-essential ninja-build python3 libicu-dev libsdl2-dev gcc-riscv64-unknown-elf srecord gcc-arm-none-eabi xxd nodejs npm
npm install -g typescript@5.0

#./install_emscripten.sh
emsdk/emsdk install latest
emsdk/emsdk activate latest
source emsdk/emsdk_env.sh

./install_icarus.sh
./install_icestorm.sh
./install_nextpnr.sh
./install_verilator.sh
./install_yosys.sh
