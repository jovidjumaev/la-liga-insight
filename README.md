# La Liga Insight Dashboard

This is a side project for my passion for football, and it is an interactive dashboard for analyzing La Liga football statistics and trends, powered by FBref data. It is also live at [My Side Project](https://mypersonalprojectbarca.streamlit.app/). 

## Features
- 2023 Season Analysis
- 2024 Season Live Updates
- Team Performance Metrics
- Player Statistics
- Interactive Visualizations
- Advanced Football Analytics

## Data Source
This project uses data from [FBref](https://fbref.com/), a comprehensive football statistics website. The data includes:
- Match results and schedules
- Team statistics
- Player performance metrics
- Advanced statistics like:
  - Expected Goals (xG)
  - Progressive Passes
  - Key Passes
  - Expected Assists (xA)
  - Goalkeeping metrics

## Installation
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/la-liga-insight.git
   cd la-liga-insight
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the dashboard
   ```bash
   streamlit run Home.py
   ```

2. Open your browser at `http://localhost:8501`

## Keep Alive System
To ensure the Streamlit app remains active with the new 12-hour inactivity threshold, this project includes an automated keep-alive system:

### GitHub Actions Workflow
- **Location**: `.github/workflows/keep-alive.yml`
- **Schedule**: Runs every 10 hours automatically
- **Action**: Creates an empty commit to trigger app activity
- **Manual Trigger**: Can be manually triggered from GitHub Actions tab

### Local Script (Optional)
- **File**: `keep_alive.py`
- **Usage**: `python keep_alive.py`
- **Purpose**: Manual keep-alive if needed
- **Features**: Error handling and status reporting

The keep-alive system ensures your app stays running without manual intervention.

## Dashboard Sections
1. **2023 Season Analysis**
   - Complete season statistics
   - Team performance metrics
   - Player statistics
   - Match results analysis

2. **2024 Season Updates**
   - Current season standings
   - Live match results
   - Recent performance trends
   - Upcoming fixtures

3. **About Section**
   - Project information
   - Developer details
   - Contact information

## Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn

## Data Updates
The dashboard is regularly updated with the latest data from FBref after the end of every season. The data includes:
- Match results
- Team statistics
- Player performance metrics
- Advanced analytics

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgments
- [FBref](https://fbref.com/) for providing comprehensive football statistics
- Streamlit for the amazing dashboard framework
- The football analytics community for inspiration and support
