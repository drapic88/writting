#!/bin/bash
# Pokreni puno učenje (lora.py --uci), drži Mac budnim dok traje i bilježi memoriju u trening-memorija.log.
cd "$(dirname "$0")/.."
python3 slike/lora.py --uci --epoha "${1:-10}" > slike/flux/lora/trening-pokretanje.log 2>&1 &
UCENJE=$!
sleep 20
PID=$(pgrep -f mflux-train | head -1)
[ -n "$PID" ] && caffeinate -i -w "$PID" &
slike/lora-mjeri.sh > slike/flux/lora/trening-memorija.log 2>&1 &
wait $UCENJE
echo "exit $?" >> slike/flux/lora/trening-pokretanje.log
