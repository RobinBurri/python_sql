INSERT INTO talents (full_name, yearly_salary, current_status) VALUES (%s, %s, %s) RETURNING *;