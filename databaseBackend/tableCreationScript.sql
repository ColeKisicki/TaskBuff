CREATE TYPE rating AS ENUM ('low', 'medium', 'high');


CREATE TABLE usersDimension (
    users_Id SERIAL NOT NULL PRIMARY KEY,
    users_FirstName VARCHAR(100) NOT NULL,
    users_LastName VARCHAR(100) NOT NULL,
    users_Email VARCHAR(100) NOT NULL,
    users_Username VARCHAR(100) NOT NULL,
    users_HashedPass VARCHAR(100) NOT NULL
);

CREATE TABLE tasksDimension (
    tasks_ID SERIAL NOT NULL PRIMARY KEY,
    tasks_Title VARCHAR(50000) NOT NULL,
    tasks_Notes VARCHAR(50000),
    tasks_Priority rating NOT NULL,
    tasks_DueDate  TIMESTAMP NOT NULL,
    tasks_IsComplete BOOLEAN DEFAULT FALSE NOT NULL,
    tasks_CompletedDate TIMESTAMP,
    tasks_Difficulty rating
);

CREATE TABLE userTasksDimension (
    userTasks_UsersID INTEGER NOT NULL REFERENCES usersDimension (users_ID),
    userTasks_TaskID INTEGER NOT NULL REFERENCES tasksDimension (tasks_ID),
    userTasks_IsOwner BOOLEAN NOT NULL,
    userTasks_IsCreator BOOLEAN NOT NULL,
    PRIMARY KEY (userTasks_UsersID, userTasks_TaskID)
);
