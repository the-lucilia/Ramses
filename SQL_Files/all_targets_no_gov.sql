SELECT Id, Name FROM Region WHERE (DelegateVotes < 3) AND (hasPassword = 0) AND (isFrontier = 1 OR hasGovernor = 0);