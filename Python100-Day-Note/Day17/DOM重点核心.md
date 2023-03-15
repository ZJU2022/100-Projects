6.DOM重点核心
文档对象模型(Document Object Model，简称DOM)，是W3C组织推荐的处理可扩展标记语言(HTML或者XML)的标准编程接口。
W3C已经定义了一系列的DOM接口，通过这些DOM接口可以改变网页的内容、结构和样式。
对于JavaScript，为了能够使JavaScript操作HTML，JavaScript就有了一套自己的dom编程接口。

对于HTML,dom使得html形成一棵dom树.包含文档、元素、节点

我们获取过来的DOM元素是一个对象（object），所以称为文档对象模型

关于dom操作，我们主要针对于元素的操作。主要有创建、增、删、改、查、属性操作、事件操作。

创建

document.write
innerHTML
createElement
增

appendChild
insertBefore
删

removeChild
改

主要修改dom的元素属性，dom元素的内容、属性、表单的值等。

修改元素属性：sic href title
修改普通元素内容：innerHTML innerText
修改表单元素：value type disable
修改元素样式：style className
查

主要获取查询dom的元素

DOM提供的API方法: getElementByld、getElementsByTagName古老用法不太推荐
H5提供的新方法:querySelector、querySelectorAll提倡
利用节点操作获取元素︰父(parentNode)、子(children)、兄(previousElementSibling、nextElementSibling) 提倡
属性操作

主要针对于自定义属性

setAttribute：设置dom的属性值
getAttribute：得到dom的属性值
removeAttribute：移除属性
事件操作

给元素注册事件，采取 事件源.事件类型 = 事件处理程序

鼠标事件	触发事件
onclick	鼠标点击左键触发
onmouseover	鼠标经过触发
onmouseout	鼠标离开触发
onfocus	获得鼠标焦点触发
onblur	失去鼠标焦点触发
onmousemove	鼠标移动触发
onmouseup	鼠标弹起触发
onmousedown	鼠标按下触发