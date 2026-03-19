SELECT 
    feature_name,
    COUNT(DISTINCT user_id) AS users_using_feature
FROM product_usage
GROUP BY feature_name
ORDER BY users_using_feature DESC;
