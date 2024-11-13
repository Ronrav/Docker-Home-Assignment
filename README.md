# Docker-Home-Assignment

setting up containerized nginx, with github actions

Testing is available via GitHub Actions - Docker CI workflow can be manually triggered

In order to run locally:

- clone the repository to your local machine
- run:
  - ./configure-nginx.sh
  - docker-compose build
  - docker-compose up
- The result file will be found under ./results
- Port numbers and dir names are configurable via .env file
- dependencies:
  -envsubst
