#! /bin/sh

COVER=coverage

${COVER} run --source flasky -m unittest discover --start-directory test --pattern test_*.py

[ $? -gt 0 ] && exit 1

${COVER} xml
