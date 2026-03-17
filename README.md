# Cavorion Navigation Prototype

This project explores the foundations of autonomous navigation systems as part of Cavorion.

## Progression

### v0 — Linear Motion
Basic position + velocity simulation.

### v1 — Orientation (Dial)
Introduced directional control and turning.

### v2 — Target Seeking
Navigation toward a single objective.

### v3 — Waypoints
Sequential mission-based navigation.

### v4 — Obstacle Avoidance
Reactive avoidance using repulsive forces.

### v5 — Changing Environment
Dynamic obstacles with continuous decision-making.

![v5](outputs/figure_5.png)

## Architecture

- **Observer**: Position, targets, environment
- **Dial**: Current orientation
- **Door**: Decision layer combining goals + constraints

## Run locally

```bash
pip install -r requirements.txt
python nav_sim.py
