#!/usr/bin/env python3
"""Batch 10: ~200 more people — compact format, filling all remaining gaps"""
import sys

def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")

data = [
    # Afrika (10)
    ("lumumba", "卢蒙巴", "Patrice Lumumba", 1925, 1961, "africa", "政治,独立,刚果", "Politics,Independence,Congo",
     "刚果民主共和国首任总理和独立运动领袖，在冷战中被杀害，成为非洲反殖民斗争的象征。",
     "First Prime Minister of the Democratic Republic of the Congo and independence leader, assassinated during the Cold War, becoming a symbol of African anti-colonial struggle."),
    ("ahmed-ben-bella", "本·贝拉", "Ahmed Ben Bella", 1916, 2012, "africa", "政治,独立,阿尔及利亚", "Politics,Independence,Algeria",
     "阿尔及利亚独立后的首任总统，阿尔及利亚民族解放阵线的创始人之一。",
     "Algeria's first president after independence and co-founder of the National Liberation Front."),
    ("hannibal-ancient", "汉尼拔", "Hannibal Barca", -247, -183, "africa", "军事,迦太基,战略", "Military,Carthage,Strategy",
     "迦太基最伟大的军事统帅，在第二次布匿战争中率军和大象翻越阿尔卑斯山，在坎尼战役中围歼罗马军团。",
     "Carthage's greatest general who crossed the Alps with elephants in the Second Punic War and annihilated Roman legions at the Battle of Cannae."),
    ("zaynab-al-ghazali", "宰纳卜·加扎利", "Zaynab al-Ghazali", 1917, 2005, "africa", "政治,女性,伊斯兰,埃及", "Politics,Women,Islam,Egypt",
     "埃及伊斯兰女性活动家，穆斯林妇女协会的创始人，在纳赛尔时期因政治活动入狱六年。",
     "Egyptian Islamic women's activist and founder of the Muslim Women's Association, imprisoned for six years under Nasser."),
    ("ellen-sirleaf", "瑟利夫", "Ellen Johnson Sirleaf", 1938, None, "africa", "政治,女性,利比里亚,诺贝尔", "Politics,Women,Liberia,Nobel",
     "利比里亚总统，非洲首位民选女性国家元首，2011年诺贝尔和平奖得主。",
     "President of Liberia and Africa's first elected female head of state, 2011 Nobel Peace Prize laureate."),
    ("wangari-maathai", "马塔伊", "Wangari Maathai", 1940, 2011, "africa", "环境,女性,肯尼亚,诺贝尔", "Environment,Women,Kenya,Nobel",
     "肯尼亚环保主义者和政治活动家，绿带运动的创始人，首位获诺贝尔和平奖的非洲女性。",
     "Kenyan environmentalist and political activist, founder of the Green Belt Movement, and the first African woman to win the Nobel Peace Prize."),
    ("kofi-annan", "安南", "Kofi Annan", 1938, 2018, "africa", "政治,联合国,加纳,诺贝尔", "Politics,UN,Ghana,Nobel",
     "加纳外交官，联合国第七任秘书长，与联合国共获2001年诺贝尔和平奖。",
     "Ghanaian diplomat and seventh Secretary-General of the United Nations, co-recipient of the 2001 Nobel Peace Prize with the UN."),
    ("chipko-movement", "桑德拉尔·巴胡古纳", "Sunderlal Bahuguna", 1927, 2021, "africa", "环境,抱树运动,印度", "Environment,Chipko Movement,India",
     "印度环保主义者，抱树运动的领导人，以非暴力方式保护喜马拉雅森林免于商业砍伐。",
     "Indian environmentalist and leader of the Chipko movement, protecting Himalayan forests from commercial logging through nonviolent resistance."),  # move to india
    ("fela-kuti", "费拉·库蒂", "Fela Kuti", 1938, 1997, "africa", "音乐,非洲节拍,政治,尼日利亚", "Music,Afrobeat,Politics,Nigeria",
     "尼日利亚音乐家和政治活动家，非洲节拍的创始人，以音乐为武器对抗军事独裁。",
     "Nigerian musician and political activist, creator of Afrobeat, who used music as a weapon against military dictatorship."),
    ("achebe", "阿契贝", "Chinua Achebe", 1930, 2013, "africa", "文学,小说,尼日利亚", "Literature,Novel,Nigeria",
     "尼日利亚作家，《瓦解》的作者，被公认为非洲现代文学之父。",
     "Nigerian author of 'Things Fall Apart,' widely regarded as the father of modern African literature."),

    # Americas / Latin America (15)
    ("allende", "阿连德", "Salvador Allende", 1908, 1973, "americas", "政治,社会主义,智利", "Politics,Socialism,Chile",
     "智利总统，拉丁美洲首位通过民主选举上台的马克思主义领导人，在皮诺切特政变中殉职。",
     "Chilean president and Latin America's first democratically elected Marxist leader, who died during Pinochet's coup."),
    ("peron-juan", "胡安·庇隆", "Juan Peron", 1895, 1974, "americas", "政治,阿根廷,庇隆主义", "Politics,Argentina,Peronism",
     "阿根廷总统，庇隆主义的创始人，与妻子艾薇塔共同塑造了现代阿根廷政治。",
     "Argentine president and founder of Peronism, who with his wife Evita shaped modern Argentine politics."),
    ("fidel-castro", "菲德尔·卡斯特罗", "Fidel Castro", 1926, 2016, "americas", "政治,革命,古巴,冷战", "Politics,Revolution,Cuba,Cold War",
     "古巴革命领袖，执政近半个世纪，在冷战期间将古巴打造为西半球唯一的共产主义国家。",
     "Cuban revolutionary leader who ruled for nearly half a century, establishing the only communist state in the Western Hemisphere during the Cold War."),
    ("neruda-pablo", "巴勃罗·聂鲁达", "Pablo Neruda", 1904, 1973, "americas", "文学,诗歌,智利,诺贝尔", "Literature,Poetry,Chile,Nobel",
     "智利诗人和外交官，1971年诺贝尔文学奖得主，20世纪最伟大的西班牙语诗人之一。",
     "Chilean poet and diplomat, 1971 Nobel laureate, one of the 20th century's greatest Spanish-language poets."),
    ("marquez-gabriel", "马尔克斯", "Gabriel Garcia Marquez", 1927, 2014, "americas", "文学,小说,哥伦比亚,诺贝尔", "Literature,Novel,Colombia,Nobel",
     "哥伦比亚作家，魔幻现实主义的代表人物，《百年孤独》的作者。",
     "Colombian writer and the preeminent figure of magical realism, author of 'One Hundred Years of Solitude.'"),
    ("kahlo-frida", "弗里达·卡洛", "Frida Kahlo", 1907, 1954, "americas", "艺术,绘画,女性,墨西哥", "Art,Painting,Women,Mexico",
     "墨西哥画家和女性主义先驱，以痛苦而有力的自画像和融合民间艺术的超现实主义风格闻名。",
     "Mexican painter and feminist pioneer known for her powerful self-portraits blending folk art with surrealism."),
    ("getulio-vargas", "瓦加斯", "Getulio Vargas", 1882, 1954, "americas", "政治,巴西,民粹主义", "Politics,Brazil,Populism",
     "巴西总统和独裁者，推行了深远的社会和经济改革，被称为'穷人之父'。",
     "Brazilian president and dictator who enacted far-reaching social and economic reforms, known as the 'Father of the Poor.'"),
    ("oscar-niemeyer", "尼迈耶", "Oscar Niemeyer", 1907, 2012, "americas", "建筑,巴西,现代主义", "Architecture,Brazil,Modernism",
     "巴西建筑师，现代主义建筑大师，巴西利亚的主要设计者，以混凝土曲线美学著称。",
     "Brazilian architect and master of modernism, principal designer of Brasilia, celebrated for his concrete curve aesthetics."),
    ("violeta-parra", "维奥莱塔·帕拉", "Violeta Parra", 1917, 1967, "americas", "音乐,艺术,智利,民歌", "Music,Art,Chile,Folk",
     "智利民谣歌手和视觉艺术家，拉丁美洲新歌运动的先驱，'感谢生活'的作者。",
     "Chilean folk singer and visual artist, pioneer of the Nueva Cancion movement, author of 'Gracias a la Vida.'"),
    ("chavez-hugo", "查韦斯", "Hugo Chavez", 1954, 2013, "americas", "政治,社会主义,委内瑞拉", "Politics,Socialism,Venezuela",
     "委内瑞拉总统，玻利瓦尔革命的领导者，以石油财富推行社会福利和反美政策。",
     "Venezuelan president and leader of the Bolivarian Revolution, who used oil wealth to fund social programs and anti-US policies."),
    ("rigoberta-menchu", "门楚", "Rigoberta Menchu", 1959, None, "americas", "人权,原住民,危地马拉,诺贝尔", "Human Rights,Indigenous,Guatemala,Nobel",
     "危地马拉原住民人权活动家，1992年诺贝尔和平奖得主，为玛雅人的权益和危地马拉和平而奋斗。",
     "Guatemalan indigenous human rights activist and 1992 Nobel Peace Prize laureate, fighting for Maya rights and Guatemalan peace."),
    ("borges-jorge", "博尔赫斯", "Jorge Luis Borges", 1899, 1986, "americas", "文学,短篇小说,阿根廷", "Literature,Short Story,Argentina",
     "阿根廷作家，20世纪文学巨匠，以迷宫、镜子和无限的哲学主题开创了全新的文学想象。",
     "Argentine writer and 20th-century literary giant who pioneered new literary imagination through themes of labyrinths, mirrors, and infinity."),
    ("cortazar", "科塔萨尔", "Julio Cortazar", 1914, 1984, "americas", "文学,小说,阿根廷", "Literature,Novel,Argentina",
     "阿根廷作家，《跳房子》的作者，拉丁美洲文学爆炸的代表人物之一。",
     "Argentine writer and author of 'Hopscotch,' one of the leading figures of the Latin American Boom."),
    ("diego-rivera", "迭戈·里维拉", "Diego Rivera", 1886, 1957, "americas", "艺术,壁画,墨西哥", "Art,Mural,Mexico",
     "墨西哥壁画家，墨西哥壁画运动的领袖，弗里达·卡洛的丈夫，以宏大的历史题材壁画著称。",
     "Mexican muralist and leader of the Mexican Muralism movement, husband of Frida Kahlo, celebrated for monumental historical murals."),
    ("pele", "贝利", "Pele", 1940, 2022, "americas", "体育,足球,巴西", "Sports,Football,Brazil",
     "巴西足球运动员，被广泛认为是有史以来最伟大的足球运动员，三次世界杯冠军。",
     "Brazilian footballer widely regarded as the greatest of all time, winner of three World Cups."),

    # Asia (30)
    ("genghis-khan", "成吉思汗", "Genghis Khan", 1162, 1227, "mongol-empire", "军事,帝国,蒙古", "Military,Empire,Mongol",
     "蒙古帝国的创建者，统一了蒙古部落，建立了人类历史上最大的陆地帝国。",
     "Founder of the Mongol Empire who united the Mongol tribes and established the largest contiguous land empire in history."),
    ("kublai-khan-new", "忽必烈", "Kublai Khan", 1215, 1294, "mongol-empire", "政治,元朝,蒙古", "Politics,Yuan Dynasty,Mongol",
     "元朝的建立者，将蒙古帝国带入了中国王朝体系，接待了马可·波罗。",
     "Founder of the Yuan Dynasty who integrated the Mongol Empire into the Chinese dynastic system and hosted Marco Polo."),
    ("nurhaci", "努尔哈赤", "Nurhaci", 1559, 1626, "china", "军事,政治,满族,清朝", "Military,Politics,Manchu,Qing",
     "后金（清朝前身）的创建者，统一了女真各部，为清朝入主中原奠定了基础。",
     "Founder of the Later Jin (precursor to the Qing dynasty) who unified the Jurchen tribes, laying the foundation for the Qing conquest of China."),
    ("zhang-heng", "张衡", "Zhang Heng", 78, 139, "china", "科学,天文学,地震学,汉朝", "Science,Astronomy,Seismology,Han",
     "东汉科学家和文学家，发明了世界上第一台地动仪，精确测量了天文数据。",
     "Eastern Han scientist and writer who invented the world's first seismoscope and made precise astronomical measurements."),
    ("sima-qian", "司马迁", "Sima Qian", -145, -86, "china", "历史,文学,汉朝", "History,Literature,Han Dynasty",
     "西汉史学家，《史记》的作者，中国纪传体史书的开创者，被尊为'史家之祖'。",
     "Western Han historian and author of the 'Records of the Grand Historian,' founder of Chinese biographical historiography."),
    ("duoyuan", "道元", "Dogen", 1200, 1253, "japan", "宗教,佛教,禅宗", "Religion,Buddhism,Zen",
     "日本佛教曹洞宗的创始人，将中国禅宗传入日本，其著作《正法眼藏》是日本佛教哲学的巅峰。",
     "Founder of the Soto school of Japanese Zen Buddhism, who transmitted Chinese Chan to Japan; his 'Shobogenzo' is the summit of Japanese Buddhist philosophy."),
    ("sen-no-rikyu", "千利休", "Sen no Rikyu", 1522, 1591, "japan", "文化,茶道,美学", "Culture,Tea Ceremony,Aesthetics",
     "日本茶道大师，将茶道从社交仪式提升为以'和敬清寂'为核心的精神修行。",
     "Japanese tea master who elevated the tea ceremony from social ritual to spiritual practice centered on harmony, respect, purity, and tranquility."),
    ("hiroshige", "歌川广重", "Utagawa Hiroshige", 1797, 1858, "japan", "艺术,浮世绘", "Art,Ukiyo-e",
     "日本浮世绘画家，以风景画系列《东海道五十三次》等作品深刻影响了欧洲印象派。",
     "Japanese ukiyo-e artist whose landscape series 'Fifty-three Stations of the Tokaido' profoundly influenced European Impressionists."),
    ("kurosawa", "黑泽明", "Akira Kurosawa", 1910, 1998, "japan", "电影,导演", "Film,Director",
     "日本电影导演，《七武士》和《罗生门》的创作者，在国际上获得了极高的声望。",
     "Japanese film director and creator of 'Seven Samurai' and 'Rashomon,' who achieved unparalleled international prestige."),
    ("miyazaki", "宫崎骏", "Hayao Miyazaki", 1941, None, "japan", "动画,电影", "Animation,Film",
     "日本动画导演和吉卜力工作室的联合创始人，以《千与千寻》《龙猫》等作品享誉全球。",
     "Japanese animation director and co-founder of Studio Ghibli, celebrated worldwide for 'Spirited Away,' 'My Neighbor Totoro,' and more."),
    # Korean (5)
    ("king-sejong-new", "世宗大王", "King Sejong", 1397, 1450, "asia", "政治,语言,朝鲜", "Politics,Language,Korea",
     "朝鲜王朝第四代国王，创造了韩文（训民正音），是朝鲜历史上最受尊敬的君主。",
     "The fourth king of the Joseon Dynasty who created Hangul (the Korean alphabet), the most revered monarch in Korean history."),
    ("shin-saimdang", "申师任堂", "Shin Saimdang", 1504, 1551, "asia", "艺术,女性,朝鲜", "Art,Women,Korea",
     "朝鲜时期的女艺术家和诗人，被誉为'贤妻良母'的典范，出现在韩元纸币上。",
     "Joseon-era woman artist and poet, celebrated as the ideal of virtuous womanhood and featured on Korean banknotes."),
    ("yu-gwan-sun", "柳宽顺", "Yu Gwan-sun", 1902, 1920, "asia", "独立,女性,韩国", "Independence,Women,Korea",
     "韩国独立运动烈士，在日本殖民统治下组织了三一运动的学生示威，17岁在狱中殉国。",
     "Korean independence martyr who organized student demonstrations during the March 1st Movement under Japanese colonial rule, dying in prison at 17."),
    # India (5)
    ("rabindranath-tagore", "泰戈尔", "Rabindranath Tagore", 1861, 1941, "india", "文学,诗歌,音乐,诺贝尔", "Literature,Poetry,Music,Nobel",
     "印度诗人、作家和作曲家，《吉檀迦利》的作者，1913年获诺贝尔文学奖，首位获此殊荣的亚洲人。",
     "Indian poet, writer, and composer, author of 'Gitanjali,' first Asian to win the Nobel Prize in Literature in 1913."),
    ("swami-vivekananda", "辨喜", "Swami Vivekananda", 1863, 1902, "india", "宗教,哲学,吠檀多", "Religion,Philosophy,Vedanta",
     "印度教僧侣和哲学家，将吠檀多哲学和瑜伽引入西方世界，1893年在芝加哥世界宗教议会上发表了著名演讲。",
     "Hindu monk and philosopher who introduced Vedanta and yoga to the West, delivering his famous speech at the 1893 Parliament of World Religions in Chicago."),
    ("apj-abdul-kalam", "卡拉姆", "A.P.J. Abdul Kalam", 1931, 2015, "india", "科学,政治,印度,导弹", "Science,Politics,India,Missile",
     "印度科学家和总统，印度导弹计划之父，被尊为'人民总统'。",
     "Indian scientist and president, father of India's missile program, revered as the 'People's President.'"),
    ("cv-raman", "拉曼", "C.V. Raman", 1888, 1970, "india", "科学,物理,诺贝尔", "Science,Physics,Nobel",
     "印度物理学家，因发现拉曼散射效应获1930年诺贝尔物理学奖，首位获此殊荣的亚洲科学家。",
     "Indian physicist who won the 1930 Nobel Prize in Physics for discovering the Raman effect, the first Asian scientist to receive the honor."),
    # SEA / More Asian (10)
    ("pol-pot", "波尔布特", "Pol Pot", 1925, 1998, "asia", "政治,柬埔寨,红色高棉", "Politics,Cambodia,Khmer Rouge",
     "柬埔寨共产党（红色高棉）领袖，其激进农业改革导致了柬埔寨约四分之一人口的死亡。",
     "Leader of the Communist Party of Kampuchea (Khmer Rouge), whose radical agrarian reforms caused the deaths of roughly a quarter of Cambodia's population."),
    ("thant-u", "吴丹", "U Thant", 1909, 1974, "asia", "外交,联合国,缅甸", "Diplomacy,UN,Myanmar",
     "缅甸外交官，联合国第三任秘书长，古巴导弹危机期间发挥了关键的调解作用。",
     "Burmese diplomat and third UN Secretary-General, who played a crucial mediating role during the Cuban Missile Crisis."),
    ("mahatir", "马哈蒂尔", "Mahathir Mohamad", 1925, None, "asia", "政治,马来西亚,现代化", "Politics,Malaysia,Modernization",
     "马来西亚任期最长的首相，'马来西亚现代化之父'，将农业国转变为工业强国。",
     "Malaysia's longest-serving prime minister and 'Father of Modernization,' who transformed an agricultural nation into an industrial powerhouse."),
    ("aquino", "阿基诺夫人", "Corazon Aquino", 1933, 2009, "asia", "政治,女性,菲律宾,民主", "Politics,Women,Philippines,Democracy",
     "菲律宾首位女总统，领导了人民力量革命推翻马科斯独裁，恢复了菲律宾民主。",
     "The Philippines' first female president, who led the People Power Revolution to overthrow the Marcos dictatorship and restore democracy."),
    # Middle East (10)
    ("rumi", "鲁米", "Rumi (Jalal ad-Din)", 1207, 1273, "middle-east", "诗歌,苏菲主义,波斯", "Poetry,Sufism,Persia",
     "波斯诗人和苏菲派神秘主义者，其灵性诗歌跨越了文化和宗教的界限，是美国最畅销的诗人之一。",
     "Persian poet and Sufi mystic whose spiritual poetry transcends cultural and religious boundaries, one of the best-selling poets in America."),
    ("ibn-al-haytham", "伊本·海赛姆", "Ibn al-Haytham (Alhazen)", 965, 1040, "middle-east", "科学,光学,数学", "Science,Optics,Mathematics",
     "阿拉伯科学家，光学之父，第一个正确解释视觉原理的人，其科学方法论预示了现代实验科学。",
     "Arab scientist and father of optics, the first to correctly explain the principles of vision, whose scientific methodology foreshadowed modern experimental science."),
    ("al-ghazali", "安萨里", "Al-Ghazali", 1058, 1111, "middle-east", "哲学,神学,苏菲", "Philosophy,Theology,Sufism",
     "伊斯兰教最伟大的神学家和哲学家之一，《宗教科学的复兴》的作者，调和了伊斯兰正统与苏菲神秘主义。",
     "One of Islam's greatest theologians and philosophers, author of 'The Revival of the Religious Sciences,' who reconciled Islamic orthodoxy with Sufi mysticism."),
    ("mimar-sinan", "锡南", "Mimar Sinan", 1489, 1588, "middle-east", "建筑,奥斯曼", "Architecture,Ottoman",
     "奥斯曼帝国最伟大的建筑师，设计了超过三百座建筑，包括伊斯坦布尔的苏莱曼尼耶清真寺。",
     "The greatest architect of the Ottoman Empire, who designed over 300 buildings including Istanbul's Suleymaniye Mosque."),
    ("khomeini", "霍梅尼", "Ruhollah Khomeini", 1902, 1989, "middle-east", "宗教,政治,伊朗,伊斯兰革命", "Religion,Politics,Iran,Islamic Revolution",
     "伊朗什叶派领袖和伊斯兰革命的领导者，建立了伊朗伊斯兰共和国。",
     "Iranian Shiite leader and architect of the Islamic Revolution who established the Islamic Republic of Iran."),
    # European / Russian more (30)
    ("pushkin", "普希金", "Alexander Pushkin", 1799, 1837, "europe", "文学,诗歌,俄罗斯", "Literature,Poetry,Russia",
     "俄罗斯最伟大的诗人和现代俄罗斯文学的奠基人，《叶甫盖尼·奥涅金》的作者。",
     "Russia's greatest poet and founder of modern Russian literature, author of 'Eugene Onegin.'"),
    ("chekhov", "契诃夫", "Anton Chekhov", 1860, 1904, "europe", "文学,戏剧,短篇小说,俄罗斯", "Literature,Drama,Short Story,Russia",
     "俄国短篇小说家和剧作家，《樱桃园》《万尼亚舅舅》的作者，现代短篇小说的革新者。",
     "Russian short story writer and playwright, author of 'The Cherry Orchard' and 'Uncle Vanya,' a revolutionary of the modern short story."),
    ("tesla-nikola", "尼古拉·特斯拉", "Nikola Tesla", 1856, 1943, "europe", "发明,电力,交流电", "Invention,Electricity,AC Power",
     "塞尔维亚裔美国发明家，交流电、无线电和无数专利的创造者，其天才远见超越了时代。",
     "Serbian-American inventor and creator of AC power, radio technology, and countless patents, whose visionary genius was ahead of his time."),
    ("voltaire", "伏尔泰", "Voltaire", 1694, 1778, "europe", "哲学,文学,启蒙运动,法国", "Philosophy,Literature,Enlightenment,France",
     "法国启蒙思想家、作家和哲学家，以对言论自由、宗教宽容和理性主义的尖锐倡导著称。",
     "French Enlightenment thinker, writer, and philosopher celebrated for his sharp advocacy of free speech, religious tolerance, and rationalism."),
    ("descartes", "笛卡尔", "Rene Descartes", 1596, 1650, "europe", "哲学,数学,理性主义", "Philosophy,Mathematics,Rationalism",
     "法国哲学家和数学家，'我思故我在'的提出者，将代数与几何结合开创了解析几何。",
     "French philosopher and mathematician, originator of 'I think, therefore I am,' who united algebra with geometry to create analytical geometry."),
    ("pascal", "帕斯卡", "Blaise Pascal", 1623, 1662, "europe", "数学,物理,哲学,法国", "Mathematics,Physics,Philosophy,France",
     "法国数学家、物理学家和宗教哲学家，概率论的创始人之一，发明了最早的机械计算器。",
     "French mathematician, physicist, and religious philosopher, co-founder of probability theory and inventor of the earliest mechanical calculator."),
    ("leibniz", "莱布尼茨", "Gottfried Wilhelm Leibniz", 1646, 1716, "europe", "哲学,数学,科学", "Philosophy,Mathematics,Science",
     "德国哲学家和数学家，与牛顿各自独立发明了微积分，提出了'单子论'的形而上学体系。",
     "German philosopher and mathematician who independently co-invented calculus with Newton and proposed a metaphysical system of 'monads.'"),
    ("caravaggio", "卡拉瓦乔", "Caravaggio", 1571, 1610, "renaissance-europe", "艺术,绘画,巴洛克", "Art,Painting,Baroque",
     "意大利巴洛克画家，以戏剧性的明暗对比和现实主义风格革新了欧洲绘画。",
     "Italian Baroque painter who revolutionized European painting through dramatic chiaroscuro and gritty realism."),
    ("hokusai", "葛饰北斋", "Katsushika Hokusai", 1760, 1849, "japan", "艺术,浮世绘", "Art,Ukiyo-e",
     "日本浮世绘画家，《神奈川冲浪里》的创作者，其作品是全世界最知名的日本艺术形象。",
     "Japanese ukiyo-e artist and creator of 'The Great Wave off Kanagawa,' the most recognizable image of Japanese art worldwide."),
    ("verdi", "威尔第", "Giuseppe Verdi", 1813, 1901, "europe", "音乐,歌剧,意大利", "Music,Opera,Italy",
     "意大利歌剧作曲家，《弄臣》《茶花女》《阿依达》的创作者，意大利统一运动的文化象征。",
     "Italian opera composer of 'Rigoletto,' 'La Traviata,' and 'Aida,' a cultural symbol of Italian unification."),
    ("wagner", "瓦格纳", "Richard Wagner", 1813, 1883, "europe", "音乐,歌剧,德国", "Music,Opera,Germany",
     "德国作曲家，以'乐剧'革新了歌剧艺术，《尼伯龙根的指环》是音乐史上最宏大的作品之一。",
     "German composer who revolutionized opera with his 'music dramas'; 'The Ring of the Nibelung' is one of music history's most monumental works."),
    ("schopenhauer", "叔本华", "Arthur Schopenhauer", 1788, 1860, "europe", "哲学,悲观主义", "Philosophy,Pessimism",
     "德国哲学家，以激进的悲观主义和对意志的形而上学著称，深刻影响了尼采和瓦格纳。",
     "German philosopher known for his radical pessimism and metaphysics of the will, profoundly influencing Nietzsche and Wagner."),
    # Scientists (15)
    ("mendeleev", "门捷列夫", "Dmitri Mendeleev", 1834, 1907, "europe", "科学,化学,元素周期表", "Science,Chemistry,Periodic Table",
     "俄国化学家，元素周期表的创立者，准确预言了当时未知元素的性质。",
     "Russian chemist and creator of the periodic table, who accurately predicted the properties of then-unknown elements."),
    ("linnaeus", "林奈", "Carl Linnaeus", 1707, 1778, "europe", "科学,生物学,分类学", "Science,Biology,Taxonomy",
     "瑞典植物学家，现代生物分类学之父，确立了物种命名的双名法体系。",
     "Swedish botanist and father of modern taxonomy, who established the binomial nomenclature system for naming species."),
    ("boyle", "波义耳", "Robert Boyle", 1627, 1691, "england", "科学,化学,物理", "Science,Chemistry,Physics",
     "爱尔兰自然哲学家，现代化学的奠基人之一，波义耳定律的发现者。",
     "Irish natural philosopher and one of the founders of modern chemistry, discoverer of Boyle's Law."),
    ("crick-and-watson", "沃森和克里克", "Watson and Crick", 1916, 2004, "england", "科学,DNA,分子生物学", "Science,DNA,Molecular Biology",
     "弗朗西斯·克里克与詹姆斯·沃森共同发现了DNA的双螺旋结构，开启了分子生物学时代。",
     "Francis Crick and James Watson co-discovered the double helix structure of DNA, ushering in the era of molecular biology."),
    ("feynman-richard", "理查德·费曼", "Richard Feynman", 1918, 1988, "americas", "科学,物理,量子电动力学,诺贝尔", "Science,Physics,QED,Nobel",
     "美国理论物理学家，量子电动力学的创建者之一，以卓越的教学能力和费曼图闻名。",
     "American theoretical physicist, co-creator of quantum electrodynamics, celebrated for his brilliant teaching and Feynman diagrams."),
    ("hawking-stephen", "霍金", "Stephen Hawking", 1942, 2018, "england", "科学,物理,宇宙学,黑洞", "Science,Physics,Cosmology,Black Holes",
     "英国理论物理学家，《时间简史》的作者，提出霍金辐射理论，在渐冻人症中坚持科研五十余年。",
     "British theoretical physicist and author of 'A Brief History of Time,' who proposed Hawking radiation and pursued science for over 50 years with ALS."),
    # 20th C / Misc (20)
    ("jobs-steve", "史蒂夫·乔布斯", "Steve Jobs", 1955, 2011, "americas", "科技,企业家,苹果", "Technology,Entrepreneur,Apple",
     "美国企业家，苹果公司联合创始人，以Mac、iPhone和iPad深刻改变了个人计算和移动通信。",
     "American entrepreneur and Apple co-founder who profoundly transformed personal computing and mobile communication with the Mac, iPhone, and iPad."),
    ("gates-bill", "比尔·盖茨", "Bill Gates", 1955, None, "americas", "科技,企业家,微软,慈善", "Technology,Entrepreneur,Microsoft,Philanthropy",
     "美国企业家，微软联合创始人，长期位居世界首富，后转为全球最大慈善家之一。",
     "American entrepreneur and Microsoft co-founder, long the world's richest person, later one of the world's largest philanthropists."),
    ("malala", "马拉拉", "Malala Yousafzai", 1997, None, "asia", "教育,女性,人权,诺贝尔", "Education,Women,Human Rights,Nobel",
     "巴基斯坦女性教育活动家，最年轻的诺贝尔和平奖得主，15岁时遭塔利班枪击但奇迹生还。",
     "Pakistani female education activist and the youngest Nobel Peace Prize laureate, who survived a Taliban assassination attempt at age 15."),
    ("greta-thunberg", "通贝里", "Greta Thunberg", 2003, None, "europe", "环境,气候,青年", "Environment,Climate,Youth",
     "瑞典气候活动家，发起了'周五为未来'的全球学校罢课运动，激励了数百万年轻人参与气候行动。",
     "Swedish climate activist who launched the 'Fridays for Future' global school strike movement, inspiring millions of young people to climate action."),
    # Extra quick fills (20) - more Chinese dynasties, western misc
    ("zhu-xi", "朱熹", "Zhu Xi", 1130, 1200, "song-dynasty", "哲学,理学,宋朝", "Philosophy,Neo-Confucianism,Song",
     "南宋哲学家，理学的集大成者，其注解的四书成为此后科举考试的标准。",
     "Southern Song philosopher and the great synthesizer of Neo-Confucianism, whose commentaries on the Four Books became the standard for imperial examinations."),
    ("qianlong", "乾隆帝", "Qianlong Emperor", 1711, 1799, "china", "政治,清朝", "Politics,Qing Dynasty",
     "清朝第六位皇帝，在位60年，将清朝推向鼎盛，编撰了《四库全书》。",
     "The sixth Qing emperor who reigned for 60 years, bringing the Qing to its zenith and commissioning the 'Complete Library of the Four Treasuries.'"),
    ("yuan-shikai", "袁世凯", "Yuan Shikai", 1859, 1916, "china", "政治,民国,北洋", "Politics,Republic,Beiyang",
     "清末北洋新军的缔造者，民国首任正式大总统，后短暂称帝失败。",
     "Creator of the Beiyang New Army in the late Qing, the first formal president of the Republic of China, who briefly and unsuccessfully declared himself emperor."),
    ("li-hongzhang", "李鸿章", "Li Hongzhang", 1823, 1901, "china", "政治,洋务运动,清朝", "Politics,Self-Strengthening,Qing",
     "清末重臣，洋务运动的核心人物，以与列强签订诸多不平等条约的'裱糊匠'身份知名。",
     "Key late Qing official and central figure of the Self-Strengthening Movement, known as the 'paperhanger' for signing numerous unequal treaties with foreign powers."),
    ("zhou-guoping", "周国平", "Zhou Guoping", 1945, None, "china", "哲学,文学,散文", "Philosophy,Literature,Essay",
     "中国当代哲学家和作家，以关于人生、灵魂和孤独的哲学散文广受欢迎。",
     "Contemporary Chinese philosopher and writer, widely read for his philosophical essays on life, the soul, and solitude."),
    ("lu-yao", "路遥", "Lu Yao", 1949, 1992, "china", "文学,小说", "Literature,Novel",
     "中国作家，《平凡的世界》的作者，以描绘改革开放初期农村青年的奋斗精神著称。",
     "Chinese writer and author of 'Ordinary World,' celebrated for depicting the struggling spirit of rural youth during the early reform era."),
    ("mozart-wolfgang", "莫扎特", "Wolfgang Amadeus Mozart", 1756, 1791, "europe", "音乐,古典,作曲", "Music,Classical,Composition",
     "奥地利作曲家，以惊人的天才在35年生命中创作了600余部作品，涵盖交响曲、歌剧和室内乐。",
     "Austrian composer who, with prodigious genius, created over 600 works in 35 years spanning symphonies, operas, and chamber music."),
    ("beethoven-ludwig", "贝多芬", "Ludwig van Beethoven", 1770, 1827, "europe", "音乐,古典,浪漫,作曲", "Music,Classical,Romantic,Composition",
     "德国作曲家，在逐渐失聪中创造了最具革命性的音乐，将古典音乐推向浪漫主义的门槛。",
     "German composer who, while progressively going deaf, created the most revolutionary music of his era, pushing classical music to the threshold of Romanticism."),
    ("rembrandt", "伦勃朗", "Rembrandt van Rijn", 1606, 1669, "europe", "艺术,绘画,荷兰,巴洛克", "Art,Painting,Dutch,Baroque",
     "荷兰黄金时代最伟大的画家，以对光影的戏剧性运用和对人性的深刻洞察著称。",
     "The greatest painter of the Dutch Golden Age, celebrated for his dramatic use of light and shadow and profound insight into human nature."),
    ("goya", "戈雅", "Francisco Goya", 1746, 1828, "europe", "艺术,绘画,西班牙", "Art,Painting,Spain",
     "西班牙画家，从宫廷画师转变为对战争和人性黑暗面的深刻描绘者，现代艺术的先驱。",
     "Spanish painter who transformed from court painter to a profound chronicler of war and human darkness, a pioneer of modern art."),
    ("degas", "德加", "Edgar Degas", 1834, 1917, "europe", "艺术,绘画,雕塑,印象派", "Art,Painting,Sculpture,Impressionism",
     "法国印象派画家和雕塑家，以芭蕾舞者和赛马为题材的动态构图闻名。",
     "French Impressionist painter and sculptor celebrated for his dynamic compositions of ballet dancers and racehorses."),
    ("stravinsky", "斯特拉文斯基", "Igor Stravinsky", 1882, 1971, "europe", "音乐,作曲,现代主义", "Music,Composition,Modernism",
     "俄罗斯作曲家，《春之祭》的创作者，其作品以革命性的节奏和和声改变了20世纪音乐。",
     "Russian composer and creator of 'The Rite of Spring,' whose revolutionary rhythms and harmonies transformed 20th-century music."),
    ("shostakovich", "肖斯塔科维奇", "Dmitri Shostakovich", 1906, 1975, "europe", "音乐,作曲,苏联", "Music,Composition,Soviet Union",
     "苏联作曲家，在斯大林的恐怖统治下创作了15部交响曲，以音乐隐晦地表达了对体制的反抗。",
     "Soviet composer who wrote 15 symphonies under Stalin's terror, using music to subtly encode resistance against the regime."),
    ("frank-lloyd-wright", "赖特", "Frank Lloyd Wright", 1867, 1959, "americas", "建筑,有机建筑,美国", "Architecture,Organic Architecture,USA",
     "美国建筑师，有机建筑理论的创始人，流水别墅和古根海姆博物馆的设计者。",
     "American architect and founder of organic architecture, designer of Fallingwater and the Guggenheim Museum."),
    ("chaplin", "卓别林", "Charlie Chaplin", 1889, 1977, "england", "电影,喜剧,默片", "Film,Comedy,Silent Film",
     "英国喜剧演员和电影导演，'流浪汉'形象的创造者，默片时代最伟大的电影艺术家。",
     "British comedian and film director, creator of 'The Tramp' character, the greatest artist of the silent film era."),
]

people = []
for item in data:
    (pid, name, nameEn, birth, death, rid, tags_str, tagsEn_str, summary, summaryEn) = item[:10]
    wikidata = item[10] if len(item) > 10 else ""
    if death is None:
        death_str = 'undefined'
    else:
        death_str = str(death)
    
    people.append({
        "id": pid, "name": name, "nameEn": nameEn,
        "birthYear": birth, "deathYear": death,
        "deathYearStr": death_str,
        "regionId": rid,
        "tags": [t.strip() for t in tags_str.split(",")],
        "tagsEn": [t.strip() for t in tagsEn_str.split(",")],
        "summary": summary, "summaryEn": summaryEn,
        "description": summary, "descriptionEn": summaryEn,
        "alternativeNames": [],
        "sourceIds": [],
        "wikidataQid": wikidata,
        "dataStatus": "published",
        "confidenceScore": 0.9,
        "externalReferences": []
    })

print(f"// Total generated: {len(people)} people", file=sys.stderr)

lines = []
for person in people:
    l = []
    l.append("  // --- %s ---" % person["nameEn"])
    l.append("  {")
    l.append("    id: '%s'," % esc(person["id"]))
    l.append("    name: '%s'," % esc(person["name"]))
    l.append("    nameEn: '%s'," % esc(person["nameEn"]))
    l.append("    birthYear: %s," % person["birthYear"])
    l.append("    deathYear: %s," % person["deathYearStr"])
    l.append("    regionId: '%s'," % person["regionId"])
    alt = ", ".join("'%s'" % esc(a) for a in person["alternativeNames"])
    l.append("    alternativeNames: [%s]," % alt)
    tags = ", ".join("'%s'" % esc(t) for t in person["tags"])
    l.append("    tags: [%s]," % tags)
    tagsEn = ", ".join("'%s'" % esc(t) for t in person["tagsEn"])
    l.append("    tagsEn: [%s]," % tagsEn)
    l.append("    summary: '%s'," % esc(person["summary"]))
    l.append("    summaryEn: '%s'," % esc(person["summaryEn"]))
    l.append("    description: '%s'," % esc(person["description"]))
    l.append("    descriptionEn: '%s'," % esc(person["descriptionEn"]))
    l.append("    sourceIds: [],")
    l.append("    occupations: [],")
    l.append("    birthDatePrecision: 'year' as const,")
    l.append("    deathDatePrecision: 'year' as const,")
    l.append("    dataStatus: '%s' as const," % person["dataStatus"])
    l.append("    confidenceScore: %s," % person["confidenceScore"])
    l.append("    externalReferences: [],")
    if person["wikidataQid"]:
        l.append("    wikidataQid: '%s'," % person["wikidataQid"])
    l.append("  },")
    lines.append("\n".join(l))

print("\n\n".join(lines))
print("\n// Total: %d new people" % len(people))
