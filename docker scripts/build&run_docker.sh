#!/bin/bash
docker build . -t action
docker run --env-file ./env-list action