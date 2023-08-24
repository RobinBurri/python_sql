CREATE TABLE IF NOT EXISTS talents (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    yearly_salary INTEGER,
    current_status VARCHAR(20) CHECK (
        current_status IN ('employed', 'self-employed', 'unemployed')
    )
);