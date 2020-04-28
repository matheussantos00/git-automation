#!/bin/bash# prints the input

function gitcr() {
  cd ~/projetos/git-automation
  python3.5 github-automation.py ${1} "${2}"
  SSH="git remote add origin git@github.com:matheussantos00/${1}.git"
  cd ~/projetos
  mkdir ${1}
  cd ${1}
  git init
  eval "${SSH}"
  echo "first push command: git push -u origin master"
}
