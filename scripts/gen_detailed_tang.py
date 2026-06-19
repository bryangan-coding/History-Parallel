#!/usr/bin/env python3
"""Generate detailed events for Tang dynasty figures."""
import json, os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'data', 'events')
os.makedirs(OUTPUT_DIR, exist_ok=True)

all_events = []

def add(id, title, titleEn, startYear, endYear=None, importance=3,
        summary='', summaryEn='', desc='', descEn='', tags=None, tagsEn=None,
        personIds=None, regionId='', sourceIds=None, isApprox=False,
        placeName=None, placeNameEn=None, coords=None):
    all_events.append({
        'id': id, 'title': title, 'titleEn': titleEn,
        'startYear': startYear, 'endYear': endYear,
        'importance': importance,
        'summary': summary, 'summaryEn': summaryEn,
        'description': desc if desc else summary,
        'descriptionEn': descEn if descEn else summaryEn,
        'tags': tags or [], 'tagsEn': tagsEn or [],
        'personIds': personIds or [], 'regionId': regionId,
        'sourceIds': sourceIds or [], 'relatedEventIds': [],
        'datePrecision': 'year', 'isApproximate': isApprox,
        'dataStatus': 'published', 'confidenceScore': 0.85,
        'externalReferences': [],
        'placeName': placeName, 'placeNameEn': placeNameEn,
        'coordinates': coords,
    })

# ==================== TANG DYNASTY ====================

# Tang Gaozu (566-635)
add('evt-gaozu-revolt', '李渊太原起兵', 'Li Yuan Raises Army at Taiyuan', 617, importance=5,
    summary='隋末天下大乱，太原留守李渊在次子李世民的极力劝说下起兵反隋，打出「尊隋讨贼」旗号。',
    summaryEn='Amid the Sui collapse, Li Yuan raised an army at Li Shimin\'s urging, under the banner of \'honoring Sui, punishing rebels.\'',
    tags=['军事', '起兵', '唐朝'], tagsEn=['Military', 'Uprising', 'Tang Dynasty'],
    personIds=['tang-gaozu', 'tang-taizong'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='太原', placeNameEn='Taiyuan', coords={'lat': 37.8, 'lng': 112.5})

add('evt-gaozu-found', '李渊建立唐朝', 'Founding of Tang Dynasty', 618, importance=5,
    summary='李渊接受隋恭帝禅让，在长安称帝建立唐朝，年号武德。',
    summaryEn='Li Yuan accepted the abdication of the last Sui emperor and proclaimed the Tang dynasty at Chang\'an.',
    tags=['政治', '建国', '唐朝'], tagsEn=['Politics', 'Founding', 'Tang Dynasty'],
    personIds=['tang-gaozu'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

add('evt-gaozu-abdicate', '玄武门之变与李渊退位', 'Xuanwu Gate Incident & Abdication', 626, importance=5,
    summary='玄武门之变后李渊被迫退位为太上皇，李世民即位。',
    summaryEn='After the Xuanwu Gate Incident, Li Yuan was forced to abdicate and became Retired Emperor.',
    tags=['政治', '政变', '唐朝'], tagsEn=['Politics', 'Coup', 'Tang Dynasty'],
    personIds=['tang-gaozu', 'tang-taizong'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Tang Gaozong (628-683)
add('evt-gaozong-ascend', '唐高宗即位', 'Emperor Gaozong Ascends the Throne', 649, importance=4,
    summary='太宗驾崩后第九子李治即位，在长孙无忌等大臣辅佐下前期颇有作为。',
    summaryEn='After Taizong\'s death, Li Zhi ascended as Emperor Gaozong, achieving much under Zhangsun Wuji\'s guidance.',
    tags=['政治', '即位', '唐朝'], tagsEn=['Politics', 'Enthronement', 'Tang Dynasty'],
    personIds=['tang-gaozong'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

add('evt-gaozong-expand', '唐朝疆域达到极盛', 'Tang Territory at Greatest Extent', 657, 668, importance=5,
    summary='高宗时期灭西突厥、百济和高句丽，唐朝疆域东至朝鲜半岛、西达咸海。',
    summaryEn='Tang destroyed Western Turks, Baekje, and Goguryeo, reaching its greatest territorial extent.',
    tags=['军事', '扩张', '唐朝'], tagsEn=['Military', 'Expansion', 'Tang Dynasty'],
    personIds=['tang-gaozong'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

add('evt-gaozong-wu', '武则天立后与二圣临朝', 'Wu Zetian Becomes Empress', 655, importance=5,
    summary='李治不顾长孙无忌等重臣反对将武则天立为皇后。660年后高宗风疾无法理政，武则天逐渐掌权并称「二圣」。',
    summaryEn='Li Zhi made Wu Zetian empress despite fierce opposition. After his stroke in 660, Wu gradually took control.',
    tags=['政治', '唐朝'], tagsEn=['Politics', 'Tang Dynasty'],
    personIds=['tang-gaozong', 'wu-zetian'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Tang Xuanzong (685-762)
add('evt-xuanzong-coup', '唐隆政变与先天政变', 'Xuanzong\'s Two Coups', 710, 713, importance=5,
    summary='李隆基先后发动唐隆政变和先天政变，铲除韦后和太平公主集团，真正掌握大权。',
    summaryEn='Li Longji launched two coups, eliminating Empress Wei and Princess Taiping\'s factions to seize power.',
    tags=['政治', '政变', '唐朝'], tagsEn=['Politics', 'Coup', 'Tang Dynasty'],
    personIds=['tang-xuanzong'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

add('evt-xuanzong-kaiyuan', '开元盛世', 'Kaiyuan Golden Age', 713, 741, importance=5,
    summary='开元年间玄宗任用姚崇、宋璟等贤相，唐朝达到全盛——长安是世界第一大都市，人口达到五千万。',
    summaryEn='Under wise ministers Yao Chong and Song Jing, Tang reached its zenith — Chang\'an was the world\'s largest city.',
    tags=['政治', '盛世', '唐朝'], tagsEn=['Politics', 'Golden Age', 'Tang Dynasty'],
    personIds=['tang-xuanzong'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

add('evt-xuanzong-anshi', '安史之乱爆发', 'An Lushan Rebellion Erupts', 755, importance=5,
    summary='755年安禄山在范阳起兵叛乱，唐朝由盛转衰的转折点。玄宗被迫逃往四川。',
    summaryEn='In 755, An Lushan rebelled at Fanyang — the turning point from Tang\'s peak to its decline.',
    tags=['战争', '叛乱', '唐朝'], tagsEn=['War', 'Rebellion', 'Tang Dynasty'],
    personIds=['tang-xuanzong', 'an-lushan'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安至成都', placeNameEn='Chang\'an to Chengdu', coords={'lat': 34.3, 'lng': 108.9})

add('evt-xuanzong-mawei', '马嵬坡兵变', 'Mawei Post Mutiny', 756, importance=5,
    summary='逃难途中禁军哗变，杨国忠被杀，玄宗被迫赐死杨贵妃。白居易《长恨歌》即以此为题材。',
    summaryEn='The Imperial Guard mutinied — Yang Guozhong killed, Yang Guifei strangled. Immortalized in Bai Juyi\'s \'Song of Everlasting Sorrow.\'',
    tags=['政治', '兵变', '唐朝'], tagsEn=['Politics', 'Mutiny', 'Tang Dynasty'],
    personIds=['tang-xuanzong', 'yang-guifei'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='马嵬驿（今陕西兴平）', placeNameEn='Mawei Post, Shaanxi', coords={'lat': 34.3, 'lng': 108.5})

# Tang Xianzong (778-820)
add('evt-xianzong-ascend', '唐宪宗即位决心削藩', 'Emperor Xianzong Ascends', 805, importance=4,
    summary='李纯即位为唐宪宗，面对藩镇割据的严峻局面，决心以武力削藩。',
    summaryEn='Li Chun ascended as Emperor Xianzong, determined to subdue autonomous provinces by force.',
    tags=['政治', '即位', '唐朝'], tagsEn=['Politics', 'Enthronement', 'Tang Dynasty'],
    personIds=['tang-xianzong'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

add('evt-xianzong-caizhou', '雪夜入蔡州', 'Snowy Night Raid on Caizhou', 817, importance=5,
    summary='李愬雪夜奇袭蔡州，生擒淮西节度使吴元济，是中国军事史上最著名的奇袭战例之一。',
    summaryEn='Li Su\'s surprise night raid captured Wu Yuanji alive — one of history\'s most famous surprise attacks.',
    tags=['军事', '削藩', '唐朝'], tagsEn=['Military', 'Anti-Warlord', 'Tang Dynasty'],
    personIds=['tang-xianzong', 'li-su'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='蔡州（今河南汝南）', placeNameEn='Caizhou, Henan', coords={'lat': 33.0, 'lng': 114.3})

add('evt-xianzong-yuanhe', '元和中兴', 'Yuanhe Restoration', 819, importance=4,
    summary='到819年全国藩镇表面上全部听命于中央，史称「元和中兴」。',
    summaryEn='By 819, all provinces nominally submitted to the center — the Yuanhe Restoration.',
    tags=['政治', '中兴', '唐朝'], tagsEn=['Politics', 'Restoration', 'Tang Dynasty'],
    personIds=['tang-xianzong'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Sun Simiao (541-682)
add('evt-sunsimiao-work', '孙思邈著《千金要方》', 'Essential Formulas Worth a Thousand Gold', 652, importance=5,
    summary='药王孙思邈完成医学巨著《备急千金要方》30卷，系统总结唐代以前的医学成就。',
    summaryEn='The King of Medicine completed his 30-volume masterpiece, systematically summarizing pre-Tang medical knowledge.',
    tags=['医学', '著作', '唐朝'], tagsEn=['Medicine', 'Scholarship', 'Tang Dynasty'],
    personIds=['sun-simiao'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='终南山', placeNameEn='Zhongnan Mountains', coords={'lat': 34.0, 'lng': 108.9})

# Li Jing (571-649)
add('evt-lijing-turk', '李靖灭东突厥', 'Li Jing Destroys Eastern Turks', 630, importance=5,
    summary='李靖率三千精骑夜袭阴山，一举擒获颉利可汗，灭亡东突厥。',
    summaryEn='Li Jing led 3,000 cavalry in a night raid, capturing the Illig Qaghan and destroying the Eastern Turkic Khaganate.',
    tags=['军事', '对外战争', '唐朝'], tagsEn=['Military', 'Foreign War', 'Tang Dynasty'],
    personIds=['li-jing'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='阴山', placeNameEn='Yin Mountains', coords={'lat': 41.0, 'lng': 110.0})

# Fang Xuanling (579-648)
add('evt-fang-du', '房谋杜断——贞观之治的设计师', 'Fang Xuanling: Architect of Zhenguan', 626, 648, importance=4,
    summary='房玄龄与杜如晦并称「房谋杜断」，任宰相二十余年，是贞观之治的核心设计师。',
    summaryEn='Fang Xuanling and Du Ruhui were the chief architects of the Zhenguan Reign, with Fang serving as chancellor for over 20 years.',
    tags=['政治', '宰相', '唐朝'], tagsEn=['Politics', 'Chancellor', 'Tang Dynasty'],
    personIds=['fang-xuanling', 'du-ruhui'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Du Ruhui (585-630)
add('evt-duruhui-chancellor', '杜如晦任相', 'Du Ruhui as Chancellor', 627, 630, importance=4,
    summary='杜如晦以果断善断著称，与房玄龄配合默契，可惜英年早逝。',
    summaryEn='Du Ruhui, famed for decisiveness alongside Fang Xuanling, died young in 630.',
    tags=['政治', '宰相', '唐朝'], tagsEn=['Politics', 'Chancellor', 'Tang Dynasty'],
    personIds=['du-ruhui', 'fang-xuanling'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Di Renjie (630-700)
add('evt-direnjie-wu', '狄仁杰劝谏武则天', 'Di Renjie Advises Wu Zetian', 690, 700, importance=4,
    summary='狄仁杰在武则天朝任宰相，以智慧和勇气劝谏武则天，为恢复李唐江山奠定基础。',
    summaryEn='Di Renjie served as chancellor under Wu Zetian, subtly persuading her to return power to the Li family.',
    tags=['政治', '唐朝'], tagsEn=['Politics', 'Tang Dynasty'],
    personIds=['di-renjie'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='洛阳', placeNameEn='Luoyang', coords={'lat': 34.6, 'lng': 112.4})

# Huineng (638-713)
add('evt-huineng-verse', '慧能作偈得传衣钵', 'Huineng\'s Verse Wins the Patriarch\'s Robe', 661, importance=5,
    summary='不识字的岭南樵夫慧能以「本来无一物，何处惹尘埃」的偈语，被五祖弘忍秘密传授禅宗衣钵。',
    summaryEn='The illiterate woodcutter Huineng won the Chan patriarch\'s robe with his verse on original emptiness.',
    tags=['佛教', '禅宗', '唐朝'], tagsEn=['Buddhism', 'Chan', 'Tang Dynasty'],
    personIds=['huineng'], regionId='tang-dynasty',
    sourceIds=['src-tanjing'], placeName='黄梅', placeNameEn='Huangmei', coords={'lat': 30.1, 'lng': 115.9})

add('evt-huineng-teach', '慧能开坛说法开创南宗禅', 'Huineng Founds Southern Chan School', 676, importance=5,
    summary='慧能隐居十五年后在广州法性寺正式开坛说法，「直指人心，见性成佛」使禅宗彻底中国化。',
    summaryEn='After 15 years in hiding, Huineng began teaching, making Chan Buddhism thoroughly Chinese.',
    tags=['佛教', '禅宗', '唐朝'], tagsEn=['Buddhism', 'Chan', 'Tang Dynasty'],
    personIds=['huineng'], regionId='tang-dynasty',
    sourceIds=['src-tanjing'], placeName='广州法性寺', placeNameEn='Faxing Temple, Guangzhou', coords={'lat': 23.1, 'lng': 113.3})

# Luo Binwang (640-684)
add('evt-luobinwang-manifesto', '骆宾王写《讨武曌檄》', 'Manifesto Against Wu Zetian', 684, importance=5,
    summary='骆宾王为徐敬业起草讨伐武则天的檄文，武则天读后叹道「宰相安得失此人」。',
    summaryEn='Luo Binwang drafted the manifesto against Wu Zetian; Wu herself lamented losing such talent.',
    tags=['文学', '政治', '唐朝'], tagsEn=['Literature', 'Politics', 'Tang Dynasty'],
    personIds=['luo-binwang'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='扬州', placeNameEn='Yangzhou', coords={'lat': 32.4, 'lng': 119.4})

# Wang Bo (650-676)
add('evt-wangbo-tengwang', '王勃写《滕王阁序》', 'Preface to Prince Teng\'s Pavilion', 675, importance=5,
    summary='王勃在滕王阁宴会上即兴写下千古名篇，「落霞与孤鹜齐飞，秋水共长天一色」。',
    summaryEn='Wang Bo improvised the immortal Preface at a banquet, producing one of Chinese literature\'s greatest works.',
    tags=['文学', '唐朝'], tagsEn=['Literature', 'Tang Dynasty'],
    personIds=['wang-bo'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='南昌滕王阁', placeNameEn='Prince Teng\'s Pavilion, Nanchang', coords={'lat': 28.7, 'lng': 115.9})

# Zhang Xu (658-747)
add('evt-zhangxu-calligraphy', '张旭——草圣', 'Zhang Xu: Sage of Cursive Script', 700, 747, importance=4,
    summary='张旭被尊为「草圣」，嗜酒大醉后以头发蘸墨书写，与怀素并称「颠张醉素」。',
    summaryEn='Zhang Xu, the Sage of Cursive, often wrote when drunk, even dipping his hair in ink.',
    tags=['书法', '艺术', '唐朝'], tagsEn=['Calligraphy', 'Art', 'Tang Dynasty'],
    personIds=['zhang-xu'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Yi Xing (683-727)
add('evt-yixing-astronomy', '僧一行编制《大衍历》', 'Yi Xing Creates Dayan Calendar', 724, 727, importance=5,
    summary='僧一行主持大规模天文测量，实测子午线长度，编制《大衍历》，精度领先世界。',
    summaryEn='Yi Xing led a massive astronomical survey, measured the meridian arc, and created the Dayan Calendar.',
    tags=['科学', '天文学', '唐朝'], tagsEn=['Science', 'Astronomy', 'Tang Dynasty'],
    personIds=['yi-xing'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Wu Daozi (685-758)
add('evt-wudaozi-paint', '吴道子画嘉陵江三百里', 'Wu Daozi Paints the Jialing River', 742, importance=5,
    summary='唐玄宗命吴道子在大同殿画三百里嘉陵江山水，他一日而毕，被誉为「画圣」。',
    summaryEn='Wu Daozi painted the entire 300-li Jialing River landscape in a single day at Datong Hall.',
    tags=['绘画', '艺术', '唐朝'], tagsEn=['Painting', 'Art', 'Tang Dynasty'],
    personIds=['wu-daozi'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安大明宫', placeNameEn='Daming Palace, Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Wang Zhihuan (688-742)
add('evt-wangzhihuan-poem', '旗亭画壁——王之涣斗诗', 'Flag Pavilion Poetry Contest', 735, importance=4, isApprox=True,
    summary='王之涣、王昌龄、高适三人在旗亭听歌女唱诗斗高下，王之涣的《凉州词》最终折服全场。',
    summaryEn='Three great poets competed as courtesans sang their works — Wang Zhihuan\'s \'Liangzhou Song\' won the day.',
    tags=['文学', '诗歌', '唐朝'], tagsEn=['Literature', 'Poetry', 'Tang Dynasty'],
    personIds=['wang-zhihuan'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Meng Haoran (689-740)
add('evt-menghaoran-poetry', '孟浩然隐居鹿门山', 'Meng Haoran\'s Hermitage at Lumen Mountain', 711, 740, importance=4,
    summary='孟浩然终身布衣隐居鹿门山，开创盛唐山水田园诗派，与王维并称「王孟」。',
    summaryEn='Meng Haoran lived as a lifelong recluse, founding the Tang landscape poetry school with Wang Wei.',
    tags=['文学', '诗歌', '唐朝'], tagsEn=['Literature', 'Poetry', 'Tang Dynasty'],
    personIds=['meng-haoran'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='襄阳鹿门山', placeNameEn='Lumen Mountain, Xiangyang', coords={'lat': 32.0, 'lng': 112.1})

# Guo Ziyi (697-781)
add('evt-guozhiyi-anshi', '郭子仪平定安史之乱', 'Guo Ziyi Suppresses the An Lushan Rebellion', 756, 763, importance=5,
    summary='郭子仪是平定安史之乱的第一功臣，收复两京，功高盖世而能善终。',
    summaryEn='Guo Ziyi was the foremost hero in suppressing the rebellion, recovering both capitals.',
    tags=['军事', '唐朝'], tagsEn=['Military', 'Tang Dynasty'],
    personIds=['guo-ziyi'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Yan Zhenqing (709-785)
add('evt-yanzhenqing-calligraphy', '颜真卿——书法与忠烈', 'Yan Zhenqing: Calligrapher and Martyr', 785, importance=5,
    summary='颜真卿是中国书法史上最伟大的楷书大家之一，同时以忠烈殉国闻名。',
    summaryEn='Yan Zhenqing was one of the greatest regular script masters and a famous loyalist martyr.',
    tags=['书法', '忠烈', '唐朝'], tagsEn=['Calligraphy', 'Martyr', 'Tang Dynasty'],
    personIds=['yan-zhenqing'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Liu Zongyuan (773-819)
add('evt-liuzongyuan-exile', '柳宗元被贬永州', 'Liu Zongyuan Exiled to Yongzhou', 805, 815, importance=5,
    summary='柳宗元因参与永贞革新失败被贬永州十年，创作了《永州八记》等千古名篇。',
    summaryEn='Exiled to Yongzhou for ten years after the failed Yongzhen Reform, Liu wrote his immortal Eight Records.',
    tags=['文学', '贬谪', '唐朝'], tagsEn=['Literature', 'Exile', 'Tang Dynasty'],
    personIds=['liu-zongyuan'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='永州', placeNameEn='Yongzhou', coords={'lat': 26.4, 'lng': 111.6})

# Du Mu (803-852)
add('evt-dumu-poems', '杜牧的咏史诗', 'Du Mu\'s Historical Poems', 830, 852, importance=4,
    summary='杜牧以七言绝句咏史著称，与李商隐并称「小李杜」，《阿房宫赋》等成为千古名篇。',
    summaryEn='Du Mu was famed for his historical quatrains, paired with Li Shangyin as \'Little Li-Du\'.',
    tags=['文学', '诗歌', '唐朝'], tagsEn=['Literature', 'Poetry', 'Tang Dynasty'],
    personIds=['du-mu'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Li Shangyin (813-858)
add('evt-lishangyin-poems', '李商隐的无题诗', 'Li Shangyin\'s Untitled Poems', 835, 858, importance=4,
    summary='李商隐以无题诗闻名，「春蚕到死丝方尽，蜡炬成灰泪始干」等深情隐晦的名句传唱至今。',
    summaryEn='Li Shangyin\'s untitled love poems, veiled in passion, remain among the most moving Chinese verse.',
    tags=['文学', '诗歌', '唐朝'], tagsEn=['Literature', 'Poetry', 'Tang Dynasty'],
    personIds=['li-shangyin'], regionId='tang-dynasty',
    sourceIds=['src-jiutangshu'], placeName='长安', placeNameEn='Chang\'an', coords={'lat': 34.3, 'lng': 108.9})

# Write output
output_file = os.path.join(OUTPUT_DIR, '_detailedEvents_tang.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_events, f, ensure_ascii=False, indent=2)

print(f"Tang dynasty: {len(all_events)} detailed events written to {output_file}")
