FaultTrek: Cloud-Native Chaos Engineering Toolkit
FaultTrek is a Python-based chaos engineering framework designed to simulate faults in containerized microservices. It helps teams test resilience, validate fault tolerance, and monitor system behavior under controlled failure conditions.

Features
Cloud-Native Chaos Experiments: Simulate latency, crashes, and network partitions.

Configurable Chaos Profiles: Easily define injection intervals and fault types using simple YAML files.

CLI & Automation: Includes a CLI tool and experiment scheduler for automated profile runs.

Real-time Observability: Designed to integrate with Prometheus and Grafana for monitoring key metrics.

CI/CD Automation: Comes with a ready-to-use GitHub Actions workflow that builds Docker images, runs automated tests, and pushes to Docker Hub.

Modular Design: Easily extend the framework with new, custom fault types.

Project Structure
.
├── .github/workflows/   # CI/CD workflows
├── deployments/         # Kubernetes manifests (optional)
├── docker/              # Dockerfile and Docker Compose for local development
├── faulttrek/           # Main Python source code
│   ├── modules/         # Individual fault injection modules
│   └── profiles/        # YAML profiles for chaos experiments
├── test-app/            # A simple target application for CI testing
├── grafana/             # Grafana dashboard configurations (optional)
├── docker-compose.ci.yml# Docker Compose file for CI testing
├── run_all_profiles.sh  # Script to run all chaos profiles
└── README.md

Installation and Usage
Clone the repository to get started. You can run experiments locally using Docker Compose or by calling modules directly in Python.

# Clone the repository
git clone [https://github.com/ramshenoy7/Fault-Trek.git](https://github.com/ramshenoy7/Fault-Trek.git)
cd Fault-Trek

# Run all chaos profiles using the provided script
./run_all_profiles.sh

Profiles simulate faults in microservices and log their results. When run with the local docker-compose.yml, metrics are exposed for Prometheus, and dashboards can be viewed in Grafana.

CI/CD
The project includes a robust CI/CD pipeline using GitHub Actions. The workflow handles:

Building the faulttrek Docker image.

Running an automated test suite against a temporary target application.

Logging into Docker Hub and pushing the new image if tests pass.

Uploading logs as build artifacts for debugging.

Tests run automatically on every push or pull request to the main branch.

Docker
The project can be run locally using Docker Compose, which also starts Prometheus and Grafana services for full observability.

# Start all services (FaultTrek, Prometheus, Grafana)
docker compose -f docker/docker-compose.yml up -d

Kubernetes Deployment (Optional)
A sample Kubernetes deployment is included under the deployments/ directory. The manifests include service deployments and chaos experiment jobs. While full cluster-level deployment was not executed due to resource constraints, they can be deployed on Minikube, kind, or a cloud cluster when resources are available.

Metrics and Observability
Prometheus collects metrics during chaos experiments.

Grafana provides dashboards for visualizing the impact of faults.

Logs are stored locally and are also uploaded as artifacts in CI/CD workflow runs.

Extending FaultTrek
Add new fault injection logic as a Python file in faulttrek/modules/.

Create a new YAML configuration in faulttrek/profiles/.

Update the run_all_profiles.sh script to include your new profile for automated execution.

Contributing
Contributions are welcome! Fork the repository, create a feature branch, write tests for your new features, and submit a pull request.
