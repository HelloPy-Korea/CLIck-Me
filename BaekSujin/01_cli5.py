### 실습5 ###
# 실행 명령어: python src/01_cli5.py

# ==========|코드 실습|========= #
import click

@click.command()
@click.option('--name', '-n', default='Pymon')
def main(name):
    click.echo(click.style(f"Hello, HelloPY!, My Name is {name}", fg='green', bg='white', bold=True))

if __name__ == "__main__":
    main()

