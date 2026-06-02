#!/usr/bin/env python3
"""Add missing 唐宋八大家: 苏洵 & 苏辙, fix 韩愈 altNames."""
# We'll handle this with a quick Python script that patches mockData.ts

def esc(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")

entries = """  {
    id: 'su-xun',
    name: '苏洵',
    nameEn: 'Su Xun',
    birthYear: 1009,
    deathYear: 1066,
    regionId: 'song-dynasty',
    occupations: ['文学家', '政治家'],
    tags: ['文学家', '宋朝', '唐宋八大家'],
    tagsEn: ['Writer', 'Song Dynasty', 'Eight Great Prose Masters'],
    summary: '唐宋八大家之一，苏轼和苏辙的父亲，「二十七始发愤」的典范，《六国论》为千古名篇。',
    summaryEn: 'One of the Eight Great Prose Masters, father of Su Shi and Su Zhe; a model of late-blooming dedication whose "On the Six States" is an immortal essay.',
    description: '苏洵27岁才开始发愤读书——在宋代几乎所有人都从幼年开始准备科举的背景下，这是一个惊人的起步。他屡试不第后焚毁了自己的全部旧稿——从头开始钻研古文。他的文章雄辩凌厉——特别是《六国论》以六国赂秦而亡的历史教训暗讽北宋对辽夏的妥协政策。他与两个儿子苏轼、苏辙一同进京——欧阳修读到他们的文章后惊叹「后来文章当在此」。三苏同列唐宋八大家——是中国文学史上最耀眼的家族传奇。',
    descriptionEn: 'Su Xun only began serious study at 27 — a shockingly late start in a Song dynasty where almost everyone began exam preparation from childhood. After repeatedly failing the examinations, he burned all his earlier writings and started anew, immersing himself in classical prose. His essays are powerfully argumentative — particularly "On the Six States," which used the historical lesson of the six states bribing Qin into oblivion to satirize the Northern Song\'s appeasement of Liao and Western Xia. He traveled to the capital with his two sons, Su Shi and Su Zhe — Ouyang Xiu was so stunned by their writing that he declared "the future of literature lies here." All three Sus were canonized among the Eight Great Prose Masters — Chinese literary history\'s most dazzling family saga.',
    alternativeNames: ['苏明允', 'Su Mingyun', '老苏'],
    sourceIds: ['src-ss'],
    wikidataQid: '',
    dataStatus: 'published',
    confidenceScore: 0.9,
    externalReferences: [],
  },
  {
    id: 'su-zhe',
    name: '苏辙',
    nameEn: 'Su Zhe',
    birthYear: 1039,
    deathYear: 1112,
    regionId: 'song-dynasty',
    occupations: ['文学家', '政治家'],
    tags: ['文学家', '宋朝', '唐宋八大家'],
    tagsEn: ['Writer', 'Song Dynasty', 'Eight Great Prose Masters'],
    summary: '唐宋八大家之一，苏轼之弟，「三苏」中最沉静者，官至副宰相，其文汪洋澹泊。',
    summaryEn: 'One of the Eight Great Prose Masters, Su Shi\'s younger brother and the most restrained of the "Three Sus"; rose to vice chancellor, his prose vast yet tranquil.',
    description: '苏辙与哥哥苏轼同年考中进士——但两人的命运截然不同。苏轼张扬奔放一生大起大落，苏辙沉静内敛——在政治上比哥哥成功得多——官至门下侍郎（副宰相）。他在苏轼因「乌台诗案」被逮捕时上疏请求以自己的官职赎兄之罪——这篇奏疏以情感深沉著称。他的文章不像苏轼的汪洋恣肆——而是汪洋澹泊——苏轼评价弟弟「其文如其为人，故汪洋澹泊，有一唱三叹之声」。他的《黄州快哉亭记》是宋代散文的典范之作。',
    descriptionEn: 'Su Zhe passed the imperial examination the same year as his elder brother Su Shi — but their destinies diverged dramatically. Where Su Shi was flamboyant and lived a life of dramatic rises and falls, Su Zhe was restrained and introspective — far more successful politically — rising to Vice Director of the Chancellery (vice chancellor). When Su Shi was arrested in the Crow Terrace Poetry Case, Su Zhe submitted a memorial offering to trade his own official post for his brother\'s life — a document of profound emotional depth. His prose is not Su Shi\'s torrential brilliance but expansive yet tranquil — Su Shi assessed: "His writing is like his character — vast yet calm, with the lingering resonance of one who sings and sighs thrice." His "Record of the Pavilion of Joyful Travel at Huangzhou" is a model of Song prose.',
    alternativeNames: ['苏子由', 'Su Ziyou', '颍滨遗老', '小苏'],
    sourceIds: ['src-ss'],
    wikidataQid: '',
    dataStatus: 'published',
    confidenceScore: 0.9,
    externalReferences: [],
  },
"""

import re

TARGET = 'src/data/mockData.ts'
with open(TARGET) as f:
    content = f.read()

# Insert new entries before closing ]; of people array  
people_closing = content.find('];\n\n// ==================== EVENTS')
if people_closing < 0:
    people_closing = content.find('];\n\nexport const events:')

content = content[:people_closing] + '\n' + entries + '\n' + content[people_closing:]

# Fix 韩愈 altNames
content = content.replace(
    "  id: 'han-yu',\n    name: '韩愈',\n    nameEn: 'Han Yu',\n    birthYear: 768,\n    deathYear: 824,\n    regionId: 'tang-dynasty',\n    occupations: ['文学家'],\n    tags: ['文学家', '唐朝'],\n    tagsEn: ['Writer', 'Tang Dynasty'],\n    summary: '唐代古文运动倡导者，「文起八代之衰」，以《师说》《进学解》等名篇推动了中国散文的变革。',\n    summaryEn: 'Tang dynasty leader of the Classical Prose Movement who revived Chinese prose with masterpieces like \"On the Teacher\" and \"Explication of Progress in Learning.\"',\n    description: '韩愈是唐代最杰出的散文家之一。……',\n    descriptionEn: 'Han Yu was one of the most outstanding Tang prose masters.……',\n    alternativeNames: [],",
    "  id: 'han-yu',\n    name: '韩愈',\n    nameEn: 'Han Yu',\n    birthYear: 768,\n    deathYear: 824,\n    regionId: 'tang-dynasty',\n    occupations: ['文学家'],\n    tags: ['文学家', '唐朝', '唐宋八大家', '古文运动'],\n    tagsEn: ['Writer', 'Tang Dynasty', 'Eight Great Prose Masters', 'Classical Prose'],\n    summary: '唐代古文运动倡导者，「文起八代之衰」，以《师说》《进学解》等名篇推动了中国散文的变革。',\n    summaryEn: 'Tang dynasty leader of the Classical Prose Movement who revived Chinese prose with masterpieces like \"On the Teacher\" and \"Explication of Progress in Learning.\"',\n    description: '韩愈是唐代最杰出的散文家之一。……',\n    descriptionEn: 'Han Yu was one of the most outstanding Tang prose masters.……',\n    alternativeNames: ['韩退之', 'Han Tuizhi', '韩昌黎', '韩文公'],"
)

with open(TARGET, 'w') as f:
    f.write(content)

print("Done. Added 苏洵 + 苏辙, fixed 韩愈 tags and altNames.")
