# -*- codeing = utf-8 -*-
# @Time  :2022/11/11 15:17
# @Author:wuyan
# @File  :fabfile.py
# @Software :PyCharm


from fabric import task
from invoke import Responder
from _credentials import github_username, github_password

def _get_github_auth_responders():
    username_responder = Responder(
        pattern="Username for 'https://github.com':",
        response='{}\n'.format(github_username)
    )
    password_responder = Responder(
        pattern="Password for 'https://{}@github.com':".format(github_username),
        response='{}\n'.format(github_password)
    )
    return [username_responder, password_responder]


@task()
def deploy(c):
    supervisor_conf_path = '~/etc/'
    supervisor_program_name = 'hellodjango-blog-tutorial'
    project_root_path = '~/apps/HelloDjango-blog-tutorial/'

    # 先停止应用
    with c.cd(supervisor_conf_path):
        cmd = 'supervisorctl stop {}'.format(supervisor_program_name)
        c.run(cmd)

    # 进入项目根目录，从git拉取最新代码
    with c.cd(project_root_path):
        cmd = 'git pull'
        responders = _get_github_auth_responders()
        c.run(cmd, watvhers=responders)

    # 安装依赖，迁移数据库，收集静态文件
    with c.cd(project_root_path):
        c.run('pipenv install --deploy --ignore-pipfile')
        c.run('pipenv run python manage.py migrate')
        c.run('pipenv run python collectstatic --noinput')

    # 重新启动应用
    with c.cd(supervisor_conf_path):
        cmd = 'supervisorctl satrt {}'.format(supervisor_program_name)
        c.run(cmd)
