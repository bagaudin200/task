#Создаем таблицу с именами колонок и значениями
CREATE TABLE petr_table (
  a INT,
  b INT
);

#Вставляем данные в таблицу
INSERT INTO petr_table (a, b) VALUES
(1, 1),
(2, 2);

#Выбираем сумму всех чисел в строках, которые удовлетворяют всем ограничениям
SELECT SUM(a + b) AS S
FROM petr_table
WHERE a < 3 AND b > 1 AND b < 3;