# HTWG Grade Calculator - Phase 1 (MVP)

## Overview

This is the Phase 1 implementation of the HTWG Grade Calculator, providing the core grading pipeline functionality.

## Features Implemented (Phase 1)

- ✅ **F1 - File upload**: Accept `.xlsx` grading files with `mtknr` in column A and numeric task scores
- ✅ **F2 - Point aggregation**: Sum all task score columns to create `pkt` column
- ✅ **F3 - Linear interpolation**: Calculate raw note (1.0-6.0) using P1 and P4 thresholds
- ✅ **F4 - Discrete grade mapping**: Apply HTWG grade mapping to convert raw notes to final grades
- ✅ **Grading table display**: Show original data plus computed columns (`pkt`, `raw_note`, `grade`)

## How to Use

### 1. Open the Calculator

- Open `index.html` in a web browser
- Works offline (no server required)

### 2. Prepare Your Excel File

Your Excel file must have:

- Column A: `mtknr` (student IDs)
- Remaining columns: Numeric task scores
- Example:

  ```text
  mtknr | Task1 | Task2 | Task3 | Task4 | Task5
  12345 |   18  |   16  |   14  |   12  |   20
  12346 |   20  |   18  |   16  |   15  |   18
  ```

### 3. Upload and Grade

- Click "Upload Grading Excel File"
- Select your `.xlsx` file
- View the results in the grading table

## Current Limitations (Phase 1)

- P1 and P4 thresholds are fixed at 80 and 40 points (will be configurable in Phase 2)
- No interactive charts or statistics (coming in Phase 2-3)
- No ID matching or clipboard functionality (coming in Phase 4)

## Grade Calculation Details

### Point Aggregation (F2)

All numeric task scores are summed: `pkt = Task1 + Task2 + ... + TaskN`

### Linear Interpolation (F3)

Raw note calculated using: `raw_note = 3/(P4 − P1) · pkt + [1 − 3·P1/(P4 − P1)]`

- P1 = 80 points → grade 1.0
- P4 = 40 points → grade 4.0

### Discrete Grade Mapping (F4)

Raw notes are mapped to HTWG grades:

- ≤ 1.15 → 1.0
- ≤ 1.50 → 1.3
- ≤ 1.85 → 1.7
- ≤ 2.15 → 2.0
- ≤ 2.50 → 2.3
- ≤ 2.85 → 2.7
- ≤ 3.15 → 3.0
- ≤ 3.50 → 3.3
- ≤ 3.85 → 3.7
- ≤ 4.15 → 4.0
- \> 4.15 → 5.0

## Testing

Test with your own Excel files that have:

- Column A: `mtknr` (student IDs)
- Remaining columns: Numeric task scores

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Edge
- Safari

## Next Phases

- **Phase 2**: Interactive sliders for P1/P4, summary statistics
- **Phase 3**: ECDF and histogram charts
- **Phase 4**: ID matching and clipboard workflow
