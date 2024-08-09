# Heatmap Visualization Tool

This project provides a simple tool for visualizing the distribution and concentration of geographical points using a heatmap. The heatmap is generated from a CSV file containing coordinates and group information. Users can interactively adjust heatmap parameters such as intensity, radius, blur, and maximum value to better analyze the data.

## Project Objective

The primary goal of this project is to offer a straightforward way to analyze and visualize the distribution and concentration of points on a map. This tool can be particularly useful for understanding geographic data distributions across different categories.

## Features

- Dynamic heatmap generation based on user-provided CSV data.
- Adjustable parameters for customizing the heatmap display:
  - Heatmap intensity
  - Point radius
  - Blur level
  - Maximum value for normalization
- Group-based filtering to visualize specific data categories.

## Access the Tool Online

You can access the heatmap visualization tool online via:

- [Heatmap Visualization Tool no GitHub Pages](https://opsteamhub.github.io/heatmap-visualizer/)
- [Heatmap Visualization Tool com CNAME oficial](https://heatmap.ops.team/)

## Getting Started

### Prerequisites

To run the project, you need:

- A web server (for example, using Python's built-in HTTP server)
- A CSV file with coordinates and group information

### Running the Project

To view the heatmap visualization, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Start a web server using Python:

```bash
python -m http.server 80
```

4. Open your web browser and go to http://localhost:80 to view the application.

### Generating Test Data

A helper script, generate_coordinates.py, is included in this repository to generate a sample CSV file for testing. You can run this script to create test data.

```bash
python3 generate_coordinates.py
```

The CSV file should have the following structure:

```
Group,Coordinates
Asia,"(13.7563,100.5018)"
Europe,"(48.8566,2.3522)"
America,"(40.7128,-74.0060)"
Europe,"(51.5074,-0.1278)"
America,"(34.0522,-118.2437)"
```

- Group: The category to which the coordinate belongs.
- Coordinates: The latitude and longitude of the point, in the format (lat, lon).

## Contributing

Feel free to submit issues, create pull requests, or fork the repository to help improve the project.

## License and Disclaimer

This project is open-source and available under [MIT License](https://opensource.org/licenses/MIT). You are free to copy, modify, and use the project as you wish. However, any responsibility for the use of the code is solely yours. Please use it at your own risk and discretion.
