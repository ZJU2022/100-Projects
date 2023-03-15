eventTarget.onclick = function (event) { }
eventTarget .addEventListener ( 'click' , function(event) {})
//这个event就是事件对象，我们还喜欢的写成e 或者evt
/**
 官方解释: event对象代表事件的状态，比如键盘按键的状态、鼠标的位置、鼠标按钮的状态。

简单理解∶事件发生后，跟事件相关的一系列信息数据的集合都放到这个对象里面，这个对象就是事件对象event，它有很多属性和方法。

比如︰

谁绑定了这个事件。

鼠标触发事件的话，会得到鼠标的相关信息，如鼠标位置。

键盘触发事件的话，会得到键盘的相关信息，如按了哪个键。
 */

//禁止鼠标右键菜单,contextmenu主要控制应该何时显示上下文菜单，主要用于程序员取消默认的上下文菜单
document.addEventListener('contextmenu',function(e){
    e.preventDefault()
})

//禁止鼠标选中( selectstart开始选中)
document.addEventListener ('selectstart',function(e){				
    e.preventDefault();
}) 

    