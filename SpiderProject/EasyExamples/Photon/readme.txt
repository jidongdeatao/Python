Photon是一种高效率的的网络爬虫，可从目标中提取URL，文件以及各类情报。其通过多线程大大加快数据提取进程。

项目地址：
https://github.com/s0md3v/Photon

数据提取
    默认情况下，Photon在抓取时会提取以下数据：
    网址（范围内和范围外的）
    带参数的网址（example.com/gallery.php?id=2）
    情报（电子邮件，社交媒体帐户，亚马逊水桶等）
    文件（pdf，png，xml等）
    JavaScript等文件
    基于自定义正则表达式模式的字符串
提取的信息按下图方式保存。
如何使用Photon高效率提取网站数据
智能多线程
大多数浮于互联网表面的工具都没有正确使用多线程，它们要么为线程提供一个项目列表，这会导致多个线程访问同一个项目，或者只是放置一个线程锁定并最终使多线程无效。
Ninja模式
在Ninja模式中，3个在线服务器用于代表你向目标发出请求。
所以基本上，现在你有4个客户端同时向同一个服务器发出请求，如果连接速度慢，那么可以提高速度，最大限度地降低连接重置的风险以及来自单个客户端的延迟请求。
这是Quark生成的比较图，其中的线代表线程：
如何使用Photon高效率提取网站数据
兼容性&依赖
兼容性
Photon目前全面兼容python2.x – 3.x，但因为这个项目正处于积极开发阶段，可能会需要python2.x不具备的功能。故开发者最终可能会放弃对python2.x的支持。
操作系统
Photon已经在Linux（Arch，Debian，Ubuntu），Termux，Windows（7&10）和Mac上进行了测试，并在所有系统上如期运行，如果你发现了任何bug，请在github上提交。
颜色
Mac和Windows不支持ANSI转义序列，因此所输出内容不会在Mac和Windows上显示颜色。
依赖
requests
urllib3
argparse
Photon所使用的其余python库是预装的python解释器的标准库。


如何使用Photon
语法: photon.py [选项]
  -u --url              目标url
  -l --level            抓取等级
  -t --threads          线程数
  -d --delay            请求间的延迟
  -c --cookie           cookie
  -r --regex            正则表达式模式
  -s --seeds            其他的子url
  -e --export           导出格式化结果
  -o --output           指定输出目录
  --exclude             通过正则表达式排除特定url
  --timeout             http 请求超时
  --ninja               ninja 模式
  --update              更新
  --dns                 转储dns数据
  --only-urls           仅提取url
  --user-agent          指定 user-agent(s)
仅抓取单个网站
选项 -u 或 –url，使用示例：
python photon.py -u "http://example.com"
抓取深度
选项 -l 或 –level，默认深度为2，使用示例：
python photon.py -u "http://example.com" -l 3
通过该选项，用户可以设置抓取的递归限制，例如，深度为2意思是Photon会从主页和子页。
线程数
选项 -t 或 –threads，默认线程数为2，使用示例：
python photon.py -u "http://example.com" -t 10
该选项可以对目标进行并发请求，-t选项可用于指定要进行的并发请求数量。值得注意的是，虽然多线程可以加速抓取，但是也可能会触发安全机制，此外，线程数过多，也有可能使小型网站宕机。
每个HTTP请求间的延迟
选项 -d 或 –delay，默认为0，使用示例：
python photon.py -u "http://example.com" -d 2
该选项可以指定每个HTTP（S）请求之间间隔的秒数。有效值是int，例如1表示1秒。
超时
选项 –timeout，默认为5，使用示例：
python photon.py -u "http://example.com --timeout=4
该选项指定HTTP（S）请求等待多长时间即为超时。
Cookies
选项 -c 或 –cookies，默认为 no cookie header is sent，使用示例：
python photon.py -u "http://example.com" -c "PHPSESSID=u5423d78fqbaju9a0qke25ca87"
该选项允许你在非ninja模式下为发出的每个HTTP请求添加Cookie header，主要用于目标网站需要基于Cookie验证的情形。
指定输出目录
选项 -o 或 –output，默认为 目标域名，使用示例：
python photon.py -u "http://example.com" -o "我的目录"
Photon将结果保存在以目标域名命名的目录中，但你可以使用此选项自定义目录。
排除特定url
选项 –exclude，使用示例：
python photon.py -u "http://example.com" --exclude="/blog/20[17|18]"
匹配指定正则表达式的网址将不会被抓取及显示在结果中。
指定子url
选项 -s 或 –seeds，使用示例：
python photon.py -u "http://example.com" --seeds "http://example.com/blog/2018,http://example.com/portals.html"
你可以使用此选项添加自定义子URL，要以逗号分隔。
指定user-agent(s)
选项 –user-agent，使用示例：
python photon.py -u "http://example.com" --user-agent "curl/7.35.0,Wget/1.15 (linux-gnu)"
你可以使用此选项使用自己的用户代理，以逗号分隔。此选项仅用于帮助用户在不修改默认user-agents.txt文件的情况下使用特定用户代理。
自定义正则表达式模式
选项 -r 或 –regex，使用示例：
python photon.py -u "http://example.com" --regex "\d{10}"
通过使用此选项指定正则表达式模式，可以在抓取期间提取字符串。
导出格式化结果
选项 -e 或 –export
通过 -e 选项，你可以指定要保存文件的输出格式，使用示例：
python photon.py -u "http://example.com" --export=json
目前支持的格式：json
跳过数据提取
选项： –only-urls，使用示例：
python photon.py -u "http://example.com" --only-urls
该选项会跳过提取js文件等数据，当你只需要抓取目标时，该选项可以派上用场。
更新
选项 –update，使用示例：
python photon.py --update
如果使用此选项，Photon会检查更新。如果有新的版本，Photon会下载并将更新文件合并到当前目录中，Photon不会覆盖其他文件。
Ninja模式
选项 –ninja
此选项启用Ninja模式。在该模式下，Photon会使用以下网站代表你发出请求。
    codebeautify.org
    photopea.com
    pixlr.com
转储DNS数据
选项 –dns，使用示例：
python photon.py -u http://example.com --dns
创建显示目标域名的DNS数据的图像。目前不支持目标是子域。
