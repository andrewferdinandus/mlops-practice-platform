#!/usr/bin/env bash

set -e

echo "Checking local prerequisites for MLOps labs..."
echo ""

check_command() {
  local command_name="$1"
  local version_command="$2"

  if command -v "$command_name" >/dev/null 2>&1; then
    echo "[OK] $command_name found"
    eval "$version_command" || true
  else
    echo "[MISSING] $command_name not found"
  fi

  echo ""
}

check_command "git" "git --version"
check_command "python3" "python3 --version"
check_command "docker" "docker --version"
check_command "curl" "curl --version | head -n 1"

if command -v docker >/dev/null 2>&1; then
  echo "Checking Docker Compose..."
  if docker compose version >/dev/null 2>&1; then
    echo "[OK] docker compose found"
    docker compose version
  else
    echo "[MISSING] docker compose not found"
  fi
  echo ""
fi

echo "Optional tools for later labs:"
echo ""

check_command "kubectl" "kubectl version --client"
check_command "kind" "kind version"
check_command "k3d" "k3d version"
check_command "helm" "helm version --short"
check_command "jq" "jq --version"

echo "Prerequisite check completed."
echo ""
echo "Note:"
echo "This script only checks local tools."
echo "It does not create cloud resources."
