# Shared Lab Guides

This folder contains common setup, cleanup, and troubleshooting guides used by the labs.

Read these guides before starting the hands-on labs.

## Who Should Read This?

These guides are useful if you are new to local MLOps practice and want to prepare your machine before running labs.

## Supported Local Environments

The guides and helper scripts are intended for:

    macOS
    Linux
    WSL2 on Windows

For Windows users, WSL2 with Docker Desktop is recommended.

Native Windows PowerShell support may be added later, but the main learning path uses shell commands that work best on macOS, Linux, or WSL2.

## Where to Run Commands

Run commands from the repository root unless a guide says otherwise.

Example:

    cd ~/mlops-practice-platform

Then run commands such as:

    ./scripts/check-prereqs.sh

## What the Shared Guides Cover

    setup-en.md              English setup guide
    setup-si.md              Sinhala setup guide
    cleanup-en.md            English cleanup guide
    cleanup-si.md            Sinhala cleanup guide
    troubleshooting-en.md    English troubleshooting guide
    troubleshooting-si.md    Sinhala troubleshooting guide

## What the Helper Scripts Do

Helper scripts are used to make local checks easier.

They should:

    check whether required tools are installed
    print useful version information
    explain what is missing
    avoid changing your system without asking
    avoid creating cloud resources

## Clean Lab Principle

Each lab should start from a clean or minimal state.

A lab should create only the resources it needs.

A lab should include cleanup steps so you can remove containers, volumes, temporary files, or local clusters created during that lab.

## Cost Note

The default labs are designed for local practice.

Expected default cost:

    Cloud cost: 0
    Local cost: laptop CPU, memory, and disk usage only

Cloud resources should only appear in optional cloud extension labs, with clear cost and cleanup notes.
