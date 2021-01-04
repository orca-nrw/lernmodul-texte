BEGIN TRANSACTION;
DROP TABLE IF EXISTS "TaskReview";
CREATE TABLE IF NOT EXISTS "TaskReview" (
	"taskID" INTEGER NOT NULL UNIQUE,
	"taskType" TEXT NOT NULL,
	"tipp" TEXT,
	"solutionForReview" TEXT NOT NULL,
	"additionalInformation" TEXT NOT NULL
);

INSERT INTO "TaskReview" VALUES (1, 'SC', 'Tipp','Richtig','Richtig, Falsch');
INSERT INTO "TaskReview" VALUES (2, 'SC', 'Tipp','Richtig','Richtig, Falsch');
INSERT INTO "TaskReview" VALUES (3, 'SC', 'Tipp','Richtig','Richtig, Falsch');

COMMIT;