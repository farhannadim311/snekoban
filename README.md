# Snekoban Solver

A Python implementation of the classic Snekoban game (a variant of Sokoban), featuring a game engine and an automated solver using Breadth-First Search (BFS).

## Overview

This project simulates the Snekoban puzzle game where a player pushes "computers" onto "target" locations within a grid-based maze. The challenge is to find the shortest sequence of moves to solve a given level.

### Key Components

- **Game Logic**: Functions to represent the game state (`make_new_game`), handle player movement (`step_game`), and check for victory (`victory_check`).
- **Solver**: An `solve_puzzle` function that uses BFS to find the optimal solution path.
- **State Representation**: Efficiently tracks game states using hashable tuples to avoid revisiting states during the search.

## Usage

The main logic resides in `lab.py`. To run the solver on a sample level:

```python
python3 lab.py
```

This will initialize a predefined level, attempt to solve it, and print the sequence of moves required.

## Implementation Details

- **Pathfinding**: Utilizes BFS to guarantee the shortest solution sequence.
- **State Management**: Uses a set of visited states (hashed via `generate_hashable`) to prune the search space and prevent infinite loops.

## Course Context

Developed for 6.1010 (Fundamentals of Programming).
