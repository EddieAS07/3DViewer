project(renderer-library)

set(library_name librenderer)

add_library(${library_name} "")
set_target_properties(${library_name} PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
)

add_subdirectory(camera)
add_subdirectory(model)
add_subdirectory(shader)
