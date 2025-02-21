# Geoglows-AWS-Infrastructure-Architecture


This repository contains a Python script that generates an architecture diagram for an AWS ECS cluster using the [Diagrams](https://diagrams.mingrammer.com/) library. The diagram includes an ECS cluster running on a t2.2xlarge EC2 instance with a 100 GiB gp2 volume, three services (Tethys Platform, GeoServer, THREDDS Unidata Server), an Application Load Balancer (ALB) with three target groups, an ECR repository, and AWS Certificate Manager (ACM) for TLS.

## Prerequisites

- **Ubuntu Linux** (this guide assumes Ubuntu is used)
- **Python 3.7+** (verify installation with `python3 --version`)
- **pip** (usually installed with Python)
- **Graphviz** system package (for rendering diagrams)

## Installation Steps

### 1. Update your package list

Open a terminal and run:
```bash
sudo apt update

```
2. Install Graphviz
Graphviz provides the underlying executables (like dot) that the Diagrams library uses:

```bash
sudo apt install graphviz
```
3. (Optional) Create and activate a Python virtual environment
It's recommended to use a virtual environment to keep dependencies isolated:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the Diagrams library using pip
Install the required Python package:

```bash
pip install diagrams
```
Running the Diagram Generation Script
Assuming your Python script is named architecture.py, you can generate the diagram by running:

```bash
python architecture.py
```
By default, the script will generate a file (e.g., AWS_ECS_Architecture.png) in your working directory. You can open this file to view your architecture diagram.