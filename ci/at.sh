#!/bin/sh

IMAGE=$(sirius docker_image_name | head -n 1)

sirius docker_deploy:flasky,${IMAGE},server=DEPLOY_SERVER,ports="9201;8080"
