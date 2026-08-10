# Zero-Shot Learning Driven Security Orchestration and Automated Response

## Overview

This project presents a Zero-Shot Learning Driven Security
Orchestration and Automated Response (SOAR) framework for
detecting and responding to web attacks.

The system analyzes web server logs and identifies malicious
activities such as SQL Injection, XSS, brute-force attacks,
and denial-of-service attempts.

## Objectives

- Detect known and unknown web attacks using Zero-Shot Learning
- Automate security responses using SOAR
- Reduce manual intervention
- Reduce incident response time
- Provide a security monitoring dashboard

## System Architecture

<img width="904" height="601" alt="architecture diagram" src="https://github.com/user-attachments/assets/a76b95d5-474d-43a7-9578-9da2d071cce6" />


## Project Workflow

The proposed system follows a sequential workflow to detect web attacks and automatically respond to security incidents.

1. **Log Collection**
   - Collects web server access logs, error logs, and relevant network activity.
   - The collected raw data is stored for further analysis.

2. **Feature Extraction & Preprocessing**
   - Processes the collected raw logs into a structured format.
   - Removes unnecessary or noisy information.
   - Extracts important features such as IP address, URL, request type, and request content.

3. **Zero-Shot Attack Detection**
   - The preprocessed web requests are passed to the Zero-Shot Learning model.
   - The model analyzes the requests and classifies suspicious activities.
   - It can identify attack categories without requiring prior training for every attack type.
   - The system generates an attack classification and risk level.

4. **SOAR Orchestration**
   - The detection result is forwarded to the SOAR layer.
   - A security incident is created based on the detected threat.
   - The appropriate response workflow is selected according to the severity of the incident.

5. **Automated Response**
   - The selected response action is automatically executed.
   - Malicious IP addresses can be blocked using firewall rules.
   - Security alerts are generated for administrators.
   - Affected systems can be isolated when required.
   - Response actions are recorded for future analysis.

6. **Security Dashboard**
   - Displays detected attacks, alerts, incidents, and response information.
   - Helps administrators monitor the security status of the web application.

7. **Performance Evaluation**
   - The system evaluates detection accuracy and incident resolution time.
   - The performance is compared with the existing approach.
## Technologies

- Python
- Flask
- HTML
- CSS
- JavaScript
- Zero-Shot Learning
- SOAR
- Ubuntu Server
- Web Server Logs

## Attack Types

- SQL Injection
- Cross-Site Scripting (XSS)
- Brute Force
- Denial of Service
- Normal Traffic

## Results

Detection Accuracy: 98.5%

Incident Resolution Time: < 1 second

## Screenshots

<img width="738" height="466" alt="Security dashboard" src="https://github.com/user-attachments/assets/f50d20a5-d8f7-47ba-a848-44c3cb40405e" />


## Future Enhancements

- Adaptive Attention Mechanisms
- Explainable AI (XAI)
