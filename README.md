# HTWG Grade Calculator

[https://oduerr.github.io/grader/](https://oduerr.github.io/grader/)

🎥 [Watch the demo video on Panopto](https://video.htwg-konstanz.de/Panopto/Pages/Viewer.aspx?id=c90020c7-7cbb-4800-b5fb-b326012e2d2c) (German)

## 🚀 Quick Start

 - See **[docs/quick-reference.md](docs/quick-reference.md)** for a quick start guide.
 - See **[docs/README.md](docs/README.md)** for a German quick start guide.

## 📊 Data Format

Your Excel / tab-separated text file should have the following structure:

| mtknr    | Task1 | Task2 | Task3 | ... |
|----------|-------|-------|-------|-----|
| 12345    | 8.5   | 7.2   | 9.1   | ... |
| 67890    | 6.8   | 8.9   | 7.5   | ... |

- **First column**: Must be named `mtknr` (student ID)
- **Following columns**: Task scores (numeric values)
- **Header row**: Required with column names
- If you want to include the total points achiviable in a task use the fake student ID  `0`.

## 🎯 Grading Formula
The HTWG grading formula maps continuous scores to grades using linear interpolation. Two fixed points define the scale: the score for grade 1.0 (P1) and the score for grade 4.0 (P4). Final grades are rounded to the nearest discrete value: 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, or 5.0. Rounding is in favor of students, e.g., a 1.15 rounds to 1.0 instead of 1.3.

## 🛠 Technical Details

- **Developed with AI Assistance** This was an exercise in agent-based programming. The key was to use the [requirements file](requirements.md) to instruct the agent what to do. The programming was done using VS Code and Claude Sonnet 4.0. The requirements file was generated itself with the help of OpenAI's ChatGPT after a discussion with the agent about the requirements. See the [development documentation](development/README.md) for more details.
- **Single File Application**: No installation required, works offline. You can run it directly from the `index.html` file or use the GitHub Pages link above.
- **Browser-Based**: Runs entirely in modern web browsers w/o server communication, no data sent to any server.
- **External Libraries**:
  - [SheetJS](https://sheetjs.com/) for Excel file processing
  - [Chart.js](https://www.chartjs.org/) for interactive visualizations

## 🤝 Contributing

This is an educational project for HTWG. Feel free to fork and adapt for your needs and give feedback. 

## 📄 License

Use at your own risk. No warranties provided.