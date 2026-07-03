CREATE OR REPLACE FUNCTION search_contact(word TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM contacts c
    WHERE c.name ILIKE '%' || word || '%'
       OR c.phone ILIKE '%' || word || '%';
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts(limit_num INT, offset_num INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM contacts c
    LIMIT limit_num
    OFFSET offset_num;
END;
$$
LANGUAGE plpgsql;
