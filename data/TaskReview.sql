BEGIN TRANSACTION;
DROP TABLE IF EXISTS "TaskReview";
CREATE TABLE IF NOT EXISTS "TaskReview" (
	"taskID" INTEGER NOT NULL UNIQUE,
	"taskType" TEXT NOT NULL,
	"tipp" TEXT,
	"solutionForReview" TEXT NOT NULL,
	"additionalInformation" TEXT NOT NULL
);

INSERT INTO "TaskReview" VALUES (1, 'SC', 'Tipp','10000','260000, 10000, 26');
INSERT INTO "TaskReview" VALUES (2, 'SC', 'Tipp','26','10, 100, 26');
INSERT INTO "TaskReview" VALUES (3, 'SC', 'Tipp','Ja','Ja, Nein');
INSERT INTO "TaskReview" VALUES (4, 'SC', 'Tipp','tweets.iloc[0]','tweets[0], tweets.take(1), tweets.iloc[0]');
INSERT INTO "TaskReview" VALUES (5, 'SC', 'Tipp','[^a-zA-ZäöüßÄÖU\s]','[^a-zA-ZäöüßÄÖU\s], [1-90?!#]');
INSERT INTO "TaskReview" VALUES (6, 'SC', 'Tipp','21.268','21.268, 16.235');
INSERT INTO "TaskReview" VALUES (7, 'SC', 'Tipp','die/und/ich','der/die/das, die/und/ich, die/das/oder');
INSERT INTO "TaskReview" VALUES (8, 'SC', 'Tipp','0.0','0.0, 1.0');
INSERT INTO "TaskReview" VALUES (9, 'SC', 'Tipp','1','0, 1, 2, 3');
INSERT INTO "TaskReview" VALUES (10, 'SC', 'Tipp','Alle Vier','Adjektiv, Adverb, Nomen, Verb, Alle Vier');
INSERT INTO "TaskReview" VALUES (11, 'SC', 'Tipp','Negativ','Negativ, Positiv');
INSERT INTO "TaskReview" VALUES (12, 'SC', 'Tipp','Deklination','Wort, Wert, Deklination, Stimmung, Typ');
INSERT INTO "TaskReview" VALUES (13, 'SC', 'Tipp','0.37','-0.23, 0.37, 1.0');
INSERT INTO "TaskReview" VALUES (14, 'SC', 'Tipp','Gefahr','Abbruch, Gefahr, widersprüchlich, schlecht');
INSERT INTO "TaskReview" VALUES (15, 'SC', 'Tipp','Neutral','Negativ, Neutral, Positiv');
INSERT INTO "TaskReview" VALUES (16, 'SC', 'Tipp','Positiv','Negativ, Positiv');

COMMIT;