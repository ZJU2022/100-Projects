/*
DOM对象：使用JavaScript中的方法获取页面中的元素返回的对象就是dom对象。
jQuery对象：jquery对象就是使用jquery的方法获取页面中的元素返回的对象就是jQuery对象。
jQuery对象其实就是DOM对象的包装集包装了DOM对象的集合（伪数组）
DOM对象与jQuery对象的方法不能混用。
*/

//DOM对象转换成jQuery对象：【联想记忆：花钱】
var $obj = $(omObj);
$(document).ready(function(){}) //就是典型的dom对象转换为jquery对象
//jQuery对象转换成DOM对象：
var $li = $('li');
//第一种方法
$li[0]
//第二种方法
$li.get(0)


