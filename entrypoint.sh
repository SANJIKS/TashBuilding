#!/bin/bash

SERVEO_DOMAIN=${SERVEO_DOMAIN}
PORT=${PORT}

ssh -o StrictHostKeyChecking=no -R ${PORT}:localhost:${PORT} ${SERVEO_DOMAIN}
