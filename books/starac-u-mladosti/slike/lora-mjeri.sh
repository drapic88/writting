#!/bin/bash
# Bilježi memoriju dok radi mflux-train: slobodno, žičano, komprimirano i swap, svakih 15 s.
until pgrep -qf mflux-train; do sleep 5; done
while pgrep -qf mflux-train; do
  echo "$(date +%H:%M:%S) $(vm_stat | awk '/^Pages free/{f=$3}/^Pages wired/{w=$4}/occupied by compressor/{c=$5}END{printf "slobodno %d MB, žičano %d MB, komprimirano %d MB", f*16/1024, w*16/1024, c*16/1024}') | $(sysctl -n vm.swapusage | tr -s ' ')"
  sleep 15
done
