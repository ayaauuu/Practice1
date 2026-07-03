CREATE OR REPLACE PROCEDURE add_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN

IF EXISTS(SELECT * FROM contacts WHERE name=p_name) THEN

UPDATE contacts
SET phone=p_phone
WHERE name=p_name;

ELSE

INSERT INTO contacts(name,phone)
VALUES(p_name,p_phone);

END IF;

END;
$$;



CREATE OR REPLACE PROCEDURE delete_contact(value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN

DELETE FROM contacts
WHERE name=value
OR phone=value;

END;
$$;



CREATE OR REPLACE PROCEDURE add_many(
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

RAISE NOTICE 'Wrong phone: %', phones[i];

END IF;

END LOOP;

END;
$$;
