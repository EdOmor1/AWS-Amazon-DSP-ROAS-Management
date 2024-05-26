import boto3

# Initialize Backup client
backup = boto3.client('backup')

def create_backup_plan(backup_plan_name, resource_arn):
    try:
        # Create Backup plan
        response = backup.create_backup_plan(
            BackupPlan={
                'BackupPlanName': backup_plan_name,
                'Rules': [
                    {
                        'RuleName': 'Rule1',
                        'TargetBackupVaultName': 'MyBackupVault',
                        'ScheduleExpression': 'cron(0 12 * * ? *)',
                        'StartWindowMinutes': 60,
                        'CompletionWindowMinutes': 60,
                        'Lifecycle': {
                            'DeleteAfterDays': 30
                        }
                    }
                ]
            }
        )
        
        print("Backup plan created:", backup_plan_name)
    
    except Exception as e:
        print("Error creating backup plan:", str(e))

if __name__ == "__main__":
    backup_plan_name = 'my-backup-plan'
    resource_arn = 'arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0'
    create_backup_plan(backup_plan_name, resource_arn)
