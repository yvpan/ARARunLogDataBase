# ARA Run Log Database

A relational database and automated monitoring framework for the Askaryan Radio Array (ARA) experiment at the South Pole.

This project was developed to manage operational run logs, automate metadata tracking, and support real-time monitoring for large-scale ultra-high-energy neutrino detector operations.

---

## Overview

The Askaryan Radio Array (ARA) is a radio-based neutrino detector designed to observe ultra-high-energy neutrinos in Antarctic ice.

Operating a distributed detector system in extreme environments generates large volumes of run metadata, detector-status logs, calibration records, and operational diagnostics. This project provides:

- A structured relational database for detector run logs
- Automated ingestion and update pipelines
- Real-time monitoring support
- Query interfaces for operational analysis
- Scalable metadata management for long-term detector operations

The framework was integrated into the ARA data-processing workflow at the University of Delaware.

---

## Key Features

- Relational database schema for detector operations
- Automated parsing and ingestion of run logs
- Real-time update pipeline
- SQL-based querying and filtering
- Monitoring support for detector health and data quality
- Automated synchronization with experimental data flow
- Lightweight and extensible architecture

---

## Database Architecture

The system is built around a normalized relational schema consisting of:

- Run metadata tables
- Detector status tables
- Trigger/event logging tables
- Calibration information tables
- Monitoring and operational state records

The database was designed to support:

- Fast querying
- Historical traceability
- Data consistency
- Automated updates
- Operational monitoring workflows

---

## Data Pipeline

The pipeline performs the following tasks:

1. Parse raw detector run logs
2. Extract operational metadata
3. Validate and normalize records
4. Insert/update SQL tables
5. Generate monitoring summaries
6. Synchronize with downstream analysis workflows

The framework supports continuous automated updates during detector operation.

---

## Tech Stack

### Languages
- Python
- SQL
- Bash

### Tools & Infrastructure
- Linux
- Git
- Relational database systems
- Automated shell workflows

---

## Example Applications

- Detector operation tracking
- Run-quality validation
- Experiment monitoring
- Data bookkeeping
- Automated report generation
- Experimental debugging support

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yvpan/ARARunLogDataBase.git
cd ARARunLogDataBase
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure database credentials and environment variables before running the pipeline.

---

## Usage

Run the ingestion pipeline:

```bash
python main.py
```

Example SQL query:

```sql
SELECT *
FROM run_log
WHERE station_id = 2
AND run_status = 'GOOD';
```

---

## Research Context

This work was developed as part of the Askaryan Radio Array (ARA) collaboration during PhD research at the University of Delaware.

The project supported operational monitoring and data management for ultra-high-energy neutrino detection research conducted in Antarctica.

---

## Future Improvements

Potential future extensions include:

- Web-based monitoring dashboard
- Distributed database support
- Streaming log ingestion
- Visualization tools
- Automated anomaly detection
- Cloud deployment support
