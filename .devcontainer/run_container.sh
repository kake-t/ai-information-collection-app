#!/bin/sh

CURRENT_DIR=$(pwd)

. $CURRENT_DIR/.env

export APP_NAME=$APP_NAME

devcontainer up --workspace-folder .