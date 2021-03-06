# xinyuanshuo
“心愿说” 是一个在线分享心愿的网站。 
http://xinyuanshuo.sinaapp.com/

一、 项目背景
“心愿说” 是一款在线分享心愿网站。 本着许愿， 助人， 交友， 娱乐的目的，
用户可以分享自己的愿望，也可以选择帮别人实现心愿。
或许你的举手之劳，是我一直心之所向。

二 、 功能介绍

围绕用户的心愿， “心愿说”主要有发布心愿、帮别人实现心愿两大功能。
主要页面如下——

首页

首页介绍心愿说。
右上角的功能菜单可作注
册、登录以及导航操作。
一键回到顶部的设计让整
个界面更加友好。

心愿池

心愿池里有目前所有用户的心愿，分为代解决、正在进行中及已实现三
种。用户可以点击感兴趣的心愿查看详细情况。

心愿主页

用户可以在心愿主页了解心愿详
情，包括许愿人、许愿人承诺的报酬、
该心愿当前完成进度等等。
如果用户对当前他人心愿感兴趣，
可以点击“果断支持”按钮，帮助对方
实现愿望。每个愿望只能有一个人帮助
实现。
心愿主页下方有评论框，用户可以
用多种途径登陆留下评论，也可以匿名。

个人中心

从菜单栏可以进入个人中心。在个人中心，用户可以查看与自己相关的不同
进度的心愿。也可以查看帮别人实现的心愿。

许愿

心愿说最大的功能就是帮助用户发布愿望，等待别人的帮助从而实现。从菜
单栏和个人中心都可进入许愿板块。
在许愿版块里，用户留下自己的愿望，可以给帮自己实现愿望的人许下一个
诱人的报酬，并附上自己的联系方式。
心愿一旦上传成功，用户可以在心愿池及个人中心中查看实现进度。

留言板

在菜单栏中可以进入留言板。这里是分享心事的平台。你可以随便写下任何
想说的话，发布留言可以匿名。

三、技术实现

1 1 、前段框架： Amaze UI
Amaze UI 以移动优先（Mobile first）为理念，从小屏逐步扩展到大屏，
最终实现所有屏幕适配，适应移动互联潮流。
相比国外框架，Amaze UI 关注中文排版，根据用户代理调整字体，实现更
好的中文排版效果；兼顾国内主流浏览器及 App 内置浏览器兼容支持。
Amaze UI 面向 HTML5 开发，使用 CSS3 来做动画交互，平滑、高效，
更适合移动设备，让 Web 应用更快速载入。

2 2 、后台支持： tornado
Tornado 是 FriendFeed 使用的可扩展的非阻塞式 web 服务器及其相
关工具的开源版本。Tornado 和现在的主流 Web 服务器框架（包括大多数
Python 的框架）有着明显的区别：它是非阻塞式服务器，而且速度相当快。得
利于其 非阻塞的方式和对 epoll 的运用， Tornado 每秒可以处理数以千计的连
接，因此 Tornado 是实时 Web 服务的一个 理想框架。

3 3 、数据库： MySQL
MySQL 是最流行的关系型数据库管理系统，在 WEB 应用方面 MySQL 是最
好的 RDBMS(Relational Database Management System：关系数据库管理
系统)应用软件之一。MySQL 是一种关联数据库管理系统，关联数据库将数据保
存在不同的表中，而不是将所有数据放在一个大仓库内，这样就增加了速度并提
高了灵活性。 MySQL所使用的SQL语言是用于访问数据库的最常用标准化语言。


4 4 、搭载平台：新浪云平台
SAE 从架构上采用分层设计，从上往下分别为反向代理层、路由逻辑层、
Web 计算服务池。而从 Web 计算服务层延伸出 SAE 附属的分布式计算型服务
和分布式存储型服务，具体又分成同步计算型服务、异步计算型服务、持久化存
储服务、非持久化存储服务。比起其他公司正在规划和建设中的云平台，SAE
强大而成熟的云端服务能力使得新浪移动云具有明显优势。
