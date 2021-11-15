# private-api
Private APIをSAMで作成したサンプルです。

# 使い方
template.yamlのVpcId, SubnetIdを利用する環境に書き換えて利用してください。

# コマンド例
Lambdaをビルド

`sam build`

スタックをデプロイ

`sam deploy --stack-name private-api --s3-bucket [your S3 bucket name] --region ap-northeast-1 --capabilities CAPABILITY_NAMED_IAM --template .aws-sam/build/template.yaml`