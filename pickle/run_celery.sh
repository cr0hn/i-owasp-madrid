#!/usr/bin/env bash

celery -A celery_exploit:app worker -l INFO