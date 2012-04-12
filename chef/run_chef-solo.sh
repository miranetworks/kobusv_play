#!/bin/bash


CHEF_DIR="$(cd "$(dirname "$0")" && pwd)"


cat <<EOF >"$CHEF_DIR/solo.rb"
file_cache_path "$CHEF_DIR"
cookbook_path "$CHEF_DIR/cookbooks"
EOF


chef-solo -c "$CHEF_DIR/solo.rb" -j "$CHEF_DIR/node.json"
