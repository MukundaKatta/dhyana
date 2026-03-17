# Dhyana

AI-powered meditation guide with session management, guided meditations, and progress tracking.

## Features

- **Guided Meditations**: 20+ scripted meditation sessions across multiple styles
- **Technique Library**: 15+ meditation techniques including Vipassana, Zazen, Yoga Nidra, and more
- **Session Tracking**: Log duration, technique, and mood for every meditation session
- **Progress Tracking**: Streaks, total time, consistency scores, and milestone badges
- **Meditation Timer**: Configurable timer with bell intervals and ambient descriptions

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Start a guided meditation
dhyana meditate

# Browse techniques
dhyana techniques

# Start a timed meditation
dhyana timer --duration 20

# View session history
dhyana history

# View your stats and progress
dhyana stats
```

## Dependencies

- **pydantic**: Data validation and models
- **click**: Command-line interface
- **rich**: Beautiful terminal output

## Author

Mukunda Katta
