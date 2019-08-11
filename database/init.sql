CREATE TABLE bill (
  id       SERIAL PRIMARY KEY,
  value     INTEGER NOT NULL,
  quantity    INTEGER  NOT NULL
);

CREATE TABLE transaction (
  id       SERIAL PRIMARY KEY,
  time     TIMESTAMP NOT NULL,
  success_status  VARCHAR NOT NULL,
  amount INTEGER NOT NULL
);

-- bills
INSERT INTO bill(value, quantity)
VALUES (20000, 150);

INSERT INTO bill(value, quantity)
VALUES (10000, 150);

INSERT INTO bill(value, quantity)
VALUES (5000, 150);

INSERT INTO bill(value, quantity)
VALUES (2000, 150);


-- transactions
INSERT INTO transaction(time, success_status, amount)
VALUES ('2015-04-03 11:30:22', 'Success', 100);

INSERT INTO transaction(time, success_status, amount)
VALUES ('2015-04-03 13:30:22', 'Success', 20000);

INSERT INTO transaction(time, success_status, amount)
VALUES ('2015-04-03 15:30:22', 'Failure', 11000);

INSERT INTO transaction(time, success_status, amount)
VALUES ('2015-04-04 8:30:22', 'Success', 100);

INSERT INTO transaction(time, success_status, amount)
VALUES ('2015-04-04 10:30:22', 'Success', 5000);

INSERT INTO transaction(time, success_status, amount)
VALUES ('2015-05-04 09:30:22', 'Failure', 1000);

INSERT INTO transaction(time, success_status, amount)
VALUES ('2015-05-04 12:30:22', 'Success', 10000);
