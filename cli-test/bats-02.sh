#!/usr/bin/env bats

@test "cli version" {
  result="grid version|grep 'Grid CLI'|awk '{$1=$1};1'"
  [ "$result" == "Grid CLI (v0.3.74)" ]
}

