-- vacansies -> often skills array string + name vacansies + id 
CREATE TABLE vacansies (
	id PRIMARY KEY,
	-- Информация о вакансии
	name varchar(50) NOT null,
	description text NOT NULL unique,
	area_name VARCHAR(50),
    employer_name VARCHAR(50),
    published_at TIMESTAMP NOT null,
    -- ЗП
	salary_from INTEGER,
    salary_to INTEGER,
    salary_currency VARCHAR(3),  
    -- Навыки
    skills text[]
    -- Метаданные
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_vacansies_skills ON vacansies USING gin(skills);