DROP FUNCTION IF EXISTS search_contact(TEXT);
DROP FUNCTION IF EXISTS get_contacts(INT,INT);

CREATE FUNCTION search_contact(word TEXT)
RETURNS TABLE(username VARCHAR, phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT p.username, p.phone
    FROM phonebook p
    WHERE p.username ILIKE '%'||word||'%'
       OR p.phone ILIKE '%'||word||'%';
END;
$$;

CREATE FUNCTION get_contacts(limit_num INT, offset_num INT)
RETURNS TABLE(username VARCHAR, phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT p.username, p.phone
    FROM phonebook p
    LIMIT limit_num
    OFFSET offset_num;
END;
$$;
