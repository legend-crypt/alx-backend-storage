DELIMITER $$
CREATE TRIGGER IF NOT EXISTS after_order_insertion 
AFTER INSERT ON orders FOR EACH ROW
BEGIN 
     UPDATE items
     SET quantity = quantity - NEW.number
     WHERE name = NEW.item_name;
END $$
DELIMITER ;