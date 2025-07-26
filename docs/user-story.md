# User Story: Instructor Grade Processing Workflow

## As an instructor, I want to efficiently convert exam scores to official grades and submit them to the university system.

---

## Scenario: End-of-Semester Grading

**Background**: Professor Schmidt has finished grading the final exam for "Data Structures and Algorithms". She has 45 students and needs to convert raw point scores to HTWG grades and submit them through the university's Excel-based system.

### Current Situation
- ✅ Exam papers graded with individual task scores
- ✅ Raw scores recorded in Excel spreadsheet
- ✅ University Excel template downloaded with official student ID list
- ❌ Needs to determine appropriate grade thresholds
- ❌ Must align grades with university ID order for submission

---

## User Journey

### Phase 1: Data Preparation
> *"I need to get my grading data ready for processing"*

**User Actions:**
1. Opens Excel with exam scores
2. Ensures first column is labeled "mtknr" (matriculation number)
3. Verifies all task scores are numeric
4. Saves file as `.xlsx` or exports as tab-separated `.txt`

**User Thoughts:**
- *"Let me double-check the student IDs are correct"*
- *"All my task scores look good - no missing data"*

### Phase 2: Grade Calculation Setup
> *"I want to see how my grading thresholds affect the grade distribution"*

**User Actions:**
1. Opens the HTWG Grade Calculator in browser
2. Uploads the grading file
3. Reviews the automatically calculated point totals
4. Examines the initial grade distribution charts

**User Thoughts:**
- *"The app calculated totals correctly"*
- *"I can see the point distribution - most students scored 65-85 points"*

### Phase 3: Threshold Optimization
> *"I need to set fair thresholds that reflect the exam difficulty"*

**User Actions:**
1. Moves P4 slider (minimum passing grade) while watching pass rate
2. Adjusts P1 slider (excellent grade threshold) 
3. Observes real-time changes in:
   - Grade histogram
   - Pass rate percentage
   - ECDF chart
4. Fine-tunes until satisfied with distribution

**User Thoughts:**
- *"With P4 at 45 points, I get a 78% pass rate - that seems reasonable"*
- *"P1 at 75 points gives a good spread of excellent grades"*
- *"The visual feedback helps me understand the impact"*

### Phase 4: University System Integration
> *"I need to align my grades with the official university student list"*

**User Actions:**
1. Opens university Excel template from server
2. Selects and copies the entire student ID column
3. Pastes IDs into the Grade Calculator's "Student IDs" field
4. Clicks "Process ID Order"
5. Reviews the aligned grade table

**User Outcomes:**
- ✅ Grades reordered to match university sequence
- ✅ Missing students clearly identified (striped rows)
- ✅ Alignment statistics displayed
- ✅ Excel checksum formula provided

**User Thoughts:**
- *"Great! It found 42 of my 45 students"*
- *"The 3 missing students must have dropped the course"*
- *"I can see the checksum formula to verify in Excel"*

### Phase 5: Final Submission
> *"I need to transfer the grades to the university system efficiently"*

**User Actions:**
1. Clicks "Copy Grades to Clipboard"
2. Switches to university Excel template
3. Pastes grades into the appropriate column
4. Uses provided checksum formula for verification
5. Clicks "Copy All to Clipboard" for personal records
6. Saves backup file with timestamp

**User Outcomes:**
- ✅ Grades transferred in correct order
- ✅ Checksum verified in Excel
- ✅ Personal backup created
- ✅ Ready for university submission

**User Thoughts:**
- *"Perfect! The grades aligned perfectly with the student IDs"*
- *"The checksum matches - everything looks correct"*
- *"I have my backup file for records"*

---

## Key User Benefits

### ⚡ **Efficiency**
- **Before**: Manual threshold testing, manual reordering, error-prone copying
- **After**: Interactive threshold adjustment, automatic reordering, one-click copying

### 🎯 **Accuracy**
- **Before**: Risk of misaligned student IDs, manual calculation errors
- **After**: Automated alignment, built-in verification, checksum validation

### 📊 **Transparency**
- **Before**: Unclear impact of threshold choices
- **After**: Real-time visual feedback, grade distribution insights

### 🔒 **Reliability**
- **Before**: Offline calculations, version control issues
- **After**: Browser-based tool, consistent results, backup generation

---

## Success Metrics

**Time Savings**: Reduces grading workflow from 2+ hours to 15 minutes
**Error Reduction**: Eliminates manual alignment errors
**Confidence**: Visual feedback ensures appropriate grade distributions
**Compliance**: Seamless integration with university submission process

---

## User Testimonial

*"The HTWG Grade Calculator transformed my grading workflow. What used to take me hours of manual work - calculating totals, testing different thresholds, reordering for the university system - now takes just minutes. The visual feedback helps me set fair thresholds, and I never worry about alignment errors anymore. It's become an essential tool for every exam I grade."*

**- Prof. Dr. Schmidt, Computer Science Department**

---

*This user story represents the complete instructor journey from raw exam scores to university-ready grade submission.*
