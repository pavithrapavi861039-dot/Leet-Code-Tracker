# Last updated: 7/25/2026, 10:04:42 AM
return stadium[stadium['island_cnt'] >= 3][['id', 'visit_date', 'people']].sort_values(by='visit_date')