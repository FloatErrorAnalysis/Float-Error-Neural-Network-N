clang -O0 -emit-llvm lli-pre-process/single/sqrt_minus3_add.cpp -S -o lli-pre-process/single/sqrt_minus3_add.ll
llvm-as lli-pre-process/single/sqrt_minus3_add.ll -o lli-pre-process/single/sqrt_minus3_add.bc
lli-pre-process/lli lli-pre-process/single/sqrt_minus3_add.bc