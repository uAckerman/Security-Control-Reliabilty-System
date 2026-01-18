# Security-Control-Reliabilty-System
I’ve seen security controls fail silently, so I built a system that continuously verifies whether our controls are actually protecting us.

**Author:** Uzair Khan

## Overview

Modern security programs often assume that controls, safeguards, or protection mechanisms continue to work correctly once configured. In reality, these controls can silently fail, drift, or degrade over time due to misconfigurations, system updates, or integration issues.  
  
Instead of trusting configuration or dashboards, the engine executes real interactions against a security control and evaluates:

**- Whether the control enforces its policy**  
**- Whether security actions are visible**  
**- Whether detection happens within an acceptable latency**

The goal is to detect silent security failures before attackers do.

## Why This Matters

In real environments, security controls can degrade due to:

- Configuration drift

- Platform upgrades

- Integration failures

- Pipeline issues

Traditional tools often validate configuration, not runtime behavior.

## How the Engine Works

At a high level:

**- The engine loads an expected control state from configuration.**

**- Active probes execute real requests against the control.**

**- Runtime behavior is captured and analyzed.**

**- Observed behavior is compared against expectations.**

**- Drift, degradation, or failures trigger alerts.**

***
<div align="center">
  <img src="doc/screenshots/project_flow.png" alt="project" width="5000"> 
</div>

***

## Example Control: Keycloak (Open-Source IdP)  
---
> ℹ️ **The architecture is tool-agnostic and can be extended to other platforms (IAM, WAF, EDR, firewalls, cloud controls)**    

---
To demonstrate the engine, I used **Keycloak** as a reference open-source security control.

**Keycloak provides:** _Authentication and Access Enforcement | Policy and Flow Configuration | Event and Audit Logging_

***
<div align="center">
  <img src="doc/screenshots/keycloak_implementation.png" alt="project" width="5000"> 
</div>

***

