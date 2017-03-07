CREATE TABLE `score` (
  `studentid` varchar(20) NOT NULL,
  `courseid` varchar(30) NOT NULL,
  `coursename` varchar(20) NOT NULL,
  `dailyscore` varchar(10) DEFAULT NULL,
  `examscore` varchar(10) DEFAULT NULL,
  `finalscore` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


ALTER TABLE `score`
  ADD PRIMARY KEY (`studentid`,`courseid`),
  ADD KEY `ix_score_studentid` (`studentid`),
  ADD KEY `ix_score_courseid` (`courseid`);

