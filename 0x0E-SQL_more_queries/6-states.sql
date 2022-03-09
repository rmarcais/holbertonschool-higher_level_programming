-- This script creates the database hbtn_0d_usa and the table states.
-- Create the database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Using hbtn_0d_usa.
USE hbtn_0d_usa;
-- Creates the table.
CREATE TABLE IF NOT EXISTS states (
       id INT AUTO_INCREMENT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id)
);
