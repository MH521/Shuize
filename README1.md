# Shuize
水泽Shuize二开，原作者https://github.com/0x727/ShuiZe_0x727

对水泽进行了如下优化

1、  调用长亭指纹识别工具xapp进行指纹识别，目前该工具只适配了Linux端，如需Windows端请自行修改\Plugins\infoGather\webInfo\Xapp

2、不使用fofa、hunter等进行C端扫描

3、空间搜索引擎去除360 kuake

4、在使用fofa等对ip进行查询前，先判断是否为云IP，若是云IP，则不进行查询

5、修复类似htts://xxx.com:8080:8080的多端口bug

6、优化探测后台地址路径和规则，对状态码大于200的域名都进行后台路径探测，并增加对nacos、springenv、swagger等识别

7、优化url探活逻辑，对于‘VPS访问不了 切换IP访问’情况，不写入execl中

8、增加对泛解析识别的规则，如果域名为泛解析则不进行扫描

9、优化CDN检测逻辑，防止卡死

上述优化只针对于-d --domains 参数
