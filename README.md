# YouCore
基于 Python3 的 Youku 维护工具

# 最近更新

YouTools 拆分两部分进行测试，更新主要实现了：

1. 检测 Youtube 指定频道视频的更新
2. 检测 (中)英文字幕的更新
3. 将数据写进 Google Doc

使用时主要的改动：
1. 需要添加支持库 pygsheets： `pip3 install pygsheets`
2. config.py 增加了 SheetID 参数 以及 Google API Console 参数
3. 根目录中需要添加 `client_secret.json` 文件

## 需要的支持库

1. requests
2. you-get 
3. mkvmerge
4. pygsheets
4. proxychains(可选)

## 使用方式

1. 在[Google API Console](https://console.developers.google.com/)申请 API 以及 OAuth 证书，下载 `client_secret.json` 文件
2. 新建 Sheet，格式见链接××××
2. 将 Sheet ID 以及 API ID 填写入 config.py
4. 将 `client_secret.json` 文件置于根目录
3. 运行 YoutubeListener.py

## 注意事项

如果不需要翻墙，请在 YouCore.py 中 22 行

`cmd = 'proxychains you-get --itag=137 -o ' + dowload_path + ' \'' + url_video + '\''`

去掉 `proxychains`

`cmd = 'you-get --itag=137 -o ' + dowload_path + ' \'' + url_video + '\''`
