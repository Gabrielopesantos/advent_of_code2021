#!/usr/bin/env bash

# usage : 
# fetch.sh $DAY

if test -z $@; then
    echo "Argument required"

else
    SESSION=$(cat session.txt)
    d="$1"
    dd=$(echo $1 | sed 's/^0*//')
    if [ ! -d "./day_$d/" ]; then
        mkdir -p day_$d/python day_$d/go
        touch day_$d/python/solution.py day_$d/go/solution.go
    else
        echo "Folder already exists"
    fi
    curl "https://adventofcode.com/2021/day/$dd/input" --cookie "$SESSION" > "day_$d/input.txt"
fi
