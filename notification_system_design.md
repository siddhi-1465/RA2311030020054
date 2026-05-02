# Notification System Design

## Overview
This system logs frontend and backend activities using a centralized logging middleware.

## Components
- Logging Middleware: Sends logs to external API
- Backend App: Generates backend logs
- Frontend App: Generates frontend logs

## Flow
1. Event occurs
2. Log() function is called
3. API request is sent to logging service
4. Log is stored and response returned

## Tech Used
- Python
- REST API
- Postman (for testing)
