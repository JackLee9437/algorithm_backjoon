-- 코드를 입력하세요
SET @h = -1;
SELECT (@h := @h+1) AS 'HOUR', (
    SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @h
)
FROM ANIMAL_OUTS
WHERE @h < 23;