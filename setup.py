import os
from setuptools import setup

setup(
    version="0.1.0",
    name="dcm-job-processor-api",
    description="api for job-processor-containers",
    author="LZV.nrw",
    install_requires=[
    ],
    packages=[
        "dcm_job_processor_api"
    ],
    package_data={
        "dcm_job_processor_api": [
            "dcm_job_processor_api/openapi.yaml",
        ],
    },
    include_package_data=True,
)
