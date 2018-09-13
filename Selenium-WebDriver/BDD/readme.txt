行为驱动测试
BDD:
Behavior Driven Development

lettue：
官网：
https://pythonhosted.org/lettuce/
GitHub：
https://github.com/gabrielfalcao/lettuce

官方的教程：
https://pythonhosted.org/lettuce/tutorial/simple.html#tutorial-simple

lettuce是实现BDD开发模式的一种测试框架，实现了使用自然语言来执行相关联测试的大门的需求。
lettuce使用Gherkin语言来描述测试功能、测试场景、测试步骤和测试结果
  Gherkin使用的注意英文关键词有Scenario、Given、When、And、Then、But等
  关键词含义如下：
    （1）Feature：特性,将多个测试用例集合到一起，对应于unittest中的test suite（测试用例集）
    （2）Scenario：情景，用于描述一个用例，对应于unittest中的test case（测试用例）
    （3）Given：如果，用例开始执行前的一个前置条件，类似于unittest中的setup方法中的一些步骤
    （4）When：当，用例开始执行时的一些关键操作步骤，类似于unittest中的以test开头的方法，比如执行一个单元元素的操作
    （5）Then：那么，验证结果，就是平时用例中的验证步骤，比如assert方法
    （6）And：和，一个步骤中如果存在多个Given操作，后面的Given可以用And替代
    （7）But：一个步骤中如果存在多个Then操作，第二个开始后面的Then可以用But替代。
  转化为中文关联词为，“场景”“如果”“当”“那么”
测试人员使用Gherkin语言编写号测试场景的每个执行步骤，lettuce就会一步一步的接近关键词右侧的自然语言并执行相应的代码。



了解BDD lettuce最通俗易懂的文章，来自虫师博客：
https://www.cnblogs.com/fnng/p/3415609.html
或者参考 easyExample.txt
