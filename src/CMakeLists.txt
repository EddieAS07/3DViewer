project(model-viewer-main)

add_subdirectory(renderer)
add_subdirectory(system)
add_subdirectory(tools)
add_subdirectory(window)

set(executable_name model-viewer)

add_executable(${executable_name} main.cpp)
set_target_properties(${executable_name} PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
)

target_link_libraries(${executable_name} 
    librenderer 
    libsystem 
    libtools 
    libwindow
)
