CREATE TABLE manufacturer
(
  manufacturer_id VARCHAR(3) NOT NULL,
  manufacturer_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (manufacturer_id)
);

CREATE TABLE cereal
(
  name VARCHAR(100) NOT NULL,
  type VARCHAR(3) NOT NULL,
  calories INT NOT NULL,
  cereal_id INT NOT NULL,
  protein INT NOT NULL,
  fat INT NOT NULL,
  sugar INT NOT NULL,
  manufacturer_id VARCHAR(3) NOT NULL,
  PRIMARY KEY (cereal_id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(manufacturer_id)
);

CREATE TABLE rating
(
  rating_id INT NOT NULL,
  rating_score FLOAT NOT NULL,
  date DATE NOT NULL,
  cereal_id INT NOT NULL,
  PRIMARY KEY (rating_id),
  FOREIGN KEY (cereal_id) REFERENCES cereal(cereal_id)
);