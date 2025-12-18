# 🚀 Kubernetes Monitoring & Load Benchmarking Coursework

## 📘 Overview
This project demonstrates the deployment of a Java benchmarking application on Kubernetes, the setup of a complete monitoring stack using Prometheus and Grafana, and the generation of load to analyse CPU and memory behaviour in real time.

The coursework is divided into four tasks, each building step by step to show how applications are deployed, monitored, and analysed in a Kubernetes environment.

---

## 🎯 Coursework Aim
The aim of this coursework is to deploy a containerised application on Kubernetes, monitor its resource usage using Prometheus and Grafana, and analyse the system behaviour under load.

---

## 🧩 Task 1: Kubernetes Dashboard & Java Application

### Objective
To deploy a Java-based benchmarking application on Kubernetes and use the Kubernetes Dashboard to visually monitor cluster resources and workloads.

### Implementation
The Java benchmark application was deployed using a Kubernetes Deployment and exposed using a Service. This application performs a prime number check, which creates CPU and memory load.

The Kubernetes Dashboard was deployed using the official YAML configuration. A service account with admin permissions was created to allow secure access. The dashboard service was exposed using NodePort so it could be accessed through a web browser using the VM IP and port.

---

## 📊 Task 2: Kubernetes Monitoring Stack

### Objective
To deploy a monitoring stack consisting of Prometheus, Grafana, Node Exporter, and kube-state-metrics to collect and visualise Kubernetes metrics.

### Implementation
Prometheus was deployed to collect metrics from the cluster. Node Exporter was deployed as a DaemonSet so that CPU and memory metrics are collected from each node. kube-state-metrics was deployed to provide Kubernetes object-level metrics.

Grafana was deployed and connected to Prometheus as a data source. Grafana was exposed using a NodePort service, allowing access from a web browser. Pre-built dashboards were used to visualise CPU, memory, disk, and network metrics.

---

## 🔥 Task 3: Load Generator

### Objective
To create a load generator that sends continuous requests to the Java application in order to simulate system load.

### Implementation
A Python script was written to send HTTP requests repeatedly to the Java benchmark service. The request rate is controlled using environment variables.

The Python script was packaged into a Docker image using a Dockerfile. This image was pushed to the local container registry so that Kubernetes could pull it and run it as a pod.

---

## 📈 Task 4: Monitoring & Benchmarking

### Objective
To observe and analyse the impact of load on system resources using Grafana dashboards.

### Implementation
The load generator was deployed as a Kubernetes Deployment. When the load generator was running, increased CPU and memory usage was observed in Grafana dashboards.

The load generator deployment was scaled up and down to start and stop the load. This allowed clear comparison between system behaviour with load and without load using real-time metrics.

---

## 📷 Screenshots Included in Report
- Kubernetes Dashboard showing running workloads  
- Prometheus targets page confirming active metric scraping  
- Grafana Prometheus data source configuration  
- Node Exporter dashboard (CPU & memory metrics)  
- Java application CPU and memory graphs  
- Load generator pod logs  
- `kubectl get pods` output for all tasks  

---

## ✅ Conclusion
This coursework successfully demonstrates how applications can be deployed and monitored in Kubernetes. By generating load and analysing real-time metrics using Prometheus and Grafana, the impact of workload on system resources was clearly observed. The project provides practical understanding of Kubernetes monitoring and performance analysis.

---

## 👤 Author
**Aaditya Kute**  
MSc Cloud Computing – Newcastle University  
GitHub: https://github.com/aadityakute04

