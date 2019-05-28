cd llvm-build
cmake ../llvm-master
cmake --build .
rm /Users/xuzihang/Desktop/lli-pre-process/lli 
rm /Users/xuzihang/Desktop/data.txt
mv /Users/xuzihang/Desktop/llvm-build/bin/lli /Users/xuzihang/Desktop/lli-pre-process