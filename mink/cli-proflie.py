### Homework ###
# 실행 명령어: python src/cli-proflie.py

# ==========|코드 실습|========= #
import click
import pyfiglet
import time

from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.markdown import Markdown

@click.command()
def main():
    console = Console()

    for step in track(range(10), description="프로필 접근 중..."):
        time.sleep(0.1)

    md = Markdown('안녕하세요, ***제 소개***를 시작하겠습니다.  \n\n'
    '- **이름**: 구민경  \n'
    '- **전공**: 전기정보공학  \n'
    '- **MBTI**: INFJ  \n')
    console.print(md)

    table = Table(title="추가 정보")
    table.add_column("분류", style="cyan")
    table.add_column("내용", justify="left")

    table.add_row("기술 스택", "Python, C/C++, C#, JavaScript, Verilog")
    table.add_row("동아리 활동", "시:동, 샌드페블즈")
    table.add_row("취미 생활", "야구 관람")
    console.print(table)

    text = '만나서 반갑습니다:)'
    click.echo(click.style(text, fg='green', bg='white'))

if __name__ == "__main__":
    main()