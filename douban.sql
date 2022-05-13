CREATE TABLE "books" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name"	TEXT NOT NULL,
	"site"	TEXT,
	"author"	TEXT,
	"tags"	TEXT,
	"date"	TEXT,
	"comments"	TEXT,
	"rating_num"	INTEGER,
	"rating"	TEXT,
	"pic"	TEXT
);
