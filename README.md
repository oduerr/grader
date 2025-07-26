# HTWG Grade Calculator

A modern, interactive web application for calculating and analyzing student grades according to HTWG (Hochschule Konstanz) grading standards.

## 🌟 Features

### ✅ **Phase 1: Core Grading Pipeline**
- **File Upload**: Import Excel files (.xlsx) with student data
- **Point Aggregation**: Automatic calculation of total points from task scores
- **Linear Interpolation**: Raw grade calculation using configurable P1/P4 thresholds
- **Discrete Grade Mapping**: German grade system (1.0-5.0) with precise intervals
- **Interactive Table**: View all student data with computed grades

### ✅ **Phase 2: Interactive Controls & Analytics**
- **Dynamic Sliders**: Adjust P1 (grade 1.0) and P4 (grade 4.0) thresholds in real-time
- **Smart Ranges**: Sliders automatically adapt to your data range
- **Live Updates**: Grades recalculate instantly as you adjust thresholds
- **Summary Statistics**: Mean grade and pass rate with live updates

### ✅ **Phase 3: Visual Feedback**
- **ECDF Chart**: Empirical Cumulative Distribution Function of student points
- **Grade Histogram**: Visual distribution of final grades with pass/fail coloring
- **Interactive Charts**: Charts update live with threshold changes
- **Responsive Design**: Works perfectly on desktop and mobile devices

## 🚀 Quick Start

1. **Open the App**: Simply open `index.html` in any modern web browser
2. **Upload Data**: Click "Upload Grading Excel File" and select your `.xlsx` file
3. **Adjust Thresholds**: Use the sliders to fine-tune P1 and P4 thresholds
4. **Analyze Results**: View the summary statistics and interactive charts
5. **Review Grades**: Check the detailed grading table with all calculations

## 📊 Data Format

Your Excel file should have the following structure:

| mtknr    | Task1 | Task2 | Task3 | ... |
|----------|-------|-------|-------|-----|
| 12345    | 8.5   | 7.2   | 9.1   | ... |
| 67890    | 6.8   | 8.9   | 7.5   | ... |

- **First column**: Must be named `mtknr` (student ID)
- **Following columns**: Task scores (numeric values)
- **Header row**: Required with column names

## 🎯 Grading Formula

The application uses the HTWG grading formula:

```
raw_note = 3/(P4 - P1) × points + [1 - 3×P1/(P4 - P1)]
```

Where:
- **P1**: Points required for grade 1.0 (excellent)
- **P4**: Points required for grade 4.0 (sufficient)
- **points**: Total points achieved by student

Final grades are mapped to discrete values: 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 5.0

## 🛠 Technical Details

- **Single File Application**: No installation required, works offline
- **Modern Web Technologies**: HTML5, CSS3, ES6 JavaScript
- **External Libraries**: 
  - [SheetJS](https://sheetjs.com/) for Excel file processing
  - [Chart.js](https://www.chartjs.org/) for interactive visualizations
- **Responsive Design**: Mobile-friendly interface
- **No Server Required**: Runs entirely in the browser

## 📱 Browser Compatibility

- ✅ Chrome/Chromium (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ⚠️ Internet Explorer not supported

## 🔄 Development Phases

This project was developed in iterative phases:

1. **Phase 1**: Core grading functionality
2. **Phase 2**: Interactive controls and statistics
3. **Phase 3**: Visual feedback and charts
4. **Phase 4**: (Planned) ID matching and clipboard workflow

See individual phase documentation in `README-Phase*.md` files for detailed development notes.

## 📝 Sample Data

The repository includes `Matrikel_Punkte.xlsx` as sample data for testing the application.

## 📚 Documentation

**Quick Start (German)**: 
- **[📋 Anleitung für Dozenten](docs/README.md)** - 7-Schritte Workflow für HTWG Notenberechnung
- **[📋 View on GitHub](https://github.com/oduerr/grader/blob/main/docs/README.md)** - Online readable version

**Detailed Documentation**:
- **[User Guide](docs/user-guide.md)** - Complete step-by-step instructions (English)
- **[Test Data](test-data/README.md)** - Sample files for testing

## 🤝 Contributing

This is an educational project for HTWG. Feel free to fork and adapt for your needs.

## 📄 License

Educational use only. Developed for HTWG Konstanz.

---

**Live Demo**: [Coming soon - GitHub Pages deployment planned]
