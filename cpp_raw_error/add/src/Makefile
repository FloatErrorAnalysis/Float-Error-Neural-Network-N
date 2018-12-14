# add/Makefile
CC = g++
BIN = ../bin
LIB_DIR = ../../iRRAM/lib
LIB1 = gmp
LIB2 = iRRAM
LIB3 = mpfr
SRC = ../src
INC2 = ../../iRRAM/include
INC1 = /usr/local/include
STD = c++11

SOURCE = $(wildcard $(SRC)/*.cpp)
PROGS = $(patsubst %.cpp, $(BIN)/%, $(notdir $(SOURCE)))

all: $(PROGS)

$(BIN)/%: $(SRC)/%.cpp $(BIN)
	$(CC) $< -o $@ -I$(INC1) -I$(INC2) -L$(LIB_DIR) -l$(LIB1) -L$(LIB_DIR) -l$(LIB2) -L$(LIB_DIR) -l$(LIB3) -std=$(STD)

$(BIN):
	mkdir -p $@

clean:
	rm -f $(PROGS)
