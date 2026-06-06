# 🎮 3D Network Threat Visualizer

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Unity](https://img.shields.io/badge/Unity-3D-black.svg)](https://unity.com/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.9.0-orange.svg)](https://scikit-learn.org/)
[![UDP](https://img.shields.io/badge/UDP-Realtime-green.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Overview

A **polymathic project** combining Python Machine Learning (98.92% accuracy) with Unity 3D to visualize network threats in real-time. The system simulates network logs, classifies threats using a Random Forest model, and displays them in an interactive 3D environment.

🔗 Links
GitHub: unity-network-visualizer

### Key Features

| Feature | Description |
|---------|-------------|
| **🎯 98.92% Accuracy** | Random Forest classifier for threat detection |
| **🎮 Unity 3D Visualization** | Real-time 3D threat visualization |
| **🟢🔴 Visual Indicators** | Green spheres (normal) vs Red spheres (threats) |
| **📝 Threat Labels** | Floating text showing threat type |
| **⚡ Real-time Processing** | 2 logs/second with <10ms latency |
| **🌐 UDP Streaming** | Low-latency network communication |

## 🏗️ Architecture
Python ML Model (Random Forest)
↓
Log Generator
↓
Threat Classification
↓
UDP Socket (Real-time)
↓
Unity 3D Receiver
↓
Visual Output
(Green/Red Spheres + Text)

text

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **ML Model** | Random Forest (98.92% accuracy) |
| **Feature Extraction** | TF-IDF Vectorization |
| **Data Processing** | Pandas, NumPy |
| **Real-time Communication** | UDP Sockets |
| **Visualization** | Unity 3D, C# |
| **Language** | Python, C# |

## 🚀 Quick Start

### Prerequisites

```bash
# Install Python dependencies
pip install scikit-learn pandas numpy joblib
Run the Pipeline
Open Unity Project - Open NetworkThreatVisualizer in Unity

Press Play - Start the Unity receiver

Run Python script - Execute the threat sender

bash
python unity_log_sender.py
🎯 What You'll See
Indicator	Meaning
🟢 Green Sphere	Normal network traffic
🔴 Red Sphere	Detected threat
Floating Text	Threat type (Ransomware, DDoS, Port Scan, etc.)
📊 Threat Detection
The ML model detects the following threat types:

Threat Type	Description
Ransomware	File encryption attacks
DDoS	Distributed denial of service
Port Scan	Network reconnaissance
Suspicious Traffic	Anomalous patterns
📦 Project Structure
text
unity-network-visualizer/
├── unity_log_sender.py              # Python ML + UDP sender
├── NetworkThreatVisualizer_Assets.rar  # Unity project files
├── requirements.txt                 # Python dependencies
├── LICENSE                          # MIT License
└── README.md                        # Documentation
🔧 Usage Examples
Python Sender
python
# Example of sending threat data
import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = {
    "threat_type": "Ransomware",
    "confidence": 0.945,
    "source_ip": "192.168.1.100"
}
sock.sendto(json.dumps(data).encode(), ('127.0.0.1', 8888))
Unity C# Receiver
csharp
// UDP receiver in Unity
UdpClient udpClient = new UdpClient(8888);
IPEndPoint remoteEndPoint = new IPEndPoint(IPAddress.Any, 0);

async void Start()
{
    while (true)
    {
        byte[] data = await udpClient.ReceiveAsync();
        string message = Encoding.UTF8.GetString(data);
        // Spawn sphere based on threat type
    }
}
📈 Performance Metrics
Metric	Value
ML Accuracy	98.92%
Processing Speed	2 logs/second
Latency	<10ms
Threat Types	4+ categories
🚀 Future Improvements
Add more attack types (SQL Injection, MITM, etc.)

Implement threat heatmaps in 3D space

Deploy to WebGL for browser-based visualization

Add real-time network traffic capture

Create dashboard for historical analysis

📄 License
MIT License

Built with 🎮, 🐍, and 🔒 by Aikaksh Singh Routela
