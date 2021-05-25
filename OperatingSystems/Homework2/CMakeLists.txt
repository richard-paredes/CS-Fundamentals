cmake_minimum_required(VERSION 3.16)
project(Homework2)

set(CMAKE_CXX_STANDARD 14)

set(THREADS_PREFER_PTHREAD_FLAG ON)
set(CMAKE_CXX_FLAGS -pthread)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -g -lpthread")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")

add_executable(Homework2Client client.cpp)
add_executable(Homework2Server server.cpp)
add_executable(Homework2Fireman fireman.cpp)