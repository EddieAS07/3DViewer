project(window-library)

set(library_name libwindow)

add_library(${library_name} "")
set_target_properties(${library_name} PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
)

add_subdirectory(frame)
add_subdirectory(loop)
add_subdirectory(properties)
