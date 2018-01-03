#!/usr/bin/env bash

gunicorn --worker-class eventlet -w 1 yj_websocket:app
