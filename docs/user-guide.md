# HTWG Grade Calculator - User Guide

*A step-by-step guide for instructors to calculate and submit student grades*

## Overview

The HTWG Grade Calculator helps you convert raw exam points into official HTWG grades (1.0-5.0) and prepares them for submission to the university system. The entire process happens in your browser - no installation required.

## Prerequisites

Before you start, make sure you have:
- ✅ Your grading file (Excel `.xlsx` or tab-separated `.txt/.tsv`)
- ✅ Access to the official university Excel template with student IDs
- ✅ A modern web browser (Chrome, Firefox, Safari, or Edge)

---

## Step-by-Step Workflow

### Step 1: Prepare Your Grading File

Create your grading file in Excel or as a tab-separated text file with this structure:

| mtknr | Task1 | Task2 | Task3 | Task4 | ... |
|-------|-------|-------|-------|-------|-----|
| 12345 | 8.5   | 7.2   | 9.1   | 6.8   | ... |
| 67890 | 6.8   | 8.9   | 7.5   | 8.2   | ... |
| 13579 | 9.2   | 6.5   | 8.8   | 7.9   | ... |

**Important Requirements:**
- 📋 **First column must be labeled "mtknr"** (student matriculation number)
- 📋 **Following columns**: Individual task scores (numeric values only)
- 📋 **Header row required**: Column names in the first row
- 📋 **File format**: Excel (`.xlsx`) or tab-separated text (`.txt`, `.tsv`)

### Step 2: Open the Grade Calculator

1. Open `index.html` in your web browser
2. You'll see the HTWG Grade Calculator interface

### Step 3: Upload Your Grading Data

1. Click **"Upload Grading File"**
2. Select your grading file (`.xlsx`, `.txt`, or `.tsv`)
3. The app will automatically:
   - Calculate total points for each student
   - Display the grading table with computed columns
   - Show summary statistics and charts

### Step 4: Adjust Grade Thresholds

Use the interactive sliders to set your grading thresholds:

- **P4 Threshold**: Points needed for grade 4.0 (minimum passing grade)
- **P1 Threshold**: Points needed for grade 1.0 (excellent grade)

**How to determine thresholds:**
1. Look at the **point distribution** in the charts
2. Consider the **difficulty** of your exam
3. Check the **pass rate** in the summary panel
4. Adjust sliders until you achieve desired grade distribution

**💡 Tip**: The charts update in real-time as you move the sliders, helping you visualize the impact of your threshold choices.

### Step 5: Get Student IDs from University System

1. **Download** the official Excel template from the university server
2. **Open** the Excel file
3. **Select and copy** the entire student ID column (usually column A or B)

> **Note**: The university Excel file contains the official list of enrolled students in the correct order for grade submission.

### Step 6: Process Grade Alignment

1. In the Grade Calculator, scroll down to **"University Submission Workflow"**
2. **Paste** the student IDs into the text area (one ID per line)
3. Click **"Process ID Order"**

The app will:
- ✅ Match student IDs with your grading data
- ✅ Reorder grades to match the university's ID sequence
- ✅ Mark missing students (IDs not in your grading file) with striped rows
- ✅ Display alignment statistics and checksum

### Step 7: Copy Grades for Submission

Choose your preferred copy option:

**Option A: Copy Grades Only**
- Click **"Copy Grades to Clipboard"**
- Paste directly into the university Excel template's grade column

**Option B: Copy All Data (Recommended for Records)**
- Click **"Copy All to Clipboard"**
- Saves both student IDs and grades in tab-separated format
- Keep this as a backup record of your grading

### Step 8: Verify and Submit

1. **Paste** the grades into the university Excel template
2. **Verify** the checksum using the provided Excel formula
3. **Double-check** that grades align with student IDs
4. **Submit** through the official university system

---

## Features Overview

### 📊 **Visual Feedback**
- **ECDF Chart**: Shows the distribution of student points
- **Grade Histogram**: Displays final grade frequencies with pass/fail coloring
- **Real-time Updates**: Charts refresh as you adjust thresholds

### 📈 **Summary Statistics**
- **Average Grade**: Mean of all calculated grades
- **Pass Rate**: Percentage of students with grades ≤ 4.0
- **Alignment Stats**: Statistics for the university-ordered grade list
- **Excel Checksum**: Formula for verification in university template

### 🔧 **Advanced Features**
- **Flexible File Formats**: Supports both Excel and text files
- **Smart Threshold Ranges**: Sliders automatically adapt to your data
- **Missing Student Handling**: Clearly marks students not in grading data
- **Clipboard Integration**: One-click copying for seamless workflow

---

## File Format Examples

### Excel Format (.xlsx)
```
A        B       C       D       E
mtknr    Task1   Task2   Task3   Task4
12345    8.5     7.2     9.1     6.8
67890    6.8     8.9     7.5     8.2
```

### Tab-Separated Format (.txt/.tsv)
```
mtknr	Task1	Task2	Task3	Task4
12345	8.5	7.2	9.1	6.8
67890	6.8	8.9	7.5	8.2
```

---

## Troubleshooting

### ❌ "First column must be mtknr"
- Ensure your first column header is exactly "mtknr" (lowercase)
- Check for extra spaces or special characters

### ❌ "No valid student data found"
- Verify your file has numeric values in task columns
- Check that student IDs are present in the first column

### ❌ "Please paste student IDs first"
- Make sure you've pasted the university student ID list
- Verify IDs are pasted one per line

### ❌ Grades don't match expectations
- Adjust P1/P4 thresholds using the sliders
- Check the grade distribution in the histogram
- Verify your total points calculation

---

## Best Practices

✅ **Always keep a backup** of your original grading file  
✅ **Test with sample data** before processing real grades  
✅ **Verify the checksum** in the university Excel template  
✅ **Double-check grade alignment** before submission  
✅ **Save the "Copy All" output** for your records  

---

## Support

For technical issues or questions about the grading formula, refer to:
- 📖 `requirements.md` - Detailed technical specifications
- 🧪 `test-data/` - Sample files for testing
- 💻 [GitHub Repository](https://github.com/oduerr/grader) - Source code and updates

---

*Last updated: July 2025*
