# HTWG Grade Calculator - Test Data

This directory contains test data files for testing the grade calculator functionality.

## Test Files

## `test_grading_data.txt`
- **Format**: Tab-separated values (.tsv format)
- **Students**: 10 students with simple IDs (10, 20, 30, 40, 50, 60, 70, 80, 90, 100) in random order
- **Tasks**: 4 tasks per student
- **Scoring Logic**: Each student's total points equals their ID number (student 10 = 10 total points, student 20 = 20 total points, etc.)
- **Point Distribution**: Points are distributed randomly across the 4 tasks using half-point increments
- **Usage**: Upload this file to test tab-separated file import and verify that grading calculations work correctly

### `test_student_ids.txt`
- **Format**: One student ID per line
- **Content**: A subset of existing student IDs in a different order: 10, 20, 50, 70, 80
- **Order**: Different from the grading file order to test ID reordering functionality
- **Usage**: Copy the content and paste into the Student IDs textarea to test:
  - ID matching and reordering functionality
  - Grade alignment and copying features

### Values
For P4=40 and P1=75 the and the ids they checksum should be 94.2 (displayed as 94 in the UI). The mean should be 94.2 and pass rate should be 60%.


## `linear_interpolation_test.tsv` Linear interpolation test data
Values from 1 pkt (student ID 1) to 100 pkt (student ID 100) with 1 point increments.