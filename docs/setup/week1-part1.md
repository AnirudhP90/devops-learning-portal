# DevOps Learning Portal - Week 1 Part 1

## Project Goal

Build a personal DevOps Learning Portal that will contain:

* Roadmaps
* Study Materials
* Interview Questions
* Notes
* Projects
* Certifications
* Progress Tracking

The portal will be built using:

* Python
* Flask
* Git
* GitHub
* AWS

The goal is not only to build a portal but also to learn real-world DevOps practices.

---

# Step 1: Update Ubuntu Server

Command:

```bash
sudo apt update
sudo apt upgrade -y
```

Why?

Before installing any software, we update the package repository and install the latest security patches.

This is a standard practice in Linux server administration.

---

# Step 2: Install Basic Tools

Command:

```bash
sudo apt install -y git curl wget zip unzip vim tree htop jq
```

Purpose of each tool:

| Tool      | Purpose                   |
| --------- | ------------------------- |
| git       | Source control            |
| curl      | API testing and downloads |
| wget      | Download files            |
| zip/unzip | Archive management        |
| vim       | Terminal editor           |
| tree      | View folder structure     |
| htop      | System monitoring         |
| jq        | Process JSON data         |

---

# Step 3: Verify Python

Command:

```bash
python3 --version
```

Why?

Flask applications require Python.

Python is the runtime that executes our application.

---

# Step 4: Create Workspace

Commands:

```bash
mkdir -p ~/projects
cd ~/projects
```

Why?

Keeping all projects under a dedicated projects directory improves organization.

---

# Step 5: Create Project Directory

Commands:

```bash
mkdir devops-learning-portal
cd devops-learning-portal
```

Why?

This directory will contain all project files.

---

# Step 6: Initialize Git Repository

Command:

```bash
git init
```

Why?

Git tracks changes to code over time.

Benefits:

* Version history
* Rollback capability
* Collaboration
* GitHub integration

Result:

```text
.git/
```

is created.

---

# Step 7: Create Project Structure

Commands:

```bash
mkdir templates
mkdir static
mkdir static/css
mkdir static/js
mkdir docs
mkdir data
```

Purpose:

## templates/

Stores HTML files rendered by Flask.

## static/

Stores CSS, JavaScript, and images.

### static/css/

Stylesheets.

### static/js/

JavaScript files.

## docs/

Project documentation.

## data/

Application data (JSON files later).

---

# Step 8: Create Virtual Environment

Command:

```bash
python3 -m venv venv
```

Why?

A virtual environment isolates project dependencies.

Without a virtual environment:

* Package conflicts occur.
* Different projects may require different versions.

Result:

```text
venv/
```

directory created.

---

# Step 9: Activate Virtual Environment

Command:

```bash
source venv/bin/activate
```

Result:

```text
(venv)
```

appears in terminal.

Why?

All Python packages will be installed inside this project only.

---

# Step 10: Install Flask

Command:

```bash
pip install flask
```

Why?

Flask is the web framework that will serve our portal pages.

Responsibilities:

* Handle requests
* Render HTML pages
* Manage routes
* Serve web content

---

# Step 11: Generate Requirements File

Command:

```bash
pip freeze > requirements.txt
```

Why?

Stores all project dependencies.

Benefits:

* Reproducible environments
* Easy deployment
* Team collaboration

Future use:

```bash
pip install -r requirements.txt
```

---

# Step 12: Create Flask Application

File:

```text
app.py
```

Purpose:

Main application entry point.

Responsibilities:

* Start Flask server
* Register routes
* Serve templates

---

# Step 13: Create Home Page

File:

```text
templates/home.html
```

Purpose:

First webpage rendered by Flask.

---

# Step 14: Run Flask Application

Command:

```bash
python app.py
```

Purpose:

Starts development server.

Default URL:

```text
http://SERVER-IP:5000
```

---

# Step 15: Configure Security Group

Opened Port:

```text
5000/TCP
```

Why?

AWS Security Groups act as a firewall.

Without opening port 5000, browser access would fail.

---

# Step 16: Create .gitignore

File:

```text
.gitignore
```

Contents:

```text
venv/
__pycache__/
*.pyc
.env
```

Why?

These files should never be committed to Git.

Benefits:

* Smaller repository
* Cleaner commits
* Better security

---

# Step 17: First Commit

Commands:

```bash
git add .
git commit -m "Initial Flask application setup"
```

Why?

Creates the first version of the project.

Benefits:

* Baseline version
* History tracking
* Rollback capability

---

# What I Learned

* Linux package management
* Python virtual environments
* Flask basics
* Git fundamentals
* AWS security groups
* Project directory structure
* Dependency management
* First web application deployment

---

# Current Architecture

```text
devops-learning-portal
│
├── app.py
├── data
├── docs
├── requirements.txt
├── static
│   ├── css
│   └── js
├── templates
│   └── home.html
└── venv
```

Status: Week 1 Part 1 Completed

