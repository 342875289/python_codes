from bs4 import BeautifulSoup

html_doc = """
<head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <title>首页 - 简书</title>
</head>

<body class="output fluid zh cn win reader-day-mode reader-font2 " data-js-module="recommendation" data-locale="zh-CN">

<ul class="article-list thumbnails">

  <li class=have-img>
      <a class="wrap-img" href="/p/49c4728c3ab2"><img src="http://upload-images.jianshu.io/upload_images/2442470-745c6471c6f8258c.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/300/h/300" alt="300" /></a>
    <div>
      <p class="list-top">
        <a class="author-name blue-link" target="_blank" href="/users/0af6b163b687">阿随向前冲</a>
        <em>·</em>
        <span class="time" data-shared-at="2016-07-27T07:03:54+08:00"></span>
      </p>
      <h4 class="title"><a target="_blank" href="/p/49c4728c3ab2"> 只装了这六款软件，工作就高效到有时间逛某宝刷某圈</a></h4>
      <div class="list-footer">
        <a target="_blank" href="/p/49c4728c3ab2">
          阅读 1830
</a>        <a target="_blank" href="/p/49c4728c3ab2#comments">
           · 评论 35
</a>        <span> · 喜欢 95</span>
          <span> · 打赏 1</span>

      </div>
    </div>
  </li>
</ul>

</body>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# 查找所有有关的节点
tags = soup.find_all('a')

print(tags)
for tag in tags:
        image = tag.img['src']
        article_user = tag.p.a.get_text()
        article_user_url = tag.p.a['href']      
        created = tag.p.span['data-shared-at']        
        article_url = tag.h4.a['href']

        # 可以在查找的 tag 下继续使用 find_all()
        tag_span = tag.div.div.find_all('span')
        likes = tag_span[0].get_text(strip=True)
