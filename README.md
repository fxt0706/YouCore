# YouCore
基于 Python3 的 Youku 维护工具

## 需要的支持库

1. requests
2. you-get 
3. mkvmerge
4. proxychains(可选）

## 使用方式

1. 填写 config.py
2. 运行 YoutubeListener.py

## 注意事项

如果不需要翻墙，请在 YouCore.py 中 22 行

`cmd = 'proxychains you-get --itag=137 -o ' + dowload_path + ' \'' + url_video + '\''`

去掉 `proxychains`

`cmd = 'you-get --itag=137 -o ' + dowload_path + ' \'' + url_video + '\''`
