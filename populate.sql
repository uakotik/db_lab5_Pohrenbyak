INSERT INTO manufacturer(manufacturer_id,manufacturer_name )
VALUES 
  ('K', 'Kelloggs'),
  ('G', 'General Mills'),
  ('R', 'Ralston Purina'),
  ('A', 'American Home Food Products'),
  ('N', 'Nabisco'),
  ('P', 'Post'),
  ('Q', 'Quaker Oats');
INSERT INTO cereal (cereal_id, name, type, calories, protein, fat, sugar,manufacturer_id)
VALUES 
  (1, 'Corn Flakes','C',100, 2, 0, 2, 'K'),
  (2, 'Apple Jacks','C', 110, 2, 0, 14, 'K'),
  (3, 'Cocoa Puffs','C',110, 1, 1, 13,'G'),
  (4, 'Corn Chex','C',110, 2, 0, 3,'R'),
  (5, 'Wheaties Honey Gold', 'C',110, 2, 1, 8,'G'),
  (6, 'Maypo', 'H',100, 4, 1, 3,'A'),
  (7, 'Lucky Charms','C',110, 2, 1, 12,'G');
INSERT INTO rating (rating_id, rating_score,date,cereal_id)
VALUES 
  (1, 45.9,'2024-01-15',1),
  (2, 33.2,'2024-01-15',2),
  (3, 22.7,'2024-01-15',3),
  (4, 41.4,'2024-01-15',4),
  (5, 36.2,'2024-01-15',5),
  (6, 54.8,'2024-01-15',6),
  (7, 26.7,'2024-01-15',7);