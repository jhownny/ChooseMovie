--criação do banco--
create database biblioteca;

--seleção do banco para modificação--
use biblioteca;

--criação da tabela e seus respctivos parametros--
create table cinema(
    id int(1) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ano decimal(4) NOT NULL,
    filme varchar(85) NOT NULL 
)engine=InnoDB default charset=utf8;