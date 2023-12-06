# REPORT

## Personal Information
- Student Name: Naga Jayanth Chennupati
- Student ID: 21002083
- WatID: NJCHENNU

## What have been done to compile and run the code
To compile and run the code, Docker was set up on a Mac, and the Mac image was used to set up the environment. After cloning my repository within the Docker environment, I followed the provided instructions step by step to build Chocolate-Doom and the provided fuzz target. This included configuring CMake, compiling the code using Ninja, and running the fuzz target as described in the instructions.
## What have been done to increase the coverage
To increase code coverage, I meticulously approached two key areas within the codebase: chocolate-doom/src/doom/p_setup.c and chocolate-doom/src/w_wad.c.
I have used 5 fuzz_targets to get the line coverage using different filenames for wad files. I have added all the fuzz targets in CMakeLists.txt.
In chocolate-doom/src/doom/p_setup.c, I emphasized thorough testing of functions and components related to game setup. This involved examining various aspects of game configuration, options, and initializations. My goal was to ensure that every aspect of setting up the game was rigorously tested.

Simultaneously, in chocolate-doom/src/w_wad.c, I dedicated significant effort to expand the test coverage for functions and routines associated with managing WAD (Where's All the Data) files. Comprehensive testing in this area is critical because it directly influences the loading and management of essential game resources and assets.

By concentrating on these specific areas within the codebase, I aimed to provide a comprehensive and robust testing strategy, ultimately improving code coverage and enhancing the overall quality of the software.
## What bugs have been found? Can you replay the bug with chocolate-doom, not with the fuzz target?
During the process of writing test cases, I did not identify any software defects or bugs to report.
## Did you manage to compile the game and play it on your local machine (Not inside Docker)?
Yes, I was able to compile the game and play it on my local machine. The screenshot is attached with the report in report folder.
