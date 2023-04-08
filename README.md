# Energy-modelling

This python project models the generation photovoltaic system (PV) with the consumption of a household.
The goal is to compare the two electricity behaviours and see where they overlap. In the future, an electric vehicle (EV) as a surplus storage of the PV systems will be integrated.

## Running the Model
When executing the main, two diagramms are created. The first one shows the electricity behaviour of a household and the PV systems.
The second diagramm depicts the availability (value 1) of two electric vehicles over the course of two weeks. One car models a 5 day working week, the other a 4 day working week. This is part of the (to be implemented) EV model.

## The Data 
The Data used in the scope of this project was obtained from a university course.
- PV_Einspeiseprofil: describes the electricity generation from the PV, sampled 4 times an hour over one year)
- LeistungHaushalte: describes the electricity demand from 30 different housholds
- 

## Notes
The source file contains two commented functions. They will also be used for future implementation of the EV scenario.

# License
Copyright 2023 Maja Heim

 [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
