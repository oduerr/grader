# HTWG Grade Calculator - Phase 2 (Interactivity)

## Overview

This is the Phase 2 implementation of the HTWG Grade Calculator, adding interactive threshold adjustment and live statistics to the core grading pipeline.

## Features Implemented (Phase 2)

### Phase 1 Features ✅
- ✅ **F1 - File upload**: Accept `.xlsx` grading files with `mtknr` in column A and numeric task scores
- ✅ **F2 - Point aggregation**: Sum all task score columns to create `pkt` column
- ✅ **F3 - Linear interpolation**: Calculate raw note (1.0-6.0) using P1 and P4 thresholds
- ✅ **F4 - Discrete grade mapping**: Apply HTWG grade mapping to convert raw notes to final grades
- ✅ **Grading table display**: Show original data plus computed columns (`pkt`, `raw_note`, `grade`)

### Phase 2 Features ✅
- ✅ **F5 - Live sliders**: Interactive sliders for P1 and P4 thresholds with real-time recalculation
- ✅ **F8 - Summary panel**: Live-updating statistics showing average grade and pass rate

## How to Use

### 1. Open the Calculator
- Open `index.html` in a web browser
- Works offline (no server required)

### 2. Upload Your Excel File
Your Excel file must have:
- Column A: `mtknr` (student IDs)
- Remaining columns: Numeric task scores

### 3. Adjust Grading Thresholds
After uploading data, you can:
- **Adjust P1 slider**: Set the point threshold for grade 1.0 (default: 20 points)
- **Adjust P4 slider**: Set the point threshold for grade 4.0 (default: 10 points)
- **Live updates**: Grades recalculate automatically as you move the sliders
- **Validation**: System ensures P1 > P4 for valid linear interpolation

### 4. Monitor Statistics
The summary panel shows:
- **Average Grade**: Mean of all final grades (updated live)
- **Pass Rate**: Percentage of students with grade < 4.15 (updated live)

## New Interface Elements

### Interactive Sliders
- **P1 Threshold**: Range 10-100 points, controls the point threshold for grade 1.0
- **P4 Threshold**: Range 5-50 points, controls the point threshold for grade 4.0
- **Live numeric display**: Shows current slider values
- **Auto-validation**: Prevents invalid combinations (P1 ≤ P4)

### Summary Statistics Panel
- **Average Grade**: Calculated as mean of `grade` column, displayed with 2 decimals
- **Pass Rate**: Percentage of students with grade < 4.15, displayed with 1 decimal
- **Live updates**: Statistics recalculate instantly when thresholds change

## Grade Calculation Details

### Linear Interpolation Formula (F3)
```
raw_note = 3/(P4 − P1) · pkt + [1 − 3·P1/(P4 − P1)]
```

- **P1**: Points threshold for grade 1.0 (adjustable slider)
- **P4**: Points threshold for grade 4.0 (adjustable slider)
- **pkt**: Total points for student (sum of task scores)

### Example Calculation
With P1=20, P4=10:
- Student with 25 points: Gets grade 1.0
- Student with 15 points: Gets grade ~2.5
- Student with 5 points: Gets grade 5.0

## Technical Implementation

### Live Recalculation
- Slider changes trigger immediate grade recalculation
- Table updates without full reload
- Statistics update in real-time
- Efficient DOM updates for smooth performance

### Validation
- P1 must be greater than P4
- Sliders auto-adjust to maintain valid relationships
- Error prevention built into the interface

## Browser Compatibility
- Chrome (recommended)
- Firefox
- Edge
- Safari

## Next Phases
- **Phase 3**: ECDF and histogram charts with Chart.js
- **Phase 4**: ID matching and clipboard workflow for grade export

## Files Structure
```
grader/
├── index.html              # Main application (Phase 1 + 2)
├── requirements.md          # Full specification
├── README-Phase2.md         # This file
└── Matrikel_Punkte.xlsx    # Sample test data
```
