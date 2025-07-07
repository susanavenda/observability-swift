# Git Strategy for Observability-Swift Project

## Branching Model

We follow a simplified Git Flow strategy:

- **main**: Production-ready, stable code. Protected branch.
- **dev**: Integration branch where features and fixes are merged before releasing to main.
- **feature/**: Individual feature branches created from `dev`.
- **hotfix/**: Emergency fixes created from `main` and merged back into both `main` and `dev`.

## Pull Request Policy

- All changes must be made through Pull Requests (PRs).
- PRs should be reviewed by at least one other team member.
- Include descriptive commit messages and link to related issues.
- PR title should follow semantic naming (e.g., `feat: add Kafka consumer retry logic`).

## Commit Message Convention

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation
- `refactor:` for code restructuring
- `test:` for test changes
- `chore:` for maintenance

## CI/CD Integration

- Each PR triggers GitHub Actions for:
  - Linting (Python, YAML)
  - Testing (pytest for Kafka consumer)
  - Terraform validation
  - Ansible syntax check
- Merges into `main` trigger deployment jobs (optional)

## Tagging and Releases

- Use semantic versioning (e.g., `v1.0.0`)
- Tags are created from `main` when a release is stable
- Release notes must be generated for every tag
