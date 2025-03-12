cmake_minimum_required(VERSION 3.22)
project(demo)

set(SOURCES demo.cpp)
set(TARGET demo)

add_executable(${TARGET} ${SOURCES})
