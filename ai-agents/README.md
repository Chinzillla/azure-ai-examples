# AI Agents

## Security Risks for AI Agents

1. Data leakage and privacy exposure
2. prompt injection and manipulation attacks
3. Unauthorized access and privilege escalation
4. Data poisoning
5. Supply chain vulnerabilities
6. unsupervised autonomous actions
7. Lack of auditability and logging
8. Model inversion and output leakage

## Mitigation Strategies

1. Add prompt filtering and validation layers
2. Enforce RBAC and least privilege permissions
3. Retrain and validate model to detect data drift or poisoning attempts
4. Sandbox or gating sensitive operations behind human approvals

## Agent Types

### Declarative agents

Agents defined through configuration rather than code

#### Prompt-based agents

Single agent configured with model, instructions, tools, and prompt

#### Workflow agents

Multi agent orchestrations defined in YAML for scenarios with multi-agent collab

### Hosted agents

Containerized agents that are created and deployed in code. Foundry takes care of infra.

## Microsoft Foundry Agent Service Key Features

### Automatic tool calling

Service handles tool-calling lifecycle
- running model
- invoke tools
- return results

### Securely managed data

Conversion states managed through Responses API
- No need for manual state management

### Extensive tool catalog

Library of built-in and community tools

Examples:
- code execution
- file search
- web search
- integrations with Azure services and external APIs

### Model Selection

Various AI model selections

### Enterprise grade security

Data privacy and compliance
- secure data handling
- keyless auth (entra and identity)
- built in content safety filters

### Customizable storage solutions

platform-managed storage or Azure Blob storage

### Observability and Tracing

Built-in monitoring
- track agent behavior
- debug issues
- optimize performance
