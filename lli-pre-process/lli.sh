#!/bin/bash 
function ergodic(){ 
for file in ` ls $1 ` 
do 
                if [ -d $1"/"$file ] 
then 
ergodic $1"/"$file 
else 
local path=$1"/"$file  #得到文件的完整的目录 
local name=$file        #得到文件的名字 
# lli and rm
../$CUR_DIR/lli ../$CUR_DIR/bc/$name
rm ../$CUR_DIR/bc/$name
fi 
        done 
} 
INIT_PATH="bc"
CUR_DIR="lli-pre-process" 
ergodic $INIT_PATH