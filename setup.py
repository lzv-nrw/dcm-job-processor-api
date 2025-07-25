import os
from setuptools import setup

setup(
    version="1.0.0",
    name="dcm-job-processor-api",
    description="specification of the DCM Job Processor API",
    author="LZV.nrw",
    license="MIT",
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
