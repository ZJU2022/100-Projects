//窗口加载事件
window.onload = function() {}
//或者
window.addEventListener("load",function(){

});
//DOMContentLoaded事件触发时，仅当DOM加载完成，不包括样式表，图片，flash等等。ie9以上才支持
//如果页面的图片很多的话，从用户访问到onload触发可能需要较长的事件。交互效果就不能实现，必然影响用户体验，此时用DOMContentLoaded事件比较合适
document.addEventListener('DOMContentLoaded',function(){

})
//调整窗口大小
window.onresize = function() {}
window.addEventListener("resize",function(){});

/*
window对象给我们提供了2个非常好用的方法-定时器

setTimeout()：setTimeout()方法用于设置一个定时器，该定时器在定时器到期后执行调用函数   
window.setTimeout(调用函数，[延迟的毫秒数]);

setTimeout()这个调用函数我们也称为回调函数callback

普通函数是按照代码顺序直接调用

而这个函数，需要等待时间，时间到了才去调用这个函数，因此称为回调函数。

简单理解：回调，就是回头调用的意思。上一件事干完，再回头调用这个函数。

以前我们讲的 element.onclick=function(H}或者element.addEventListener("click",fn);里面的函数也是回调函数。


setInterval()：window.setInterval(回调函数，[间隔的毫秒数]);

setInterval()方法重复调用一个函数，每隔这个时间，就去调用一次回调函数。

注意：

window可以省略
这个调用函数可以直接写函数，或者写函数名或者采取字符串’函数名’三种形式。
间隔的毫秒数省略默认是0，如果写，必须是毫秒，表示每隔多少毫秒就自动调用这个函数。
因为定时器可能有很多，所以我们经常给定时器赋值一个标识符。
*/




