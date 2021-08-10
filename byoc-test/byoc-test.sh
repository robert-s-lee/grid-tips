cd ~/github/terraform-aws-gridbyoc/quick-start

export GRID_REGION=$(aws ec2 describe-regions \
    --all-regions \
    --query "Regions[].{Name:RegionName}" \
    --output text | shuf - | head -n 1)
export EXTERNAL_ID=$(terraform output -json | jq -r '.external_id.value')
export ROLE_ARN=$(terraform output -json | jq -r '.role_arn.value')
export GRID_CLUSTER=rslee-$(date '+%m%d')-$GRID_REGION
echo "$GRID_REGION $GRID_CLUSTER $EXTERNAL_ID $ROLE_ARN"

grid clusters aws --role-arn $ROLE_ARN --external-id $EXTERNAL_ID --region $GRID_REGION --instance-types t2.medium,t2.large $GRID_CLUSTER


