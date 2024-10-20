-- Get full description of the 'books' table from the 'alx_book_store' database
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, EXTRA
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' 
AND TABLE_NAME = 'books';
