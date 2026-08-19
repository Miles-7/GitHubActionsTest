# GitHubActionsTest

A minimal end-to-end pipeline built to learn REST APIs and CI/CD fundamentals: a single FastAPI endpoint, containerized with Docker, and deployed to AWS Lambda via GitHub Actions.

## What it does

- Exposes one FastAPI endpoint
- Packaged as a Docker container image (Lambda container image deployment, not a zip package)
- CI/CD pipeline via GitHub Actions builds the image and deploys it to AWS Lambda on push

## Stack

- **FastAPI** — API framework
- **Docker** — containerization
- **AWS Lambda** — deployment target (container image)
- **GitHub Actions** — CI/CD

## Branches

- `boiler_code` — active development branch

## Setup / Deployment notes

- AWS interactions are done via **AWS CloudShell** rather than a local AWS CLI install, due to credential/token issues encountered locally.
- [Add specific setup steps here: env vars, IAM role/permissions needed, how to trigger the workflow manually if applicable.]

## Status

Work in progress — learning project focused on understanding the REST API → Docker → Lambda → CI/CD flow end-to-end.
