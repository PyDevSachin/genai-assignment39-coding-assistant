
---
title: AI Coding Assistant
emoji: 💻
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---

# Assignment 39: GenAI App Deployment

## Project Overview

This project demonstrates the deployment of a Generative AI coding assistant using Streamlit Cloud and Hugging Face Spaces.

The application helps users generate Python code, explain existing code, debug programming errors, and optimize code.

## Technologies Used

- Python
- Streamlit
- Groq API
- GPT-OSS 20B
- GitHub
- Streamlit Community Cloud
- Hugging Face Spaces
- Docker

## Application Features

1. Generate Code
2. Explain Code
3. Debug Code
4. Optimize Code

## Deployment Architecture

The application uses Streamlit for its user interface and the Groq API for AI-generated responses.

The API key is stored securely using the secrets management features of the deployment platforms.

The application does not require a locally installed Ollama model when deployed.

## Project Structure

- app.py - Main Streamlit application
- task3.py - Reusable coding assistant functions
- prompts.py - Prompt templates
- requirements.txt - Python dependencies
- Dockerfile - Hugging Face deployment configuration
- .gitignore - Files excluded from Git
- README.md - Project documentation

## Installation

Install the dependencies:

pip install -r requirements.txt

Configure the GROQ_API_KEY environment variable before running the application locally.

## Run Locally

streamlit run app.py

## Task 1: Streamlit Cloud Deployment

The project is uploaded to GitHub and deployed using Streamlit Community Cloud.

The deployed application is tested using its public Streamlit URL.

## Task 2: Hugging Face Spaces Deployment

The application is deployed using Hugging Face Spaces with Docker and Streamlit.

The Groq API key is configured securely through Space settings.

The deployed application is tested using its Hugging Face URL.

## Task 3: Platform Comparison

### Streamlit Cloud

Streamlit Cloud provides a simple way to deploy Streamlit applications directly from GitHub.

Advantages:
- Easy deployment.
- Direct GitHub integration.
- Automatic application updates after repository changes.
- Simple secrets management.

Disadvantages:
- Resource limitations.
- Primarily designed for Streamlit applications.
- Less flexibility for custom container configurations.

### Hugging Face Spaces

Hugging Face Spaces provides a platform for hosting and sharing machine learning and AI applications.

Advantages:
- Designed for sharing AI and machine learning demos.
- Supports Docker-based deployment.
- Integrates with the Hugging Face ecosystem.
- Supports different application frameworks.

Disadvantages:
- Docker deployment requires additional configuration.
- Build and deployment process can be more complex.
- Compute availability and pricing depend on the selected hardware and account plan.

### When to Use Each Platform

Streamlit Cloud is suitable for quickly deploying and sharing Streamlit applications.

Hugging Face Spaces is suitable for hosting AI and machine learning demonstrations, especially when Docker configuration or Hugging Face integration is required.

## Conclusion

This assignment demonstrates how a Generative AI application can be deployed and made accessible to users through cloud platforms.

The same AI coding assistant was prepared for deployment on Streamlit Community Cloud and Hugging Face Spaces.