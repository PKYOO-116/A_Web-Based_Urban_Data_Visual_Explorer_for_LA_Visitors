[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zCmYDy35)

# Neighborhood Visualization and Analysis: A Guide to Los Angeles for Travelers and Residents

## Project Overview

This project presents a multi-topic, interactive data visualization dashboard designed to assist future visitors to Los Angeles—particularly those attending the 2028 Summer Olympics—in exploring key urban trends. The system integrates four distinct public datasets to help users navigate crime patterns, hospitality availability, restaurant options, and mobility services in the city.

The goal is to deliver a user-friendly and informative web application that supports spatial and temporal analysis through effective, interactive charts and maps.

## Topics Covered

The platform visualizes data across four main categories:

1. **Crime Data**  
   Historical crime reports across neighborhoods, categorized by type, frequency, and location.

2. **Hotel Data**  
   Hotel pricing, reviews, and location-based filters to help users evaluate lodging options.

3. **Restaurant Data**  
   Ratings, categories, and review counts for restaurants across Los Angeles, highlighting food trends and hotspots.

4. **Bike Sharing Data**  
   Usage patterns and station-level availability across LA’s bike sharing infrastructure.

## Technology Stack

- **Frontend Framework:** Vue.js
- **Visualization Libraries:** Chart.js, D3.js, Plotly
- **Data Processing:** Pre-cleaned datasets (processed offline using Python and spreadsheet tools)
- **Design Tools:** Figma (UI/UX prototyping)
- **Deployment:** Static hosting / Local development using Vue CLI

## Features

- Modular dashboard with four separate visual interfaces
- Real-time interactivity with filter, zoom, and hover features
- Vue component-based architecture for reusability and scalability
- Integrated layout and visual design based on Figma wireframes
- Focused on usability for tourists and non-technical users

## Repository Structure

This repository is organized into the following structure:

### `Project_App/`

Main project directory containing the complete Vue.js application and supporting materials.

#### `public/`

Public assets directory used by the Vue application.  
 Contains all datasets and related preprocessing scripts required for the four visualization topics—Crime, Hotel, Restaurant, and Bike.  
 Data files are stored in `.json`, `.csv`, and `.geojson` formats, and were cleaned and transformed as needed prior to use.

#### `ReferencePapers/`

A collection of external research papers and reference materials that informed the direction and framing of the project.

#### `src/`

Vue.js source code directory.  
 Contains all `.vue` files, view components, and routing logic used to construct and render the application interface and data visualizations.

---

## Author

**Paul Yoo**  
M.S. in Applied Data Science  
University of Southern California, Fall 2024  
Data processing, Data Analysis, Vue.js dashboard development, visualization implementation, and UI/UX design integration, final presentation visualization.
[LinkedIn](https://www.linkedin.com/in/pkyoo) | [GitHub](https://github.com/PKYOO-116)
