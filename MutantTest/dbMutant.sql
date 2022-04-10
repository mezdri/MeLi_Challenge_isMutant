DROP TABLE IF EXISTS mutantTests;

CREATE TABLE mutantTests (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  dna TEXT NOT NULL,
  dna_token TEXT NOT NULL unique,
  is_mutant integer not null
);