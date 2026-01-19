# Keycloak Core Configuration

A dedicated Keycloak realm is used to keep everything isolated and safe for testing.

## Configuration Steps
The Keycloak environment is configured with the following core components:

### 1. Realm Isolation
A dedicated Keycloak realm named **scrs-core** is created to provide logical isolation of users, authentication flows, and security controls.

***
<div align="center">
  <img src="doc/screenshots/p1.png" alt="project" width="5000"> 
</div>

***

### 2. User Provisioning
A test account **uzair-test** is created with temporary **Password** and **TOTP** to ensure consistent authentication behavior across automated and manual tests.

***
<div align="center">
  <img src="doc/screenshots/p2.png" alt="project" width="5000"> 
</div>

***
<div align="center">
  <img src="doc/screenshots/p4.png" alt="project" width="5000"> 
</div>

***

### 3. MFA Enforcement
Time-based One-Time Password (TOTP) MFA is configured and enforced using a custom authentication flow called **Browser_Flow**, ensuring all interactive logins require a second authentication factor.

***
<div align="center">
  <img src="doc/screenshots/p5.png" alt="project" width="5000"> 
</div>

***
<div align="center">
  <img src="doc/screenshots/p6.png" alt="project" width="5000"> 
</div>

***
