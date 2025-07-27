import pandas as pd

def generate_linear_interpolation_test_data():
    """
    Generate test data where student ID = total points scored
    Range: 1 to 100 in increments of 1 point
    This creates 100 students for linear interpolation testing
    """
    
    # Generate point values from 1 to 100 in increments of 1
    point_values = list(range(1, 101))
    
    print(f"Generating {len(point_values)} students with points from {point_values[0]} to {point_values[-1]}")
    
    # Create student data
    students = []
    for points in point_values:
        # Student ID = total points
        student_id = points  # 1 -> 1, 2 -> 2, etc.
        
        # Distribute points across 4 tasks
        # Task 1: 40% of total points
        # Task 2: 30% of total points  
        # Task 3: 20% of total points
        # Task 4: 10% of total points
        task1 = round(points * 0.40, 2)
        task2 = round(points * 0.30, 2)
        task3 = round(points * 0.20, 2)
        task4 = round(points * 0.10, 2)
        
        # Adjust task4 to ensure exact total (handle rounding errors)
        actual_total = task1 + task2 + task3 + task4
        if actual_total != points:
            task4 = round(task4 + (points - actual_total), 2)
        
        students.append({
            'mtknr': student_id,
            'Task1': task1,
            'Task2': task2, 
            'Task3': task3,
            'Task4': task4
        })
    
    # Create DataFrame
    df = pd.DataFrame(students)
    
    # Verify totals
    df['total_check'] = df['Task1'] + df['Task2'] + df['Task3'] + df['Task4']
    df['expected_total'] = df['mtknr']
    df['difference'] = abs(df['total_check'] - df['expected_total'])
    
    print(f"Max difference between expected and actual totals: {df['difference'].max()}")
    print(f"Students with perfect totals: {len(df[df['difference'] < 0.001])}/{len(df)}")
    
    # Remove check columns for final output
    df_final = df[['mtknr', 'Task1', 'Task2', 'Task3', 'Task4']].copy()
    
    return df_final

def save_test_files():
    """Generate and save test files in multiple formats"""
    
    df = generate_linear_interpolation_test_data()
    
    # Save as tab-separated file (primary format)
    tsv_file = 'linear_interpolation_test.tsv'
    df.to_csv(tsv_file, sep='\t', index=False)
    print(f"✅ Saved TSV file: {tsv_file}")
    
    # Save as Excel file (alternative format)
    xlsx_file = 'linear_interpolation_test.xlsx'
    df.to_excel(xlsx_file, index=False)
    print(f"✅ Saved Excel file: {xlsx_file}")
    
    # Create sample student ID file for testing (every 10th student)
    sample_ids = df[df['mtknr'] % 10 == 0]['mtknr'].tolist()  # 10, 20, 30, etc.
    sample_ids.extend([1, 5, 15, 25, 99])  # Add some irregular ones
    
    ids_file = 'linear_test_student_ids.txt'
    with open(ids_file, 'w') as f:
        for student_id in sorted(sample_ids):
            f.write(f"{student_id}\n")
    
    print(f"✅ Saved sample student IDs: {ids_file}")
    print(f"   Sample contains {len(sample_ids)} student IDs")
    
    # Print some statistics
    print(f"\n📊 Dataset Statistics:")
    print(f"   Total students: {len(df)}")
    print(f"   Point range: {df['mtknr'].min()} - {df['mtknr'].max()}")
    print(f"   Student ID range: {df['mtknr'].min()} - {df['mtknr'].max()}")
    print(f"   Sample data preview:")
    print(df.head(10).to_string(index=False))

if __name__ == "__main__":
    save_test_files()
