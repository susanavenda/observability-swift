# GitHub Actions Workflows – observability-swift

This project uses a comprehensive set of GitHub Actions workflows to automate CI/CD, testing, release management, and security scanning.

---

## CI & Testing

| File | Description |
|------|-------------|
| `checks.yml` | Runs code formatting (e.g., flake8, black) and unit tests to maintain code quality. |
| `run-integration-tests.yml` | Executes integration tests across system components like Kafka and Elasticsearch. |
| `gradle-wrapper-validation.yml` | Ensures `gradle-wrapper.jar` is valid and secure. Common in Java projects. |

---

## Build & Deployment

| File | Description |
|------|-------------|
| `build-images.yml` | Builds Docker images for services when code changes are detected. |
| `component-build-images.yml` | Shared job used by other workflows to modularize image builds. |
| `main.yml` | Default pipeline triggered on pushes to `main`, likely coordinating other jobs. |
| `release.yml` | Publishes GitHub releases and versioned artifacts (tags, changelogs, images). |
| `nightly-release.yml` | Scheduled nightly builds and releases to ensure continuous delivery. |

---

## Automation & Bots

| File | Description |
|------|-------------|
| `stale.yml` | Closes inactive PRs/issues after a threshold, keeping the repository clean. |
| `label-pr.yml` | Applies labels automatically to pull requests based on their content. |
| `assign-reviewers.yml` | Assigns reviewers automatically using code ownership or folder rules. |
| `dependabot-auto-update-protobuf-diff.yml` | Specialized update job for protobuf changes via Dependabot. |

---

## Security & Quality

| File | Description |
|------|-------------|
| `fossa.yml` | Checks license compliance of project dependencies using FOSSA. |
| `ossf-scorecard.yml` | Runs OpenSSF Scorecard to evaluate repository security and best practices. |