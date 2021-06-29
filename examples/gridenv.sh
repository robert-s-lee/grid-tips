# setup conda environment
gridenv() {
  local name=${1:-$(basename -- $(pwd))}
  local pyver=${2:-3.8.5}
  local envexist=$(conda env list | grep "^${name}[ \t]*")
  [ -z "${envexist}" ] && conda create --yes --name ${name} python=${pyver}
  conda activate ${name}
  [ -f requirements.txt ] && pip install -r requirements.txt
  pip install lightning-grid --upgrade
  [ ! -z "${GRID_API}" ] && eval grid login $GRID_API
}