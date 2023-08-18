create database biblioteca;

use biblioteca;

create table cinema(
    id int() NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ano decimal(4) NOT NULL,
    filme varchar(85) NOT NULL 
)engine=InnoDB default charset=utf8;