CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email varchar NOT NULL UNIQUE,
    password_hash varchar NOT NULL,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp DEFAULT CURRENT_TIMESTAMP

);

CREATE FUNCTION update_users_timestamps()
RETURNS TRIGGER
AS $$
BEGIN 
NEW.updated_at= CURRENT_TIMESTAMP;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER user_updated_at
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_users_timestamps();



