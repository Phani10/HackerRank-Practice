SELECT contest_id, hacker_id, name, 
    SUM(total_submissions) AS total_submissions, SUM(total_accepted_submissions) AS total_accepted_submissions,
    SUM(total_views) AS total_views, SUM(total_unique_views) AS total_unique_views
FROM (
        SELECT *, 
                CASE WHEN total_submissions + total_accepted_submissions + total_views + total_unique_views = 0 then 0
                    ELSE 1 end AS flag
        FROM (
            SELECT t1.contest_id, hacker_id, name, IFNULL(total_submissions, 0) total_submissions, IFNULL(total_accepted_submissions, 0) total_accepted_submissions, IFNULL(total_views, 0) total_views, IFNULL(total_unique_views, 0) total_unique_views
            FROM (
                SELECT c1.contest_id, hacker_id, name, c2.college_id, c3.challenge_id
                FROM contests c1
                LEFT JOIN colleges c2 ON c1.contest_id = c2.contest_id
                LEFT JOIN challenges c3 ON c2.college_id = c3.college_id) t1
                LEFT JOIN (SELECT challenge_id,SUM(total_views) AS total_views, SUM(total_unique_views) AS total_unique_views 
                            FROM view_stats
                            GROUP BY challenge_id) vs 
                            ON t1.challenge_id = vs.challenge_id
                LEFT JOIN (SELECT challenge_id,SUM(total_submissions) AS total_submissions, SUM(total_accepted_submissions) AS total_accepted_submissions 
                            FROM submission_stats
                            GROUP BY challenge_id) ss
                            ON t1.challenge_id = ss.challenge_id) t2
    ) t3
WHERE t3.flag=1
GROUP BY contest_id, hacker_id, name
ORDER BY t3.contest_id;
