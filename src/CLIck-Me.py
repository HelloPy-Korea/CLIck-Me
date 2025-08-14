"""
실행 명령어: python src/CLIck-Me.py
"""
import click
import subprocess

@click.group()
def CLIck_Me():
    """
    HelloPY의 CLIck-Me 프로젝트의 명령어 그룹입니다.
    """
    pass

@CLIck_Me.command()
def hellopy_world():
    """hellopy_world를 출력합니다."""
    click.echo("Running: python sample/cli-profile_sample.py")
    subprocess.run(["python", "sample/cli-profile_sample.py"])

@CLIck_Me.command()
def suminnn():
    """suminnn님의 자기소개 CLI를 출력합니다."""
    click.echo("Running: python suminnn/cli-proflie_with_AI.py")
    subprocess.run(["python", "suminnn/cli-proflie_with_AI.py"])

@CLIck_Me.command()
def other1():
    """other1님의 자기소개 CLI를 출력합니다."""
    click.echo("Running: python other/cli-proflie_with_AI.py")
    subprocess.run(["python", "other/cli-proflie_with_AI.py"])

@CLIck_Me.command()
def other2():
    """other2님의 자기소개 CLI를 출력합니다."""
    click.echo("Running: python other/cli-proflie_with_AI.py")
    subprocess.run(["python", "other/cli-proflie_with_AI.py"])

if __name__ == '__main__':
    CLIck_Me()
