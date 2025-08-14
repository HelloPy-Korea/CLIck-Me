"""
실행 명령어: python CLIck-Me.py
"""
import click
import subprocess

from rich.table import Table
from rich.console import Console

@click.group(invoke_without_command=True)
@click.pass_context
def CLIck_Me(ctx):
    """
    HelloPY의 CLIck-Me 프로젝트의 명령어 그룹입니다.
    """
    if ctx.invoked_subcommand is None:
        table = Table(title="명령어 목록")

        table.add_column("명령어", style="cyan", no_wrap=True)
        table.add_column("설명", style="white")

        for name, cmd in sorted(ctx.command.commands.items()):
            table.add_row(name, cmd.help or "")

        console = Console()
        console.print(table)

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
