CREATE TYPE rating AS ENUM ('low', 'medium', 'high');


CREATE TABLE userTasksFact (
    userTasks_UserID INTEGER NOT NULL REFERENCES usersDimension (users_ID),
    userTasks_TaskID INTEGER NOT NULL REFERENCES tasksDimension (tasks_ID),
    userTasks_IsOwner BOOLEAN NOT NULL,
    userTasks_IsCreator BOOLEAN NOT NULL,
    PRIMARY KEY (userTasks_UserID, userTasks_TaskID)
);
