import os
import datetime
import pgzrun
import random
from pygame import Rect
from PIL import Image
#PIL，图像处理库，Image是具体执行图像操作的类，包括打开，图块的变换
from json_tool import *
import sys

TITLE = "myPuzzle"
WIDTH = 600 + 300
HEIGHT = 600

def processPath(path):
    '''
    :param path: 相对于根目录的路径
    :return: 拼接好的路径
    '''
    if getattr(sys, 'frozen', False):  # 判断是否存在属性frozen，以此判断是打包的程序还是源代码。false为默认值，即没有frozen属性时返回false
        base_path = sys._MEIPASS  # 该属性也是打包程序才会有，源代码尝试获取该属性会报错
    else:
        base_path = os.path.abspath(".")  # 当源代码运行时使用该路径
    return os.path.join(base_path, path)
class Game():
    LEVEL_CONFIG = {"e": ["简单", 3, 0], "m": ["中等", 4, 80], "h": ["困难", 5, 160]}  # 游戏难度配置
    IMAGE_SIZE = 600  # 图片尺寸

    def __init__(self):
        self.record_data = None
        self.button = [[Rect((640, 200), (100, 30)), "开始游戏", self.start_game],
                       [Rect((760, 200), (100, 30)), "结束游戏", self.stop_game],
                       [Rect((640, 250), (100, 30)), "查看原图", self.basic_info],
                       [Rect((760, 250), (100, 30)), "更换图片", self.change_img]]
        
        self.return_to_game_button = [Rect((700, 100), (100, 30)), "返回拼图", self.return_to_game]
        self.choose_level_button = {k: [Rect((640 + v[2], 130), (60, 20)), v[0], self.choose_level] for k, v in
                                    Game.LEVEL_CONFIG.items()}
        
        #这里动态地设置三个按钮，v是指e、m、h，然后v[2]就是0、80、160,640+v[2]就是设置按钮的左边开始坐标,用for循环将k和v在level_config遍历
        self.level = "e"  # 游戏等级 简单(E 3) 中等(M 4) 困难(H 5)
        self.image_source = ["pic1","pic2"]
        self.choose_img = None  # 所选图片
        self.split_n = None  # 拼图分成几块
        self.step = None
        self.choose_img_actor = None
        self.img_actors = []  # 拼图对象列表
        self.base_pos = None  # 位置参照
        self.img_pos = None  # 当前位置
        self.game_state = 0  # 0:未开始 1:进行中 2:完成
        self.isbasic = False  # 是否查看原图
        self.start_time = None  # 游戏开始时间
        self.use_time = 0  # 游戏进行时间
        self.last_click_index = None  # 最后一次点击位置
        self.get_record_data()
        self.init()

    def get_record_data(self):
        try:
            self.record_data = read_json("record.json")
        except:
            self.record_data = {i: None for i in Game.LEVEL_CONFIG.keys()}
            save_json(self.record_data, "record.json")

    def init(self):
        self.random_img()

    def choose_level(self, level):
        self.stop_game()
        self.level = level
        self.init()

    def judge_success(self):
        if self.img_pos == self.base_pos:
            self.game_state = 2
            if self.record_data[self.level] is None or self.record_data[self.level] > self.use_time:
                self.record_data[self.level] = self.use_time
                save_json(self.record_data, "record.json")

    def change_img(self):
        self.stop_game()
        self.init()

    def start_game(self):
        self.game_state = 1  # 更改游戏状态为进行中
        self.init_img()
        self.use_time = 0
        self.start_time = datetime.datetime.now()

    def stop_game(self):
        self.game_state = 0

    def basic_info(self):
        self.isbasic = True

    def return_to_game(self):
        self.isbasic = False

    def init_img(self):
        self.split_n = Game.LEVEL_CONFIG[self.level][1]  # 拼图分成几块
        im = Image.open(processPath(f'images\\{self.choose_img}_base.png'))
        im = im.resize((Game.IMAGE_SIZE, Game.IMAGE_SIZE))
        self.step = Game.IMAGE_SIZE / self.split_n
        self.img_actors = []
        self.base_pos = [i for i in range(self.split_n * self.split_n)]
        self.img_pos = [i for i in range(self.split_n * self.split_n)]
        for i in range(self.split_n):  # i:行
            for j in range(self.split_n):  # j:列
                if not os.path.exists(processPath(f'images\\{self.choose_img}_{self.level}_{j}_{i}.png')):
                    box = (j * self.step, i * self.step, (j + 1) * self.step, (i + 1) * self.step)
                    pic = im.crop(box)
                    pic.save(processPath(f'images\\{self.choose_img}_{self.level}_{j}_{i}.png'))
                actor = Actor(processPath(f'images\\{self.choose_img}_{self.level}_{j}_{i}')) # type: ignore
                self.img_actors.append(actor)
        random.shuffle(self.img_pos)
        self.init_pos()

    def init_pos(self):
        for i in range(self.split_n):
            for j in range(self.split_n):
                index = self.get_index(i, j)
                self.img_actors[self.img_pos[index]].left = j * self.step  # 左边
                self.img_actors[self.img_pos[index]].top = i * self.step  # 上边

    def get_index(self, i, j):
        return int(self.split_n * i + j)

    def swap_position(self, index_1, index_2):
        self.img_pos[index_1], self.img_pos[index_2] = self.img_pos[index_2], self.img_pos[index_1]
        self.init_pos()
        self.judge_success()

    def random_img(self):
        self.choose_img = random.choice(self.image_source)
        im = Image.open(processPath(f'images\\{self.choose_img}.png'))
        im = im.resize((Game.IMAGE_SIZE, Game.IMAGE_SIZE))
        im.save(processPath(f'images\\{self.choose_img}_base.png'))
        self.choose_img_actor = Actor(processPath(f'images\\{self.choose_img}_base')) # type: ignore
        self.choose_img_actor.left = 0
        self.choose_img_actor.top = 0


game_manager = Game()


def update():
    if game_manager.game_state == 1:
        game_manager.use_time = (datetime.datetime.now() - game_manager.start_time).seconds


def on_mouse_down(pos, button):  # 当鼠标按键时执行
    # 查看图片时
    if game_manager.isbasic:
        if game_manager.return_to_game_button[0].collidepoint(pos):
            game_manager.return_to_game()
            return
    # 处理按钮
    for b in game_manager.button:
        rect_obj, _, fnc = b
        if rect_obj.collidepoint(pos):
            fnc()
            return
    for k, b in game_manager.choose_level_button.items():
        rect_obj, _, fnc = b
        if rect_obj.collidepoint(pos):
            fnc(k)
            return
    # 处理图片点击
    if pos[0] <= game_manager.IMAGE_SIZE and pos[1] <= game_manager.IMAGE_SIZE and game_manager.game_state == 1:
        x, y = pos
        col_index = x // game_manager.step
        row_index = y // game_manager.step
        index = game_manager.get_index(row_index, col_index)
        if game_manager.last_click_index is None:
            game_manager.last_click_index = index
        elif game_manager.last_click_index == index:
            game_manager.last_click_index = None
        else:
            game_manager.swap_position(game_manager.last_click_index, index)
            game_manager.last_click_index = None


def draw():
    screen.clear() # type: ignore
    # 画背景
    screen.fill("black") # type: ignore
    # 游戏状态
    font_config = {"fontsize": 30, "color": "orange", "fontname": "aafengkuangyuanshiren-2.ttf"}
    screen.draw.text("游戏尚未开始", (610, 10), **font_config) if game_manager.game_state == 0 else screen.draw.text( # type: ignore
        f"游戏已进行:{game_manager.use_time}秒", (610, 10),
        **font_config) if game_manager.game_state == 1 else screen.draw.text( # type: ignore
        f"恭喜你完成游戏\n耗时:{game_manager.use_time}秒", (610, 10), **font_config)
    # 榜单记录
    record_font_config = {"fontsize": 20, "color": "sky blue", "fontname": "aafengkuangyuanshiren-2.ttf"}
    y = 400
    screen.draw.text("榜单记录:", (640, y - 40), **record_font_config) # type: ignore
    for level, da in game_manager.LEVEL_CONFIG.items():
        screen.draw.text( # type: ignore
            f"{da[0]} : {f'{game_manager.record_data[level]} 秒' if game_manager.record_data[level] is not None else '暂无记录'}",
            (640, y), **record_font_config)
        y += 40
    # 按钮
    if not game_manager.isbasic:
        screen.draw.text("请选择挑战难度:", (640, 100), **record_font_config) # type: ignore
        for k, v in game_manager.choose_level_button.items():
            rect_obj, text, _ = v
            screen.draw.rect(rect_obj, "white") # type: ignore
            screen.draw.textbox(text, rect_obj, color="yellow" if game_manager.level == k else "white", # type: ignore
                                fontname="aafengkuangyuanshiren-2.ttf")

    if not game_manager.isbasic:
        for b in game_manager.button:
            rect_obj, text, _ = b
            screen.draw.rect(rect_obj, "white") # type: ignore
            screen.draw.textbox(text, rect_obj, color="white", fontname="aafengkuangyuanshiren-2.ttf") # type: ignore
    else:
        rect_obj, text, _ = game_manager.return_to_game_button
        screen.draw.rect(rect_obj, "white") # type: ignore
        screen.draw.textbox(text, rect_obj, color="white", fontname="aafengkuangyuanshiren-2.ttf") # type: ignore

    # 画图片
    if game_manager.game_state != 1 or game_manager.isbasic:
        game_manager.choose_img_actor.draw()
    else:
        for tile in game_manager.img_actors:
            tile.draw()
        # 画红框
        if game_manager.last_click_index is not None:
            screen.draw.rect( # type: ignore
                Rect((game_manager.img_actors[game_manager.img_pos[game_manager.last_click_index]].left,
                      game_manager.img_actors[game_manager.img_pos[game_manager.last_click_index]].top),
                     (game_manager.step, game_manager.step)), 'red')





pgzrun.go()  # 开始执行游戏
