case "$OSTYPE" in
  linux*)   echo "! Sorry build_art.sh is incompatible with Linux / WSL. Try calling art/scripts/conductor.py manually."; sleep 5;;
  darwin*)  echo "deploying" ;
                ./bin/purge_build.sh;
                ./bin/make_dist.sh;
                ./bin/deploy_pypi_dist.sh;
                echo "done";;
  win*)     echo "! Sorry build_art.sh is incompatible with Windows. Try calling art/scripts/conductor.py manually." ; sleep 5;;
  msys*)    echo "Welcome to the equities/art build pipeline! :) "; sleep 5;;
  cygwin*)  echo "! Sorry build_art.sh is incompatible with Cygwin. Try calling art/scripts/conductor.py manually." sleep 5; ;;
  bsd*)     echo "! Sorry build_art.sh is incompatible with BSD. Try calling art/scripts/conductor.py manually." sleep 5; ;;
  solaris*) echo "! Sorry build_art.sh is incompatible with Solaris. Try calling art/scripts/conductor.py manually." sleep 5; ;;
  *)        echo "! Sorry build_art.sh is incompatible with unknown: $OSTYPE.  Try calling art/scripts/conductor.py manually." sleep 5; ;;
esac

sleep 5;