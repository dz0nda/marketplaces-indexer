-- Create toolkit extension for hyperfunctions

-- CREATE EXTENSION timescaledb_toolkit;
-- ALTER EXTENSION timescaledb_toolkit UPDATE;

-- Make 'marketplace_activity' table an hypertable

ALTER TABLE marketplace_activity
    DROP CONSTRAINT marketplace_activity_pkey;

ALTER TABLE marketplace_activity
    ADD PRIMARY KEY (id, operation_timestamp);

SELECT create_hypertable('marketplace_activity', 'operation_timestamp');

-- Make 'marketplace_order' table an hypertable

ALTER TABLE marketplace_order
    DROP CONSTRAINT marketplace_order_pkey;

ALTER TABLE marketplace_order
    ADD PRIMARY KEY (id, created_at);

SELECT create_hypertable('marketplace_order', 'created_at');
