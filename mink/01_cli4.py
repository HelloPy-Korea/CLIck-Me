### 실습4 ###
# 실행 명령어1: python src/01_cli4.py name
# 실행 명령어2: python src/01_cli4.py mbti

# ==========|코드 실습|========= #
import click

@click.group()
def main():
    pass

@main.command()
@click.option('--name', '--n', default = 'Pymon')
def name(name):
    click.echo(f"My name is {name}")

@main.command()
@click.option('--mbti', '--m', default='infj')
def mbti(mbti):
    click.echo(f"MBTI is {mbti}")

if __name__ == "__main__":
    main()