# HTWG Grade Calculator - Phase 4 (ID Matching & Clipboard Workflow)

## Overview

This is the Phase 4 implementation of the HTWG Grade Calculator, adding the university submission workflow with student ID matching and clipboard integration for seamless grade transfer to official university Excel files.

## Features Implemented (Phase 4)

### Phase 1-3 Features ✅
- ✅ **F1 - File upload**: Accept `.xlsx` grading files with `mtknr` in column A and numeric task scores
- ✅ **F2 - Point aggregation**: Sum all task score columns to create `pkt` column
- ✅ **F3 - Linear interpolation**: Calculate raw note (1.0-6.0) using P1 and P4 thresholds
- ✅ **F4 - Discrete grade mapping**: Apply HTWG grade mapping to convert raw notes to final grades
- ✅ **F5 - Live sliders**: Interactive sliders for P1 and P4 thresholds with real-time recalculation
- ✅ **F6 - ECDF chart**: Empirical Cumulative Distribution Function of student points
- ✅ **F7 - Histogram**: Grade frequency distribution with pass/fail color coding
- ✅ **F8 - Summary panel**: Live-updating statistics showing average grade and pass rate
- ✅ **Grading table display**: Show original data plus computed columns (`pkt`, `raw_note`, `grade`)
- ✅ **Visual feedback**: Interactive charts that update with threshold changes

### Phase 4 Features ✅
- ✅ **F9 - Student ID matching**: Process pasted student IDs from university Excel files
- ✅ **F10 - Clipboard workflow**: Copy aligned grades to clipboard for easy pasting into official forms
- ✅ **Grade alignment table**: Visual confirmation of ID matching with clear missing student indicators
- ✅ **University submission workflow**: Complete end-to-end process for official grade submission

## How to Use

### 1. Open the Calculator
- Open `index.html` in a web browser
- Works offline (no server required)

### 2. Upload Your Excel File
Your Excel file must have:
- Column A: `mtknr` (student IDs)
- Remaining columns: Numeric task scores

### 3. Adjust Grading Thresholds (Optional)
After uploading data, you can:
- **Adjust P1 slider**: Set the point threshold for grade 1.0 (default: 20 points)
- **Adjust P4 slider**: Set the point threshold for grade 4.0 (default: 10 points)
- **Live updates**: Grades recalculate automatically as you move the sliders
- **Visual feedback**: Charts update in real-time to show distribution changes

### 4. Monitor Statistics and Charts
The interface provides:
- **Summary panel**: Average grade and pass rate (updated live)
- **ECDF chart**: Distribution of student points with threshold markers
- **Histogram**: Grade frequency distribution with pass/fail color coding

### 5. University Submission Workflow (NEW)

#### Step 1: Get Official Student ID List
- Open your official university Excel file
- Copy the student ID column (usually `mtknr` or similar)
- The order matters - this will determine the final grade order

#### Step 2: Process Student IDs
- Scroll to the "University Submission Workflow" section
- Paste the student IDs into the textarea (one per line)
- Click **"Process ID Order"**

#### Step 3: Review Grade Alignment
- The "Grade Alignment (University Excel Order)" table appears
- Shows the exact order from your university Excel
- Missing students are clearly marked with stripes and "not found"
- Grades are displayed in the correct order for your official submission

#### Step 4: Copy Grades to Clipboard
- Click **"Copy Grades to Clipboard"** in the Grade Alignment section
- Grades are copied in the exact order of your university Excel
- Missing students result in empty lines (as expected)
- Paste directly into your official university Excel file

## Technical Implementation

### ID Matching Algorithm
- Parses pasted student IDs (whitespace-tolerant)
- Matches each ID against the grading data
- Preserves the exact order from the university Excel
- Handles missing students gracefully (empty grade entries)

### Clipboard Integration
- Uses modern `navigator.clipboard.writeText()` API
- Automatic fallback to `document.execCommand()` for older browsers
- Creates newline-separated grade list ready for Excel pasting
- Handles missing students with empty lines

### Visual Feedback
- **Found students**: Normal table rows with computed grades
- **Missing students**: Striped background with "not found" indicator
- **Real-time validation**: Immediate feedback on ID processing
- **Clear messaging**: Success/error messages with match statistics

## Sample Workflow

```
1. Upload grading Excel → Table appears with 50 students
2. Adjust P1=25, P4=12 → Grades recalculate, charts update
3. Copy 52 student IDs from university Excel → Paste in textarea
4. Click "Process ID Order" → Alignment table shows 50 matches, 2 missing
5. Click "Copy Grades" → 52 lines copied (50 grades + 2 empty lines)
6. Paste into university Excel → Perfect alignment with official format
```

## File Structure

```
grader/
├── index.html              # Complete Phase 4 implementation
├── Matrikel_Punkte.xlsx    # Sample data file
├── README.md               # Main project documentation
├── README-Phase1.md        # Phase 1 documentation
├── README-Phase2.md        # Phase 2 documentation
├── README-Phase3.md        # Phase 3 documentation
├── README-Phase4.md        # This file
└── requirements.md         # Complete requirements specification
```

## Browser Compatibility

- ✅ Chrome 80+
- ✅ Firefox 80+
- ✅ Safari 14+
- ✅ Edge 80+
- ✅ Works offline
- ✅ No server dependencies

## Next Steps (Phase 5+)

Potential enhancements for future phases:
- Input validation (duplicate IDs, invalid thresholds)
- Persistent settings in localStorage
- PDF report generation
- Dark mode toggle
- Advanced export options

## Validation

The Phase 4 implementation successfully addresses:
- ✅ **F9**: Student ID pasting and table reordering with missing student handling
- ✅ **F10**: Single-click clipboard copying of aligned grades
- ✅ **University workflow**: Complete end-to-end submission process
- ✅ **Error handling**: Robust validation and clear user feedback
- ✅ **Accessibility**: Clear visual indicators for missing data
