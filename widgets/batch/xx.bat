@echo off
IF [%1] == [r] SET reclaim_tickets=yes
SET open_timestamp2=%open_timestamp%
CALL X