


# Ansible Project Overview

This directory contains the Ansible configuration for automating RHEL system patching as part of the `observability-swift` platform.

## Structure

```
ansible/
├── ansible.md                  # This documentation file
├── patch_rhel.yml              # Playbook to patch RHEL systems
└── roles/
    └── patch/
        ├── tasks/
        │   └── main.yml        # Main tasks to apply updates
        └── handlers/
            └── main.yml        # Handlers to restart services
```

## Playbook: `patch_rhel.yml`

This playbook applies updates to RHEL-based systems. It includes a `patch` role which:
- Updates all installed packages
- Uses handlers to restart key services like `sshd` or `network` only when needed

### Usage

Run the playbook with:

```bash
ansible-playbook -i inventory patch_rhel.yml
```

## Role: `patch`

- **tasks/main.yml**: Defines tasks to apply system updates via `dnf update -y`.
- **handlers/main.yml**: Contains handlers to restart `sshd` and `network` services when changes occur.

## Inventory

The inventory file should define hosts and groups (not yet included in this repo) that you want to target.

---

## To Do

- Add an inventory file with real or test hosts
- Expand with additional roles (e.g., install agents, configure logging)
- Parameterize patching tasks for flexibility
