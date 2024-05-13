# gempy-geotop-pilot

This project is a first attempt to model some of the areas the Netherlands using GemPy and
its supported packages.


## Minimal Actionable actions for 2024 (Meeting 9.5.2024)

### Resources:

- Willem 3 weeks
- Miguel - In kind
- Reinder - In kind

### Task:

1. Setting up repository - Willem
2. Main project structure - Miguel (done)
3. Pilot projects (priority):
   1. Subsection of South model - Miguel (High)
      1. Clay layer - Willem (High)
      2. Well correlation 40km 40 km 
   2. Zeeland - Reinder (Low)
   3. Internal structural (Low)
   4. Jan Diederik/Clinoform (Low)


## Data Types

- Directly supported by GemPy:

**Borehole data**
- The specific way data is provided is not supported by subsurface out of the box.
- ? Is it worth to make the effort to make it compatible with subsurface?
  - I will start by making the reader in this package and then I can decide if it is worth to move it to subsurface.

**Auxiliary data**
- Not implemented yet

**Topography**
- Not implemented yet


## Issues

- (solved) Vertical exaggeration for pyvista plot is a bit broken and orientations did not show properly.
- (solved) Pyvista volume does not show the right colors
  - The issue seems to be that pyvista is splitting the scalar field not exactly at 1.5
  - **It was just float error**
