# Autonomous PCB Defect Inspection Agent 🔍⚡
> **OpenCV AI Competition 2026 Submission** | Powered by **OpenCV 5** & **AWS**

## 📌 Overview
An intelligent, closed-loop PCB defect detection system that uses **OpenCV 5** for computer vision and **AWS Serverless infrastructure** to run an **Agentic Decision Loop**. 

Unlike static inspection scripts, this system evaluates visual evidence dynamically: when a defect is detected, the agent determines the next best action—adjusting image capture parameters, triggering localized high-resolution re-scans, dispatching alerts via AWS SNS, and logging structured defect analytics in AWS DynamoDB.

---

## 🏗️ System Architecture
```mermaid
graph TD
    %% Custom Styling
    classDef perception fill:#1f2937,stroke:#3b82f6,stroke-width:2px,color:#fff;
    classDef agent fill:#111827,stroke:#10b981,stroke-width:2px,color:#fff;
    classDef aws fill:#1e1b4b,stroke:#8b5cf6,stroke-width:2px,color:#fff;

    A[📷 High-Res PCB Image Stream] --> B[🔍 1. Perception Layer: OpenCV 5]:::perception
    B -->|Adaptive Threshold & Denoising| C[Detect Defect Contours & Severity]:::perception
    
    C -->|Defect Bounding Box & Metadata| D[🧠 2. Agentic Decision & Control Loop]:::agent
    
    D -->|High Severity Defect| E[🚨 Trigger AWS Alert Queue]:::agent
    D -->|Low Severity Analytics| F[📊 Log Telemetry]:::agent
    
    E --> G[☁️ AWS SNS / Lambda Dispatch]:::aws
    F --> H[🗄️ AWS DynamoDB Telemetry Store]:::aws
    B -->|High-Res Crop| I[📦 AWS S3 Defect Vault]:::aws
```
---

## ✨ Key Features
- **Agentic Perception-Decision Loop:** Vision outputs directly drive execution workflow decisions.
- **OpenCV 5 Optimization:** Fast feature extraction and defect isolation.
- **AWS Cloud Integration:** Fully serverless telemetry, storage, and event routing.
- **Reproducible Evaluation:** Comprehensive test scripts with synthetic and real-world PCB defect samples.

---

## 🚀 Getting Started
```bash
# Clone the repository
git clone [https://github.com/umeshianjana/PCB-Defect-Inspection-Agent.git](https://github.com/umeshianjana/PCB-Defect-Inspection-Agent.git)
cd PCB-Defect-Inspection-Agent

# Install dependencies
pip install -r requirements.txt
