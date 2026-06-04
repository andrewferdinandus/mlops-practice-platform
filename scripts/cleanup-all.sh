#!/usr/bin/env bash

set -e

echo "Safe cleanup helper for mlops-practice-platform"
echo ""
echo "This script removes common local generated files from this repository."
echo "It does not delete cloud resources."
echo "It does not run global Docker prune commands."
echo ""

read -r -p "Continue cleanup? Type yes to continue: " confirm

if [ "$confirm" != "yes" ]; then
  echo "Cleanup cancelled."
  exit 0
fi

echo ""
echo "Removing common generated folders if they exist..."

find . -type d -name "__pycache__" -prune -exec rm -rf {} +
find . -type d -name ".pytest_cache" -prune -exec rm -rf {} +
find . -type d -name "mlruns" -prune -exec rm -rf {} +
find . -type d -name "mlartifacts" -prune -exec rm -rf {} +

echo "Removing common generated files if they exist..."

find . -type f -name "*.pyc" -delete
find . -type f -name ".DS_Store" -delete

echo ""
echo "Cleanup completed."
echo ""
echo "Docker containers, Docker volumes, and Kubernetes clusters are not removed by this script."
echo "Use lab-specific cleanup instructions for those resources."
