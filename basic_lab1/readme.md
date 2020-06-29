# 【算法入门与基础提升】第一次作业

## 第一章

- [1.10](sorting_partice.py)     
- [1.11](search_a_2_d_matrix_ii.py)     
- [1.12](fibonacci_number.py)     

## 第二章

- [2.11](sorting_partice_ii.py)
    - [三个高级排序算法](advanced_sorting.py)  
    - [三个高级排序算法的比较器测试](test_advanced_sorting.py)  
- [2.12](sort_string.py)
- [2.13](shortest_unsorted_continuous_subarray.py)

## 关于测试

前缀为 test 的文件都是测试，如 advanced_sorting.py 的测试文件是 test_advanced_sorting.py

###如何跳转到相应的测试

将输入光标放到函数名上，按 `Ctrl-B`，可以看到该函数所有的调用位置。选择以 test 为前缀的文件

![跳转截图](img/jump_to_usage.png)

###如何运行测试

直接点击绿色的播放按钮就行了。  
(也许可以使用 pytest 的之类的命令行工具，不过我现在脱坑命令行了。。。)

![运行截图](img/run_test.png)

###如何创建测试

将输入光标放到函数名上，按 `Ctrl-Shift-T`

![创建截图](img/create_test.png)

###运行测试之前

需要将目录结构弄成这样，不然导入可能会出问题

![目录结构截图](img/project_struct.png)

Pycharm 单元测试的官方文档: 
https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html#write-test  

## 致谢

助教幸苦了惹 (´▽`ʃ♡ƪ) 比心