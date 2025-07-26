I'm working on the HTWG Grade Calculator, a single-page HTML+JS application for instructors to calculate and analyze student grades. The project is located at /Users/oli/Documents/GitHub/grader/

## Current Status (Phase 8 Complete)
- ✅ Core grading pipeline (Excel/TSV upload, point aggregation, grade calculation)
- ✅ Interactive P1/P4 threshold sliders with live updates
- ✅ Visual feedback (ECDF chart, grade histogram with Chart.js)
- ✅ ID matching workflow (paste student IDs, reorder grades, clipboard export)
- ✅ Summary statistics and alignment stats with Excel formulas
- ✅ Support for both Excel (.xlsx) and tab-separated (.txt, .tsv) files
- ✅ Test data organized in test-data/ directory

## Key Files
- `index.html` - Main application (single-page app)
- `requirements.md` - Complete specifications
- `test-data/` - Sample test files with documentation
- GitHub repo: https://github.com/oduerr/grader

## Test Data
- `test-data/test_grading_data.txt` - 10 students (IDs: 10,20,30...100), total points = student ID
- `test-data/test_student_ids.txt` - Subset for testing: 10,20,50,70,80,898

The app is fully functional and ready for use. Please help me continue development or troubleshooting as needed.