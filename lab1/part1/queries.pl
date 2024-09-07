% Простые запросы к базе знаний для поиска фактов:
% Какой главный персонаж в игре "League of Legends"?
?- main_character('League of Legends', Character).
% Какой жанр у игры "Overwatch"?
?- genre('Overwatch', Genre).

% Запросы, использующие логические операторы (и, или, не) для формулирования сложных условий:
% Какие игры либо являются шутерами, либо имеют рейтинг выше 9?
?- (genre(Game, 'Shooter') ; rating(Game, Rating), Rating > 9).
% Какие игры выпущены до 2015 года и имеют рейтинг выше 8?
?- videogame(Game), release_year(Game, Year), Year < 2015, rating(Game, Rating), Rating > 8.
% Какие игры не являются шутерами?
?- videogame(Game), \+ genre(Game, 'Shooter').

% Запросы, использующие переменные для поиска объектов с определенными характеристиками: 
% Какие игры поддерживают мультиплеерный режим?
?- supports_game_mode(Game, 'Multiplayer').
% Какие игры подходят для детей младше 10 лет?
?- age(Game, Age), Age < 10.

% Запросы, которые требуют выполнения правил для получения результата:
% Какие игры считаются хорошо оцененными?
?- list_of_well_rated_games(WellRatedGames).
% Какие игры имеют рейтинг выше 8 и поддерживают мультиплеерный режим?
?- well_rated(Game), supports_game_mode(Game, 'Multiplayer').



% Запросы по всем правилам
?- well_rated(Game).
?- list_of_video_games(Games).
?- old_game(Game).
?- belongs_to_genre(Game, 'Action-Adventure').
?- supports_game_mode(Game, 'Single player').
?- list_of_well_rated_games(WellRatedGames).
