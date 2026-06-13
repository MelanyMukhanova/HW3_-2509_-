#!/bin/bash

case "$1" in
    build_generator)
        docker build -t generator ./generator
        ;;
    run_generator)
        docker run --rm -v "$(pwd)/data:/data" generator
        ;;
    create_local_data)
        python generator/generate.py ./local_data
        ;;
    build_reporter)
        docker build -t reporter ./reporter
        ;;
    run_reporter)
        docker run --rm -v "$(pwd)/data:/data" reporter
        ;;
    structure)
        find . -type f -not -path "./.git/*" | sort
        ;;
    clear_data)
        rm -f data/*.csv data/*.html
        echo "Данные очищены"
        ;;
    inside_generator)
        docker run --rm -v "$(pwd)/data:/data" generator ls -la /data
        ;;
    inside_reporter)
        docker run --rm -v "$(pwd)/data:/data" reporter ls -la /data
        ;;
    *)
        echo "Использование: ./run.sh {build_generator|run_generator|create_local_data|build_reporter|run_reporter|structure|clear_data|inside_generator|inside_reporter}"
        exit 1
        ;;
esac