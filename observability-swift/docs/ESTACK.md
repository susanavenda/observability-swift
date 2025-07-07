### `docs/elastic-stack.md` — Elastic Stack Kubernetes Deployment Guide

This document provides an overview of all components in the `elastic-stack` directory. It helps you understand the purpose of each manifest and how they work together in your observability pipeline.

## File Descriptions

| File | Purpose |
|------|---------|
| `ns-elastic.yaml` | Creates the `elastic` namespace to scope all resources. Deploy this first. |
| `eck-operator-certified.yaml`<br>`sub-elasticsearch-eck-operator-certified.yaml` | Deploys the **Elastic Cloud on Kubernetes (ECK)** Operator either via manifest or OperatorHub subscription. |
| `elasticsearch-elasticsearch.yaml` | Deploys a multi-node Elasticsearch cluster managed by ECK. |
| `kibana-kibana.yaml` | Deploys Kibana and connects it to the Elasticsearch instance. |
| `agent-fleet-server.yaml` | Deploys Fleet Server that manages Elastic Agent policies. Must be reachable by Kibana. |
| `agent-elastic-agent.yaml` | Deploys the Elastic Agent in **Fleet mode**, connected to Fleet Server and Kibana. |
| `apmserver-apm-server.yaml` | Deploys the APM Server to ingest application traces and metrics. |
| `cr-elastic-agent.yaml` | Creates a Kubernetes ClusterRole for Elastic Agent to collect logs and metrics from the cluster. |
| `sa-elastic-agent.yaml` | ServiceAccount for the Elastic Agent to operate with the necessary RBAC permissions. |
| `route-*.yaml` | Optional ingress routes (or OpenShift Routes) for external access to Kibana, APM, and Elasticsearch. |
| `kustomization.yaml` | Optional Kustomize configuration to manage deployment of multiple resources at once. |

## Deployment Order

To deploy correctly, follow this order:

```sh
kubectl apply -f ns-elastic.yaml
kubectl apply -f eck-operator-certified.yaml
kubectl apply -f elasticsearch-elasticsearch.yaml
kubectl apply -f kibana-kibana.yaml
kubectl apply -f agent-fleet-server.yaml
kubectl apply -f cr-elastic-agent.yaml
kubectl apply -f sa-elastic-agent.yaml
kubectl apply -f agent-elastic-agent.yaml
kubectl apply -f apmserver-apm-server.yaml
kubectl apply -f route-kibana.yaml    # Optional
kubectl apply -f route-apm-server.yaml  # Optional
```

## Fleet Server & TLS Configuration

To ensure a successful deployment and secure communication:

- **TLS Considerations**: Confirm that both Kibana and Fleet Server endpoints are reachable and their TLS certificates are valid and trusted by your local environment. Use valid routes or DNS entries to avoid certificate verification issues.
- **Manual Fleet Enrollment**: After deploying Fleet Server, access the Kibana interface, navigate to *Management > Fleet > Agents*, and enroll the server manually if it doesn't appear automatically.
- **Agent Policy Setup**: Before deploying Elastic Agents, ensure the `eck-agent` policy exists in Kibana or create it manually. This policy defines what data is collected and where it’s sent.

## Optional Improvements

- Kustomize is already used in this setup. Optionally, convert to a Helm chart for templating and advanced reuse.
- Use GitOps (e.g. ArgoCD) to sync and maintain the state of these resources.
- Add dashboards under `elastic/dashboards/` for automated observability views.
