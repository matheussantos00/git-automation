#!/bin/bash# prints the input

function gitcr() {
  cd ~/projetos
  mkdir ${1}
  cd ${1}
  git init
}
