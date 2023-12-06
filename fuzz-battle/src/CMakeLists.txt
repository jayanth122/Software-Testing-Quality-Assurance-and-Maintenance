set(EXTRA_LIBS textscreen pcsound opl SDL2::SDL2main SDL2::SDL2 SDL2::mixer SDL2::net )

set(DOOM_BINARY_DIR ${Chocolate\ Doom_BINARY_DIR})

set(FREEDOOM_WAD "${PROJECT_SOURCE_DIR}/freedoom-0.12.1/freedoom2.wad")

set(OPC_FILE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../chocolate-doom/opl/opl.c")

set(OLP_LIB_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../chocolate-doom/opl")

add_executable(doom_fuzz fuzz_target.c fuzz_target1.c fuzz_target2.c fuzz_target3.c fuzz_target4.c)
target_include_directories(doom_fuzz PRIVATE ${DOOM_BINARY_DIR} ${DOOM_ROOT}/src ${DOOM_ROOT}/src/doom)
target_link_libraries(doom_fuzz PRIVATE game doom ${EXTRA_LIBS} )

# require LLD on Linux. Apple has it's own linker
if(UNIX AND NOT APPLE)
	target_link_libraries(doom_fuzz PRIVATE -fuse-ld=lld)
endif()

target_compile_options(doom_fuzz PRIVATE -fsanitize=fuzzer,address )
target_link_libraries(doom_fuzz PRIVATE -fsanitize=fuzzer,address)
target_compile_definitions(doom_fuzz PRIVATE FREEDOM_WAD="${FREEDOOM_WAD}")

