# Quick Reference: HTWG Grade Calculator

## 🚀 5-Minute Quick Start

### 1. Prepare Your File
- First column: **mtknr** (student IDs)
- Other columns: Task scores (numbers only)
- Save as Excel (`.xlsx`) or tab-separated text (`.txt`, `.tsv`)

### 2. Upload & Adjust
- Upload your file → App calculates totals
- Move **P4 slider** (points for grade 4.0)
- Move **P1 slider** (points for grade 1.0)
- Watch the charts and pass rate

### 3. University Workflow
- Copy student IDs from university Excel
- Paste into "Student IDs" field
- Click "Process ID Order"
- Click "Copy Grades to Clipboard"
- Paste into university Excel template

---

## 📋 File Format Template

```
mtknr   Task1   Task2   Task3   Total_Points   Grade
12345   8.5     7.2     9.1     24.8          2.3
67890   6.8     8.9     7.5     23.2          2.7
```
*(Total_Points and Grade are calculated automatically)*

---

## ⚡ Keyboard Shortcuts

- **Upload**: Click file input or drag & drop
- **Copy Grades**: Ctrl/Cmd+C after clicking copy button
- **Slider Adjustment**: Use number inputs for precise values

---

## ✅ Checklist Before Submission

- [ ] P1/P4 thresholds set appropriately
- [ ] Pass rate looks reasonable (check summary panel)
- [ ] University student IDs pasted and processed
- [ ] Grades copied to university Excel template
- [ ] Excel checksum formula verified
- [ ] Backup copy saved ("Copy All to Clipboard")

---

## 🔧 Common Issues

| Problem | Solution |
|---------|----------|
| "First column must be mtknr" | Rename first column header to exactly "mtknr" |
| No data appears | Check file format, ensure numeric task scores |
| Wrong grade distribution | Adjust P1/P4 sliders, check point ranges |
| Missing students in output | Normal - these students not in your grading file |

---

*For detailed instructions, see `docs/user-guide.md`*
