# HTWG Grade Calculator - Test Files

This directory contains test data files for Phase 8 implementation:

## Test Files

### `test_grading_data.txt`
- **Format**: Tab-separated values
- **Students**: 10 dummy students (IDs: 12345, 67890, 13579, 24680, 11111, 22222, 33333, 44444, 55555, 66666)
- **Tasks**: 4 tasks, each with max 5 points
- **Scoring**: Only full points and half points (0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)
- **Usage**: Upload this file to test tab-separated file import functionality

### `test_student_ids.txt`
- **Format**: One student ID per line
- **Content**: 
  - Some student IDs from the grading file: 67890, 13579, 44444, 12345, 55555
  - Some additional IDs NOT in grading file: 99999, 77777, 88888
- **Order**: Different from the grading file order
- **Usage**: Copy the content and paste into the Student IDs textarea to test the filtering and missing student functionality

## Testing Workflow

1. **Upload the grading file**: Use `test_grading_data.txt` 
2. **Test grading**: Verify that points are calculated correctly with the slider thresholds
3. **Test ID matching**: Copy content from `test_student_ids.txt` and paste into the Student IDs field
4. **Verify filtering**: 
   - Students 67890, 13579, 44444, 12345, 55555 should show grades
   - Students 99999, 77777, 88888 should show "not found" (striped rows)
   - Order should match the pasted ID list

This tests both the new tab-separated file support and the robustness of the ID matching system.
