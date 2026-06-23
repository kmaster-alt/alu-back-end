# API Data Extraction Project

## Description

This project uses a REST API to fetch employee TODO list data and display their progress.

It retrieves:

* Employee name
* Total number of tasks
* Number of completed tasks
* Titles of completed tasks

## Requirements

* Python 3
* `requests` module
* Ubuntu 14.04 LTS compatible
* PEP8 style compliance

## File Structure

```
alu-back-end/
└── api/
    └── 0-gather_data_from_an_API.py
```

## Usage

Run the script with an employee ID:

```bash
python3 0-gather_data_from_an_API.py 2
```

## Example Output

```
Employee Ervin Howell is done with tasks(8/20):
    task title 1
    task title 2
```

## Author

Student project – ALU Backend API Task
