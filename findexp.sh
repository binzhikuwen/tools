#!/bin/bash

find . -iname \*.[ch] -exec grep --color -wn -H "$1" \{\} \;
find . -iname \*.cpp -exec grep --color  -wn -H "$1" \{\} \;
