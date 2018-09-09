行为驱动测试
BDD:
Behavior Driven Development

lettuce是实现BDD开发模式的一种测试框架，实现了使用自然语言来执行相关联测试的大门的需求。
lettuce使用Gherkin语言来描述测试功能、测试场景、测试步骤和测试结果
  Gherkin使用的注意英文关键词有Scenario、Given、When、And、Then、But等
  关键词含义如下：
    （1）Feature：特性
    （2）Scenario：情景
    （3）Given：如果
    （4）When：当
    （5）Then：那么
    （6）And：和
    （7）But：
  转化为中文关联词为，“场景”“如果”“当”“那么”
测试人员使用Gherkin语言编写号测试场景的每个执行步骤，lettuce就会一步一步的接近关键词右侧的自然语言并自信相应的代码。



了解BDD lettuce最通俗易懂的文章，来自虫师博客：
https://www.cnblogs.com/fnng/p/3415609.html
或者参考 easyExample.txt
