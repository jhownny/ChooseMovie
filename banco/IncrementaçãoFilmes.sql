--inserção do conteúdo da tabela--
insert into cinema values

(default,'1960', 'The Great Escape'),
(default,'1960', 'What Ever Happened to Baby Jane?'),
(default,'1960', 'For a Few Dollars More'),
(default,'1960', 'Night of the Living Dead'),
(default,'1960', 'Psycho'),
(default,'1960', 'Harakiri'),
(default,'1960', 'The Good, the Bad and the Ugly'),
(default,'1960', 'Eyes Without a Face'),

(default,'1970', 'Alien'),
(default,'1970', 'Blazing Saddles'),
(default,'1970', 'Taxi Driver'),
(default,'1970', 'The Godfather'),
(default,'1970', 'Stalker'),
(default,'1970', 'Jaws'),
(default,'1970', 'The Exorcist'),
(default,'1970', 'A Clockwork Orange'),

(default,'1980', 'Beetlejuice'),
(default,'1980', 'An American Werewolf in London'),
(default,'1980', 'The Thing'),
(default,'1980', 'Scarface'),
(default,'1980', 'The Color Purple'),
(default,'1980', 'The Shining'),
(default,'1980', 'Apocalypse Now'),
(default,'1980', 'Once Upon a Time in America'),

(default,'1990', 'Malcolm X'),
(default,'1990', 'Se7en'),
(default,'1990', 'Heat'),
(default,'1990', 'The Devils Advocate'),
(default,'1990', 'Perfect Blue'),
(default,'1990', 'Misery'),
(default,'1990', 'Schindlers List'),
(default,'1990', 'GoodFellas'),

(default,'2000', 'Office Space'),
(default,'2000', 'No Country for Old Men'),
(default,'2000', 'Watchmen'),
(default,'2000', 'Who Am I'),
(default,'2000', 'The Conjuring'),
(default,'2000', 'Into the Wild'),
(default,'2000', 'The Imitation Game'),
(default,'2000', 'Get Out');

/*seleção da tabela cinema para visualização*/
select * from cinema;

/*Funções de delete*/
delete from cinema where id = '44';
delete from  cinema where id > 40;