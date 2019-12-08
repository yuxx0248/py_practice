#!/bin/bash

python3 as_server.py localhost 50051 &
python3 tgs_server.py localhost 50052 &
python3 b_server.py localhost 50053 &
