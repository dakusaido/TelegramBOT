from environs import Env
from utils.getProjectPath import get_project_path

env = Env()

env.read_env(get_project_path() + r'\data\config\BOT_TOKEN.env')

BOT_TOKEN = env.str('BOT_TOKEN')

ADMINS_ID = []
