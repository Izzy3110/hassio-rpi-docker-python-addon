#!/usr/bin/with-contenv bashio
if [[ -r "options.json" ]]; then
  CorF=$(cat options.json |jq -r '.CorF')
fi

until false; do

  python3 /main.py

  sleep 30;
done
