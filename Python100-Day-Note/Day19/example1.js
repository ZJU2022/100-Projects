<head>
<script src="jquery.js"></script>
</head>

    /*1.设置一个样式*/
    //两个参数  设置的样式属性,具体样式
    $('li').css('color','red');
    //传入对象（设置的样式属性:具体样式）
    $('li').css({'color':'red'});
    /*2.设置多个样式*/
    $('li').css({
        'color':'green',
        'font-size':'20px'
    });

        /*1.添加一个类*/
        $('li').addClass('now');
        /*2.删除一个类*/
        $('li').removeClass('now');
        /*3.切换一个类  有就删除没有就添加*/
        $('li').toggleClass('now');
        /*4.匹配一个类  判断是否包含某个类  如果包含返回true否知返回false*/
        $('li').hasClass('now');

        
    /*1.获取属性*/
    $('li').attr('name');
    /*2.设置属性*/
    $('li').attr('name','tom');
    /*3.设置多个属性*/
    $('li').attr({
        'name':'tom',
        'age':'18'
    });
    /*4.删除属性*/
    $('li').removeAttr('name');

        /*对于布尔类型的属性，不要attr方法，应该用prop方法 prop用法跟attr方法一样。*/
        $("#checkbox").prop("checked");
        $("#checkbox").prop("checked", true);
        $("#checkbox").prop("checked", false);
        $("#checkbox").removeProp("checked");
    

    /*注意：动画的本质是改变容器的大小和透明度*/
    /*注意：如果不传参数是看不到动画*/
    /*注意：可传入特殊的字符  fast normal slow*/
    /*注意：可传入数字 单位毫秒*/
    /*1.展示动画*/
    $('li').show();
    /*2.隐藏动画*/
    $('li').hide();
    /*3.切换展示和隐藏*/
    $('li').toggle();



    /*注意：动画的本质是改变容器的高度*/
    /*1.滑入动画*/
    $('li').slideDown();
    /*2.滑出动画*/
    $('li').slideUp();
    /*3.切换滑入滑出*/
    $('li').slideToggle();


 /*注意：动画的本质是改变容器的透明度*/
    /*1.淡入动画*/
    $('li').fadeIn();
    /*2.淡出动画*/
    $('li').fadeOut();
    /*3.切换淡入淡出*/
    $('li').fadeToggle();
    $('li').fadeTo('speed','opacity');
    

    /*
    * 自定义动画
    * 参数1：需要做动画的属性
    * 参数2：需要执行动画的总时长
    * 参数3：执行动画的时候的速度
    * 参数4：执行动画完成之后的回调函数
    * */
    $('#box1').animate({left:800},5000);
    $('#box2').animate({left:800},5000,'linear');
    $('#box3').animate({left:800},5000,'swing',function () {
        console.log('动画执行完成');
    });




