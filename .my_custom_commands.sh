#!/bin/bash# prints the input

function gitcr() {
  cd ~/projetos/git-automation
  python3.5 github-automation.py ${1} ${2}
  cd ~/projetos
  mkdir ${1}
  cd ${1}
#  git init
# return: SSH path; executar SSH path
}
