-- Create table for storing campaign data in Amazon RDS
CREATE TABLE IF NOT EXISTS ad_campaign_data (
    campaign_id INT,
    impressions INT,
    clicks INT,
    spend DECIMAL(10, 2),
    roas DECIMAL(5, 2),
    market VARCHAR(255),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
