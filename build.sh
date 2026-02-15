#!/bin/bash
# Build script for Render

# Install dependencies
pip install -r backend/requirements.txt

# Copy frontend to backend directory for deployment
cp -r frontend backend/
