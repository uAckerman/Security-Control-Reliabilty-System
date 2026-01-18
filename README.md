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

***
<div align="center">
  <img src="doc/screenshots/project_flow.png" alt="project" width="5000"> 
</div>

***

## Why This Matters

In real environments, security controls can degrade due to:

- Configuration drift

- Platform upgrades

- Integration failures

- Pipeline issues

Traditional tools often validate configuration, not runtime behavior.

## Example Control: Keycloak (Open-Source IdP)
