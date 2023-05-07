-- 创建员工表
CREATE TABLE IF NOT EXISTS `employee` (
  `emp_id` INT(10) NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `gender` ENUM('Male', 'Female') NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  `contact` VARCHAR(50) NOT NULL,
  `hometown` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- 创建菜品表
CREATE TABLE IF NOT EXISTS `dish` (
  `dish_id` INT(10) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `price` DECIMAL(10,2) NOT NULL,
  `quantity` INT(10) NOT NULL,
  `spiciness` ENUM('No', 'Mild', 'Moderate', 'Hot', 'Very hot') NOT NULL,
  `is_recommend` BOOLEAN NOT NULL,
  `created_time` DATETIME NOT NULL,
  `cost` DECIMAL(10,2) NOT NULL,
  `emp_id` INT(10) NOT NULL,
  PRIMARY KEY (`dish_id`),
  FOREIGN KEY (`emp_id`) REFERENCES `employee` (`emp_id`)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 创建客户表
CREATE TABLE IF NOT EXISTS `customer` (
  `cust_id` INT(10) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `contact` VARCHAR(50) NOT NULL,
  `gender` ENUM('Male', 'Female') NOT NULL,
  `id_card` VARCHAR(50) NOT NULL,
  `ethnicity` VARCHAR(50) NOT NULL,
  `hometown` VARCHAR(50) NOT NULL,
  `username` VARCHAR(50) NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`cust_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 创建订单表
CREATE TABLE IF NOT EXISTS `order` (
  `order_id` INT(10) NOT NULL AUTO_INCREMENT,
  `cust_id` INT(10) NOT NULL,
  `dish_id` INT(10) NOT NULL,
  `order_time` DATETIME NOT NULL,
  `quantity` INT(10) NOT NULL,
  PRIMARY KEY (`order_id`),
  FOREIGN KEY (`cust_id`) REFERENCES `customer` (`cust_id`)
    ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`dish_id`) REFERENCES `dish` (`dish_id`)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 创建原材料表
CREATE TABLE IF NOT EXISTS `material` (
  `material_id` INT(10) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `quantity` INT(10) NOT NULL,
  `category` VARCHAR(50) NOT NULL,
  `storage_location` VARCHAR(50) NOT NULL,
  `dish_id` INT(10) NOT NULL,
  PRIMARY KEY (`material_id`),
  FOREIGN KEY (`dish_id`) REFERENCES `dish` (`dish_id`)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
