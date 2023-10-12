riscv64-unknown-elf-gcc --version | grep "(12"
if [ $? -eq 0 ]
then
	echo 12
fi
riscv64-unknown-elf-gcc --version | grep "(10"
if [ $? -eq 0 ]
then
        echo 10
fi
