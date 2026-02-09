"""
离线佛历万年历工具 - Python版本
完全本地离线运行，支持Windows/Mac/Linux
需要安装: pip install zhdate
"""

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta
import zhdate
import calendar


class BuddhistCalendarApp:
    # 十斋日（农历日期）
    TEN_ZHAI_DAYS = [1, 8, 14, 15, 18, 23, 24, 28, 29, 30]

    # 佛历起始年份（佛陀涅槃公元前543年）
    BUDDHIST_ERA_START = 543

    # 天干
    HEAVENLY_STEMS = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']

    # 地支
    EARTHLY_BRANCHES = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

    # 生肖
    ZODIAC_ANIMALS = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']

    # 农历月份名称
    LUNAR_MONTHS = ['正月', '二月', '三月', '四月', '五月', '六月',
                     '七月', '八月', '九月', '十月', '冬月', '腊月']

    # 农历日期名称
    LUNAR_DAYS = ['初一', '初二', '初三', '初四', '初五', '初六', '初七', '初八', '初九', '初十',
                  '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九', '二十',
                  '廿一', '廿二', '廿三', '廿四', '廿五', '廿六', '廿七', '廿八', '廿九', '三十']

    # 节气（简化版本）
    SOLAR_TERMS = ['小寒', '大寒', '立春', '雨水', '惊蛰', '春分', '清明', '谷雨',
                   '立夏', '小满', '芒种', '夏至', '小暑', '大暑', '立秋', '处暑',
                   '白露', '秋分', '寒露', '霜降', '立冬', '小雪', '大雪', '冬至']

    # 主要佛菩萨圣诞（农历）
    BUDDHA_FESTIVALS = {
        (1, 1): '弥勒菩萨圣诞',
        (1, 9): '华严菩萨圣诞',
        (2, 8): '释迦牟尼佛出家',
        (2, 15): '释迦牟尼佛涅槃',
        (2, 19): '观世音菩萨圣诞',
        (2, 21): '普贤菩萨圣诞',
        (3, 16): '准提菩萨圣诞',
        (4, 4): '文殊菩萨圣诞',
        (4, 8): '释迦牟尼佛圣诞',
        (4, 15): '佛吉祥日',
        (5, 13): '伽蓝菩萨圣诞',
        (6, 3): '韦驮菩萨圣诞',
        (6, 19): '观世音菩萨成道',
        (7, 13): '大势至菩萨圣诞',
        (7, 15): '佛欢喜日',
        (7, 24): '龙树菩萨圣诞',
        (7, 30): '地藏菩萨圣诞',
        (8, 15): '月光菩萨圣诞',
        (9, 9): '摩诃迦叶尊者圣诞',
        (9, 19): '观世音菩萨出家',
        (9, 30): '药师佛圣诞',
        (10, 5): '达摩祖师圣诞',
        (11, 11): '阿弥陀佛圣诞',
        (11, 17): '日光菩萨圣诞',
        (12, 8): '释迦牟尼佛成道',
        (12, 21): '文殊菩萨出家',
        (12, 29): '华严菩萨圣诞',
    }

    def __init__(self, root):
        self.root = root
        self.root.title("离线佛历万年历工具")
        self.root.geometry("1200x750")

        # 当前显示的年月
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
        self.selected_date = datetime.now()

        # 设置样式
        self.setup_styles()

        # 创建界面
        self.create_widgets()

        # 检查十斋日提醒
        self.root.after(500, self.check_zhai_reminder)

        # 渲染日历
        self.render_calendar()
        self.update_date_details()

    def setup_styles(self):
        """设置样式"""
        self.colors = {
            'primary': '#8B4513',
            'secondary': '#A0522D',
            'accent': '#FFD700',
            'bg_light': '#f9f3e9',
            'bg_white': '#ffffff',
            'text': '#333333',
            'zhai': '#52c41a',
            'tomorrow_zhai': '#fa8c16',
            'festival': '#722ed1',
            'buddha': '#fa8c16',
            'today': '#fffbe6',
        }

        self.root.configure(bg=self.colors['bg_light'])

        # 配置ttk样式
        style = ttk.Style()
        style.theme_use('clam')

        # 按钮样式
        style.configure('Nav.TButton',
                       background=self.colors['primary'],
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       padding=(10, 5))
        style.map('Nav.TButton',
                 background=[('active', self.colors['secondary'])])

    def create_widgets(self):
        """创建界面组件"""
        # 主容器
        main_frame = tk.Frame(self.root, bg=self.colors['bg_light'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 标题
        header = tk.Frame(main_frame, bg='#8B4513', height=80)
        header.pack(fill=tk.X, pady=(0, 10))
        header.pack_propagate(False)

        title_label = tk.Label(header, text='离线佛历万年历工具',
                              font=('Microsoft YaHei', 20, 'bold'),
                              bg='#8B4513', fg='#FFD700')
        title_label.pack(pady=(15, 5))

        subtitle_label = tk.Label(header, text='完全本地离线运行，无需网络连接',
                                 font=('Microsoft YaHei', 10),
                                 bg='#8B4513', fg='#FFD700')
        subtitle_label.pack()

        # 内容区域
        content_frame = tk.Frame(main_frame, bg=self.colors['bg_light'])
        content_frame.pack(fill=tk.BOTH, expand=True)

        # 左侧日历区域
        calendar_frame = tk.Frame(content_frame, bg='white', relief=tk.RAISED, borderwidth=1)
        calendar_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))

        # 导航栏
        nav_frame = tk.Frame(calendar_frame, bg='#f5f1eb', height=60)
        nav_frame.pack(fill=tk.X, padx=15, pady=15)
        nav_frame.pack_propagate(False)

        # 年月显示
        self.month_year_label = tk.Label(nav_frame,
                                        text=f'{self.current_year}年{self.current_month}月',
                                        font=('Microsoft YaHei', 18, 'bold'),
                                        bg='#f5f1eb', fg=self.colors['primary'])
        self.month_year_label.pack(side=tk.LEFT, padx=15)

        # 导航按钮
        btn_frame = tk.Frame(nav_frame, bg='#f5f1eb')
        btn_frame.pack(side=tk.RIGHT, padx=15)

        buttons = [
            ('上一年', lambda: self.change_year(-1)),
            ('上一月', lambda: self.change_month(-1)),
            ('今天', self.go_today),
            ('下一月', lambda: self.change_month(1)),
            ('下一年', lambda: self.change_year(1)),
        ]

        for text, command in buttons:
            btn = tk.Button(btn_frame, text=text, command=command,
                           bg=self.colors['primary'], fg='white',
                           font=('Microsoft YaHei', 10),
                           relief=tk.FLAT, padx=12, pady=6,
                           cursor='hand2',
                           activebackground=self.colors['secondary'])
            btn.pack(side=tk.LEFT, padx=3)

        # 星期标题
        weekday_frame = tk.Frame(calendar_frame, bg='#f5f1eb')
        weekday_frame.pack(fill=tk.X, padx=15, pady=(0, 10))

        weekdays = ['日', '一', '二', '三', '四', '五', '六']
        for i, day in enumerate(weekdays):
            lbl = tk.Label(weekday_frame, text=day,
                          font=('Microsoft YaHei', 11, 'bold'),
                          bg='#f5f1eb', fg=self.colors['primary'],
                          width=10, padx=5, pady=8)
            lbl.grid(row=0, column=i, sticky='ew', padx=2, pady=2)
            weekday_frame.columnconfigure(i, weight=1)

        # 日历格子容器
        self.calendar_container = tk.Frame(calendar_frame, bg='white')
        self.calendar_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

        # 图例
        legend_frame = tk.Frame(calendar_frame, bg='#f5f1eb')
        legend_frame.pack(fill=tk.X, padx=15, pady=(0, 15))

        legends = [
            ('今天', self.colors['today'], self.colors['accent']),
            ('斋日', self.colors['zhai'], 'black'),
            ('佛菩萨圣诞', self.colors['buddha'], 'black'),
            ('明日斋日', self.colors['tomorrow_zhai'], 'black'),
        ]

        for text, bg, fg in legends:
            item_frame = tk.Frame(legend_frame, bg='#f5f1eb')
            item_frame.pack(side=tk.LEFT, padx=10)

            color_box = tk.Label(item_frame, text='  ', bg=bg, fg=fg,
                               relief=tk.SOLID, borderwidth=1)
            color_box.pack(side=tk.LEFT, padx=(0, 5))

            tk.Label(item_frame, text=text, bg='#f5f1eb',
                    font=('Microsoft YaHei', 9)).pack(side=tk.LEFT)

        # 右侧信息区域
        info_frame = tk.Frame(content_frame, bg='#fbf9f5', relief=tk.RAISED, borderwidth=1)
        info_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(5, 0))
        info_frame.pack_propagate(False)
        info_frame.configure(width=350)

        # 日期详情
        details_frame = tk.Frame(info_frame, bg='white', relief=tk.SOLID, borderwidth=1)
        details_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(details_frame, text='日期详情', font=('Microsoft YaHei', 12, 'bold'),
                bg='white', fg=self.colors['primary'], pady=10).pack()

        self.details_vars = {}
        detail_items = [
            ('gregorian', '公历'),
            ('lunar', '农历'),
            ('buddhist', '佛历'),
            ('zodiac', '生肖'),
            ('ganzhi', '干支'),
            ('jiezhi', '节气'),
            ('festivals', '节日'),
        ]

        details_container = tk.Frame(details_frame, bg='white')
        details_container.pack(fill=tk.X, padx=15, pady=(0, 15))

        for key, label in detail_items:
            frame = tk.Frame(details_container, bg='white')
            frame.pack(fill=tk.X, pady=5)

            tk.Label(frame, text=label, width=8, anchor='w',
                    font=('Microsoft YaHei', 10, 'bold'),
                    bg='white', fg=self.colors['primary']).pack(side=tk.LEFT)

            var = tk.StringVar()
            self.details_vars[key] = var
            tk.Label(frame, textvariable=var, anchor='w',
                    font=('Microsoft YaHei', 10),
                    bg='white', fg='black').pack(side=tk.LEFT, fill=tk.X, expand=True)

        # 斋日类型说明
        zhai_frame = tk.Frame(info_frame, bg='white', relief=tk.SOLID, borderwidth=1)
        zhai_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(zhai_frame, text='斋日类型', font=('Microsoft YaHei', 12, 'bold'),
                bg='white', fg=self.colors['primary'], pady=10).pack()

        zhai_content = tk.Frame(zhai_frame, bg='white')
        zhai_content.pack(fill=tk.X, padx=15, pady=(0, 15))

        zhai_types = [
            ('十斋日', '每月10天：初一、初八、十四、十五、十八、廿三、廿四、廿八、廿九、三十'),
            ('六斋日', '每月6天：初八、十四、十五、廿三、廿九、三十'),
            ('朔望斋', '每月2天：初一（朔日）、十五（望日）'),
        ]

        for title, desc in zhai_types:
            frame = tk.Frame(zhai_content, bg='white')
            frame.pack(fill=tk.X, pady=5)

            tk.Label(frame, text=title, font=('Microsoft YaHei', 10, 'bold'),
                    bg='white', fg=self.colors['primary']).pack(anchor='w')
            tk.Label(frame, text=desc, font=('Microsoft YaHei', 9),
                    bg='white', fg='#666').pack(anchor='w')

        # 底部说明
        note_frame = tk.Frame(info_frame, bg='#fff7e6', relief=tk.SOLID, borderwidth=1)
        note_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        note_text = """使用说明：
1. 完全本地离线运行，无需网络连接
2. 点击日历中的日期查看详细信息
3. 绿色标记为斋日，橙色为佛菩萨圣诞
4. 佛历以释迦牟尼佛涅槃年为纪元元年"""

        tk.Label(note_frame, text=note_text, font=('Microsoft YaHei', 9),
                bg='#fff7e6', fg='#8B4513', justify=tk.LEFT,
                padx=15, pady=15).pack(anchor='w')

    def render_calendar(self):
        """渲染日历"""
        # 清空日历容器
        for widget in self.calendar_container.winfo_children():
            widget.destroy()

        today = datetime.now()

        # 获取当月第一天
        first_day = datetime(self.current_year, self.current_month, 1)

        # 计算日历显示范围（42天，6周）
        # 找到当月第一天是星期几 (0=周一, 6=周日)
        first_weekday = first_day.weekday()
        # 转换为周日=0, 周一=1, ..., 周六=6
        first_weekday_sunday = (first_weekday + 1) % 7

        # 计算显示的第一天（可能是上月日期）
        display_start = first_day - timedelta(days=first_weekday_sunday)

        # 渲染42个格子（6周 × 7天）
        for week_idx in range(6):
            for day_idx in range(7):
                # 计算当前格子的日期
                current_date = display_start + timedelta(days=week_idx * 7 + day_idx)

                # 只显示当月的日期
                if current_date.year == self.current_year and current_date.month == self.current_month:
                    is_other_month = False
                    self.create_day_cell(current_date, is_other_month, today, week_idx, day_idx)

    def create_day_cell(self, date, is_other_month, today, row, column):
        """创建日期格子"""
        # 转换为农历
        try:
            lunar_date = zhdate.ZhDate.from_datetime(date)
            lunar_day = lunar_date.lunar_day
            lunar_month = lunar_date.lunar_month
            lunar_year = lunar_date.lunar_year

            # 获取农历日期名称
            lunar_day_name = self.LUNAR_DAYS[lunar_day - 1] if lunar_day <= 30 else self.LUNAR_DAYS[-1]

            # 检查是否是斋日
            is_zhai = lunar_day in self.TEN_ZHAI_DAYS

            # 检查明天是否是斋日
            tomorrow = date + timedelta(days=1)
            try:
                tomorrow_lunar = zhdate.ZhDate.from_datetime(tomorrow)
                is_tomorrow_zhai = tomorrow_lunar.lunar_day in self.TEN_ZHAI_DAYS
            except:
                is_tomorrow_zhai = False

            # 检查是否是佛菩萨圣诞
            festival = self.BUDDHA_FESTIVALS.get((lunar_month, lunar_day), '')

            # 判断样式
            is_today = (date.year == today.year and
                       date.month == today.month and
                       date.day == today.day)

            # 选择背景色
            if is_today:
                bg_color = self.colors['today']
                border_color = self.colors['accent']
            elif is_other_month:
                bg_color = '#f9f9f9'
                border_color = '#e8e0d8'
            else:
                bg_color = '#fcfaf6'
                border_color = '#e8e0d8'

            # 创建格子
            cell_frame = tk.Frame(self.calendar_container,
                                 bg=bg_color,
                                 relief=tk.SOLID,
                                 borderwidth=1,
                                 width=80,
                                 height=90)

            # 使用grid布局，位置已在render_calendar中计算好
            cell_frame.grid(row=row, column=column,
                           sticky='nsew', padx=2, pady=2)
            # 阻止格子根据内容自动调整大小
            cell_frame.grid_propagate(False)

            # 配置grid权重
            for i in range(7):
                self.calendar_container.columnconfigure(i, weight=1)
            for i in range(6):
                self.calendar_container.rowconfigure(i, weight=1)

            # 日期数字
            day_label = tk.Label(cell_frame,
                                text=str(date.day),
                                font=('Microsoft YaHei', 16, 'bold'),
                                bg=bg_color, fg='#333')
            day_label.pack(anchor='ne', padx=5, pady=(5, 0))

            # 农历日期
            lunar_label = tk.Label(cell_frame,
                                  text=lunar_day_name,
                                  font=('Microsoft YaHei', 11),
                                  bg=bg_color, fg=self.colors['primary'])
            lunar_label.pack(pady=2)

            # 斋日/节日标签
            if is_zhai:
                label = tk.Label(cell_frame,
                               text='十斋日',
                               font=('Microsoft YaHei', 9, 'bold'),
                               bg=self.colors['zhai'],
                               fg='white',
                               padx=3, pady=1)
                label.pack(pady=1)
            elif is_tomorrow_zhai and not is_zhai:
                label = tk.Label(cell_frame,
                               text='明日斋日',
                               font=('Microsoft YaHei', 9, 'bold'),
                               bg=self.colors['tomorrow_zhai'],
                               fg='white',
                               padx=3, pady=1)
                label.pack(pady=1)
            elif festival:
                label = tk.Label(cell_frame,
                               text=festival[:6],
                               font=('Microsoft YaHei', 9),
                               bg=self.colors['buddha'],
                               fg='white',
                               padx=3, pady=1)
                label.pack(pady=1)

            # 绑定点击事件
            cell_frame.bind('<Button-1>', lambda e, d=date: self.on_date_click(d))
            day_label.bind('<Button-1>', lambda e, d=date: self.on_date_click(d))
            lunar_label.bind('<Button-1>', lambda e, d=date: self.on_date_click(d))

            # 保存所有标签的原始配置用于恢复
            labels = [day_label, lunar_label]
            orig_configs = []

            for lbl in labels:
                config = {'widget': lbl, 'bg': lbl.cget('bg')}
                try:
                    config['fg'] = lbl.cget('fg')
                except:
                    pass
                orig_configs.append(config)

            # 如果有节日/斋日标签，也需要保存
            if is_zhai or is_tomorrow_zhai or festival:
                festival_label = cell_frame.winfo_children()[-1]
                config = {'widget': festival_label, 'bg': festival_label.cget('bg')}
                try:
                    config['fg'] = festival_label.cget('fg')
                except:
                    pass
                orig_configs.append(config)

            # 添加悬停效果
            def on_enter(e, configs=orig_configs):
                # 悬停时使用深蓝色背景和白色文字，强烈对比
                for cfg in configs:
                    widget = cfg['widget']
                    try:
                        widget.configure(bg='#1890ff', fg='white')
                    except:
                        try:
                            widget.configure(bg='#1890ff')
                        except:
                            pass

            def on_leave(e, configs=orig_configs):
                # 恢复原始颜色
                for cfg in configs:
                    widget = cfg['widget']
                    try:
                        if 'fg' in cfg:
                            widget.configure(bg=cfg['bg'], fg=cfg['fg'])
                        else:
                            widget.configure(bg=cfg['bg'])
                    except:
                        try:
                            widget.configure(bg=cfg['bg'])
                        except:
                            pass

            cell_frame.bind('<Enter>', on_enter)
            cell_frame.bind('<Leave>', on_leave)

        except Exception as e:
            print(f"Error creating day cell for {date}: {e}")

    def get_week_number(self, date):
        """获取日期在月历中的周数"""
        first_day = datetime(date.year, date.month, 1)
        return (date.day + first_day.weekday()) // 7

    def get_prev_month(self):
        """获取上个月的年月"""
        if self.current_month == 1:
            return (self.current_year - 1, 12)
        else:
            return (self.current_year, self.current_month - 1)

    def get_next_month(self):
        """获取下个月的年月"""
        if self.current_month == 12:
            return (self.current_year + 1, 1)
        else:
            return (self.current_year, self.current_month + 1)

    def get_last_day_of_month(self, year, month):
        """获取某月的最后一天"""
        if month == 12:
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, month + 1, 1)
        return (next_month - timedelta(days=1)).day

    def on_date_click(self, date):
        """日期点击事件"""
        self.selected_date = date
        self.update_date_details()

    def update_date_details(self):
        """更新日期详情"""
        try:
            date = self.selected_date
            lunar_date = zhdate.ZhDate.from_datetime(date)

            # 公历
            self.details_vars['gregorian'].set(
                f"{date.year}年{date.month}月{date.day}日")

            # 农历
            lunar_str = f"{lunar_date.lunar_year}年 {self.LUNAR_MONTHS[lunar_date.lunar_month - 1]}{self.LUNAR_DAYS[lunar_date.lunar_day - 1]}"
            self.details_vars['lunar'].set(lunar_str)

            # 佛历
            buddhist_year = date.year + self.BUDDHIST_ERA_START
            self.details_vars['buddhist'].set(f"佛历{buddhist_year}年")

            # 生肖
            zodiac_index = (lunar_date.lunar_year - 4) % 12
            self.details_vars['zodiac'].set(self.ZODIAC_ANIMALS[zodiac_index])

            # 干支
            year_ganzhi = self.get_ganzhi(lunar_date.lunar_year)
            self.details_vars['ganzhi'].set(f"{year_ganzhi}年")

            # 节气（简化显示）
            self.details_vars['jiezhi'].set('无')

            # 节日
            festival = self.BUDDHA_FESTIVALS.get((lunar_date.lunar_month, lunar_date.lunar_day), '')

            # 检查斋日
            is_zhai = lunar_date.lunar_day in self.TEN_ZHAI_DAYS

            # 检查明天是否是斋日
            tomorrow = date + timedelta(days=1)
            try:
                tomorrow_lunar = zhdate.ZhDate.from_datetime(tomorrow)
                is_tomorrow_zhai = tomorrow_lunar.lunar_day in self.TEN_ZHAI_DAYS

                festival_text = festival if festival else '无'
                if is_tomorrow_zhai:
                    tomorrow_str = f"{self.LUNAR_MONTHS[tomorrow_lunar.lunar_month - 1]}{self.LUNAR_DAYS[tomorrow_lunar.lunar_day - 1]}"
                    if festival_text == '无':
                        festival_text = f"明日{tomorrow_str}十斋日"
                    else:
                        festival_text += f"，明日{tomorrow_str}十斋日"

                if is_zhai:
                    if festival_text == '无':
                        festival_text = '十斋日（持戒修行吉日）'
                    else:
                        festival_text += '，十斋日（持戒修行吉日）'

                self.details_vars['festivals'].set(festival_text)
            except:
                self.details_vars['festivals'].set(festival if festival else '无')

        except Exception as e:
            print(f"Error updating date details: {e}")

    def get_ganzhi(self, lunar_year):
        """获取干支纪年"""
        stem_index = (lunar_year - 4) % 10
        branch_index = (lunar_year - 4) % 12
        return self.HEAVENLY_STEMS[stem_index] + self.EARTHLY_BRANCHES[branch_index]

    def change_year(self, delta):
        """切换年份"""
        self.current_year += delta
        self.update_month_year_label()
        self.render_calendar()

    def change_month(self, delta):
        """切换月份"""
        self.current_month += delta
        if self.current_month > 12:
            self.current_month = 1
            self.current_year += 1
        elif self.current_month < 1:
            self.current_month = 12
            self.current_year -= 1
        self.update_month_year_label()
        self.render_calendar()

    def go_today(self):
        """回到今天"""
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
        self.selected_date = datetime.now()
        self.update_month_year_label()
        self.render_calendar()
        self.update_date_details()

    def update_month_year_label(self):
        """更新年月标签"""
        self.month_year_label.config(
            text=f'{self.current_year}年{self.current_month}月')

    def check_zhai_reminder(self):
        """检查十斋日提醒"""
        try:
            today = datetime.now()
            lunar_date = zhdate.ZhDate.from_datetime(today)

            # 检查今天是否是斋日
            is_today_zhai = lunar_date.lunar_day in self.TEN_ZHAI_DAYS

            # 检查明天是否是斋日
            tomorrow = today + timedelta(days=1)
            tomorrow_lunar = zhdate.ZhDate.from_datetime(tomorrow)
            is_tomorrow_zhai = tomorrow_lunar.lunar_day in self.TEN_ZHAI_DAYS

            message = ""
            if is_today_zhai and is_tomorrow_zhai:
                message = f"🙏 今日十斋日提醒 🙏\n\n"
                message += f"今天是{self.LUNAR_MONTHS[lunar_date.lunar_month - 1]}{self.LUNAR_DAYS[lunar_date.lunar_day - 1]}，十斋日\n"
                message += f"明日{self.LUNAR_MONTHS[tomorrow_lunar.lunar_month - 1]}{self.LUNAR_DAYS[tomorrow_lunar.lunar_day - 1]}，亦是十斋日\n\n"
                message += "连续两日斋戒，请持戒清净，精进修持！"
            elif is_today_zhai:
                message = f"🙏 今日十斋日提醒 🙏\n\n"
                message += f"今天是{self.LUNAR_MONTHS[lunar_date.lunar_month - 1]}{self.LUNAR_DAYS[lunar_date.lunar_day - 1]}，十斋日\n\n"
                message += "请持戒清净，精进修持！"
            elif is_tomorrow_zhai:
                message = f"🙏 明日十斋日提醒 🙏\n\n"
                message += f"明日是{self.LUNAR_MONTHS[tomorrow_lunar.lunar_month - 1]}{self.LUNAR_DAYS[tomorrow_lunar.lunar_day - 1]}，十斋日\n\n"
                message += "请提前准备，明日持戒清净，精进修持！"

            if message:
                messagebox.showinfo("十斋日提醒", message)
        except Exception as e:
            print(f"Error checking zhai reminder: {e}")


def main():
    """主函数"""
    root = tk.Tk()

    # 设置窗口图标（如果有）
    try:
        # 可以添加图标文件
        # root.iconbitmap('icon.ico')
        pass
    except:
        pass

    app = BuddhistCalendarApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
