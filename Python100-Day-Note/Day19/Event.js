/*
jQuery事件机制
JavaScript中已经学习过了事件，但是jQuery对JavaScript事件进行了封装，增加并扩展了事件处理机制。jQuery不仅提供了更加优雅的事件处理语法，而且极大的增强了事件的处理能力。

jQuery事件发展历程(了解)
简单事件绑定>>bind事件绑定>>delegate事件绑定>>on事件绑定(推荐)
 */

//简单注册事件
click(handler)			//单击事件
mouseenter(handler)		//鼠标进入事件
mouseleave(handler)		//鼠标离开事件

//bind方式注册事件，缺点：不支持动态事件绑定

    //第一个参数：事件类型
    //第二个参数：事件处理程序
    $("p").bind("click mouseenter", function(){
        //事件响应方法
    });

//delegate注册委托事件

    // 第一个参数：selector，要绑定事件的元素
    // 第二个参数：事件类型
    // 第三个参数：事件处理函数
    $(".parentBox").delegate("p", "click", function(){
        //为 .parentBox下面的所有的p标签绑定事件
    });

//on注册事件（重点）
on注册简单事件

    // 表示给$(selector)绑定事件，并且由自己触发，不支持动态绑定。
    $(selector).on( "click", function() {});
1
2
on注册委托事件

    // 表示给$(selector)绑定代理事件，当必须是它的内部元素span才能触发这个事件，支持动态绑定
    $(selector).on( "click",'span', function() {});
1
2
on注册事件的语法

    // 第一个参数：events，绑定事件的名称可以是由空格分隔的多个事件（标准事件或者自定义事件）
    // 第二个参数：selector, 执行事件的后代元素（可选），如果没有后代元素，那么事件将有自己执行。
    // 第三个参数：data，传递给处理函数的数据，事件触发的时候通过event.data来使用（不常使用）
    // 第四个参数：handler，事件处理函数
    $(selector).on(events,[selector],[data],handler);