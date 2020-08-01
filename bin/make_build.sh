#!/bin/bash

case "$OSTYPE" in
  linux*)   echo "! Sorry build_art.sh is incompatible with Linux / WSL. Try calling art/scripts/conductor.py manually."; sleep 5;;
  darwin*)  echo "Welcome to the equities/art build pipeline! You are about to build the app locally. We require access to darwin root. Don't worry, you can trust us :) " ;
                python3 -m venv env
                source env/bin/activate
                echo "+ [ darwin ] Created python virtual env"
                cd ./art;
                sudo -H pip3 install -r ./requirements.txt;
                echo "+ [ darwin ] Installed art requirements to env";
                cd ../services/server; 
                sudo -H pip3 install -r ./requirements.txt;
                echo "+ [ darwin ] Installed services/server python requirements to env"
                cd ../../art/scripts;
                python3 conductor.py make_build; 
                echo "+ [ darwin ] The orchestra has finished playing. The conductor bows.";
                cd ../.. 
                sleep 5;;
  win*)     echo "! Sorry build_art.sh is incompatible with Windows. Try calling art/scripts/conductor.py manually." ; sleep 5;;
  msys*)    echo "Welcome to the equities/art build pipeline! :) "; sleep 5;;
  cygwin*)  echo "! Sorry build_art.sh is incompatible with Cygwin. Try calling art/scripts/conductor.py manually." sleep 5; ;;
  bsd*)     echo "! Sorry build_art.sh is incompatible with BSD. Try calling art/scripts/conductor.py manually." sleep 5; ;;
  solaris*) echo "! Sorry build_art.sh is incompatible with Solaris. Try calling art/scripts/conductor.py manually." sleep 5; ;;
  *)        echo "! Sorry build_art.sh is incompatible with unknown: $OSTYPE.  Try calling art/scripts/conductor.py manually." sleep 5; ;;
esac

sleep 5;