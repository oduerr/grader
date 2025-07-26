# HTWG Grade Calculator

[https://oduerr.github.io/grader/](https://oduerr.github.io/grader/)

<iframe src="https://video.htwg-konstanz.de/Panopto/Pages/Embed.aspx?id=c90020c7-7cbb-4800-b5fb-b326012e2d2c&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## 🚀 Quick Start

1. **Open the App**: Simply open `index.html` in any modern web browser
2. **Upload Data**: Click "Upload Grading Excel File" and select your `.xlsx` file
3. **Adjust Thresholds**: Use the sliders to fine-tune P1 and P4 thresholds
4. **Analyze Results**: View the summary statistics and interactive charts
5. **Review Grades**: Check the detailed grading table with all calculations
6. **Export Data**: Sort the student IDs as in the university excel template
7. **Copy to Clipboard**: Use the "Copy to Clipboard" button to export the final grades
 
See **[docs/README.md](docs/README.md)** for a German quick start guide.

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
You pass if the final grade is less than or equal to 4.15.

## 🛠 Technical Details

- **Single File Application**: No installation required, works offline
- **Modern Web Technologies**: HTML5, CSS3, ES6 JavaScript
- **External Libraries**: 
  - [SheetJS](https://sheetjs.com/) for Excel file processing
  - [Chart.js](https://www.chartjs.org/) for interactive visualizations
- **Responsive Design**: Mobile-friendly interface
- **No Server Required**: Runs entirely in the browser


## 🤝 Contributing

This is an educational project for HTWG. Feel free to fork and adapt for your needs.

## 📄 License

Educational use only. Use at your own risk. No warranties provided.