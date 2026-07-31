# Last updated: 7/31/2026, 9:06:25 AM
merged.rename(
    columns={
        'employee_id_y': 'employee_id',  # This is the actual manager's ID
    }, 
    inplace=True
)
final_output = merged[['employee_id', 'name', 'reports_count', 'average_age']]