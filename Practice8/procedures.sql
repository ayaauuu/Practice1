DROP PROCEDURE IF EXISTS add_contact(VARCHAR,VARCHAR);
DROP PROCEDURE IF EXISTS delete_contact(VARCHAR);
DROP PROCEDURE IF EXISTS add_many(VARCHAR[],VARCHAR[]);

CREATE PROCEDURE add_contact(
    p_username VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN

IF EXISTS(SELECT 1 FROM phonebook WHERE username=p_username) THEN

UPDATE phonebook
SET phone=p_phone
WHERE username=p_username;

ELSE

INSERT INTO phonebook(username,phone)
VALUES(p_username,p_phone);

END IF;

END;
$$;


CREATE PROCEDURE delete_contact(val VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN

DELETE FROM phonebook
WHERE username=val
OR phone=val;

END;
$$;


CREATE PROCEDURE add_many(
names VARCHAR[],
phones VARCHAR[]
)
LANGUAGE plpgsql
AS $$
DECLARE
i INT;
BEGIN

FOR i IN 1..array_length(names,1)

LOOP

IF phones[i] ~ '^[0-9]+$' THEN

CALL add_contact(names[i],phones[i]);

ELSE

RAISE NOTICE 'Wrong phone: %',phones[i];

END IF;

END LOOP;

END;
$$;
