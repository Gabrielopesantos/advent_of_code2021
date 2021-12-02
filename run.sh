#!/usr/bin/env bash

print_day() {
  i=$1
  GOFILE="./day_$i/go/solution.go"
  PYFILE="./day_$i/python/solution.py"
  if test -f "$GOFILE" || test -f "$PYFILE"; then
    echo "#### Day $i ####"
    if test -f $GOFILE & test -s $GOFILE; then
      echo "Go: "
      go run $GOFILE
    fi

    if test -f $PYFILE & test -s $PYFILE; then
      echo "Python: "
      python3 $PYFILE
    fi
    printf "\n"
  fi
}

if test -z $@; then
  for i in $(seq -f "%2g" 1 25)
  do
    print_day $i
  done
else
  print_day $1
fi
