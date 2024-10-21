# --------------Классы и объекты--------

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []
    current_user = 'Вход в систему не выполнен'
    data_user = {}
    data_video = {}
    video_duration = {}

    def __init__(self):
        pass

    def log_in(self, nickname, password):
        if nickname in self.users:
            for i in self.users:
                if hash(i) == hash(password):
                    UrTube.current_user = nickname
                    # print(f'Верные имя пользователя и пароль. {nickname} Добро пожаловать!')
        else:
            print('Такого пользователя нет, либо пароль неверный')

    def register(self, nickname, password, age):
        if nickname not in self.users:
            User.nickname = nickname
            User.password = password
            User.age = age
            self.users.append(nickname)
            self.users.append(password)
            self.users.append(age)
            self.data_user[nickname] = age
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = 'Вход в систему не выполнен'

    def add(self, *args):
        for i in range(0, len(args)):
            if args[i].title != self.videos:
                self.videos.append(args[i].title)
                self.data_video[args[i].title] = args[i].adult_mode
                self.video_duration[args[i].title] = args[i].duration

    def get_videos(self, *args):
        spisok = []
        up_1 = list(s.upper() for s in args)
        up_2 = list(s.upper() for s in self.videos)
        for i in range(0, len(up_2)):
            if up_2[i].count(*up_1) > 0:
                spisok.append(self.videos[i])
        if len(spisok) == 0:
            return str('Видео не найдено')
        else:
            return str(spisok)

    def watch_video(self, title):
        if self.videos.count(title) > 0:
            if self.current_user == 'Вход в систему не выполнен':
                print('Войдите в аккаунт, чтобы смотерть видео')
            elif self.data_user.get(self.current_user) < 18 and self.data_video.get(title):
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                import time
                for i in range(0, self.video_duration.get(title) + 1):
                    time.sleep(0.5)
                    print(i, ' ', end="")
                print('Конец видео')
                self.video_duration[title] = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))



# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')