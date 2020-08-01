case "$OSTYPE" in
  linux*)   echo "! Sorry build_art.sh is incompatible with Linux / WSL. Try calling art/scripts/conductor.py manually."; sleep 5;;
  darwin*)  echo "generating dist" ;
                python3 -m pip install --user --upgrade setuptools wheel
                python3 setup.py sdist bdist_wheel;;
  win*)     echo "! Sorry build_art.sh is incompatible with Windows. Try calling art/scripts/conductor.py manually." ; sleep 5;;
  msys*)    echo "Welcome to the equities/art build pipeline! :) "; sleep 5;;
  cygwin*)  echo "! Sorry build_art.sh is incompatible with Cygwin. Try calling art/scripts/conductor.py manually." sleep 5; ;;
  bsd*)     echo "! Sorry build_art.sh is incompatible with BSD. Try calling art/scripts/conductor.py manually." sleep 5; ;;
  solaris*) echo "! Sorry build_art.sh is incompatible with Solaris. Try calling art/scripts/conductor.py manually." sleep 5; ;;
  *)        echo "! Sorry build_art.sh is incompatible with unknown: $OSTYPE.  Try calling art/scripts/conductor.py manually." sleep 5; ;;
esac

sleep 5;