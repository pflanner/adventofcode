from jinja2 import Environment, FileSystemLoader
import os


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    loader = FileSystemLoader(path)
    env = Environment(loader=loader)
    template = env.get_template('template.jinja2')

    for day in range(13, 26):
        text = template.render({'day': day})
        with open(os.path.join(path, f'{day}.py'), mode='w') as f:
            f.write(text)