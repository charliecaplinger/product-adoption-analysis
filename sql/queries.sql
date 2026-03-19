-- Feature adoption
SELECT 
    feature_name,
    COUNT(DISTINCT user_id) AS users
FROM product_usage
GROUP BY feature_name
ORDER BY users DESC;

-- Adoption by plan
SELECT 
    plan,
    feature_name,
    COUNT(DISTINCT user_id) AS users
FROM product_usage
GROUP BY plan, feature_name;

-- Daily active users
SELECT 
    event_date,
    COUNT(DISTINCT user_id) AS dau
FROM product_usage
GROUP BY event_date
ORDER BY event_date;
