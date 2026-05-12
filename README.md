# ARA Run Log Database

A relational database and automated run-monitoring framework for the **Askaryan Radio Array (ARA)** experiment at the South Pole.

This project manages detector run logs, operational metadata, and run-quality information through an automated SQLite-based ingestion pipeline and query interface.

The system was developed during research with the ARA collaboration at the University of Delaware to support real-time detector operations and downstream physics analyses.

---

## Overview

The Askaryan Radio Array (ARA) is an ultra-high-energy neutrino detector embedded in Antarctic ice.

Detector operation generates large volumes of run metadata, configuration files, calibration records, and quality annotations that must be systematically tracked for:

- Detector monitoring
- Data-quality validation
- Physics analysis selection
- Calibration bookkeeping
- Operational debugging

This repository provides an automated framework to:

- Parse ARA run logs
- Extract detector configuration metadata
- Store run information in a relational database
- Track run quality
- Query analysis-ready runs
- Automate database updates

---

## Key Features

### Automated Run Metadata Extraction
The pipeline parses ARA run files to automatically extract:

- Run start/end timestamps
- Run type
- Trigger settings
- Detector configuration parameters
- Antenna settings
- Operational status
- Run comments
- Quality labels

### SQLite Relational Database
Run information is stored in a structured SQLite database for:

- Fast querying
- Historical traceability
- Analysis reproducibility
- Consistent run bookkeeping

### Analysis-Oriented Query Interface
The repository includes accessor functions for:

- Selecting good runs
- Filtering by run quality
- Detector/station-level querying
- Analysis-specific run selection

### Real-Time Update Workflow
Database updates can be automated during detector operation using shell scripts and ingestion utilities.

---

## Repository Structure

```text
ARARunLogDataBase/
│
├── database/
│   ├── runDataBase2018.sqlite
│   ├── runDataBase2018.txt
│   └── runDataBaseEmpty.sqlite
│
├── logs/
│   ├── a1_log.txt
│   ├── a2_log.txt
│   ├── a3_log.txt
│   ├── a4_log.txt
│   └── a5_log.txt
│
├── access_functions/
│   ├── access_tools.py
│   ├── example1.py
│   ├── example2.py
│   └── README.md
│
├── runDataBaseSqlite.py
├── runDataBaseText.py
├── pushDataBaseSqlite.py
├── pushDataBaseSqlite.sh
├── runDataBaseBackwards.sh
└── README.md
```

---

## Database Pipeline

The ingestion workflow performs:

1. Parse detector run logs
2. Read run configuration files
3. Extract detector metadata
4. Identify run start/end conditions
5. Record trigger and operational settings
6. Store structured outputs in SQLite
7. Enable downstream querying for analyses

The system automatically reads files such as:

- `runStart.runXXXXXX.dat`
- `runStop.runXXXXXX.dat`
- `configFile.runXXXXXX.dat`

and extracts operational metadata directly into the database.

---

## Recorded Metadata

The database stores fields including:

| Category | Example Information |
|----------|---------------------|
| Run Information | station number, run ID, run type |
| Timing | start/end timestamps |
| Detector Configuration | antenna settings, attenuation settings |
| Trigger Configuration | external trigger status |
| Operational Status | run start/end type |
| Data Quality | quality flags |
| Comments | automated and user comments |

This enables consistent detector bookkeeping across years of operations.

---

## Accessor Functions

The repository includes a lightweight query API in:

```python
access_functions/access_tools.py
```

which simplifies database access for analysis workflows.

### Example 1: Check Run Quality

Determine whether a run is suitable for a diffuse neutrino analysis.

```bash
python example1.py ARA04 3277
```

### Example 2: Query Runs by Quality

Find all runs with a given quality label.

```bash
python example2.py ARA04 roofpulse
```

Example quality categories include:

- `good`
- `roofpulse`
- `calibration`
- detector-specific quality flags

---

## Usage

### Populate SQLite Database

Run the ingestion script:

```bash
python runDataBaseSqlite.py \
10493 ARA01 2018 FILTERED \
/path/to/run/logs/
```

Arguments:

```text
runDataBaseSqlite.py
    [run_number]
    [station]
    [year]
    [run_type]
    [input_directory]
```

Example:

```bash
python runDataBaseSqlite.py \
10493 ARA01 2018 CALIBRATION \
/data/run_009503/logs/
```

### Push Database Updates

Automated update utilities are included:

```bash
bash pushDataBaseSqlite.sh
```

### Backward Processing

Historical runs can be processed using:

```bash
bash runDataBaseBackwards.sh
```

---

## Tech Stack

### Languages
- Python
- SQL
- Bash

### Storage
- SQLite

### Techniques
- Relational database design
- Log parsing
- Automated metadata extraction
- Experimental monitoring
- Detector operations bookkeeping

---

## Research Context

This framework was developed as part of the **Askaryan Radio Array (ARA)** collaboration during PhD research at the University of Delaware.

The database supported:

- Real-time detector monitoring
- Experiment operations
- Run-quality tracking
- Physics-analysis data selection
- Long-term detector bookkeeping

for ultra-high-energy neutrino research conducted in Antarctica.

---

## Future Improvements

Potential future extensions include:

- Web-based monitoring dashboard
- PostgreSQL migration for scalability
- REST API for querying
- Detector-status visualization
- Automated anomaly detection
- Cloud deployment support
- Run-quality classification models

---

## Citation

If you use this repository for research or analysis, please cite relevant ARA collaboration publications.

---

## License

This repository is intended for research and educational purposes.
