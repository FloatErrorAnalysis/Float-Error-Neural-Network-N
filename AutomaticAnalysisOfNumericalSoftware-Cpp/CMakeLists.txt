cmake_minimum_required(VERSION 3.13)
project(AutomaticAnalysisOfNumericalSoftware_Cpp)

set(CMAKE_CXX_STANDARD 11)
# include
include_directories(iRRAM/include /usr/local/include)
# link
link_libraries(${AutomaticAnalysisOfNumericalSoftware_Cpp_SOURCE_DIR}/iRRAM/lib/libiRRAM.a)
link_libraries(${AutomaticAnalysisOfNumericalSoftware_Cpp_SOURCE_DIR}/iRRAM/lib/libgmp.a)
link_libraries(${AutomaticAnalysisOfNumericalSoftware_Cpp_SOURCE_DIR}/iRRAM/lib/libmpfr.a)
set(SOURCE_FILES main.cpp)

add_executable(AutomaticAnalysisOfNumericalSoftware_Cpp ${SOURCE_FILES})