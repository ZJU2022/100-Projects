//jquery入口函数
//第一种写法
$(document).ready(function() {
	
});
//第二种写法
$(function() {
	
});


//<script>
  //1.$是什么?
  //如果报了这个错误:$ is not defined,就说明没有引入jQuery文件.
  // $(function () {
  //
  // });


  //2.jQuery文件结构.
  //其实是一个自执行函数.
  // (function(){
  //   window.jQuery = window.$ = jQuery;
  // }());


  //3.
  //a.引入一个js文件,是会执行这js文件中的代码的.
  //console.log(num);//10
  //b.jQuery文件是一个自执行函数,执行这个jQUERY文件中的代码,其实就是执行这个自执行函数.
  //c.这个自执行文件就是给window对象添加一个jQuery属性和$属性.
  //console.log(window);
  //d.$其实和jQuery是等价的,是一个函数.

  // console.log(window.jQuery === window.$);//true
  // console.log(Object.prototype.toString.call($));//'[object Function]'


  //4.$是一个函数
  //参数传递不同,效果也不一样.
  //4.1 如果参数传递的是一个匿名函数-入口函数
  // $(function(){
  // });

  //4.2 如果参数传递的是一个字符串-选择器/创建一个标签
  //$('#one');
  //$('<div>啦啦,我是一个div</div>');

  //4.3 如果参数是一个dom对象,那他就会把dom对象转换成jQuery对象.
  //$(dom对象);

//</script>

