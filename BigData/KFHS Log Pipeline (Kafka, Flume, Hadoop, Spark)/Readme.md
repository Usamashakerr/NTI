# KFHS Log Pipeline (Kafka, Flume, Hadoop, Spark)

This project implements a **real-time log processing pipeline** using:

- **Apache Kafka** for high-throughput log ingestion
- **Apache Flume** for log data collection and movement
- **Hadoop (HDFS)** for distributed data storage
- **Apache Spark** for real-time and batch data processing

## 📌 Objective

To build a scalable and efficient pipeline that collects, transports, stores, and analyzes logs in real-time, enabling advanced monitoring and insights into system/application behavior.

##  Components Overview

- **Kafka**: Acts as the message broker to handle streaming log data.
- **Flume**: Collects logs from source systems and pushes them into Kafka or HDFS.
- **HDFS**: Stores log data in a fault-tolerant, distributed environment.
- **Spark**: Processes stored logs for analytics, pattern detection, or alerting.

##  Use Cases

- Monitoring server or application logs
- Detecting anomalies or errors in real-time
- Generating analytics dashboards or reports


