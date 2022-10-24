from setuptools import setup

version_tool = "setuptools-git-versioning"

setup(
    name="reproduce-bug",
    description="Transfer DOC PDFs to the APP workspace",
    setup_requires=["setuptools-git-versioning==1.12.0"],
    setuptools_git_versioning={
        "enabled": True,
        "template": "{tag}",
        "dev_template": "{tag}.dev1+{branch}.{ccount}.{sha}",
        "dirty_template": "{tag}.dev1+{branch}.{ccount}.{sha}.dirty",
    },
    python_requires=">=3.8",
)
