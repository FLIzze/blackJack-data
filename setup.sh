#!/bin/bash
npm install
pip install -r requirements.txt
echo "API_URL=http://localhost:5000/" > .env

