[Live Demo](https://displacement-dashboard.onrender.com/) · [GitHub Repo](https://github.com/ArjunChikka/Displacement-in-Yugoslav-Wars-Mapping)

# Displacement Dashboard: Yugoslav Conflicts (1991–1999)

An interactive web dashboard built with Dash and Plotly that visualizes refugee and displacement data from the Yugoslav Wars (1991–1999). The app includes detailed maps, pie charts of displacement destinations, expanded historical timelines, and survivor testimonies.

## Features

- **Interactive Map**: Embeds pre-generated HTML maps for each conflict period.
- **Displacement Pie Chart**: Shows breakdown of where refugees fled or were internally displaced.
- **Expanded Timelines**: Provides in-depth, chronological events for each war period.
- **Survivor Testimonies**: Shares first-hand accounts of displaced individuals.
- **Responsive Layout**: Built with Dash Bootstrap Components for a fluid, mobile-friendly UI.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/yugoslavia-displacement-dashboard.git
   cd yugoslavia-displacement-dashboard
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *Dependencies include: dash, dash-bootstrap-components, pandas, plotly*

3. Place the `maps/` directory and the CSV data file (`Yugoslav War Data.csv`) in the project root.

## Usage

Run the app locally:
```bash
python app.py
```
Then open your browser at `http://127.0.0.1:8050/`.

## Project Structure

```
Displacement-in-Yugoslav-Wars-Mapping/
│
├── app.py                         # Main Dash application
├── MapGeneration.ipynb            # Notebook for preprocessing & map generation
├── maps/                          # Pre-generated HTML maps
│   ├── displacement_map_1991_1992.html
│   ├── displacement_map_1992_1995.html
│   └── displacement_map_1998_1999.html
├── Yugoslav War Data.csv          # CSV of refugee/displacement flows
├── requirements.txt               # Python dependencies
└── README.md                      # This file

```

- **app.py**: Main Dash application code.
- **maps/**: Pre-generated Folium/Mapbox HTML files for each period.
- **Yugoslav War Data.csv**: Tabular dataset of refugee flows.
- **requirements.txt**: Python library dependencies.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for bug fixes, enhancements, or data updates.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
