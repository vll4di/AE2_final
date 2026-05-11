# Disneyland Review Analyser

A terminal-based Python application for analysing Disneyland park reviews from a CSV dataset.
Built as the AE2 coursework submission for **QHO444 – Problem Solving Through Programming** (completed 6 February 2026).

## Screenshots
 
**Main Menu**
![Main menu](screenshots/menu.png)
 
**Average Rating**
![Average rating](screenshots/average.png)
 
**Pie Chart Visualisation**
![Pie chart](screenshots/pie_chart.png)
 


## Files

| File | Description |
|---|---|
| `main.py` | Entry point — runs the main program loop |
| `process.py` | Data loading and analysis functions |
| `tui.py` | Terminal user interface (menus, input, display) |
| `visual.py` | Chart and graph generation |
| `disneyland_reviews.csv` | Dataset of Disneyland park reviews |
| `summary.txt` | Exported summary output (auto-generated) |

## Features

- View all reviews for a given Disneyland park
- Count reviews by reviewer location
- Calculate average scores by year or location
- Visualise data via bar charts, pie charts, and monthly average charts
- Export a summary report to `summary.txt`

## How to Run

```bash
python main.py
```

Requires Python 3. No external dependencies beyond `matplotlib` for visualisations.

## Module

QHO444 – Problem Solving Through Programming
