| no | code   | status    | polarity | index | name | type | constraint | hint | 
|----|--------|-----------|----------|-------|------|------|------------|------|
| 0  | 000000 | No Action | 0        | 0     | 0    | 0    | 0          | 0    |
| 2  | 000010 | No Action | 0        | 0     | 0    | 0    | 1          | 0    |
| 3  | 000011 | No Action | 0        | 0     | 0    | 0    | 1          | 1    |
| 6  | 000110 | No Action | 0        | 0     | 0    | 1    | 1          | 0    |
| 32 | 100000 | No Action | 1        | 0     | 0    | 0    | 0          | 0    |
| 34 | 100010 | No Action | 1        | 0     | 0    | 0    | 1          | 0    |
| 35 | 100011 | No Action | 1        | 0     | 0    | 0    | 1          | 1    |
| 39 | 100111 | Rename    | 1        | 0     | 0    | 1    | 1          | 1    |
| 43 | 101011 | Alter     | 1        | 0     | 1    | 0    | 1          | 1    |
| 47 | 101111 | Move      | 1        | 0     | 1    | 1    | 1          | 1    |
| 50 | 110010 | No Action | 1        | 1     | 0    | 0    | 1          | 0    |
| 59 | 111011 | Alter     | 1        | 1     | 1    | 0    | 1          | 1    |
|    | 111011 |           |          |       |      |      |            |      |


- ::  4 :: col_04 :: varchar(50) :: NOT NULL :: moved from line 4 to 4
+ ::  4 :: col_04 :: varchar(51) :: NOT NULL :: moved from line 4 to 4
