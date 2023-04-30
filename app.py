#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_project.aws_cdk_project_stack import AwsCdkProjectStack


app = cdk.App()
AwsCdkProjectStack(app, "aws-cdk-project")

app.synth()
