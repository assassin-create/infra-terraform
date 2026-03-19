import os
import logging
import re

from infra.terraform import TerraformError

log = logging.getLogger(__name__)

def get_aws_region_from_terraform_context(context):
    """Extracts AWS region from Terraform context"""
    return os.environ.get('AWS_DEFAULT_REGION') or context['region']

def is_truthy(value):
    """Tries to convert a value to a boolean, returning True if truthy"""
    if isinstance(value, bool):
        return value
    else:
        return value.lower() in ['true', 'yes', '1']

def get_terraform_resource_value(resource, key):
    """Extracts a value for a given key from a Terraform resource"""
    return resource.get(key)