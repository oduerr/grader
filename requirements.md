# HTWG Grade Calculator – Requirements (v0.3 – 2025-07-25)

## 1. Purpose & Scope

| Item             | Description                                                                                                                                                                     |
|-----------------------|-------------------------------------------------|
| **Goal**         | Provide exam graders with a browser tool to convert raw points into HTWG grade codes, visualise the distribution, and align grades with the official university Excel template. |
| **Out of scope** | Multi-sheet batch processing, authentication, server-side storage, syllabus-specific grading curves.                                                                            |

------------------------------------------------------------------------

## 2. Stakeholders

| Role                  | Interest                                        |
|-----------------------|-------------------------------------------------|
| Instructors / graders | Fast, error-free grading without local scripts. |
| Students              | Transparent, consistent grading.                |
| IT support            | Zero-install deployment (static file).          |

------------------------------------------------------------------------

## 3. Functional Requirements (updated)

1. **F1 – File upload**  
   Accept a single `.xlsx` grading file (first sheet) whose column **A** is `mtknr` (student ID) and the remaining columns are numeric task scores.

2. **F2 – Point aggregation**  
   Sum all task-score columns per row → new column **`pkt`**.

3. **F3 – Linear interpolation**  
   Compute a raw note (1.0 – 6.0) using thresholds **P1** (points → 1.0) and **P4** (points → 4.0):  
   `raw_note = 3/(P4 − P1) · pkt + [1 − 3·P1/(P4 − P1)]`.

4. **F4 – Discrete grade mapping**  
   Apply the following R-style function to `raw_note`; the result is divided by 100 to give a two-digit grade:  

   ```r
   note <- function(n) {
     if (n <= 1.15)        n <- 100
     else if (n <= 1.50)   n <- 130
     else if (n <= 1.85)   n <- 170
     else if (n <= 2.15)   n <- 200
     else if (n <= 2.50)   n <- 230
     else if (n <= 2.85)   n <- 270
     else if (n <= 3.15)   n <- 300
     else if (n <= 3.50)   n <- 330
     else if (n <= 3.85)   n <- 370
     else if (n <= 4.15)   n <- 400
     else                  n <- 500
     n / 100               # → 1.0, 1.3, …, 5.0
   }
    ```

5. **F5 – Live sliders**  
   Two range inputs for **P1** and **P4**; any change recomputes **F3** and **F4**.

6. **F6 – ECDF chart**  
   Display a stepped-line ECDF of `pkt`, updating live.

7. **F7 – Histogram**  
   Display a bar chart of the discrete `grade` frequencies, updating live.

8. **F8 – Summary panel**  
   Show mean `grade` (two decimals) and pass rate (`grade < 4.15`).

9. **F9 – Paste external student IDs**  
   Provide a textarea to paste an ordered list of student IDs from the official Excel file.  
   - Reorder the internal table to match the pasted ID list.  
   - If a pasted ID does not exist in the grading file, insert a **new blank row** (only `mtknr` filled) and **grey it out**.

10. **F10 – Copy grade column**  
    A button copies the `grade` column (aligned to pasted IDs) to the clipboard.

11. **F11 – Client-only processing**  
    All computations happen entirely in the browser; nothing is sent to any server.

> 📌 **Note:** The final grade (from F4) is stored in a new column called **`grade`**. It is computed by applying the HTWG mapping to `raw_note` and then dividing the result by 100 to produce values like 1.0, 1.3, 1.7, ..., 5.0.


------------------------------------------------------------------------

## 4. Non-Functional Requirements

| Category            | Requirement                                                                                |
|-------------------------------|----------------------------------------|
| **Technology**      | Pure HTML + vanilla JS + [SheetJS](https://sheetjs.com) + [Chart.js](https://chartjs.org). |
| **Performance**     | ≤ 1 s for 1 000 rows on a typical laptop.                                                  |
| **Browser support** | Latest Chrome, Firefox, Edge, Safari.                                                      |
| **Accessibility**   | Keyboard-accessible sliders, sufficient colour contrast, focusable table rows.             |
| **Security**        | No server communication; works offline.                                                    |
| **Deployment**      | Single `.html` file; GitHub Pages or `file://` compatible.                                 |
| **Maintainability** | All thresholds, bins and codes defined in constants at top of source.                      |

------------------------------------------------------------------------

## 5. User Interface Specification (updated)

| Area | Components |
|------|------------|
| **Header** | Title “HTWG Grade Calculator”. |
| **Control bar** | – **File input** for the grading `.xlsx`.<br>– Two **sliders** for **P1** and **P4** with live numeric labels.<br>– **Textarea** to paste the ordered list of student IDs from the university Excel.<br>– **Download** button (creates graded `.xlsx`). |
| **Summary** | Live-updating text showing **average grade** (mean of `grade` column, two decimals) and **pass rate** (`grade < 4.05`). |
| **Charts** | **Left panel:** ECDF of `pkt` (stepped line).<br>**Right panel:** Histogram of discrete **`grade`** values (bar chart). |
| **Grading table** | Displays the uploaded grading data *plus* computed columns: `pkt`, `raw_note`, `grade`.<br>Scrollable if > 30 rows. |
| **ID-Match table** | Displays the pasted ID list (original order) with corresponding **`grade`**.<br>Rows where `mtknr` is **not found** in the grading table are **greyed out** and show “not found” in `grade`. |
| **Clipboard actions** | A **“Copy grades”** button copies only the `grade` column from the ID-Match table (preserving row order) to the clipboard. |
| **Styling** | Light theme, accent colour `#0065bd`, rounded corners, responsive (flex/grid). Greyed rows use reduced opacity and a subtle cross-hatch pattern for accessibility. |                                        |

------------------------------------------------------------------------

## 6. Development Phases  (updated)

### 🟩 Phase 1 – MVP  
Core grading pipeline, no interactivity or visualisations.

- Implement **F1–F4**  
  (file upload, point aggregation, raw-note interpolation, discrete grade mapping).  
- Show the grading table with the new columns (`pkt`, `raw_note`, `grade`).  
  _No sliders, charts, or ID-matching yet._

---

### 🟨 Phase 2 – Interactivity  
Add live threshold adjustment and quick stats.

- Implement **F5**  (sliders for P1 & P4, live recompute).  
- Implement **F8**  (summary panel: mean grade & pass-rate).

---

### 🟦 Phase 3 – Visual Feedback  
Bring in exploratory plots.

- Implement **F6**  (ECDF of `pkt`).  
- Implement **F7**  (histogram of `grade`).

---

### 🟧 Phase 4 – ID matching & clipboard workflow

- Implement **F9**  (textarea for pasted student IDs, reorder table, add blank rows, grey out unmatched).  
- Implement **F10** (single “Copy grades” button that copies the aligned `grade` column).

### Phase 5 Polishing 
1. Add link in header to the GitHub repo.
2. Sliders for P1 and P4 should have 0.5 increments and it should be possible to set them manually by typing.

### Phase 6 Polishing
3. In the Grade Alignment (University Excel Order) table add mean, pass rate, pass number, and also a checksum calculated of the mean of the student id column multiplied by the grade column in excel that would be =AVERAGE(PRODUCT(F6:F20,G6:G20)) Also add the Excel code in a copy and paste fashion so that the user can copy the formula easily to the Excel sheet.

### Phase 7 Polishing
At the position copy grades to clipboard make another button saying copy all to clipboard. The idea of it would be that the final grades together with the Student ID could then be stored by the user for later reference.

### Phase 8 Polishing
**File format extension and test data:**
1. Extend file upload to accept tab-separated text files (`.txt`, `.tsv`) in addition to Excel files
2. Create test grading data file: 10 students, 4 tasks (max 5 points each), tab-separated format, using only full points and half points (0, 0.5, 1.0, 1.5, 2.0, etc.)
3. Create test student ID file: Simple text file with one ID per line, containing some (but not all) student IDs from grading file plus some additional IDs not in grading file, in different order - for testing the filtering and missing student functionality
