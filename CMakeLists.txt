cmake_minimum_required(VERSION 3.21.3)
project(model-viewer 
    LANGUAGES C CXX
    VERSION 1.0
    DESCRIPTION "A program that can let the user view 3D models."
)

add_subdirectory(extern)
add_subdirectory(src)
add_subdirectory(test)
