# HealthCare_Metrics

Below is a step by process on how the pipeline was designed for the Healthcare Metrics project.
The project uses mostly AWS services.

Glue Jobs
NurseHours: Glue job for totalhours worked by nurses.
deficiencies: Glue job for healthcare deficiencies by state.
demojob: Glue job for readmission rate.



S3 Bucket
S3 bucket will be used as our datalake.
S3 will be used to store our raw data as well
as our transformed data

WHY S3: S3 is cheap, scalable, can handle structured, semi-structured and unstructured data types


AWS Glue
Glue will be used to ingest data from google drive into S3
Glue will be used for extract tranform and load procedure.
Glue will extract the data from S3 bucket. We will use glue
to perform joins and aggregation and other necessary transformation tasks.
Once this is done glue will load the data back into S3 bucket.


WHY Glue:
Glue is serverless, scalable and suitable for the requirements being asked for this project.
Glue can handle incremental loads, scheduling and orchestration as well


Streamlit
Streamlit will be used to viisualize our transformed data




Metrics
I Calculated readmission rates by City. 
I calculated the total number of health and fire deficiencies for the year 2024 for each state
I also calculated the total hours worked by nurses by city
I have included the snapshots of the visualization in my deliverables folder



file:NH_SurveySummary_Oct2024
Health Safety Deficencies for the 2024



SQL COMMANDS USED IN GLUE

Radmission Rate
SELECT
    city_town,
    coalesce(AVG(score),0) AS average_score
FROM
    myDataSource
GROUP BY
    city_town;
	
	
Nurse Hours
SELECT *,
CONCAT(
    SUBSTRING(WorkDate, 1, 4), '-', 
    SUBSTRING(WorkDate, 5, 2), '-', 
    SUBSTRING(WorkDate, 7, 2)
) AS new_date
,
(Hrs_RNDON + Hrs_RNDON_emp + Hrs_RNDON_ctr + Hrs_RNadmin + Hrs_RNadmin_emp + Hrs_RNadmin_ctr + Hrs_RN + Hrs_RN_emp + Hrs_RN_ctr + Hrs_LPNadmin + Hrs_LPNadmin_emp + Hrs_LPNadmin_ctr + Hrs_LPN + Hrs_LPN_emp + Hrs_LPN_ctr + Hrs_CNA + Hrs_CNA_emp + Hrs_CNA_ctr) AS total_hours

from myDataSource




Deficencies
select
    state,
    SUM(total_number_of_health_deficiencies) as health_deficiency_count,
    SUM(total_number_of_fire_safety_deficiencies) as fire_deficiency_count
from
    myDataSource
where
    YEAR(health_survey_date) = 2024
GROUP by
    state


