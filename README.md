# 2508_DS5111_nnu7hu
DS 5111 Class Content

# Data Science VM Setup Guide

## Prerequisites

Before starting, ensure you have:
- A fresh Ubuntu VM instance (AWS EC2 or similar)
- SSH access to the VM
- A GitHub account with SSH key already configured on the VM
- Basic familiarity with command line operations

## Quick Setup Instructions

Follow these steps to transform a bare VM into a fully functional Data Science development environment:

### 1. Initial VM Setup

Run the bootstrap script to install essential packages:

```bash
chmod +x scripts/init.sh
bash scripts/init.sh
```

**Expected outcome:** The script will update the system and install `make`, `python3.12-venv`, and `tree`. Test by running `tree` - you should see your directory structure instead of an error.

### 2. Configure Git Credentials

Set up your GitHub identity for commits:

```bash
# First, edit the script with your details
nano scripts/init_git_creds.sh
# Replace <your github email> and <your github user name> with your actual credentials

# Make executable and run
chmod +x scripts/init_git_creds.sh
bash scripts/init_git_creds.sh
```

**Expected outcome:** You should see your email and username displayed twice (before and after configuration).

### 3. Clone Repository

Clone your project repository:

```bash
git clone git@github.com:<your-username>/2508_DS5111_<your-uvaid>.git
cd 2508_DS5111_<your-uvaid>
```

### 4. Create Python Virtual Environment

Set up an isolated Python environment with required packages:

```bash
make update
```

**Expected outcome:** This creates a virtual environment in the `env/` directory and installs pandas and numpy.

### 5. Verify Installation

Test that everything is working correctly:

```bash
# Activate virtual environment
. env/bin/activate

# Check installed packages
pip list
```

**Expected outcome:** You should see `(env)` in your prompt and `pandas` and `numpy` listed in the pip output.

## Project Structure

After setup, your project should look like this:

```
├── README.md
├── makefile
├── requirements.txt
├── scripts/
│   ├── init.sh
│   └── init_git_creds.sh
└── env/
    └── [virtual environment files]
```

## Available Make Commands

- `make` - Display makefile contents
- `make update` - Create/update virtual environment and install packages
- `make env` - Create virtual environment only

## Troubleshooting

**SSH Key Issues:** If git clone fails, ensure your SSH key is properly configured with GitHub. Test with `ssh -T git@github.com`.

**Permission Errors:** If scripts won't run, ensure they're executable with `chmod +x script_name.sh`.

**Package Installation Fails:** Make sure you're running `make update` from the repository root directory where the `requirements.txt` file is located.

## Next Steps

With your environment set up, you can:
1. Activate your virtual environment: `. env/bin/activate`
2. Start developing Python scripts
3. Add new packages to `requirements.txt` and run `make update`
4. Commit and push your work to GitHub

## Recovery from VM Loss

If your VM crashes or is lost, simply:
1. Provision a new VM with SSH key access
2. Follow this README from step 1
3. Your work will be restored from GitHub

This setup ensures you're never more than a few commands away from a fully functional development environment.
