# Docker-Home-Assignment

setting up containerized nginx, with github actions

Testing is available via GitHub Actions - Docker CI workflow can be manually triggered

In order to run locally:

- clone the repository to your local machine
- run:
  - python3 configure_templates.py
  - docker-compose build
  - docker-compose up
- The result file will be found under ./results
