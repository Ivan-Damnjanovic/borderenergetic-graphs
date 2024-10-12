# borderenergetic-graphs

This repository contains the programming code needed to perform the computer-assisted search for finding all the borderenergetic graphs of order 12 and all the borderenergetic chemical graphs. The programming code is located within the [search_code](search_code) folder, while the search results are given in the [search_results](search_results) folder.

The [search_code/java_check](search_code/java_check) subfolder contains the Java code based on Graph6Java that does the preliminary graph generation and inspection. These files are used to build the [search_code/spawned_search/be-selector.jar](search_code/spawned_search/be-selector.jar) file, which should then be run by the [search_code/spawned_search/main.py](search_code/spawned_search/main.py) Python file from the same [search_code/spawned_search](search_code/spawned_search) subfolder.

The [search_code/mathematica_check](search_code/mathematica_check) subfolder contains a single file representing the Wolfram Mathematica script that performs the subsequent candidate graph filtering and verification.

The [search_code/python_check](search_code/python_check) subfolder contains a single Python file that is used to verify the nonexistence of borderenergetic chemical graphs on 20 or 21 vertices.
